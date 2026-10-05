import math
"""
print('Funcionou!!!')
"""
exercice_counter = 0
activity_counter = 0

print(f'\nExercicio {exercice_counter} - escrever uma mensagem na tela')
print('Hey, I am Python')

exercice_counter += 1
print(f'\nExercicio {exercice_counter} - calculo de valores')

vendas_mes = 12500.00

meta = 100000.00

desvio = vendas_mes - meta

print(f'O valor de vendas do mes é de: {vendas_mes}')
print(f'O valor da meta é de: {meta}')
print(f'O desvio da meta é de: {desvio}')

print(f'\nExercicio {exercice_counter} - Estimativa mensal')

receita_mensal = 18000.00

estimativa_custos = 12500.00

resultado = receita_mensal - estimativa_custos
margem = (resultado / receita_mensal) * 100

# indica se a margem calculada é aceitável ou não, retornando True ou Falseo
margem_aceitavel = margem >= 25.00

print(f'O resultado da estimativa mensal é de: {resultado}')
print(f'A margem de lucro estimada é de: {margem:.2f}%')  # 2 casas decimais
# indica a validação acima é verdadeira ou falsa
print(f'A margem de lucro é aceitável? {margem_aceitavel}')

exercice_counter += 1
print(f'\nExercicio {exercice_counter} - If/Elif/Else')

vendas_mes = 0.00  # inicializa a variavel vendas_mes com valor 0.00
# vendas_mes = float(input('Digite o valor de vendas do mes: '))#indica input do utilizador, convertendo para float

vendas_mes = 12500.00  # valor de vendas do mes

meta = 100000.00

if vendas_mes > meta:  # verifica se o valor de vendas do mes é maior ou igual a meta
    print('Parabéns, você ultrapassou a meta de vendas do mês!')
elif vendas_mes == meta:
    print('Parabéns, você igualou a meta de vendas do mês!')
else:
    print('Infelizmente você não atingiu a meta de vendas do mês.')

activity_counter += 1
print(f'\nAtividade {activity_counter} - If/Elif/Else')

campanha = 20.1

if campanha < 0:
    print('Campanha negativa')
elif campanha <= 20:
    print('Campanha positiva')
else:
    print('Campanha muito positiva')

print(f'Valor da campanha {campanha}')

exercice_counter += 1
print(f'\nExercicio {exercice_counter} - Ciclo For')

total_vendas = 0.00
meses_acima_meta = 0

for vendas in [12500.00, 15000.00, 20000.00, 8000.00, 100000.00, 5000.00]:
    total_vendas += vendas  # Acumulador  de valor total de vendas
    if vendas > 12000.00:
        meses_acima_meta += 1  # Contador de meses acima da meta

print(f'Total de vendas: {total_vendas}')
print(f'Número de meses acima da meta: {meses_acima_meta}')


exercice_counter += 1
print(f'\nExercicio {exercice_counter} - Ciclo While')

saldo = 0.00
contadorDoCiclo = 0

while saldo < 100.00:
    print(f'Saldo atual: {saldo}')
    contadorDoCiclo += 1
    saldo += 25.00  # Adiciona 25.00 ao saldo

print(f'Saldo final: {saldo}, com {contadorDoCiclo} iterações')

activity_counter += 1
print(f'\nAtividade {activity_counter} - For e While')

meta_semanal= 5000
total_semanal = 0

for vendas_diarias in [850, 1200, 980, 1450, 1100]:
    total_semanal += vendas_diarias  # Acumulador de vendas diarias

if total_semanal >= meta_semanal:
    print(f'Parabéns, você atingiu a meta semanal de vendas: {total_semanal}€')
else:
    print(f'Infelizmente você não atingiu a meta semanal de vendas: {total_semanal}€ de 5000€')    

exercice_counter += 1
print(f'\nExercicio {exercice_counter} - Matematica e Funções')  

x = (int(input('Digite um número para calcular a raiz quadrada: ')))

raiz_quadrada = math.sqrt(x)  # calcula a raiz quadrada de x

print(f'A raiz quadrada de {x} é: {raiz_quadrada:.2f}')  # 2 casas decimais