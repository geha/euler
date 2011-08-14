#!/usr/bin/ruby

primes = [2, 3, 5, 7, 11, 13, 17]
pandigitals = []

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9].permutation.each do |number|
  number = number.join
  add = true
  primes.each_index do |i|
    if not (number[i+1..i+3].to_i % primes[i] == 0)
      add = false
      break
    end
  end

  if add
    pandigitals << number.to_i
  end
end

sum = 0
pandigitals.each { |x| sum += x }
p sum
