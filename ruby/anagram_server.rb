require 'socket'
require 'pp'

def start(port, lookup)
  s = TCPServer.open(port)

loop do

  Thread.new ( s.accept) do |c|
    c.puts "HEY!"
    read = c.gets.chomp
    c.puts "Looking for #{read} #{hash(read)}"
    c.puts "#{lookup[hash(read)]}"
    puts read
    c.close
  end
end

end

def hash(w)
  w.chars.sort.join
end

words = File.readlines('/usr/share/dict/words').map {|l| l.chomp.downcase }
lookup = {}
words.each {|w| lookup[hash(w)] ||= []; lookup[hash(w)] << w }
puts "Starting"
start(3000, lookup)


