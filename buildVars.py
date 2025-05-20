# -*- coding: UTF-8 -*-

def _(arg):
    return arg

addon_info = {
    "addon_name": "indianNumberSystem",  # Internal name
    "addon_summary": _("Indian Number System"),
    "addon_description": _(
        "This NVDA add-on improves how numbers are spoken by the screen reader, "
        "especially for users in India who prefer the crore/lakh format instead of "
        "the western million/billion format.\n\n"

        "🔢 Features\n"
        "✅ Indian Number Mode\n"
        "• Automatically formats numbers with 6 or more digits into Indian style\n"
        "➤ Example: 12345678 → \"1 Crore 23 Lakh 45678\"\n\n"

        "✅ Western Mode (NVDA Default)\n"
        "• No formatting — NVDA reads numbers as it normally does\n"
        "➤ Example: 12345678 → \"twelve million three hundred forty-five thousand six hundred seventy-eight\"\n\n"

        "✅ Digit-by-Digit Mode\n"
        "• Reads all numbers (with 2 or more digits) one digit at a time\n"
        "➤ Example: 987654 → \"9 8 7 6 5 4\" (good for phone numbers, OTPs)\n\n"

        "✅ Keyboard Shortcut\n"
        "• Press NVDA + Shift + F to toggle between modes\n"
        "• Cycles through: Indian → Western (default) → Digit-by-digit → Indian..."
    ),
    "addon_version": "1.1",
    "addon_author": "Ramesh Patil <rameshpatil.rp019@gmail.com>",
    "addon_url": "https://github.com/rameshpatil7721/indianNumberSystem-NVDA-Addon/releases/tag/v1.1",
    "addon_sourceURL": None,
    "addon_docFileName": "readme.html",
    "addon_minimumNVDAVersion": "2024.1",
    "addon_lastTestedNVDAVersion": "2024.4.2",
    "addon_updateChannel": None,
    "addon_license": "GPL",
    "addon_licenseURL": "https://www.gnu.org/licenses/gpl-2.0.html",
}

pythonSources = ["addon/globalPlugins/indianNumber/*.py"]
i18nSources = pythonSources + ["buildVars.py"]
excludedFiles = []
baseLanguage = "en"
markdownExtensions = []
brailleTables = {}
symbolDictionaries = {}
