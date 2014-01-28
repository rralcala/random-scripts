#!/bin/ruby

File.open(ARGV[0],'r+') do |f|
  ARGV[1].to_i.times do
    break if f.eof?
    puts f.gets
  end
end
