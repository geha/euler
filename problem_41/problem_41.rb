#!/usr/bin/ruby
require_relative "../common/primes"
require_relative "../problem_32/problem_32"

primes = primes(7654321)
digits = [1, 2, 3, 4, 5, 6, 7]
numbers = []
digits.permutation.each { |x| numbers << x.join.to_i }
numbers.reverse.each do |number|
  if primes.include?(number)
    p number
    break
  end
end
