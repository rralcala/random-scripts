require './binary_tree.rb'
require 'pp'
module BinaryTree
  # Create a binary tree from an array recursively  
  def create_binary(a, startid, endid)
     return nil if startid > endid
     mid = (endid + startid) / 2
     root = Node.new a[mid]
     root.left = create_binary(a, startid, mid - 1)
     root.right = create_binary(a, mid + 1, endid)
     root

  end
end 

include BinaryTree
puts 'hola'
a = 10.times.map { Random.rand 200 }.sort
a = (0..10).to_a
t = Tree.new 1
t.root = create_binary(a , 0 , a.size - 1)
t.bfs
