#!/usr/bin/env python3
"""
Generates the action symbols shown next to each action in the Options+ picker.

The plugin service looks for one SVG per action in the package's actionsymbols/
folder, named after the action's full class name. Every one of our shortcut actions
is a parameter of SeShortcutCommand, so those files carry the parameter name after a
three underscore separator. A missing file falls back to the class level symbol, and
then to a generic one, so an unmapped action still looks reasonable.

Symbols must be SVG, transparent, and a single black colour.

Usage:  python3 scripts/gen-action-symbols.py
"""
import pathlib

NS = "Loupedeck.SubtitleEditPlugin"
OUT = pathlib.Path(__file__).resolve().parent.parent / "SubtitleEditPlugin" / "package" / "actionsymbols"

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" '
        'fill="none" stroke="black" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">')
TAIL = "</svg>"

# Every glyph is drawn on a 24x24 grid, black only, transparent background.
G = {
    # playback
    "play":        '<path d="M8 5l11 7-11 7z" fill="black" stroke="none"/>',
    "pause":       '<rect x="7" y="5" width="3.5" height="14" fill="black" stroke="none"/>'
                   '<rect x="13.5" y="5" width="3.5" height="14" fill="black" stroke="none"/>',
    "playpause":   '<path d="M4 5l8 7-8 7z" fill="black" stroke="none"/>'
                   '<rect x="14" y="5" width="3" height="14" fill="black" stroke="none"/>'
                   '<rect x="19" y="5" width="3" height="14" fill="black" stroke="none"/>',
    "playpause2":  '<path d="M3 5l7 7-7 7z" fill="black" stroke="none"/>'
                   '<rect x="12" y="5" width="2.6" height="14" fill="black" stroke="none"/>'
                   '<rect x="16" y="5" width="2.6" height="14" fill="black" stroke="none"/>'
                   '<circle cx="21" cy="6" r="1.6" fill="black" stroke="none"/>',
    "play_lines":  '<path d="M4 6h8M4 12h8M4 18h5"/><path d="M15 8l6 4-6 4z" fill="black" stroke="none"/>',
    "play_loop":   '<path d="M5 9a6 6 0 0 1 6-6h4"/><path d="M13 1l2 2-2 2"/>'
                   '<path d="M19 15a6 6 0 0 1-6 6H9"/><path d="M11 23l-2-2 2-2"/>'
                   '<path d="M10 10l5 3-5 3z" fill="black" stroke="none"/>',
    "fullscreen":  '<path d="M3 9V4h5M21 9V4h-5M3 15v5h5M21 15v5h-5"/>',
    "vid_back_s":  '<path d="M12 5l-8 7 8 7z" fill="black" stroke="none"/><path d="M20 5v14"/>',
    "vid_fwd_s":   '<path d="M12 5l8 7-8 7z" fill="black" stroke="none"/><path d="M4 5v14"/>',
    "vid_back_l":  '<path d="M11 5l-7 7 7 7z" fill="black" stroke="none"/>'
                   '<path d="M20 5l-7 7 7 7z" fill="black" stroke="none"/>',
    "vid_fwd_l":   '<path d="M13 5l7 7-7 7z" fill="black" stroke="none"/>'
                   '<path d="M4 5l7 7-7 7z" fill="black" stroke="none"/>',
    "video_dial":  '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M12 6v12"/><path d="M7 12h-2M19 12h-2"/>',

    # timing
    "set_start":   '<path d="M7 4v16"/><path d="M11 12h9"/><path d="M16 8l4 4-4 4"/>',
    "set_end":     '<path d="M17 4v16"/><path d="M13 12H4"/><path d="M8 8l-4 4 4 4"/>',
    "set_end_next":'<path d="M14 4v16"/><path d="M10 12H3"/><path d="M6 8l-4 4 4 4"/><path d="M18 8l4 4-4 4"/>',
    "sel_new":     '<path d="M4 6v12M20 6v12"/><rect x="8" y="8" width="8" height="8" rx="1"/>',
    "zoom_in":     '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/><path d="M10.5 8v5M8 10.5h5"/>',
    "zoom_out":    '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/><path d="M8 10.5h5"/>',
    "wave_paste":  '<path d="M4 10v4M8 7v10M12 9v6M16 6v12M20 10v4"/>',
    "point_sync":  '<circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="12" r="2.5"/><path d="M8.5 12h7"/>',
    "clock":       '<circle cx="12" cy="12" r="8"/><path d="M12 7v5l3.5 2"/>',

    # lines
    "next_line":   '<path d="M4 5h16M4 10h16"/><path d="M12 14v6M9 17l3 3 3-3"/>',
    "prev_line":   '<path d="M4 19h16M4 14h16"/><path d="M12 10V4M9 7l3-3 3 3"/>',
    "next_error":  '<path d="M11 3L2 19h18L11 3z"/><path d="M11 9v4M11 16h.01"/>'
                   '<path d="M18 15l3 3-3 3" stroke-width="1.6"/>',
    "prev_error":  '<path d="M13 3L4 19h18L13 3z"/><path d="M13 9v4M13 16h.01"/>'
                   '<path d="M5 15l-3 3 3 3" stroke-width="1.6"/>',
    "insert_after":'<path d="M4 6h16M4 11h16"/><path d="M12 15v6M9 18h6"/>',
    "insert_before":'<path d="M4 18h16M4 13h16"/><path d="M12 3v6M9 6h6"/>',
    "merge":       '<path d="M4 6h7l5 6M4 18h7l5-6"/><path d="M16 12h5"/><path d="M18 9l3 3-3 3"/>',
    "split":       '<path d="M12 3v6M12 15v6"/><path d="M4 12h16"/><path d="M9 6l3-3 3 3"/><path d="M9 18l3 3 3-3"/>',
    "delete":      '<path d="M4 7h16"/><path d="M9 7V4h6v3"/><path d="M6 7l1 13h10l1-13"/><path d="M10 11v6M14 11v6"/>',
    "extend_next": '<path d="M5 5v14"/><path d="M9 12h10"/><path d="M15 8l4 4-4 4"/>',
    "extend_prev": '<path d="M19 5v14"/><path d="M15 12H5"/><path d="M9 8l-4 4 4 4"/>',
    "focus_line":  '<rect x="3" y="9" width="18" height="6" rx="1"/><path d="M12 3v3M12 18v3"/>',
    "auto_break":  '<path d="M4 6h16"/><path d="M4 12h11a4 4 0 0 1 0 8h-4"/><path d="M12 17l-3 3 3 3" stroke-width="1.6"/>',
    "goto_line":   '<path d="M4 6h16M4 12h9M4 18h9"/><path d="M16 12l4 3-4 3z" fill="black" stroke="none"/>',
    "line_dial":   '<path d="M4 5h16M4 12h16M4 19h16"/><circle cx="19" cy="12" r="2.5" fill="black" stroke="none"/>',
    "error_dial":  '<path d="M12 3L3 19h18L12 3z"/><path d="M12 9v4M12 16h.01"/>',

    # text
    "italic":      '<path d="M15 4h-6M15 20H9M14 4l-4 16" stroke-width="2"/>',
    "case_toggle": '<path d="M2 18L6 6l4 12M3.4 14h5.2"/><path d="M20 11a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"/><path d="M23 11v6"/>',
    "to_upper":    '<path d="M3 18L8 5l5 13M4.6 14h6.8"/><path d="M18 18V8M15 11l3-3 3 3"/>',
    "to_lower":    '<path d="M6 12a3 3 0 1 0 0 6 3 3 0 0 0 0-6z"/><path d="M9 12v6"/><path d="M18 6v10M15 13l3 3 3-3"/>',

    # file
    "file_new":    '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>',
    "folder_open": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h6a2 2 0 0 1 2 2v1"/><path d="M3 9h18l-2 9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/>',
    "save":        '<path d="M5 3h11l3 3v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/>'
                   '<path d="M8 3v6h7V3"/><rect x="8" y="13" width="8" height="6"/>',
    "save_as":     '<path d="M5 3h9l3 3v6"/><path d="M3 5a2 2 0 0 1 2-2v18a2 2 0 0 1-2-2z"/>'
                   '<path d="M8 3v5h5V3"/><path d="M20 13l-6 6-3 1 1-3 6-6z"/>',

    # edit
    "undo":        '<path d="M4 9h10a5 5 0 0 1 0 10h-4"/><path d="M8 5L4 9l4 4"/>',
    "redo":        '<path d="M20 9H10a5 5 0 0 0 0 10h4"/><path d="M16 5l4 4-4 4"/>',
    "select_all":  '<rect x="3" y="3" width="18" height="18" rx="2" stroke-dasharray="3 2.4"/>'
                   '<path d="M8 12.5l2.6 2.6L16.5 9"/>',
    "inverse_sel": '<rect x="3" y="3" width="12" height="12" rx="1"/>'
                   '<rect x="9" y="9" width="12" height="12" rx="1" fill="black" stroke="none"/>',
    "bookmark":    '<path d="M6 3h12v18l-6-5-6 5z"/>',

    # find
    "find":        '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/>',
    "find_next":   '<circle cx="9.5" cy="9.5" r="5.5"/><path d="M13.5 13.5L17 17"/><path d="M17 21l3-3-3-3" stroke-width="1.6"/>',
    "find_prev":   '<circle cx="9.5" cy="9.5" r="5.5"/><path d="M13.5 13.5L17 17"/><path d="M21 21l-3-3 3-3" stroke-width="1.6"/>',
    "replace":     '<path d="M4 7h10"/><path d="M11 4l3 3-3 3"/><path d="M20 17H10"/><path d="M13 20l-3-3 3-3"/>',
    "replace_all": '<path d="M4 6h9"/><path d="M10 3l3 3-3 3"/><path d="M20 14H11"/><path d="M14 17l-3-3 3-3"/>'
                   '<path d="M4 20h16" stroke-width="1.6"/>',

    # tools
    "spellcheck":  '<path d="M2 18L6.5 6 11 18M3.6 14h5.8"/><path d="M13 13l3 3 6-6"/>',
    "wrench":      '<path d="M20 5a5 5 0 0 1-6.6 6.6L5 20l-2-2 8.4-8.4A5 5 0 0 1 18 3z"/>',
    "ai_review":   '<path d="M12 2l1.8 4.7L18.5 8l-4.7 1.8L12 14l-1.8-4.2L5.5 8l4.7-1.3z" fill="black" stroke="none"/>'
                   '<path d="M18 15l.9 2.3 2.3.9-2.3.9-.9 2.3-.9-2.3-2.3-.9 2.3-.9z" fill="black" stroke="none"/>',
    "translate":   '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18z"/>',
    "batch":       '<path d="M12 2l9 5-9 5-9-5z"/><path d="M3 12l9 5 9-5"/><path d="M3 17l9 5 9-5"/>',
    "hearing":     '<path d="M8 8a4 4 0 1 1 8 0c0 3-3 3-3 6a2 2 0 0 1-4 0"/><path d="M11 20h.01"/><path d="M3 5l3 3M3 11h3"/>',
    "source_view": '<path d="M8 7l-5 5 5 5"/><path d="M16 7l5 5-5 5"/>',
    "list_errors": '<path d="M4 6h10M4 12h10M4 18h6"/><path d="M19 8v5M19 16h.01"/>',
    "rtl_toggle":  '<path d="M20 6H9a4 4 0 0 0 0 8h11"/><path d="M16 2l4 4-4 4"/><path d="M4 18h16"/>',
    "translate_mode":'<rect x="3" y="3" width="9" height="13" rx="1"/><rect x="12" y="8" width="9" height="13" rx="1"/>',

    # clipboard
    "copy":        '<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>',
    "cut":         '<circle cx="6" cy="18" r="2.6"/><circle cx="18" cy="18" r="2.6"/><path d="M7.8 16.2L19 3M16.2 16.2L5 3"/>',
    "paste":       '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>'
                   '<rect x="8" y="2" width="8" height="4" rx="1"/>',
    "paste_fill":  '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>'
                   '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M8 12h8M8 16h8"/>',

    # general / misc
    "data_folder": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'
                   '<path d="M12 11v5M9.5 13.5L12 16l2.5-2.5"/>',
    "lang_file":   '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>'
                   '<path d="M8 13h8M12 13v5"/>',
    "se4_badge":   '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M14 9v4h4"/><path d="M17 9v7"/>',
    "name_list":   '<circle cx="8" cy="8" r="3"/><path d="M3 20a5 5 0 0 1 10 0"/><path d="M16 9h5M16 13h5M16 17h5"/>',
    "double_words":'<path d="M2 8l2 8 2.5-6L9 16l2-8"/><path d="M13 8l2 8 2.5-6L20 16l2-8"/>',
    "help":        '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.6 2.6 0 1 1 3.4 2.5c-.8.3-1 .9-1 1.7"/><path d="M12 17h.01"/>',
    "reload":      '<path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20 4v5h-5"/>',
    "waveform":    '<path d="M3 10v4M7 6v12M11 9v6M15 4v16M19 8v8"/>',
    "wave_insert": '<path d="M3 10v4M7 7v10M11 9v6"/><path d="M18 8v8M14 12h8"/>',

    # generic fallback: a caption block
    "generic":     '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 12h6M7 15.5h10"/>',
}

# Maps each Subtitle Edit action to a glyph. Anything absent falls back to "generic".
ACTIONS = {
    # playback
    "TogglePlayPauseCommand": "playpause",
    "TogglePlayPause2Command": "playpause2",
    "PlayCommand": "play",
    "PauseCommand": "pause",
    "PlaySelectedLinesWithoutLoopCommand": "play_lines",
    "PlaySelectedLinesWithLoopAndFocusWaveformCommand": "play_loop",
    "VideoFullScreenCommand": "fullscreen",
    "VideoOneSecondBackCommand": "vid_back_l",
    "VideoOneSecondForwardCommand": "vid_fwd_l",
    "Video500MsBackCommand": "vid_back_s",
    "Video500MsForwardCommand": "vid_fwd_s",

    # timing
    "WaveformSetStartCommand": "set_start",
    "WaveformSetEndCommand": "set_end",
    "WaveformSetEndAndGoToNextCommand": "set_end_next",
    "WaveformInsertNewSelectionCommand": "sel_new",
    "WaveformVerticalZoomInCommand": "zoom_in",
    "WaveformVerticalZoomOutCommand": "zoom_out",
    "WaveformPasteFromClipboardCommand": "wave_paste",
    "WaveformInsertAtPositionAndFocusTextBoxCommand": "wave_insert",
    "ShowPointSyncCommand": "point_sync",
    "ShowSyncAdjustAllTimesCommand": "clock",

    # lines
    "GoToNextLineCommand": "next_line",
    "GoToPreviousLineCommand": "prev_line",
    "GoToNextErrorCommand": "next_error",
    "GoToPreviousErrorCommand": "prev_error",
    "InsertLineAfterCommand": "insert_after",
    "InsertLineBeforeCommand": "insert_before",
    "MergeSelectedLinesCommand": "merge",
    "SplitAtTextBoxCursorPositionCommand": "split",
    "DeleteSelectedLinesCommand": "delete",
    "RippleDeleteSelectedLinesCommand": "delete",
    "ExtendSelectedToNextCommand": "extend_next",
    "ExtendSelectedToPreviousCommand": "extend_prev",
    "FocusSelectedLineCommand": "focus_line",
    "AutoBreakCommand": "auto_break",
    "ShowGoToLineCommand": "goto_line",

    # text
    "ToggleLinesItalicOrSelectedTextCommand": "italic",
    "ToggleCasingCommand": "case_toggle",
    "SelectionToUpperCommand": "to_upper",
    "SelectionToLowerCommand": "to_lower",

    # file
    "CommandFileNewCommand": "file_new",
    "CommandFileOpenCommand": "folder_open",
    "CommandFileSaveCommand": "save",
    "CommandFileSaveAsCommand": "save_as",

    # edit
    "UndoCommand": "undo",
    "RedoCommand": "redo",
    "SelectAllLinesCommand": "select_all",
    "InverseSelectionCommand": "inverse_sel",
    "AddOrEditBookmarkCommand": "bookmark",

    # find
    "ShowFindCommand": "find",
    "FindNextCommand": "find_next",
    "FindPreviousCommand": "find_prev",
    "ShowReplaceCommand": "replace",
    "ShowMultipleReplaceCommand": "replace_all",

    # tools
    "ShowSpellCheckCommand": "spellcheck",
    "ShowToolsFixCommonErrorsCommand": "wrench",
    "ShowToolsAiReviewCommand": "ai_review",
    "ShowAutoTranslateCommand": "translate",
    "ShowToolsBatchConvertCommand": "batch",
    "ShowToolsChangeCasingCommand": "case_toggle",
    "ShowToolsRemoveTextForHearingImpairedCommand": "hearing",
    "ShowSourceViewCommand": "source_view",
    "ListErrorsCommand": "list_errors",
    "RightToLeftToggleCommand": "rtl_toggle",
    "ToggleTranslationModeCommand": "translate_mode",

    # subtitle list / text box clipboard
    "SubtitleGridCopyCommand": "copy",
    "SubtitleGridCutCommand": "cut",
    "SubtitleGridPasteCommand": "paste",
    "FillSelectedLinesWithClipboardCommand": "paste_fill",
    "TextBoxCopyCommand": "copy",
    "TextBoxCutCommand": "cut",
    "TextBoxCut2Command": "cut",
    "TextBoxPasteCommand": "paste",
    "TextBoxSelectAllCommand": "select_all",
    "TextBoxDeleteSelectionCommand": "delete",

    # general
    "OpenDataFolderCommand": "data_folder",
    "SaveLanguageFileCommand": "lang_file",
    "SetupLikeSe4Command": "se4_badge",
    "ShowAddToNameListCommand": "name_list",
    "ShowFindDoubleWordsCommand": "double_words",
    "ShowHelpCommand": "help",
}

# Class level symbols: the dials, the reload command, and the fallback for any
# shortcut action that has no parameter symbol of its own.
CLASSES = {
    "SeCommand": "generic",
    "SeReloadCommand": "reload",
    "SeLineAdjustment": "line_dial",
    "SeVideoAdjustment": "video_dial",
    "SeWaveformZoomAdjustment": "waveform",
    "SeErrorAdjustment": "error_dial",
}


def write(name, glyph):
    body = G.get(glyph) or G["generic"]
    (OUT / f"{name}.svg").write_text(HEAD + body + TAIL, encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.svg"):
        old.unlink()

    for cls, glyph in CLASSES.items():
        write(f"{NS}.{cls}", glyph)

    for action, glyph in ACTIONS.items():
        write(f"{NS}.SeCommand___{action}", glyph)

    missing = sorted({g for g in ACTIONS.values() if g not in G})
    if missing:
        raise SystemExit(f"glyphs referenced but not defined: {missing}")

    total = len(list(OUT.glob("*.svg")))
    unused = sorted(set(G) - set(ACTIONS.values()) - set(CLASSES.values()))
    print(f"wrote {total} symbols to {OUT}")
    print(f"actions mapped: {len(ACTIONS)}, class symbols: {len(CLASSES)}")
    if unused:
        print(f"unused glyphs: {', '.join(unused)}")


if __name__ == "__main__":
    main()
