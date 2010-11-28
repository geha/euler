#!/usr/bin/env python
# -*- coding: utf-8 -*-

powlist = []
for i in range(0,10):
	powlist.append(i**5)

def isPowSum(number):
	ret = False
	sum = 0
	string = str(number)
	for i in range(0, len(string)):
		sum += powlist[int(string[i])]

	if (number == sum):
		ret = True

	return ret

def main():
	sum = 0
	for i in range(3, 999999):
		if (isPowSum(i)):
			sum += i
			print(i)

	print(sum)

	return 0

if __name__ == '__main__':
	main()

