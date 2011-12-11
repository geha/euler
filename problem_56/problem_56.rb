#!/usr/bin/ruby
max = 0

for a in 1..99
	for b in 1..99
		c = a**b
		max = [c.to_s.chars.inject(0) {|sum, digit| sum + digit.to_i}, max].max
	end
end

puts max
