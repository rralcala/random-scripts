#!/bin/ruby
require 'csv'
require 'date'

if ARGV[0].nil?
	abort 'CSV filename required.'
end

csv_text = File.read(ARGV[0])
csv = CSV.parse(csv_text)
csv.each do |line|
  unless line[1].nil?
    Date.parse line[1]
  end
end
