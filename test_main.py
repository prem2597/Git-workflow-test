from main import order


assert(order(10) == 1)
assert(order('abcd') == 1)
assert(order(0) == 0)
assert(order(1234) == 3)
assert(order('10') == 1)
assert(order(1/0) == 1/0)
assert(order(123.456) == 3)
assert(order(0/0) == 1)