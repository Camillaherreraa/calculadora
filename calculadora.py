def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b



print("=== CALCULADORA ===")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(f"Soma: {somar(a, b)}")
print(f"Subtração: {subtrair(a, b)}")
print(f"Multiplicação: {multiplicar(a, b)}")
print(f"Divisão: {dividir(a, b)}")