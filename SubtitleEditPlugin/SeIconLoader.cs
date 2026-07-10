namespace Loupedeck.SubtitleEditPlugin
{
    using System;
    using System.Collections.Concurrent;
    using System.IO;

    /// <summary>
    /// Loads an action's SVG so it can be drawn on the device (the Actions Ring bubble
    /// and console keys). The action symbols in the package draw the icon next to the
    /// name in the configuration list; the button image on the device is separate and
    /// comes from GetCommandImage / GetAdjustmentImage, which is what uses this.
    ///
    /// The same SVG files serve both, so they are read from the package's actionsymbols
    /// folder rather than duplicated. Results are cached; a missing file returns null so
    /// the caller falls back to drawing the action name.
    /// </summary>
    internal static class SeIconLoader
    {
        private static readonly String Folder = ResolveFolder();
        private static readonly ConcurrentDictionary<String, String> Cache =
            new ConcurrentDictionary<String, String>(StringComparer.Ordinal);

        private static String ResolveFolder()
        {
            foreach (var baseDir in new[]
            {
                Path.GetDirectoryName(typeof(SeIconLoader).Assembly.Location),
                AppContext.BaseDirectory,
            })
            {
                if (String.IsNullOrEmpty(baseDir))
                {
                    continue;
                }

                // The plugin dll lives in bin/, with actionsymbols/ next to it.
                var sibling = Path.GetFullPath(Path.Combine(baseDir, "..", "actionsymbols"));
                if (Directory.Exists(sibling))
                {
                    return sibling;
                }

                var here = Path.Combine(baseDir, "actionsymbols");
                if (Directory.Exists(here))
                {
                    return here;
                }
            }

            return null;
        }

        /// <summary>Returns the SVG for a symbol file name, or null if there is none.</summary>
        public static String LoadSvg(String fileName)
        {
            if (Folder == null || String.IsNullOrEmpty(fileName))
            {
                return null;
            }

            return Cache.GetOrAdd(fileName, name =>
            {
                try
                {
                    var path = Path.Combine(Folder, name);
                    return File.Exists(path) ? File.ReadAllText(path) : null;
                }
                catch (Exception e)
                {
                    PluginLog.Warning($"Could not read action symbol {name}: {e.Message}");
                    return null;
                }
            });
        }

        /// <summary>Draws the SVG for an action, or null to let the service draw the name.</summary>
        public static BitmapImage Image(String symbolFileName)
        {
            var svg = LoadSvg(symbolFileName);
            if (String.IsNullOrEmpty(svg))
            {
                return null;
            }

            try
            {
                return BitmapImage.FromSvg(svg);
            }
            catch (Exception e)
            {
                PluginLog.Warning($"Could not render action symbol {symbolFileName}: {e.Message}");
                return null;
            }
        }
    }
}
