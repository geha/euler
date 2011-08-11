#!/usr/bin/ruby

def pandigital? number
  result = false
  number = number.to_s
  if number.length == 9
    digits = []
    number.chars { |c| digits << c.to_i }
    result = digits.sort == [1, 2, 3, 4, 5, 6, 7, 8, 9]
  end
  result
end

if __FILE__ == $0

  products = []
  for i in (1..9876)
    max = 10**(4-Math.log10(i).to_i)
    max.downto(i) do |j|
      if pandigital?(i.to_s + j.to_s + (i*j).to_s)
        products << i*j unless products.include?(i*j)
      end
    end
  end

  sum = 0
  products.each { |x| sum += x }
  print sum

end
