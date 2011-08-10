#!/usr/bin/ruby

require "Set"

def sieve limit
  if limit > 0
    primes = [true] * (limit + 1)
    primes[0] = false
    primes[1] = false

    for i in (2..Math.sqrt(limit)+1.to_i)
      if (primes[i])
        for j in (i**2..limit).step(i)
          primes[j] = false
        end
      end
    end
    primes
  end
end

def prime? number
  if number < 2
    false
  else
    sieve(number)[number]
  end
end

def primes limit
  sieve = sieve limit
  primes = Set.new
  sieve.each_index {|i| primes << i if sieve[i]}
  primes
end
