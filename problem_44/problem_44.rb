#!/usr/bin/ruby
require "Set"

def pent number
  number * (3 * number - 1) / 2
end

pentagonals = Set.new

1.upto(3000) { |n| pentagonals << pent(n) }

min = pentagonals.max

pentagonals.each do |j|
  pentagonals.each do |k|
    if pentagonals.include?(j + k) and pentagonals.include?(k-j)
      min = [(k-j).abs, min].min
    end
  end
end

p min
