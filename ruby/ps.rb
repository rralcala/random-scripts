#!/bin/ruby
entries = Dir.entries("/proc")

processes = entries.each.select { |entry| /^[0-9]+$/.match(entry) }

puts "PID\tNAME\tSTATE"
processes.each do |p|
    p_info = File.readlines("/proc/#{p}/stat")[0].match /^[0-9]+\s\(([^\)]+)\)\s([a-zA-Z]{1,2})\s/
    puts "#{p}\t#{p_info[1]}\t#{p_info[2]}" unless p_info.nil?
end

