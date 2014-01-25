def reverse (a, c = 0)
  if c == a.size 
   return ''
  end
  reverse(a, c + 1) + a[c].chr
end


puts reverse "hola"