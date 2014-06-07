#!/bin/ruby
Node = Struct.new(:next, :val)

def print_list(head)
  p = head
  while(!p.nil?)
    puts p.val
    p = p.next
  end
end

def gen_list(n)
  p = head = Node.new(nil, Random.rand(100))
  (n - 1).times do 
    p.next = Node.new(nil, Random.rand(100))
    p = p.next 
  end

  head
end

def list_len(head)
  p = head
  len = 0
  while !p.nil?
    p = p.next
    len += 1
  end

  len
end

def merge_sort(head)
  return head if(head.nil? || head.next.nil?)
  count = list_len head
  middle = count / 2
  r = head
  (middle - 1).times { r = r.next }
  r.next, r = nil, r.next
  h1 = merge_sort(head)
  h2 = merge_sort(r)

  merge(h1,h2) 
end

def merge(h1,h2)
  fakeHead = Node.new(nil, 1)
  pNew = fakeHead

  while(!h1.nil? || !h2.nil?)
    if(h1.nil?)
      pNew.next = Node.new(nil, h2.val)
      h2 = h2.next
      pNew = pNew.next
    elsif (h2.nil?)
      pNew.next = Node.new(nil, h1.val)
      h1 = h1.next
      pNew = pNew.next
    elsif (h1.val == h2.val)
      pNew.next = Node.new(Node.new(nil, h2.val), h1.val)
      pNew = pNew.next.next
      h1 = h1.next
      h2 = h2.next
    elsif (h1.val < h2.val)
      pNew.next = Node.new(nil, h1.val)
      pNew = pNew.next
      h1 = h1.next
    else
      pNew.next = Node.new(nil, h2.val)
      pNew = pNew.next
      h2 = h2.next
    end
  end
  fakeHead.next
end

list = gen_list(10)
print_list list
list = merge_sort list
print_list list
