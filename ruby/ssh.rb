require 'pp'

abort ('User is required') if ARGV[1].nil?
abort ('Command is required') if ARGV[2].nil?

user = ARGV[1]
command = ARGV[2]

f = File.open(ARGV[0], "r")
hosts = f.readlines
hosts.each(&:strip!)

results = []

ts = []
20.times do 
  ts << Thread.new() do
    while queue.size > 0
       run = [hosts.pop]
       run[1] = `ssh #{user}@#{run[0]} #{command}`
       results << run
    end
  end
end

ts.each(&:join)

pp results
f.close

