#!/usr/bin/ruby

def dec_fraction denominator
  result = ""
  numerator = 1
  recurring = []
  while numerator != 0
    result += (numerator / denominator).to_s
    numerator = numerator.remainder(denominator)*10
    break if recurring.include?(numerator)
    recurring << numerator
  end
  if not recurring.include?(0)
    result.insert(recurring.index(numerator)+1, "(")
    result += ")"
  end
  if recurring.length > 1
    result.insert(1, ".")
  end
  result
end

max = 0
d = 0

for i in (1..1000) do
  cycle = dec_fraction(i).match(/\(\d+\)/)
  if cycle.respond_to?(:length)
    length = cycle.to_s.length - 2
    if length > max
      max = length
      d = i
    end
  end
end

puts d
