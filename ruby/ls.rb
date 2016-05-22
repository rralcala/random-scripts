#!/bin/ruby

require 'sorted_array'

dir_path = ARGV[0]

exit(0) if dir_path.nil?

unless File.directory?(dir_path)
  puts "#{dir_path} is not a directory."
  exit(1)
end

entries = SortedArray.new

# Exclude hidden files
Dir.entries(dir_path).each do |d|
 # /^(?!\.)/.match(d) Useful for custom filters, not here.
 entries << d if d[0] != '.'
end

entries.each { |entry| puts entry }
