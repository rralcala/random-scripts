require 'pp'

abort ('User is required') if ARGV[1].nil?
abort ('Command is required') if ARGV[2].nil?

user = ARGV[1]
command = ARGV[2]

# Build a clean array of host names from a file
# And later use the Array as a queue of commands
f = File.open(ARGV[0], "r")
hosts = f.readlines
f.close
hosts.each(&:strip!)

results = []
threads = []

20.times do 
  threads << Thread.new() do
    while hosts.size > 0
       run = [hosts.pop]
       run[1] = `ssh #{user}@#{run[0]} #{command}`
       results << run
    end
  end
end

# Wait for the threads before printing results.
threads.each(&:join)
pp results

