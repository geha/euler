#!/usr/bin/ruby

require_relative "../common/primes"

primes = primes(10**6)
results = {}

for a in (-999..999)
  if a % 100 == 0
    print "a = #{a}\n"
  end
  for b in (-999..999)
    for n in (0..200)
      break unless primes.include?(n*n + a*n + b)
      if n > 20
        results[[a, b]] = n
      end
    end
  end
end

result = results.key(results.values.max)

print "#{result[0] * result[1]}\n"
