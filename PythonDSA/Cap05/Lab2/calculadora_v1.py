# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")
operacao = int(input("Selecione uma operação:\n\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n\nDigite sua opção(1/2/3/4):"))

while (operacao > 4 or operacao < 1):
    operacao = int(input("Selecione uma opção válida!:\n\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n\nDigite sua opção(1/2/3/4):"))

soma = lambda x,y: x + y
sub = lambda x,y: x - y
mult = lambda x,y: x * y
div = lambda x,y: x / y

num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

if(operacao == 1):
    result = soma(num1,num2)
    print("Resultado: " + str(num1) + " + " + str(num2) + " = " + str(result))
elif(operacao == 2):
    result = sub(num1,num2)
    print("Resultado: " + str(num1) + " - " + str(num2) + " = " + str(result))
elif(operacao == 3):
    result = mult(num1,num2)
    print("Resultado: " + str(num1) + " * " + str(num2) + " = " + str(result))
elif(operacao == 4):
    result = div(num1,num2)
    print("Resultado: " + str(num1) + " / " + str(num2) + " = " + str(result))