# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.1

# Usage
# python3 mapit.py 33 Aldergrove Ave, Toronto, ON M4C 1B3

# mapIt.py - launches a map in the browser using an address from the command line or clipboard...

import webbrowser, sys, pyperclip

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
logging.disable(logging.CRITICAL) # enable/disable by commenting it in or out

if len(sys.argv) > 1:

	logging.debug("User entered the following arguments through sys.argv()")
	logging.debug(sys.argv)

	# get address from command line
	address = ' '.join(sys.argv[1:]) # sys.argv() usually gives a list of strings and you want only one string, using [1:] you avoid program name in the string (at pos 0 i.e. mapit), chopping it out

	logging.debug("The address string after joining is:  %s" % (address))
else:
	# get address from clipboard if no address argument supplied through command line
	address = pyperclip.paste()
	logging.debug("Address copied from clipboard is:  %s" % (address))

# open the address in Google Maps
logging.debug("The address is now being opened in Google Maps, in the default browser")
webbrowser.open("https://www.google.ca/maps/place/" + address)
