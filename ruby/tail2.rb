BUF_SIZE = 4096

t = ARGV[1].to_i
f = File.open(ARGV[0])
f.seek(-1, IO::SEEK_END)

if f.pos == -1 
  puts "No random access available"
  exit(0)
else
  #puts "Random access available"
end
f.seek(0, IO::SEEK_SET)

begin
  f.seek(-BUF_SIZE, IO::SEEK_END)
rescue 
end

all = ""
c = 0
start = true
while (c < t && (f.pos != 0 || start))
  buf = f.read(4096)
  c += buf.count("\n")
  all = buf + all
  begin
    f.seek(-(BUF_SIZE*2), IO::SEEK_CUR)
  rescue
    f.seek(-f.pos, IO::SEEK_CUR)
  end
  start = false
end
lines = all.split("\n")
if c < t
  puts lines
else
  puts lines [-t..-1]
end

