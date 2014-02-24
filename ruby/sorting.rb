class Sorting
	def partition_qsort(a, left, right, pivot)
	  pivot_value = a[pivot]
	  a[pivot] , a[right] = a[right] , a[pivot]
	  store_index = left
	  (left..right-1).each do |i|
	    if a[i] <= pivot_value
	      a[store_index] , a[i] = a[i] , a[store_index]
	      store_index += 1
	    end
	  end
          a[store_index] , a[right] = a[right] , a[store_index]
	  store_index

	end
	def qsort(a, left, right)
		if left < right
			pivot = (right + left) / 2
			pivot_new = partition_qsort(a, left, right, pivot)
			qsort(a, left, pivot_new - 1)
			qsort(a, pivot_new + 1, right)
		end
	end
end
