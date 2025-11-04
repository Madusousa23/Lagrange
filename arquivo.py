#Desafio Riemann
def f(x):
  return x**2
interv1 = 0
interv2 = 10
n = 5

delta = (interv2 - interv1) / n

soma = 0
for i in range(n):
  ponto_medio = interv1 + (i + 0.5) * delta
  soma = soma + f(ponto_medio)
integral = soma * delta

print("Integral: ",integral)
