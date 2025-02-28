N=int(input())

Segundos = int(N % 60)
Minutos = int(N / 60)
Horas = int(Minutos / 60)

print(f"{Horas}:{Minutos % 60}:{Segundos}")
