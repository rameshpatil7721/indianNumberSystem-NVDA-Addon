# Indian Number System – NVDA Add-on

This NVDA add-on enhances the reading of numeric values in a way that matches the Indian numbering system. It also provides a digit-by-digit reading mode for improved clarity with phone numbers or codes.

---

## 🔑 Features

- **Indian Number Mode**:  
  Reads large numbers like `12345678` as:  
  ➜ _"1 Crore 23 Lakh 45678"_

- **Western Mode (Default)**:  
  NVDA's default speech behavior — no formatting applied.

- **Digit-by-Digit Mode**:  
  Reads numbers like `987654` as:  
  ➜ _"9, 8, 7, 6, 5, 4"_

- **Keyboard Toggle**:  
  Press `NVDA+Shift+F` to switch between:
  1. Indian Number System
  2. NVDA Default (Western)
  3. Digit-by-Digit

- **Remembers Mode**:  
  The last used mode is saved and restored on NVDA restart.

---

## 🎛 How to Use

1. Install the add-on or place it in NVDA's `scratchpad/globalPlugins/` folder.
2. Press `NVDA+Shift+F` to cycle modes.
3. Navigate text using arrow keys or read it aloud — NVDA will apply the selected mode.

---

## 🔧 Developer Notes

- Written in Python
- Uses NVDA's `speechDictHandler` and `config.conf` for custom processing
- Built using the official NVDA add-on template

---

## 👨‍💻 Author

**Ramesh Patil**  
Developer of Indian Number System NVDA Add-on  
[GitHub: rameshpatil7721](https://github.com/rameshpatil7721)

---

## 📄 License

This add-on is released under the GNU General Public License (GPL v2 or later).  
See `COPYING.txt` for full terms.

---

## 🚀 Contributions

Pull requests, issues, and ideas are welcome.  
Feel free to fork and improve!
