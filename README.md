# Keylogger_Software
A keylogger or keystroke logger/keyboard capturing is a form of malware or hardware that keeps track of and records your keystrokes as you type. It takes the information and sends it to a hacker using a command-and-control (C&amp;C) server.

# Keylogger and Activity Tracker

This Python project captures keystrokes, clipboard content, screenshots, and active window titles. It logs these activities to files, making it useful for monitoring system usage. **Note:** This software should only be used on systems where you have explicit permission to do so.

## Features

- **Keylogger**: Logs every key press.
- **Clipboard Logger**: Monitors and logs clipboard content.
- **Screen Capture**: Takes periodic screenshots.
- **Activity Tracker**: Tracks and logs active windows and running processes.

## Requirements

- Python 3.x
- Required Python packages (can be installed via pip):
  - `pynput`
  - `pyperclip`
  - `Pillow`
  - `psutil`
  - `pygetwindow`

Install the required packages with:

```bash
pip install pynput pyperclip Pillow psutil pygetwindow
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Pavann36/Keylogger_Software.git
   cd Keylogger_Software
   ```

2. Ensure the required Python packages are installed as shown above.

3. Run the script:

   ```bash
   python keylogger.py
   ```

## Logging Details

- **Keystrokes**: Saved to `Documents/keylogger_logs/keylog.txt`.
- **Clipboard Content**: Saved to `Documents/keylogger_logs/clipboard_log.txt`.
- **Screenshots**: Saved to `Documents/keylogger_logs/screenshots/`.
- **Active Windows & Processes**: Saved to `Documents/keylogger_logs/process_log.txt`.

## Security and Ethical Considerations

- Use this software only on systems where you have permission.
- Unauthorized monitoring of individuals' activities is illegal in many jurisdictions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

The developers of this software are not responsible for any misuse of this program. This tool is provided for educational purposes only.

---
