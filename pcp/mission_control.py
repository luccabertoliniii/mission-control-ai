NOME_MISSAO = "Projeto Aurora Nexus"
NOME_EQUIPE = "Esquadrão Órion Prime"

registros_nexus = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

setores_monitorados = [
    "Temperatura da nave",
    "Sinal de comunicação",
    "Nível energético",
    "Suporte respiratório",
    "Estabilidade estrutural"
]

def verificar_temperatura(valor_temp):
    if valor_temp < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do ideal"
    elif 18 <= valor_temp <= 30:
        return "NORMAL", 0, "Temperatura controlada"
    elif 30 < valor_temp <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Perigo de superaquecimento"

def verificar_comunicacao(valor_com):
    if valor_com < 30:
        return "CRÍTICO", 2, "Sinal em estado crítico"
    elif 30 <= valor_com <= 59:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"

def verificar_energia(valor_energia):
    if valor_energia < 20:
        return "CRÍTICO", 2, "Energia em nível crítico"
    elif 20 <= valor_energia <= 49:
        return "ATENÇÃO", 1, "Energia abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estabilizada"

def verificar_oxigenio(valor_oxi):
    if valor_oxi < 80:
        return "CRÍTICO", 2, "Oxigênio em estado crítico"
    elif 80 <= valor_oxi <= 89:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"

def verificar_estabilidade(valor_est):
    if valor_est < 40:
        return "CRÍTICO", 2, "Estrutura em estado crítico"
    elif 40 <= valor_est <= 69:
        return "ATENÇÃO", 1, "Estabilidade reduzida"
    else:
        return "NORMAL", 0, "Estrutura estável"

def classificar_operacao(pontuacao_total):
    if pontuacao_total <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao_total <= 5:
        return "MISSÃO EM ALERTA"
    else:
        return "MISSÃO CRÍTICA"

def analisar_evolucao(risco_inicial, risco_final):
    if risco_final > risco_inicial:
        return "A missão apresentou evolução negativa."
    elif risco_final < risco_inicial:
        return "A missão apresentou melhora operacional."
    else:
        return "A missão permaneceu estável durante os ciclos."

def gerar_protocolo(status_setores):
    protocolos = []

    if status_setores[0] in ["CRÍTICO", "ATENÇÃO"]:
        protocolos.append("Revisar sistema térmico")

    if status_setores[1] == "CRÍTICO":
        protocolos.append("Restabelecer comunicação orbital")

    if status_setores[2] == "CRÍTICO":
        protocolos.append("Ativar reserva energética")

    if status_setores[3] == "CRÍTICO":
        protocolos.append("Executar protocolo respiratório")

    if status_setores[4] == "CRÍTICO":
        protocolos.append("Reduzir atividades secundárias")

    if not protocolos:
        return "Continuar operação normal e monitoramento."

    return " | ".join(protocolos) + "."

def main():
    print("========================================")
    print("CENTRAL DE CONTROLE ESPACIAL")
    print("========================================")
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Total de ciclos analisados: {len(registros_nexus)}")
    print("========================================")

    riscos_ciclos = []
    pontos_setores = [0, 0, 0, 0, 0]
    soma_setores = [0, 0, 0, 0, 0]

    total_ciclos_criticos = 0
    ciclo_critico = 0
    maior_risco = -1

    for indice, ciclo in enumerate(registros_nexus):

        temperatura, comunicacao, energia, oxigenio, estabilidade = ciclo

        soma_setores[0] += temperatura
        soma_setores[1] += comunicacao
        soma_setores[2] += energia
        soma_setores[3] += oxigenio
        soma_setores[4] += estabilidade

        st_temp, pt_temp, msg_temp = verificar_temperatura(temperatura)
        st_com, pt_com, msg_com = verificar_comunicacao(comunicacao)
        st_ene, pt_ene, msg_ene = verificar_energia(energia)
        st_oxi, pt_oxi, msg_oxi = verificar_oxigenio(oxigenio)
        st_est, pt_est, msg_est = verificar_estabilidade(estabilidade)

        pontos_setores[0] += pt_temp
        pontos_setores[1] += pt_com
        pontos_setores[2] += pt_ene
        pontos_setores[3] += pt_oxi
        pontos_setores[4] += pt_est

        pontuacao_ciclo = (
            pt_temp +
            pt_com +
            pt_ene +
            pt_oxi +
            pt_est
        )

        riscos_ciclos.append(pontuacao_ciclo)

        classificacao = classificar_operacao(pontuacao_ciclo)

        if pontuacao_ciclo > maior_risco:
            maior_risco = pontuacao_ciclo
            ciclo_critico = indice + 1

        if classificacao == "MISSÃO CRÍTICA":
            total_ciclos_criticos += 1

        protocolo = gerar_protocolo(
            [st_temp, st_com, st_ene, st_oxi, st_est]
        )

        print(f"\nCICLO {indice + 1}")
        print(f"Temperatura: {temperatura}°C | {st_temp} | {msg_temp}")
        print(f"Comunicação: {comunicacao}% | {st_com} | {msg_com}")
        print(f"Energia: {energia}% | {st_ene} | {msg_ene}")
        print(f"Oxigênio: {oxigenio}% | {st_oxi} | {msg_oxi}")
        print(f"Estabilidade: {estabilidade}% | {st_est} | {msg_est}")

        print(f"Pontuação de risco: {pontuacao_ciclo}")
        print(f"Classificação: {classificacao}")
        print(f"Protocolo recomendado: {protocolo}")

    print("\n========================================")
    print("RELATÓRIO FINAL DA MISSÃO")
    print("========================================")

    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Total de ciclos analisados: {len(registros_nexus)}")

    quantidade_ciclos = len(registros_nexus)

    print(f"\nMédia de temperatura: {soma_setores[0] / quantidade_ciclos:.2f}°C")
    print(f"Média de comunicação: {soma_setores[1] / quantidade_ciclos:.2f}%")
    print(f"Média de energia: {soma_setores[2] / quantidade_ciclos:.2f}%")
    print(f"Média de oxigênio: {soma_setores[3] / quantidade_ciclos:.2f}%")
    print(f"Média de estabilidade: {soma_setores[4] / quantidade_ciclos:.2f}%")

    print(f"\nCiclo mais crítico: Ciclo {ciclo_critico}")
    print(f"Maior pontuação registrada: {maior_risco}")

    risco_medio = sum(riscos_ciclos) / quantidade_ciclos

    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {total_ciclos_criticos}")

    tendencia = analisar_evolucao(
        riscos_ciclos[0],
        riscos_ciclos[-1]
    )

    print(f"\nTendência da missão:")
    print(tendencia)

    print("\nPontuação acumulada por setor:")

    for indice in range(5):
        print(f"{setores_monitorados[indice]}: {pontos_setores[indice]} pontos")

    maior_pontuacao_setor = max(pontos_setores)
    setor_mais_afetado = pontos_setores.index(maior_pontuacao_setor)

    print("\nSetor mais afetado:")
    print(setores_monitorados[setor_mais_afetado])

    print("\nClassificação final da missão:")
    print(classificar_operacao(risco_medio))

    print("\nConclusão:")

    if risco_medio > 2:
        print("A missão apresentou falhas relevantes durante a operação espacial.")
    else:
        print("A missão operou dentro dos padrões esperados de estabilidade.")

if __name__ == "__main__":
    main()