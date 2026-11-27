import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# LEITURA DA BASE

df = pd.read_csv("weather_dataset.csv")

# VARIÁVEIS ESCOLHIDAS

variavel_discreta = "uv"
variavel_continua = "temp"

# TABELA DE FREQUÊNCIA
# VARIÁVEL DISCRETA

freq_discreta = df[variavel_discreta].value_counts().sort_index()

freq_discreta_df = pd.DataFrame({
    "Frequência": freq_discreta,
    "Frequência Relativa (%)": round(
        freq_discreta / len(df) * 100, 2
    )
})

print("\n" + "=" * 60)
print("TABELA DE FREQUÊNCIA - VARIÁVEL DISCRETA (UV)")
print("=" * 60)
print(freq_discreta_df)

freq_discreta_df.to_csv(
    "tabela_frequencia_discreta.csv",
    encoding="utf-8-sig"
)

# TABELA DE FREQUÊNCIA
# VARIÁVEL CONTÍNUA

classes = 10

freq_continua = pd.cut(
    df[variavel_continua],
    bins=classes
).value_counts().sort_index()

freq_continua_df = pd.DataFrame({
    "Intervalo": freq_continua.index.astype(str),
    "Frequência": freq_continua.values,
    "Frequência Relativa (%)":
        np.round(freq_continua.values / len(df) * 100, 2)
})

print("\n" + "=" * 60)
print("TABELA DE FREQUÊNCIA - VARIÁVEL CONTÍNUA (TEMP)")
print("=" * 60)
print(freq_continua_df)

freq_continua_df.to_csv(
    "tabela_frequencia_continua.csv",
    index=False,
    encoding="utf-8-sig"
)

# GRÁFICO 1
# HISTOGRAMA DA TEMPERATURA

plt.figure(figsize=(10, 6))

plt.hist(
    df["temp"],
    bins=10,
    color="skyblue",
    edgecolor="black"
)

plt.title("Distribuição da Temperatura")
plt.xlabel("Temperatura")
plt.ylabel("Frequência")

plt.grid(True)

plt.savefig(
    "grafico_temperatura.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# GRÁFICO 2
# BARRAS - UV

plt.figure(figsize=(10, 6))

freq_discreta.plot(
    kind="bar",
    color="orange"
)

plt.title("Distribuição do Índice UV")
plt.xlabel("Índice UV")
plt.ylabel("Frequência")

plt.grid(axis="y")

plt.savefig(
    "grafico_uv.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# FUNÇÃO DE ESTATÍSTICA

def estatisticas(coluna):

    dados = df[coluna]

    media = dados.mean()
    mediana = dados.median()
    moda = dados.mode().iloc[0]

    maximo = dados.max()
    minimo = dados.min()

    amplitude = maximo - minimo

    variancia = dados.var()

    desvio_padrao = dados.std()

    coef_variacao = (
        desvio_padrao / media
    ) * 100

    q1 = dados.quantile(0.25)
    q2 = dados.quantile(0.50)
    q3 = dados.quantile(0.75)

    resultado = pd.DataFrame({
        "Medida": [
            "Média",
            "Mediana",
            "Moda",
            "Máximo",
            "Mínimo",
            "Amplitude",
            "Variância",
            "Desvio Padrão",
            "Coeficiente de Variação (%)",
            "1º Quartil",
            "2º Quartil",
            "3º Quartil"
        ],
        "Valor": [
            media,
            mediana,
            moda,
            maximo,
            minimo,
            amplitude,
            variancia,
            desvio_padrao,
            coef_variacao,
            q1,
            q2,
            q3
        ]
    })

    return resultado

# ANÁLISE UNIVARIADA 1
# TEMPERATURA


estat_temp = estatisticas("temp")

print("\n" + "=" * 60)
print("ANÁLISE UNIVARIADA - TEMPERATURA")
print("=" * 60)
print(estat_temp)

estat_temp.to_csv(
    "estatisticas_temperatura.csv",
    index=False,
    encoding="utf-8-sig"
)

# ANÁLISE UNIVARIADA 2
# VELOCIDADE DO VENTO

estat_vento = estatisticas("wind_spd")

print("\n" + "=" * 60)
print("ANÁLISE UNIVARIADA - VELOCIDADE DO VENTO")
print("=" * 60)
print(estat_vento)

estat_vento.to_csv(
    "estatisticas_vento.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nENCERRANDO.")