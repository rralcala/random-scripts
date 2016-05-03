def merge(a, ileft, iright, iend, b)
  i = ileft
  j = iright

  (ileft..iend-1).each do |k|
    if(i < iright && ( j >= iend || a[i] <= a[j]))
      b[k] = a[i]
      i += 1
    else
      b[k] = a[j]
      j+= 1
    end
  end
end

def merge_sort(a, b, n)
  width = 1
  while (width < n) do
    i = 0
    while (i < n)
      merge(a, i, [i + width, n].min, [i + 2*width, n].min, b)
      i = i + 2 * width
    end
    copy(a,b,a.size)
    width *= 2
  end
end

def copy(a,b,n)
  (0..n-1).each do |i|
    a[i] = b[i]
  end
end

a = [ 1 , 3 , 234, 5, 6, 44, 78 , 3 , 9 , 0 ]
b = []
merge_sort(a,b,a.size)
puts "#{a}"

