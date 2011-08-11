#!/usr/bin/ruby

results = Hash.new(0)
for p in (2..1000).step(2)
  if p % 10 == 0
    p p
  end
  1.upto(p) do |a|
    p.downto(a) do |b|
      c = p - a - b
      if (a**2)+(b**2) == (c)**2
        results[p] += 1
      end
    end
  end
end

p results.key(results.values.max)
