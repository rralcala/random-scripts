def reverse(a)
  (0..((a.size/2) - 1)).each { |i| a[i] , a[-i-1] = a[-i-1], a[i] }
  a
end

puts reverse "heladera"
puts reverse "zapallito"
