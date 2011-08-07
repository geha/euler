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
