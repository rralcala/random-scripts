def even_numbers(n)
i = 1
n.times {  yield i ; i += 2 }
end

even_numbers(100) { |v| puts v }
