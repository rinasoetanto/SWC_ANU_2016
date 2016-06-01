#!/usr/bin/env python

import sys

def celsius_to_fahr(temp_c):
	temp_f = temp_c * 1.8 + 32
	return temp_f

celc = float(sys.argv[1])
print(celsius_to_fahr(celc))

