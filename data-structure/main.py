import random
import time

# Listas para armazenar o histórico
historico_temperatura = []
historico_energia = []
historico_comunicacao = []
historico_status = []


def animacao_carregamento():
    print("\nInicializando sistema", end="")

    for i in range(3):
        time.sleep(0.5)
        print(".", end="")

    print("\n")


def inserir_dados():
    print("\nINSERIR DADOS DOS SENSORES\n")

    temperatura = float(input("Temperatura da nave (°C): "))
    energia = int(input("Nível de energia (%): "))
    comunicacao = int(input("Comunicação ativa? (1 = Sim | 0 = Não): "))

    historico_temperatura.append(temperatura)
    historico_energia.append(energia)
    historico_comunicacao.append(comunicacao)

    status = analisar_condicoes(temperatura, energia, comunicacao)
    historico_status.append(status)

    print("\nDados registrados com sucesso!\n")


def simular_sensores():
    print("\nSIMULAÇÃO AUTOMÁTICA DOS SENSORES\n")

    temperatura = round(random.uniform(40, 120), 1)
    energia = random.randint(5, 100)
    comunicacao = random.randint(0, 1)

    print(f"Temperatura gerada: {temperatura}°C")
    print(f"Energia gerada: {energia}%")

    if comunicacao == 1:
        print("Comunicação: ONLINE")
    else:
        print("Comunicação: OFFLINE")

    historico_temperatura.append(temperatura)
    historico_energia.append(energia)
    historico_comunicacao.append(comunicacao)

    status = analisar_condicoes(temperatura, energia, comunicacao)
    historico_status.append(status)

    print("\nLeitura simulada registrada!\n")


def analisar_condicoes(temperatura, energia, comunicacao):

    alertas = []

    if temperatura > 80:
        alertas.append("ALERTA DE SUPERAQUECIMENTO")

    if energia < 20:
        alertas.append("ECONOMIA DE ENERGIA ATIVADA")

    if comunicacao == 0:
        alertas.append("FALHA DE COMUNICAÇÃO")

    if len(alertas) == 0:
        return "SISTEMA OPERANDO NORMALMENTE"

    return " | ".join(alertas)


def visualizar_status():

    if len(historico_temperatura) == 0:
        print("\nNenhum dado disponível.\n")
        return

    print("\nSTATUS ATUAL DA MISSÃO\n")

    temperatura = historico_temperatura[-1]
    energia = historico_energia[-1]
    comunicacao = historico_comunicacao[-1]
    status = historico_status[-1]

    print(f"Temperatura Atual: {temperatura}°C")
    print(f"Energia Atual: {energia}%")

    if comunicacao == 1:
        print("Comunicação Atual: ONLINE")
    else:
        print("Comunicação Atual: OFFLINE")

    print(f"Status Operacional: {status}\n")


def executar_analise():

    if len(historico_temperatura) == 0:
        print("\nNenhuma leitura disponível para análise.\n")
        return

    print("\nANÁLISE OPERACIONAL DA MISSÃO\n")

    temperatura = historico_temperatura[-1]
    energia = historico_energia[-1]
    comunicacao = historico_comunicacao[-1]

    if temperatura > 80:
        print("Temperatura acima do limite seguro.")
    else:
        print("Temperatura dentro da faixa ideal.")

    if energia < 20:
        print("Nível crítico de energia detectado.")
    else:
        print("Energia operando normalmente.")

    if comunicacao == 0:
        print("Sistema sem comunicação com a base.")
    else:
        print("Comunicação estabelecida com sucesso.")

    print(f"\nResultado Geral: {historico_status[-1]}\n")


def mostrar_historico():

    if len(historico_temperatura) == 0:
        print("\nNenhum histórico registrado.\n")
        return

    print("\nHISTÓRICO COMPLETO DAS LEITURAS\n")

    for i in range(len(historico_temperatura)):

        print(f"Leitura {i + 1}")

        print(f"Temperatura: {historico_temperatura[i]}°C")
        print(f"Energia: {historico_energia[i]}%")

        if historico_comunicacao[i] == 1:
            print("Comunicação: ONLINE")
        else:
            print("Comunicação: OFFLINE")

        print(f"Status: {historico_status[i]}")
        print("-" * 40)


def relatorio_final():

    if len(historico_temperatura) == 0:
        print("\nNenhum dado disponível para relatório.\n")
        return

    media_temperatura = sum(historico_temperatura) / len(historico_temperatura)
    media_energia = sum(historico_energia) / len(historico_energia)

    falhas_comunicacao = historico_comunicacao.count(0)

    print("\nRELATÓRIO GERAL DA MISSÃO\n")

    print(f"Quantidade de leituras: {len(historico_temperatura)}")
    print(f"Média de temperatura: {media_temperatura:.1f}°C")
    print(f"Média de energia: {media_energia:.1f}%")
    print(f"Falhas de comunicação detectadas: {falhas_comunicacao}")

    if media_temperatura > 80:
        print("A missão apresentou risco térmico elevado.")
    else:
        print("Temperatura média dentro do esperado.")

    if media_energia < 20:
        print("Consumo energético crítico.")
    else:
        print("Energia média satisfatória.")

    print()


animacao_carregamento()

while True:

    print("SISTEMA DE MONITORAMENTO ESPACIAL")
    print("1 - Inserir dados manualmente")
    print("2 - Simular sensores automaticamente")
    print("3 - Visualizar status atual")
    print("4 - Executar análise operacional")
    print("5 - Mostrar histórico das leituras")
    print("6 - Gerar relatório da missão")
    print("7 - Encerrar sistema")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        inserir_dados()

    elif opcao == "2":
        simular_sensores()

    elif opcao == "3":
        visualizar_status()

    elif opcao == "4":
        executar_analise()

    elif opcao == "5":
        mostrar_historico()

    elif opcao == "6":
        relatorio_final()

    elif opcao == "7":
        print("\nEncerrando sistema da missão espacial...")
        time.sleep(1)
        print("Sistema finalizado com sucesso.")
        break

    else:
        print("\nOpção inválida. Tente novamente.\n")
