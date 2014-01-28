#!/bin/ruby

lines = File.readlines(ARGV[0])

i = -1
first_word = lines.each.map do |v|
  { :string => /^(?:\s+)?([^\s]+)\s?/.match(v)[1], :pos => i += 1 }
end

first_word.sort! { |x,y| x[:string] <=> y[:string] }

first_word.each do |word|
  puts lines[word[:pos]]
end

