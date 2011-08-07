#!/usr/bin/ruby

class Pyramid
  @values

  def initialize values
    values.map! { |item| item.to_i }
    @values = []
    depth = 1
    while values.length > 0
      @values << values.slice!(0, depth)
      depth += 1
    end
  end

  def values=(value)
    @values = value
  end

  def valid?
    result = false
    @values.length.times do |level|
      result = @values[level].length == level + 1
      break unless result
    end
    result
  end

  def max_route
    values = []
    @values.each { |ary| values << ary.clone }

    values.each_index do |row|
      if row > 0
        values[row].each_index do |item|
          case item
            when 0
              values[row][item] += values[row-1].first
            when values[row].length
              values[row][item] += values[row-1].last
            else
              values[row][item] += values[row-1].slice(item-1, 2).max
          end
        end
      end
    end
    values.last.max
  end
end


py = Pyramid.new %w[3 7 4 2 4 6 8 5 9 3]
big_py = Pyramid.new %w[75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 07 23]

p big_py.max_route


