#!/usr/bin/ruby

class Pyramid
  @values

  def initialize values
    @values = values.map { |value| value.to_i }
  end

  def values=(value)
    @values = value
  end

  def sum
    sum = 0
    @values.each { |value| sum += value }
    sum
  end

  def sub_pyramid left
    result = nil
    if valid?
      length = @values.length
      values = @values.clone
      values[0] = nil
      if left
        index = 2
        add = 3
      else
        index = 1
        add = 2
      end

      while index < length
        values[index] = nil
        index += add
        add += 1
      end
      values.compact!
      result = Pyramid.new values
    end
    result
  end

  def valid?
    result = false

    if not @values.empty?
      length = 0
      self.depth.times { |i| length += i+1 }

      if length == @values.length
        result = true
      end
    end
    result
  end

  def max
    if valid?
      max = @values[0]
      if @values.length > 1
        if sub_pyramid(true).sum <= sub_pyramid(false).sum
          max += sub_pyramid(false).max
          puts @values[0]
        else
          max += sub_pyramid(true).max
          puts @values[0]
        end
      else
        return max
      end
      max
    end
  end

  def depth
    if not @values.empty?
      length = @values.length
      depth = 1

      while length > 0
        length -= depth
        depth += 1
      end

      depth -= 1
    end
    depth
  end

  def show
    if valid?
      values = @values.clone
      max_entry_length = @values.sort { |x, y| y <=> x }.first.to_s.length
      self.depth.times do |i|
        values.slice!(0, i+1).each { |item| print "#{item.to_s.ljust(max_entry_length + 1)}" }
        print "\n"
      end
    end
  end
end


# test pyramid
py = Pyramid.new %w[3 7 4 2 4 6 8 5 9 3]

#big_py = Pyramid.new %w[75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23]
big_py = Pyramid.new %w[75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23]
