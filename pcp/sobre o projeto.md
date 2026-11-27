# Mission Control AI - Projeto Aurora Nexus

## Descrição

O Mission Control AI é um sistema desenvolvido em Python para simular o monitoramento inteligente de uma missão espacial experimental. O programa analisa diferentes ciclos operacionais da missão, identifica riscos, gera alertas automáticos e produz um relatório final com indicadores de desempenho e segurança dos sistemas monitorados.

---

## Informações da Missão

**Nome da Missão:** Projeto Aurora Nexus

**Nome da Equipe:** Esquadrão Órion Prime

---

## Objetivo

Desenvolver um sistema capaz de:

* Armazenar dados simulados de uma missão espacial;
* Monitorar múltiplos ciclos operacionais;
* Identificar situações de atenção e criticidade;
* Calcular o nível de risco de cada ciclo;
* Gerar recomendações automáticas;
* Identificar tendências da missão;
* Determinar a área mais afetada durante a operação;
* Produzir um relatório final completo.

---

## Estrutura dos Dados

Os dados da missão são armazenados em uma matriz chamada `registros_nexus`, onde cada linha representa um ciclo de monitoramento.

Exemplo:

```python
[24, 92, 88, 96, 90]
```

Ordem das informações:

| Posição | Informação   |
| ------- | ------------ |
| 0       | Temperatura  |
| 1       | Comunicação  |
| 2       | Energia      |
| 3       | Oxigênio     |
| 4       | Estabilidade |

---

## Áreas Monitoradas

O sistema acompanha os seguintes setores:

* Temperatura da nave
* Sinal de comunicação
* Nível energético
* Suporte respiratório
* Estabilidade estrutural

---

## Regras de Classificação

### Temperatura

| Condição          | Status  |
| ----------------- | ------- |
| Menor que 18°C    | ATENÇÃO |
| Entre 18°C e 30°C | NORMAL  |
| Entre 31°C e 35°C | ATENÇÃO |
| Acima de 35°C     | CRÍTICO |

### Comunicação

| Condição        | Status  |
| --------------- | ------- |
| Menor que 30%   | CRÍTICO |
| Entre 30% e 59% | ATENÇÃO |
| 60% ou mais     | NORMAL  |

### Energia

| Condição        | Status  |
| --------------- | ------- |
| Menor que 20%   | CRÍTICO |
| Entre 20% e 49% | ATENÇÃO |
| 50% ou mais     | NORMAL  |

### Oxigênio

| Condição        | Status  |
| --------------- | ------- |
| Menor que 80%   | CRÍTICO |
| Entre 80% e 89% | ATENÇÃO |
| 90% ou mais     | NORMAL  |

### Estabilidade

| Condição        | Status  |
| --------------- | ------- |
| Menor que 40%   | CRÍTICO |
| Entre 40% e 69% | ATENÇÃO |
| 70% ou mais     | NORMAL  |

---

## Sistema de Pontuação

Cada classificação recebe uma pontuação de risco:

| Status  | Pontos |
| ------- | ------ |
| NORMAL  | 0      |
| ATENÇÃO | 1      |
| CRÍTICO | 2      |

A soma das pontuações gera o risco total do ciclo.

### Classificação da Missão

| Pontuação | Classificação    |
| --------- | ---------------- |
| 0 a 2     | MISSÃO ESTÁVEL   |
| 3 a 5     | MISSÃO EM ALERTA |
| 6 ou mais | MISSÃO CRÍTICA   |

---

## Funcionalidades Implementadas

* Monitoramento de múltiplos ciclos da missão;
* Avaliação automática de todos os sistemas;
* Geração de alertas e mensagens operacionais;
* Cálculo de risco por ciclo;
* Classificação automática da missão;
* Identificação do ciclo mais crítico;
* Cálculo das médias dos indicadores;
* Análise de tendência operacional;
* Identificação do setor mais afetado;
* Geração de protocolos de ação;
* Relatório final detalhado.

---

## Funções Desenvolvidas

O sistema utiliza as seguintes funções:

* `verificar_temperatura()`
* `verificar_comunicacao()`
* `verificar_energia()`
* `verificar_oxigenio()`
* `verificar_estabilidade()`
* `classificar_operacao()`
* `analisar_evolucao()`
* `gerar_protocolo()`
* `main()`

---

## Tecnologias Utilizadas

* Python 3
* Estruturas condicionais (`if`, `elif`, `else`)
* Estruturas de repetição (`for`)
* Matrizes (listas de listas)
* Funções
* Manipulação de listas

---


## Resultado Esperado

Ao executar o programa, serão exibidos:

* Dados de cada ciclo analisado;
* Status de todos os sistemas;
* Pontuação de risco;
* Classificação operacional;
* Recomendações automáticas;
* Relatório final completo da missão.

---

## Conclusão

O Projeto Aurora Nexus demonstra a aplicação de lógica computacional para monitoramento espacial, permitindo identificar riscos operacionais, acompanhar a evolução da missão e apoiar a tomada de decisão por meio de análises automatizadas.

O sistema atende todos os requisitos propostos pela atividade, utilizando estruturas fundamentais da linguagem Python para simular um ambiente de controle de missão espacial.
