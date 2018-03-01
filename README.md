# Map It Demo Program Using the `webbrowser` module

The program gets a street address from the command line arguments or the clipboard.

It then opens the web browser to the Google Maps page for the supplied address.

By default the script will use the command line arguments instead of the clipboard.  

If there are no command line arguments then the program will use clippings on the clipboard.

## Actions

* read the command line arguments from sys.argv

* read the clipboard contents

* call the `webbrowser.open()` function to open the web browser

## Test Address

33 Aldergrove Ave, Toronto, ON M4C 1B3

## Execution

using the test address

	python3 mapit.py 33 Aldergrove Ave, Toronto, ON M4C 1B3

otherwise

	python3 mapit.py ADDRESS

## References

ABSP:  386