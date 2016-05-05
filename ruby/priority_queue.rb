require 'sorted_array'
require 'element'
class PriorityQueue
  def initialize
    @elements = SortedArray.new
  end

  def <<(element)
    @elements << element
  end

  def pop
    @elements.pop
  end
end

if __FILE__==$0
  q = PriorityQueue.new
  q << Element.new("bar", 1)
  q << Element.new("foo", 3)
  q << Element.new("baz", 2)
  q << Element.new("miau", 3)

  p q.pop.name # => "foo"
  p q.pop.name
  p q.pop.name
  p q.pop.name
end
