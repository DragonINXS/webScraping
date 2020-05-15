# Launches google maps from CLI or clipbaord address

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # get address from the CLI
    address = ' '.join(sys.argv[1:])
else: 
    # get address from the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
