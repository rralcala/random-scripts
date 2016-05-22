class SortedArray < Array
  def initialize(*args, &sort_by)
    @sort_by = sort_by || Proc.new { |x,y| x <=> y }
    super(*args)
    sort! &sort_by
   end

  def insert(i, v)
    return super(0, v) if size == 0
    insert_before = binary_search(v) 
    super(insert_before ? insert_before+1 : -1, v)
  end

  def binary_search(value, from=0, to=nil)
    if to == nil
        to = count - 1
    end
   
    mid = (from + to) / 2
    return  mid if from > to
  
    comp = @sort_by.call(self[mid], value)

    if comp == 1
        binary_search value, from, mid - 1
    elsif comp == -1
        binary_search value, mid + 1, to
    else
        mid
    end
  end

  def <<(v)
    insert(0, v)
  end

  alias push <<
  alias unshift <<
end

if __FILE__==$0
  a = SortedArray.new
  a << 1
  a << 3
  a << 7
  a << 100
  a << 2
  a << 1
  a << 8
  a << 11
  a << 13
  a << 12
  a.each { |v| puts v }
end 
