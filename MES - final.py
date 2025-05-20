import random

"""
Estrutura esperada:

[
    (idx = 0, domingo)
    [
        ["nome_exercicio", "tempo_gasto_em_min", calorias_queimadas],
        ...
    ],
    ...,
    (idx = 6, sabado)
    [
        ["nome_exercicio", "tempo_gasto_em_min", calorias_queimadas],
        ...
    ],
]

Assim:
    (str)   nome_exercicio:     exercicios[dia_da_semana - 1][N][0]
    (str)   tempo_gasto_em_min: exercicios[dia_da_semana - 1][N][1]
    (float) calorias_queimadas: exercicios[dia_da_semana - 1][N][2]
    (int)   dia_da_semana:      dia_da_semana - 1, indice do vetor
"""
# exercicios = [
#     # Domingo
#     [],
#     # Segunda-Feira
#     [],
#     # Terca-Feira
#     [],
#     # Quarta-Feira
#     [],
#     # Quinta-Feira
#     [],
#     # Sexta-Feira
#     [],
#     # Sabado
#     []
# ]

exercicios = [
    # Domingo
    [
        ["Corrida", 30, 250.0],
        ["Abdominal", 15, 50.0]
    ],
    # Segunda-Feira
    [
        ["Caminhada", 40, 180.0]
    ],
    # Terca-Feira
    [
        ["Bicicleta", 60, 400.0],
        ["Corrida", 20, 170.0]
    ],
    # Quarta-Feira
    [],
    # Quinta-Feira
    [
        ["Natação", 45, 350.0]
    ],
    # Sexta-Feira
    [
        ["Corrida", 25, 200.0]
    ],
    # Sabado
    [
        ["Yoga", 50, 120.0]
    ]
]

"""
Valor da meta semanal definida futuramente pelo usuario.
"""
valor_meta_semanal = None

def cadastrar_exercicio():
    """
    Permitir que o usuário registre o nome do exercício realizado,
    tempo gasto em minutos, calorias queimadas e dia da semana.
    """
    dia_da_semana = int(input("Digite o dia da semana: "))

    nome_exercicio = input("Digite o nome do exercício feito: ")
    
    tempo_gasto_em_min = int(input("Digite quanto tempo foi gasto no exercício (em min): "))

    calorias_queimadas = float(input("Digite o número de calorias queimadas: "))

    exercicios[dia_da_semana - 1].append([nome_exercicio, tempo_gasto_em_min, calorias_queimadas])

def relatorio_diario():
    """
    Exibir um resumo dos exercícios realizados em um determinado dia da semana,
    informando tempo total gasto e calorias queimadas.
    """
    global exercicios

    dia_da_semana = int(input("Digite o dia da semana: "))
    print()

    tipos_exercicios = []
    calorias_totais = []
    tempos_totais_gastos = []

    total_tempo = 0
    total_calorias = 0.0

    for exercicio in exercicios[dia_da_semana - 1]:
        nome = exercicio[0]
        tempo = exercicio[1]
        calorias = exercicio[2]

        if nome not in tipos_exercicios:
            tipos_exercicios.append(nome)
            tempos_totais_gastos.append(tempo)
            calorias_totais.append(calorias)
        else:
            index = tipos_exercicios.index(nome)
            calorias_totais[index] += calorias
            tempos_totais_gastos[index] += tempo

        total_tempo += tempo
        total_calorias += calorias

    for i in range(len(tipos_exercicios)):
        print(f"Nome do Ex.: {tipos_exercicios[i]}")
        print(f"Tempo Total Gasto: {tempos_totais_gastos[i]}")
        print(f"Calorias Totais: {calorias_totais[i]}")
        print()

    print(f"Tempo Geral: {total_tempo} min")
    print(f"Calorias Geral: {total_calorias} cal")

def calcular_imc():
    """
    Calcular e informar o Índice de Massa Corporal (IMC) do usuário com base em seu peso e altura,
    indicando a respectiva classificação (baixo peso, normal, sobrepeso, obesidade).
    """
    peso = float(input("Digite seu peso (em quilos): "))
    altura = float(input("Digite sua altura (em metros): "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print(f"IMC: {imc:.2f} - Abaixo do Peso")
    elif imc < 24.9:
        print(f"IMC: {imc:.2f} - Peso Normal")
    elif imc < 29.9:
        print(f"IMC: {imc:.2f} - Sobrepeso")
    else:
        print(f"IMC: {imc:.2f} - Obesidade")

def meta_semanal():
    """
    Permitir ao usuário definir uma meta semanal de calorias queimadas e verificar
    se essa meta foi atingida com base nos exercícios registrados.
    """
    global valor_meta_semanal

    if valor_meta_semanal is None:
        valor_meta_semanal = int(input("Qual a sua meta para a semana? "))

    while True:
        option = int(input("Deseja atualizar a meta (1) ou verificar se ela foi atingida (2)? "))

        match option:
            case 1:
                valor_meta_semanal = int(input("Novo valor: "))
                break
            case 2:
                valor_atual = 0

                for dia_da_semana in exercicios:
                    for estatisticas in dia_da_semana:
                        valor_atual += estatisticas[2]

                if valor_atual >= valor_meta_semanal:
                    print(f"Parabens! Voce atingiu sua Meta ({valor_meta_semanal})! Valor Total: {valor_atual}")
                else:
                    print(f"Sua meta ({valor_meta_semanal}) nao foi atingida... Valor atual: {valor_atual}, Restam: {valor_meta_semanal - valor_atual}")
                break
            case _:
                print("Opcao invalida...")

def frase_motivacional():
    """
    Apresentar ao usuário frases motivacionais aleatórias relacionadas à prática de exercícios.
    """
    frases = [
        "A palavra 'Impossivel' foi inventada para ser desafiada.",
        "Cada passo conta, continue firme!",
        "A persistência te leva ao sucesso!",
        "Seu esforço será recompensado!",
        "Desistir não é uma opção!",
        "Corpo são, mente sã!",
        "A força não provém da capacidade física. Provém de uma vontade indomável."
        "Respeite seu corpo e trate com carinho a sua mente."
        "Você já fez uma caminhada tão bonita até agora. Parabenize-se."
        "Existe apenas um canto do universo que você pode ter certeza de aperfeiçoar, que é você mesmo."
    ]

    print(random.choice(frases))

def media_de_calorias_por_exercicio():
    """
    Calcular e exibir a média de calorias queimadas por tipo de exercício realizado.
    """
    global exercicios

    tipos_exercicios = []
    calorias_totais = []
    quantidades = []

    # Agrupar calorias por tipo de exercício
    for dia in exercicios:
        for exercicio in dia:
            nome = exercicio[0]
            calorias = exercicio[2]

            if nome not in tipos_exercicios:
                tipos_exercicios.append(nome)
                calorias_totais.append(calorias)
                quantidades.append(1)
            else:
                index = tipos_exercicios.index(nome)
                calorias_totais[index] += calorias
                quantidades[index] += 1

    if tipos_exercicios:
        print("Média de calorias queimadas por tipo de exercício:")

        for i in range(len(tipos_exercicios)):
            media = calorias_totais[i] / quantidades[i]

            print(f"- {tipos_exercicios[i]}: {media:.2f} calorias")
    else:
        print("Nenhum exercício registrado para calcular a média.")

def fazer_codigo_barras():
    """
    Exibir um gráfico simples em forma de código de barras no terminal representando
    visualmente as calorias queimadas por exercício cadastrado.
    """
    global exercicios

    tipos_exercicios = []
    calorias_totais = []
    razao_caloria_barrinha = 10

    # Agrupar calorias por tipo de exercício
    for dia in exercicios:
        for exercicio in dia:
            nome = exercicio[0]
            calorias = exercicio[2]

            if nome not in tipos_exercicios:
                tipos_exercicios.append(nome)
                calorias_totais.append(calorias)
            else:
                index = tipos_exercicios.index(nome)
                calorias_totais[index] += calorias

    if tipos_exercicios:
        print("Gráfico de calorias queimadas por exercício:")
        for i in range(len(tipos_exercicios)):
            barras = "#" * (int(calorias_totais[i] // razao_caloria_barrinha)) # Cada '#' representa 10 calorias
            print(f"{tipos_exercicios[i]:<15}: {barras} ({calorias_totais[i]:.2f} calorias)")
    else:
        print("Nenhum exercício registrado para exibir o gráfico.")

def menu():
    """
    Menu principal da aplicacao.
    """
    print("""
        1. Cadastrar exercício
        2. Relatório diário
        3. Calcular IMC
        4. Meta semanal
        5. Frase motivacional
        6. Média de calorias por exercício
        7. Fazer código de barras
        8. Sair
    """)

if __name__ == "__main__":
    while True:
        menu()

        option = int(input(">> "))

        match option:
            case 1:
                cadastrar_exercicio()
            case 2:
                relatorio_diario()
            case 3:
                calcular_imc()
            case 4:
                meta_semanal()
            case 5:
                frase_motivacional()
            case 6:
                media_de_calorias_por_exercicio()
            case 7:
                fazer_codigo_barras()
            case 8:
                print("Obrigado por utilizar nossa aplicacao! Ate a proxima!")
                break
            case _:
                print("Opcao invalida...")
