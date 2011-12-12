#!/usr/bin/ruby

keys = File.open("keylog.txt").readlines

weights = Hash.new(0.0)
count = Hash.new(0)

keys.each do |key|
	(key.to_s.length-1).times do |i|
		weights[key[i]] += i+1
		count[key[i]] += 1
	end
end

weights.each {|k, v| weights[k] = v/count[k]}
weights = weights.sort {|a, b| a[1]<=>b[1]}

weights.each {|v| print v[0]}
