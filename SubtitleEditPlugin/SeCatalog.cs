namespace Loupedeck.SubtitleEditPlugin
{
    using System;
    using System.Collections.Generic;
    using System.Text;

    /// <summary>
    /// Turns Subtitle Edit action names into names a user can read, and sorts them
    /// into groups in the action picker. Any action not listed here still shows up,
    /// with a name derived from the action name, so a new Subtitle Edit release never
    /// leaves an action hidden.
    /// </summary>
    internal static class SeCatalog
    {
        private static readonly Dictionary<String, String> DisplayNames =
            new Dictionary<String, String>(StringComparer.Ordinal)
            {
                // Playback
                { "TogglePlayPauseCommand", "Play/pause" },
                { "TogglePlayPause2Command", "Play/pause (alternate)" },
                { "PlayCommand", "Play" },
                { "PauseCommand", "Pause" },
                { "PlaySelectedLinesWithoutLoopCommand", "Play selected lines" },
                { "PlaySelectedLinesWithLoopAndFocusWaveformCommand", "Play selected lines (loop)" },
                { "VideoFullScreenCommand", "Full screen video" },
                { "VideoOneSecondBackCommand", "Video back 1 second" },
                { "VideoOneSecondForwardCommand", "Video forward 1 second" },
                { "Video500MsBackCommand", "Video back 500 ms" },
                { "Video500MsForwardCommand", "Video forward 500 ms" },

                // Timing
                { "WaveformSetStartCommand", "Set start" },
                { "WaveformSetEndCommand", "Set end" },
                { "WaveformSetEndAndGoToNextCommand", "Set end and go to next" },
                { "WaveformInsertNewSelectionCommand", "Insert new selection" },
                { "WaveformVerticalZoomInCommand", "Waveform zoom in" },
                { "WaveformVerticalZoomOutCommand", "Waveform zoom out" },
                { "WaveformPasteFromClipboardCommand", "Paste into waveform" },
                { "ShowPointSyncCommand", "Point sync" },
                { "ShowSyncAdjustAllTimesCommand", "Adjust all times" },

                // Lines
                { "GoToNextLineCommand", "Go to next line" },
                { "GoToPreviousLineCommand", "Go to previous line" },
                { "GoToNextErrorCommand", "Go to next error" },
                { "GoToPreviousErrorCommand", "Go to previous error" },
                { "InsertLineAfterCommand", "Insert line after" },
                { "InsertLineBeforeCommand", "Insert line before" },
                { "MergeSelectedLinesCommand", "Merge selected lines" },
                { "SplitAtTextBoxCursorPositionCommand", "Split at cursor" },
                { "DeleteSelectedLinesCommand", "Delete selected lines" },
                { "ExtendSelectedToNextCommand", "Extend to next" },
                { "ExtendSelectedToPreviousCommand", "Extend to previous" },
                { "FocusSelectedLineCommand", "Focus selected line" },
                { "AutoBreakCommand", "Auto break" },
                { "ShowGoToLineCommand", "Go to line" },

                // Text
                { "ToggleLinesItalicOrSelectedTextCommand", "Italic" },
                { "ToggleCasingCommand", "Toggle casing" },
                { "SelectionToUpperCommand", "Selection to upper case" },
                { "SelectionToLowerCommand", "Selection to lower case" },

                // File and edit
                { "CommandFileNewCommand", "New" },
                { "CommandFileOpenCommand", "Open" },
                { "CommandFileSaveCommand", "Save" },
                { "CommandFileSaveAsCommand", "Save as" },
                { "UndoCommand", "Undo" },
                { "RedoCommand", "Redo" },
                { "SelectAllLinesCommand", "Select all lines" },
                { "InverseSelectionCommand", "Inverse selection" },
                { "AddOrEditBookmarkCommand", "Add or edit bookmark" },

                // Find and replace
                { "ShowFindCommand", "Find" },
                { "FindNextCommand", "Find next" },
                { "FindPreviousCommand", "Find previous" },
                { "ShowReplaceCommand", "Replace" },
                { "ShowMultipleReplaceCommand", "Multiple replace" },

                // Tools
                { "ShowSpellCheckCommand", "Spell check" },
                { "ShowToolsFixCommonErrorsCommand", "Fix common errors" },
                { "ShowToolsAiReviewCommand", "AI review" },
                { "ShowAutoTranslateCommand", "Auto translate" },
                { "ShowToolsBatchConvertCommand", "Batch convert" },
                { "ShowToolsChangeCasingCommand", "Change casing" },
                { "ShowToolsRemoveTextForHearingImpairedCommand", "Remove text for hearing impaired" },
                { "ShowSourceViewCommand", "Source view" },
                { "ListErrorsCommand", "List errors" },
                { "RightToLeftToggleCommand", "Toggle right to left" },
                { "ToggleTranslationModeCommand", "Toggle translation mode" },
            };

        // Which group each action appears under. Falls back to the Subtitle Edit
        // control name (General, SubtitleGrid, TextBox, Waveform) when not listed.
        private static readonly Dictionary<String, String> Groups =
            new Dictionary<String, String>(StringComparer.Ordinal)
            {
                { "TogglePlayPauseCommand", "Playback" },
                { "TogglePlayPause2Command", "Playback" },
                { "PlayCommand", "Playback" },
                { "PauseCommand", "Playback" },
                { "PlaySelectedLinesWithoutLoopCommand", "Playback" },
                { "PlaySelectedLinesWithLoopAndFocusWaveformCommand", "Playback" },
                { "VideoFullScreenCommand", "Playback" },
                { "VideoOneSecondBackCommand", "Playback" },
                { "VideoOneSecondForwardCommand", "Playback" },
                { "Video500MsBackCommand", "Playback" },
                { "Video500MsForwardCommand", "Playback" },

                { "WaveformSetStartCommand", "Timing" },
                { "WaveformSetEndCommand", "Timing" },
                { "WaveformSetEndAndGoToNextCommand", "Timing" },
                { "WaveformInsertNewSelectionCommand", "Timing" },
                { "WaveformVerticalZoomInCommand", "Timing" },
                { "WaveformVerticalZoomOutCommand", "Timing" },
                { "WaveformPasteFromClipboardCommand", "Timing" },
                { "ShowPointSyncCommand", "Timing" },
                { "ShowSyncAdjustAllTimesCommand", "Timing" },

                { "GoToNextLineCommand", "Lines" },
                { "GoToPreviousLineCommand", "Lines" },
                { "GoToNextErrorCommand", "Lines" },
                { "GoToPreviousErrorCommand", "Lines" },
                { "InsertLineAfterCommand", "Lines" },
                { "InsertLineBeforeCommand", "Lines" },
                { "MergeSelectedLinesCommand", "Lines" },
                { "SplitAtTextBoxCursorPositionCommand", "Lines" },
                { "DeleteSelectedLinesCommand", "Lines" },
                { "ExtendSelectedToNextCommand", "Lines" },
                { "ExtendSelectedToPreviousCommand", "Lines" },
                { "FocusSelectedLineCommand", "Lines" },
                { "AutoBreakCommand", "Lines" },
                { "ShowGoToLineCommand", "Lines" },

                { "ToggleLinesItalicOrSelectedTextCommand", "Text" },
                { "ToggleCasingCommand", "Text" },
                { "SelectionToUpperCommand", "Text" },
                { "SelectionToLowerCommand", "Text" },

                { "CommandFileNewCommand", "File" },
                { "CommandFileOpenCommand", "File" },
                { "CommandFileSaveCommand", "File" },
                { "CommandFileSaveAsCommand", "File" },

                { "UndoCommand", "Edit" },
                { "RedoCommand", "Edit" },
                { "SelectAllLinesCommand", "Edit" },
                { "InverseSelectionCommand", "Edit" },
                { "AddOrEditBookmarkCommand", "Edit" },

                { "ShowFindCommand", "Find" },
                { "FindNextCommand", "Find" },
                { "FindPreviousCommand", "Find" },
                { "ShowReplaceCommand", "Find" },
                { "ShowMultipleReplaceCommand", "Find" },

                { "ShowSpellCheckCommand", "Tools" },
                { "ShowToolsFixCommonErrorsCommand", "Tools" },
                { "ShowToolsAiReviewCommand", "Tools" },
                { "ShowAutoTranslateCommand", "Tools" },
                { "ShowToolsBatchConvertCommand", "Tools" },
                { "ShowToolsChangeCasingCommand", "Tools" },
                { "ShowToolsRemoveTextForHearingImpairedCommand", "Tools" },
                { "ShowSourceViewCommand", "Tools" },
                { "ListErrorsCommand", "Tools" },
                { "RightToLeftToggleCommand", "Tools" },
                { "ToggleTranslationModeCommand", "Tools" },
            };

        public static String GetDisplayName(String actionName) =>
            DisplayNames.TryGetValue(actionName, out var name) ? name : Prettify(actionName);

        public static String GetGroupName(String actionName, String controlName) =>
            Groups.TryGetValue(actionName, out var group) ? group : PrettifyGroup(controlName);

        /// <summary>"ShowFindDoubleWordsCommand" becomes "Show find double words".</summary>
        internal static String Prettify(String actionName)
        {
            if (String.IsNullOrEmpty(actionName))
            {
                return String.Empty;
            }

            var name = actionName;
            if (name.EndsWith("Command", StringComparison.Ordinal))
            {
                name = name.Substring(0, name.Length - "Command".Length);
            }

            if (name.Length == 0)
            {
                return actionName;
            }

            var builder = new StringBuilder(name.Length + 8);
            for (var i = 0; i < name.Length; i++)
            {
                var c = name[i];
                if (i > 0 && Char.IsUpper(c) && !Char.IsUpper(name[i - 1]))
                {
                    builder.Append(' ').Append(Char.ToLowerInvariant(c));
                }
                else
                {
                    builder.Append(i == 0 ? Char.ToUpperInvariant(c) : c);
                }
            }

            return builder.ToString();
        }

        private static String PrettifyGroup(String controlName)
        {
            switch (controlName)
            {
                case "SubtitleGrid": return "Subtitle list";
                case "SubtitleGridAndTextBox": return "Subtitle list and text box";
                case "TextBox": return "Text box";
                case "Waveform": return "Waveform";
                default: return "General";
            }
        }
    }
}
