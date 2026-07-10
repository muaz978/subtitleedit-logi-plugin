namespace Loupedeck.SubtitleEditPlugin
{
    using System;
    using System.Collections.Generic;

    /// <summary>
    /// One plugin action per Subtitle Edit shortcut that has keys assigned. Pressing
    /// the button sends that shortcut to the focused application.
    ///
    /// The parameters are built from the settings file, so an action the user has not
    /// bound in Subtitle Edit never appears here: there would be no keystroke to send.
    /// </summary>
    public class SeShortcutCommand : PluginDynamicCommand
    {
        public SeShortcutCommand()
            : base()
        {
        }

        protected override Boolean OnLoad()
        {
            var bindings = new List<SeBinding>(SubtitleEditPlugin.GetBindings());
            bindings.Sort((a, b) => String.CompareOrdinal(
                SeCatalog.GetDisplayName(a.ActionName),
                SeCatalog.GetDisplayName(b.ActionName)));

            foreach (var binding in bindings)
            {
                this.AddParameter(
                    binding.ActionName,
                    SeCatalog.GetDisplayName(binding.ActionName),
                    SeCatalog.GetGroupName(binding.ActionName, binding.ControlName));
            }

            PluginLog.Info($"Subtitle Edit plugin exposed {bindings.Count} actions");
            return true;
        }

        protected override void RunCommand(String actionParameter)
        {
            if (String.IsNullOrEmpty(actionParameter))
            {
                return;
            }

            if (!SubtitleEditPlugin.TryGetBinding(actionParameter, out var binding))
            {
                PluginLog.Warning($"No Subtitle Edit shortcut bound for {actionParameter}");
                return;
            }

            this.Plugin.ClientApplication.SendKeyboardShortcut(binding.KeyCode, binding.Modifiers);
            PluginLog.Verbose($"Sent {binding.KeysText} for {binding.ActionName}");
        }
    }
}
