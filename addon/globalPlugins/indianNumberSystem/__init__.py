import globalPluginHandler
import speechDictHandler
import re
import ui
import config

# Ensure plugin config section exists
if "indianNumber" not in config.conf:
    config.conf["indianNumber"] = {}

# Load saved mode (default to 0 = Indian)
Mode = int(config.conf["indianNumber"].get("mode", 0))

# Regex patterns
indian_pattern = re.compile(r'\d{6,}')
digitwise_pattern = re.compile(r'\d{2,}')

# Format number in Indian style
def indiannumber(original):
    try:
        num = abs(int(original))
    except ValueError:
        return original

    parts = []
    crore = num // 10000000
    if crore:
        parts.append(f'{crore} Crore ')
        num %= 10000000

    lakh = num // 100000
    if lakh:
        parts.append(f'{lakh} Lakh ')
        num %= 100000

    if num > 0:
        parts.append(str(num))

    return " ".join(parts)

# Match replacers
def replace_with_indian_format(match):
    return indiannumber(match.group(0))

def replace_with_digit_spacing(match):
    return '  '.join(match.group(0))

# Backup NVDA’s original speech processor
_originalProcessText = None

# Main speech processor with skip optimization
def newProcessText(text):
    global Mode
    if Mode == 0:
        if not indian_pattern.search(text):
            return _originalProcessText(text)
        return indian_pattern.sub(replace_with_indian_format, text)
    elif Mode == 2:
        if not digitwise_pattern.search(text):
            return _originalProcessText(text)
        return digitwise_pattern.sub(replace_with_digit_spacing, text)
    else:
        return _originalProcessText(text)

# Global Plugin class
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super().__init__()
        global _originalProcessText
        _originalProcessText = speechDictHandler.processText
        speechDictHandler.processText = newProcessText

    def terminate(self):
        speechDictHandler.processText = _originalProcessText

    def script_toggleIndianNumbers(self, gesture):
        global Mode
        Mode = (Mode + 1) % 3
        config.conf["indianNumber"]["mode"] = Mode
        config.conf.save()

        if Mode == 0:
            ui.message("Indian Number System Enabled.")
        elif Mode == 1:
            ui.message("Western (NVDA Default) Number System Enabled.")
        else:
            ui.message("Telephone Pattern Enabled.")

    __gestures = {
        "kb:NVDA+shift+f": "toggleIndianNumbers"
    }
