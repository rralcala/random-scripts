# Implement basic operations that can be performed on a binary tree
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

  # Insert a node trying to build a binary search tree
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

  # Depth first search
  def dfs()
    do_dfs(@root)
  end
  def do_dfs(cur)
     puts cur.val
     do_dfs(cur.left) if !cur.left.nil?
     do_dfs(cur.right) if !cur.right.nil?
  end

  # Breadth first search
  def bfs()
    queue = []
    do_bfs(queue, @root)
  end

  def do_bfs(queue, cur)
    queue.push cur
    while queue.length > 0
      cur = queue.shift 
      puts cur.val
      queue.push cur.left if !cur.left.nil?
      queue.push cur.right if !cur.right.nil?
    end
  end
 end

end
