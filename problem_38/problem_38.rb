#!/usr/bin/ruby
require_relative "../problem_32/problem_32"

max = 0
10.upto(10000) do |x|
  2.upto(4) do |n|
    number = ""
    1.upto(n) do |i|
      number += (x*i).to_s
    end
    if pandigital?(number)
      max = [max, number.to_i].max
    end
  end
end

print max
