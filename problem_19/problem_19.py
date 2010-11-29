#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, timedelta

def main():

	start = date(1901, 1, 1)
	end = date(2000, 12, 31)
	d = timedelta(days = 1)
	count = 0;

	while (start.toordinal() <= end.toordinal()):
		if (start.weekday() == 6 and start.day == 1):
			count += 1

		start += d

	print (count)

	return 0

if __name__ == '__main__':
	main()

