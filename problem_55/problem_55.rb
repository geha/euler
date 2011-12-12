#!/usr/bin/ruby

def is_palindrome? number
	number = number.to_s
	length = number.length
	if length >= 2
		number[0..(length-1)/2] == number[-((length+1)/2)..-1].reverse
	else
		false
	end
end

def is_lychrel? number
	result = true

	50.times do
		number += number.to_s.reverse.to_i
		if is_palindrome? number
			result = false
			break
		end
	end
	result
end

counter = 0

for i in 1..9999
	if is_lychrel? i
		counter += 1
	end
end

puts counter
