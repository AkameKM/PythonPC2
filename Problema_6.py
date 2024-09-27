###################### Problema 6 #########################

def fibonacci():

      prev = 0
      next = 1
      while prev <=50:
          print(prev)
          fib = prev + next
          prev = next
          next = fib
   
fibonacci()



