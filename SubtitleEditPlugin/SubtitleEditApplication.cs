namespace Loupedeck.SubtitleEditPlugin
{
    using System;

    /// <summary>
    /// Links the plugin to Subtitle Edit: the process name on Windows and the bundle
    /// identifier on macOS. Both were taken from the shipped application.
    /// </summary>
    public class SubtitleEditApplication : ClientApplication
    {
        public SubtitleEditApplication()
        {
        }

        protected override String GetProcessName() => "SubtitleEdit";

        protected override String GetBundleName() => "dk.nikse.subtitleedit";
    }
}
