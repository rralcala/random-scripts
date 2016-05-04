require 'pp'
def coins(amount, coins)

coins.sort!
result = []

coins.size.times do
  result << Array.new([amount, 1].max) { 0 }
end

(1..amount).each do |total|
  i = 0
  coins.each do |coin|
    if total >= coin
      if i > 0
        result[i][total] = [result[i][total-coin] + 1, result[i-1][total] ].min 
      else
        result[i][total] = result[i][total-coin] + 1
      end
    elsif i > 0
      result[i][total] = result[i-1][total]
    else
      result[i][total] = -1
    end
    i = i + 1
  end
end

min = -1

result.each do |line|
  min = line[-1] if line[-1] < min || min == -1
end

min
end



def coins_r(a, coins, sum = 0, depth = 0)

  return -1  if sum > a
  return depth if sum == a
  min = -1

  coins.each do |v|
    temp = coins_r(a, coins, v+sum, depth+1)
    min = temp if (temp < min && temp > -1) || min == -1
  end 

  return min
end

puts coins(7130, [294,128,316,466,108,463,321,490])
puts coins(5897, [46,295,485,415,449,379,183,323])
puts coins(100, [2,5])
puts coins(11, [1, 2, 5])
