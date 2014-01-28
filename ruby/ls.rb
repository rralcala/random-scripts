#!/bin/ruby

entries = Dir.entries('.').select do |d|
  /^(?!\.)/.match(d)
end

entries.sort.each { |e| puts e }
