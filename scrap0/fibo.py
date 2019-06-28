def fib(n):
  a, b = 0, 1
  while a < n:
    print(a, end =', ')
    a, b = b, a+b
    
def fib2(n):
  results = []
  a, b = 0, 1
  while a < n:
    results.append(a)
    a, b = b, a+b
  return results