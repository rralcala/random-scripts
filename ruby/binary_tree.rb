module BinaryTree
Node = Struct.new :val, :left, :right

class Tree
 attr_accessor :root
 def initialize(val)
   @root = Node.new val
 end
 def inorder(node = root)
   if !node[:left].nil?
     inorder(node[:left])
   end
   puts node[:val]
   if !node[:right].nil?
     inorder(node[:right])
   end
 end
 def insert(val,cur = root)
     node = Node.new val
     if cur.val > val
       if cur.left.nil?
         cur.left = node
       else
         insert(val, cur.left)
       end
     else
       if cur.right.nil?
         cur.right = node
       else
         insert(val, cur.right)
       end
     end
     
  end
 end
end
