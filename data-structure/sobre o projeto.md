O sistema desenvolvido tem como objetivo simular o monitoramento de uma missão 
espacial experimental, recebendo informações dos sensores da nave, analisando as 
condições operacionais e exibindo alertas ao usuário quando necessário. O programa foi 
construído utilizando conceitos fundamentais da linguagem Python, como funções, 
estruturas condicionais, laços de repetição, listas e manipulação de dados. 
O funcionamento do sistema começa com a inicialização das listas responsáveis pelo 
armazenamento das leituras da missão. Foram utilizadas listas para guardar os valores de 
temperatura, nível de energia, comunicação e status operacional. Essas listas funcionam 
como um histórico, permitindo registrar todas as informações inseridas ou simuladas durante 
a execução do programa. 
Após a inicialização, o sistema exibe uma animação simples de carregamento e entra no 
menu principal. O menu funciona através de um laço de repetição utilizando while True, 
fazendo com que o programa permaneça em execução até que o usuário escolha a opção 
de encerramento. O usuário pode navegar entre as funcionalidades digitando o número 
correspondente à opção desejada. 
O sistema possui duas formas de obtenção de dados. A primeira é a inserção manual, na 
qual o usuário informa a temperatura da nave, o nível de energia e o status da comunicação. 
A segunda é a simulação automática dos sensores, onde o programa gera valores aleatórios 
utilizando a biblioteca random, simulando o comportamento de sensores reais de uma 
missão espacial. 
Sempre que uma nova leitura é realizada, os dados são armazenados nas listas através do 
método .append(). Dessa forma, todas as informações ficam registradas para consultas 
futuras, como histórico e geração de relatórios. 
Após salvar os dados, o sistema executa uma análise automática das condições 
operacionais da missão. Essa análise é feita através da função analisar_condicoes(), 
que utiliza estruturas condicionais (if) para verificar possíveis situações críticas. Caso a 
temperatura seja maior que 80°C, o sistema emite um alerta de superaquecimento. Se o 
nível de energia estiver abaixo de 20%, o programa informa a necessidade de economia de 
energia. Além disso, se o status da comunicação for igual a 0, o sistema detecta uma falha 
de comunicação com a base. 
Se nenhuma condição crítica for encontrada, o programa informa que o sistema está 
operando normalmente. Todos os alertas identificados também são armazenados no 
histórico de status da missão. 
O sistema ainda possui uma funcionalidade de visualização do status atual, que apresenta 
os dados mais recentes registrados na missão. Para isso, o programa acessa a última 
posição das listas utilizando o índice [-1], exibindo a temperatura atual, nível de energia, 
estado da comunicação e situação operacional da nave. 
Outra funcionalidade importante é o histórico das leituras. O programa percorre todas as 
listas utilizando um laço de repetição for, exibindo todas as informações registradas desde 
o início da execução. Dessa forma, é possível acompanhar toda a evolução da missão 
espacial e verificar os alertas gerados ao longo do monitoramento. 
Além disso, o sistema conta com uma função de relatório geral da missão. Nessa etapa, o 
programa realiza cálculos utilizando funções como sum() e len() para determinar a média 
de temperatura, média de energia e quantidade de falhas de comunicação registradas. Após 
os cálculos, o sistema interpreta os resultados e apresenta uma análise geral da missão. 
Por fim, o programa pode ser encerrado através da opção “Encerrar sistema”. Quando essa 
opção é selecionada, o comando break interrompe o laço principal, finalizando a execução 
do sistema de monitoramento espacial. 
De forma geral, o projeto simula um sistema básico de controle operacional de uma missão 
espacial, sendo capaz de coletar dados, armazenar informações, analisar condições críticas, 
emitir alertas e gerar relatórios operacionais. O desenvolvimento permitiu a aplicação prática 
de conceitos fundamentais de programação em Python, além da simulação de um cenário 
tecnológico inspirado em sistemas reais de monitoramento espacial.
