namespace Loupedeck.SubtitleEditPlugin
{
    using System;

    /// <summary>
    /// Re-reads Settings.json so a shortcut changed in Subtitle Edit takes effect
    /// without restarting the plugin service. New actions appear after a reload of
    /// the plugin, since the action list is built when the plugin loads.
    /// </summary>
    public class SeReloadCommand : PluginDynamicCommand
    {
        public SeReloadCommand()
            : base(displayName: "Reload shortcuts",
                   description: "Re-read the shortcuts from Subtitle Edit settings",
                   groupName: "Plugin")
        {
        }

        protected override void RunCommand(String actionParameter) => SubtitleEditPlugin.ReloadBindings();
    }
}
