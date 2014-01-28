#!/bin/ruby

if ARGV[1].nil?
  f = STDIN
  lines = ARGV[0]
else
  f = File.open(ARGV[0],'r+')
  lines = ARGV[1]
end

lines.to_i.times do
  break if f.eof?
  puts f.gets
end

