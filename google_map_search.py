# Run the program with address
# Automatically load the Google Maps and search the address that you typed in terminal window
# Use the address in clipboard if the program is executed without any address 

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
