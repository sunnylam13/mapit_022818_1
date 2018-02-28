# Scratch File

For recording project musings and issues and lessons.

## Wednesday, February 28, 2018 6:34 PM

You have to know how to construct the string of the address for Google...

	https://www.google.ca/maps/place/33+Aldergrove+Ave,+Toronto,+ON+M4C+1B3/@43.6819557,-79.3150798,17z/data=!3m1!4b1!4m5!3m4!1s0x89d4cc6d34fb5c37:0xc7c9779d9483dbd3!8m2!3d43.6819557!4d-79.3128911?hl=en

except you can skip the extra meta data that's usually attached and it should work...

	https://www.google.ca/maps/place/33+Aldergrove+Ave,+Toronto,+ON+M4C+1B3

just tried it and it works...

so convert that...

	https://www.google.ca/maps/place/your_address_string

where `your_address_string` is the address you want to map

Resulting output on run for address...

	MacBook-Air:mapit sunnyair$ python3 mapit.py 33 Aldergrove Ave, Toronto, ON M4C 1B3
	 2018-02-28 18:45:34,732 - DEBUG - User entered the following arguments through sys.argv()
	 2018-02-28 18:45:34,733 - DEBUG - ['mapit.py', '33', 'Aldergrove', 'Ave,', 'Toronto,', 'ON', 'M4C', '1B3']
	 2018-02-28 18:45:34,733 - DEBUG - The address string after joining is:  33 Aldergrove Ave, Toronto, ON M4C 1B3

