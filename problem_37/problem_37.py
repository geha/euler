#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isTruncatable (value):
	ret = True
	value = str(value)
	for i in range(1, len(value)):
		if (not isPrime(int(value[i:]))):
			ret = false
		elif (not isPrime(int(value[:i]))):
			ret = false

	return ret



def main():

	print (sys.path)

	#~ print(isTruncatable(3797))

	return 0

if __name__ == '__main__':
	main()
