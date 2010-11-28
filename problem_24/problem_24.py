#!/usr/bin/env python
# -*- coding: utf-8 -*-

def perm(number):
	if (number < 1000000000):
		string = str(0) + str(number)
	else:
		string = str(number)
	unique = False
	#~ for i in range (0, len(string)):
		#~ for j in range (i+1, len(string)):
			#~ if (string[i] == string[j]):
				#~ unique = False

	if (str(9) in string and str(8) in string and str(7) in string and str(6) in string and str(5) in string and str(4) in string and str(3) in string and str(2) in string and str(1) in string and str(0) in string):
		unique = True

	return unique

def main():
	counter = 0
	i = 123456789
	while (i <= 9876543210):
		if (perm(i)):
			counter += 1

		if counter == 1000000:
			print()
			print(i)
			break

		i += 1
	return 0


if __name__ == '__main__':

	main()
