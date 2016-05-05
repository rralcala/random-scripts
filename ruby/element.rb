# From http://www.brianstorti.com/implementing-a-priority-queue-in-ruby/
class Element
  include Comparable

  attr_accessor :name, :priority

  def initialize(name, priority)
    @name, @priority = name, priority
  end

  def <=>(other)
    @priority <=> other.priority
  end
end
