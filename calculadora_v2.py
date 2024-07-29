saida = ''
def adicao(a, b):
    return a + b
def subracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    if operacao in ('+', 'adição'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtração'):
        resultado = subracao(num1, num2)
    elif operacao in ('*', 'multiplicação'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisão'):
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou o nome da operação): ").strip().lower()
        resultado = calculadora(num1, num2, operacao)
        print(f'Resultado da operação: {resultado}')

    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

    saida = input("Deseja continuar? (S/N): ").strip().lower()
    if saida not in ('s', 'n'):
        print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")
        saida = 'n'
