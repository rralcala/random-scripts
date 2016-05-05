require 'pp'

class CrappyHash
  include Enumerable

  def initialize(size = 10)
    @buckets = []
    @size = size
  end  

  def insert(k,v)
    index = hash_func(k) % @size
    @buckets[index] ||= []
    element = @buckets[index].index { |key_value| key_value[0] == k }
    # Overwrite if the key already exists.
    if element.nil? 
      @buckets[index] << [k,v]
    else
      @buckets[index][element][1] = v
    end
  end

  def retrieve(k)
    index = hash_func(k) % @size
    return nil if @buckets[index].nil?
    # As per our insert method, there should be only one
    element = @buckets[index].find { |key| key[0] == k }
    element[0] unless element.nil?
  end

  def each(&block)
    @buckets.each do |b|
      b.each { |v| block.call(v[1]) } unless b.nil?
    end
  end

  private

  def hash_func(k)
    size = k.size 
    val = 0
    val = k[0].ord if size > 0
    val = k[1].ord << 8 if size > 1
    val = k[2].ord << 16 if size > 2
    val = k[3].ord << 24 if size > 3
    val
  end
end

m = CrappyHash.new(10)

pp m.retrieve('element')

m.insert('1',2)
m.insert('1',3)
m.insert('abcdef',4)
m.insert('doggy', 'hola')
m.insert('element', 5)

puts "Retrieve:"
pp m.retrieve('element')
pp m.retrieve('noexiste')

puts "Iterate:"
m.each { |v| puts v } 
