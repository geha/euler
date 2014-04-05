#!/usr/bin/ruby
require "../common/primes"

primes = (primes 10**6).to_a.sort!

puts primes
