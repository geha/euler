#!/usr/bin/ruby
require "linguistics"
Linguistics::use( :en ) # extends Array, String, and Numeric

sum = 0

for number in (1..1000)
  sum += number.en.numwords.gsub(/[ -]/, "").length
end

puts sum
