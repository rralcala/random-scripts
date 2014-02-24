class Searching
  def binary_search(a, what, min, max)
    mid = nil
    if(max >= min)
      mid = (max + min) / 2
      if (a[mid] > what)
        mid = binary_search(a,what,min,mid - 1)
      elsif (a[mid] < what)
        mid = binary_search(a,what,mid+1,max)
      end
    end
    mid
  end
end
