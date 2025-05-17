# -*- coding: UTF-8 -*-

def _(arg):
	return arg

addon_info = {
	"addon_name": "indianNumberSystem",  # Internal name
	"addon_summary": _("Indian Number Formatter"),
	"addon_description": _("Reads large numbers in Indian number system (crore/lakh) or digit-by-digit."),
	"addon_version": "1.1",
	"addon_author": "Ramesh Patil <rameshpatil.rp019@gmail.com>",
	"addon_url": None,  # Optional: add your GitHub repo or blog URL if you have one
	"addon_sourceURL": None,
	"addon_docFileName": "readme.html",  # You can change this if your doc file is .md or named differently
	"addon_minimumNVDAVersion": "2022.1",
	"addon_lastTestedNVDAVersion": "2024.3",
	"addon_updateChannel": None,
	"addon_license": "GPL",
	"addon_licenseURL": "https://www.gnu.org/licenses/gpl-2.0.html",
}

# Path to your Python files
pythonSources = ["addon/globalPlugins/indianNumber/*.py"]

# Include this file for translation if needed
i18nSources = pythonSources + ["buildVars.py"]

excludedFiles = []

baseLanguage = "en"

markdownExtensions = []

brailleTables = {}

symbolDictionaries = {}
