def eval_rpn(tokens)
  stack = []
  while tokens.size > 0
    val = tokens.shift
    if val.to_i.to_s == val
      stack.push(val.to_i)
    else
      oper1 = stack.pop.to_i
      oper2 = stack.pop.to_i
      case val
        when "+"
          result = oper2 + oper1
        when "-"
          result = oper2 - oper1
        when "*"
          result = oper2 * oper1
        when "/"
          result = oper2 / oper1
          # Ruby doesn't round negatives like C
          if (oper2 < 0 && oper1 > -1) || (oper1 < 0 && oper2 > -1)
            result = (oper2.to_f / oper1.to_f).ceil()
          else
            result = oper2 / oper1
          end
        else
         raise "Err"
       end
       stack.push result
    end
  end
  stack.shift.to_i
end
