namespace Loupedeck.SubtitleEditPlugin
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Text.Json;

    /// <summary>
    /// One Subtitle Edit shortcut, resolved to what the plugin service can send.
    /// </summary>
    internal sealed class SeBinding
    {
        public String ActionName { get; set; }
        public String ControlName { get; set; }
        public VirtualKeyCode KeyCode { get; set; }
        public ModifierKey Modifiers { get; set; }
        public String KeysText { get; set; }
    }

    /// <summary>
    /// Reads the shortcuts out of the user's own Subtitle Edit Settings.json.
    ///
    /// Subtitle Edit registers its actions by name and keeps the key bindings in the
    /// settings file, so the keys are whatever the user configured. Reading them here,
    /// instead of hard coding a default set, keeps the plugin correct for a user who
    /// has remapped anything, and across Windows and macOS where the primary modifier
    /// differs. Actions with no keys assigned are skipped: there is nothing to send.
    /// </summary>
    internal static class SeShortcuts
    {
        /// <summary>Set SUBTITLE_EDIT_SETTINGS to point at a portable Settings.json.</summary>
        private const String PathOverrideVariable = "SUBTITLE_EDIT_SETTINGS";

        public static String ResolveSettingsPath()
        {
            var overridePath = Environment.GetEnvironmentVariable(PathOverrideVariable);
            if (!String.IsNullOrWhiteSpace(overridePath) && File.Exists(overridePath))
            {
                return overridePath;
            }

            foreach (var candidate in GetCandidatePaths())
            {
                if (!String.IsNullOrEmpty(candidate) && File.Exists(candidate))
                {
                    return candidate;
                }
            }

            return null;
        }

        private static IEnumerable<String> GetCandidatePaths()
        {
            // Subtitle Edit builds this same path from SpecialFolder.ApplicationData.
            var appData = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            if (!String.IsNullOrEmpty(appData))
            {
                yield return Path.Combine(appData, "Subtitle Edit", "Settings.json");
            }

            var home = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
            if (!String.IsNullOrEmpty(home))
            {
                yield return Path.Combine(home, "Library", "Application Support", "Subtitle Edit", "Settings.json");
            }
        }

        /// <summary>
        /// Returns every action that has a usable key binding, keyed by action name.
        /// Returns an empty map when Subtitle Edit has never been run, so the plugin
        /// still loads and simply has nothing to send.
        /// </summary>
        public static Dictionary<String, SeBinding> Load()
        {
            var result = new Dictionary<String, SeBinding>(StringComparer.Ordinal);

            var path = ResolveSettingsPath();
            if (path == null)
            {
                PluginLog.Warning("Subtitle Edit Settings.json not found, no shortcuts loaded");
                return result;
            }

            try
            {
                // ReadAllText strips the byte order mark that Subtitle Edit writes.
                var json = File.ReadAllText(path, System.Text.Encoding.UTF8);
                using var document = JsonDocument.Parse(json);

                if (!TryGetProperty(document.RootElement, "Shortcuts", out var shortcuts) ||
                    shortcuts.ValueKind != JsonValueKind.Array)
                {
                    PluginLog.Warning("No Shortcuts array in " + path);
                    return result;
                }

                foreach (var entry in shortcuts.EnumerateArray())
                {
                    var binding = ReadBinding(entry);
                    if (binding != null)
                    {
                        // First one wins, matching how Subtitle Edit groups by action name.
                        if (!result.ContainsKey(binding.ActionName))
                        {
                            result[binding.ActionName] = binding;
                        }
                    }
                }

                PluginLog.Info($"Loaded {result.Count} Subtitle Edit shortcuts from {path}");
            }
            catch (Exception e)
            {
                PluginLog.Error(e, "Could not read Subtitle Edit settings from " + path);
            }

            return result;
        }

        private static SeBinding ReadBinding(JsonElement entry)
        {
            if (!TryGetProperty(entry, "ActionName", out var actionElement))
            {
                return null;
            }

            var actionName = actionElement.GetString();
            if (String.IsNullOrWhiteSpace(actionName))
            {
                return null;
            }

            if (!TryGetProperty(entry, "Keys", out var keysElement) || keysElement.ValueKind != JsonValueKind.Array)
            {
                return null;
            }

            var keys = new List<String>();
            foreach (var key in keysElement.EnumerateArray())
            {
                if (key.ValueKind == JsonValueKind.String)
                {
                    keys.Add(key.GetString());
                }
            }

            // An action with no keys is unassigned in Subtitle Edit; there is no
            // keystroke to simulate, so it must not become a plugin action.
            if (!SeKeyMap.TryParse(keys, out var keyCode, out var modifiers))
            {
                return null;
            }

            var controlName = TryGetProperty(entry, "ControlName", out var controlElement)
                ? controlElement.GetString()
                : null;

            return new SeBinding
            {
                ActionName = actionName,
                ControlName = String.IsNullOrWhiteSpace(controlName) ? "General" : controlName,
                KeyCode = keyCode,
                Modifiers = modifiers,
                KeysText = String.Join("+", keys),
            };
        }

        private static Boolean TryGetProperty(JsonElement element, String name, out JsonElement value)
        {
            if (element.TryGetProperty(name, out value))
            {
                return true;
            }

            // Settings.json is written with Pascal case, but be forgiving.
            foreach (var property in element.EnumerateObject())
            {
                if (String.Equals(property.Name, name, StringComparison.OrdinalIgnoreCase))
                {
                    value = property.Value;
                    return true;
                }
            }

            value = default;
            return false;
        }
    }
}
