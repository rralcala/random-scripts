class IO
  TAIL_BUF_LENGTH = 1 << 16

  def tail(n)
    return [] if n < 1
    lines = []
    nr = 0
    begin
    while nr < n
     lines[nr] = readline
     nr+=1  
    end
    while new_line = readline
       lines.shift(1)
       lines.push(new_line)
    end
    rescue
    end
    lines

#    if size > TAIL_BUF_LENGTH
#      seek -TAIL_BUF_LENGTH, SEEK_END
#    end
#    buf = ""
#    while buf.count("\n") <= n 
#      buf = read(TAIL_BUF_LENGTH) + buf
#      if pos < 2 * TAIL_BUF_LENGTH
#        break
#      end
#      seek 2 * -TAIL_BUF_LENGTH, SEEK_CUR
#    end

#    unless pos < TAIL_BUF_LENGTH
#      buff_size = pos - TAIL_BUF_LENGTH
#      seek -buff_size - TAIL_BUF_LENGTH, SEEK_CUR
#      buf = read(buff_size) + buf
#    end
#    array = buf.split("\n")
#    if array.size > n
#      array[-n..-1]
#    else
#      array
#    end
  end
end


unless ARGV[0].nil? 
  begin
       puts STDIN.tail(ARGV[0].to_i)
  rescue Errno::EPIPE
    
  end
end
