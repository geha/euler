#!/usr/bin/env python
# -*- coding: utf-8 -*-

def compare(a, b):
	ret = True

	a = str(a)
	b = str(b)

	if (len(a) != len(b)):
		ret = False

	else:
		for i in range(0, len(a)):
			if (a[i] not in b):
				ret = False

	return ret


def main():

	for i in range(2, 10**7):
		isSame = True
		for j in range(2, 7):
			if (compare(i, i*j) == False):
				isSame = False

		if (isSame):
			print(i)
			break

	return 0

if __name__ == '__main__':
	main()

