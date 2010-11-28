#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	list = []
	for a in range (2, 101):
		for b in range (2, 101):
			number = a**b
			if (number not in list):
				list.append(number)

	print(len(list))

	return 0

if __name__ == '__main__':
	main()

