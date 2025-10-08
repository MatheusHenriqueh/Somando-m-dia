# Projeto calculamento de média (boletim escolar)
#Autor: Matheus Ruivo
#07/10/2025
nome = str(input("Qual é seu nome?"))
num1 = float(input("Sua nota em Matemática?"))
num2 = float(input("Sua nota em Português?"))
num3 = float(input("Sua nota em História?"))
num4 = float(input("Sua nota em Geografia?"))
num5 = float(input("Sua nota em Educação Física?"))
num6 = float(input("Sua nota em Inglês (ou sua lingua que está aprendendo)?"))
conta1 = num1 + num2 + num3 + num4 + num5 + num6
conta2 = conta1 / 6
print(nome,'sua média (boletim escolar) é', conta2)