def factorial (n):
  i=1
  factorial=1
  for i in range (1,n+1):
    factorial=factorial*i
  return(factorial)
print(factorial(2))

def operacion(n):
  j=0
  sumatoria=0
  if n == 1:
    return -1
  else:
    sumatoria = -1
    for i in range(1,n,1):
        j = j+2
        if i % 2 != 0:
            sumatoria=sumatoria+j/factorial(j)
            print(sumatoria)
        else:
            sumatoria=sumatoria-j/factorial(j)
            print(sumatoria)
    return sumatoria







n=int(input("ingrese n: "))      
print(operacion(n))