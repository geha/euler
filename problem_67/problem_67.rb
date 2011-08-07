#!/usr/bin/ruby
require "../problem_18/pyramid"

py = Pyramid.new IO.read("triangle.txt").gsub!(/\n/, " ").split(/ /)

puts py.max_route
