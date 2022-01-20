# Pharmacy-Sales-Forecast


<img src="https://github.com/nortonvanz/Pharmacy-Sales-Forecast/blob/main/img/rossmann_sales_prediction_img.jpg?raw=true" width=70% height=70%/>

Projeto de Previsão de Vendas de uma rede de farmácias.

Contextualização:
A Rossmann é uma das maiores redes de farmácias da Europa, possuindo mais de 4.000 lojas, e 56 mil colaboradores até 2020.
Os dados utilizados no projeto são reais, e foram disponibilizados pela empresa através do site Kaggle, para uma competição de ciência de dados.
Foram disponibilizados 1.017.209 registros de vendas, contendo 18 colunas detalhando cada venda.
O contexto de negócios é fictício, porém descreve um problema real de uma grande varejista: prever com assertividade suas vendas.

## 1. Problema de negócios
### 1.1 Problema
A previsão de vendas de todas as lojas foi requisitada pelo CFO aos gerentes das lojas, em uma reunião mensal de resultados.
O CFO precisa da previsão de vendas (faturamento) das próximas 6 semanas, pra saber quanto cada loja pode contribuir financeiramente para uma grande reforma (padronização da rede).

### 1.2 Objetivo
Propiciar a melhoria na gestão financeira da empresa, através de maior assertividade na previsão de suas vendas, tendo como resultado um aumento no seu lucro líquido semestral entre 1 e 2%.


## 2. Premissas de negócio
- A consulta da previsão de vendas deve estar disponível 24/7, e deve ser acessível via dispositivos móveis.
- O planejamento da solução será validado com os gerentes, visando garantir que as decisões tomadas na construção da solução são as melhores considerando o conhecimento de negócios já disponível.

As variáveis do dataset original são:

Variável | Definição
------------ | -------------
|store | id único de cada loja.|
|day_of_week | indica o dia da semana que era aquele dia (assumindo 1-Sun -> 7-Sat).|
|date | data do registro.|
|sales | faturamento da loja naquele dia.|
|customers | número de clientes na loja naquele dia.|
|open | loja aberta ou fechada: (0 = closed, 1 = open).|
|state_holiday | feriado nacional (a = public holiday, b = Easter holiday, c = Christmas, 0 = Dia Comum).|
|school_holiday | indica se a loja naquele dia foi afetada pelo fechamento das escolas públicas.|
|store_type | indica qual dos 4 modelos distintos é esta loja: (a, b, c, d).|
|assortment | indica o nível de sortimento da loja: (a = basic, b = extra, c = extended).|
|competition_distance | indica a distancia em metros do competidor mais próximo.|
|competition_open_since_month | indica mês aproximado da abertura do competidor mais próximo.|
|competition_open_since_year | indica ano aproximado da abertura do competidor mais próximo.|
|promo | indica se a loja está com uma promoção ativa naquele dia.|
|promo2 | é uma promoção contínua e consecutiva: (0 = store not participating, 1 = store participating).|
|promo2_since_week | indica a semana do calendário onde a loja entrou em Promo2.|
|promo2_since_year' , 'indica o ano onde a loja entrou em Promo2.|
|promo_interval | indica os meses de início anual onde Promo2 é iniciada (ex: "Feb,May,Aug,Nov").|

As variáveis derivadas no Feature Selection são:
Variável | Definição
------------ | -------------
|competition_since | data onde a partir dela, existem competidores. |
|competition_time_month | número de meses desde que a competição iniciou. |
|promo2_since | data desde quando a Promo2 está ativa. |
|promo2_time_week | números de semanas em que a Promo2 ficou ativa |


## 3. Planejamento da solução
### 3.1. Produto final
O que será entregue efetivamente?
- Um bot (robô) no aplicativo de mensagens Telegram, que recebe o número da loja, e retorna em tempo real qual a sua previsão de vendas (faturamento) para as próximas 6 semanas.

### 3.2. Ferramentas
Quais ferramentas serão usadas no processo?
- Python 3.8.12;
- Jupyter Notebook;
- Git e Github;
- Heroku Cloud;
- Algoritmo de aprendizado de máquina Gxboost.  

### 3.3 Processo
#### 3.3.1 Estratégia de solução
Minha estratégia para resolver esse desafio, baseado na metodologia CRISP-DS, é:
1. Compreender com clareza o modelo e o problema de negócios, através da estatística descritiva;
2. Tratar os dados (formatos, dados faltantes, outliers), realizando a sua limpeza.
3. Levantar hipóteses junto ao time de negócio das variáveis que impactam nas vendas, validar as hipóteses, gerando insights de negócios, e percebendo quais delas são insumos relevantes para o algoritmo.
4. Preparar os dados para a criação do modelo de previsão de vendas, realizando transformações, separação do dataframe entre treino e teste, e seleção de features através de algoritmo com esta finalidade.   
5. Treinar 5 algoritmos de aprendizado de máquina (lineares e não lineares), comparar sua performance, e selecionar o que melhor desempenha.
6. Encontrar o conjunto de parâmetros que maximiza o aprendizado do modelo selecionado, reduzindo o seu erro nas previsões.
7. Interpretar o erro do modelo e traduzir em resultado financeiro para a empresa.
8. Avaliar se a publicação da previsão de vendas já entrega valor, a publicando em produção, ou realizando um novo ciclo de melhorias pontuais.
9. Publicada a previsão na internet, criar robô no Telegram que acesse a previsão em tempo real, de qualquer lugar.
10. Apresentar e disponibilizar o bot do Telegram aos gerentes, detalhando o funcionamento do modelo e esclarecendo as suas dúvidas.


## 4. Os 3 principais insights dos dados

#### 1 Lojas com promoções ativas por mais tempo vendem menos!
* Insight de negócio: Descontinuar de promoções ativas por tempo estendido, visto que constatou-se queda nas vendas após o período promocional normal.

#### 2 Lojas vendem menos durante os feriados escolares, exceto nos meses de agosto!
* Insight de negócio: Considerar esta particularidade do mês de agosto na elaboração de promoções envolvendo clientes em faixas etárias escolares.

#### 3 Lojas vendem menos no segundo semestre do ano.
* Insight de negócio: Considerar o declínio sazonal histórico de vendas entre os meses de agosto a novembro, compensando este fenômeno como ações de marketing.  


## 5. Resultados financeiros para o negócio
As previsões de vendas da Rossmann eram até antes deste projeto, eram realizadas por meio de histórico de vendas em planilhas, através de uma média móvel.
A taxa de erros média das lojas era de 36%, chegando a 70% em algumas lojas mais recentes.
Após a implementação deste modelo de previsão de vendas, a taxa de erro média das lojas passou a ser de 9,65%.
Por meio da melhoria na gestão financeira da empresa, agora de posse de uma previsão de vendas mais assertiva, foi constatado um aumento de 1.9% no seu lucro líquido semestral após a implementação do modelo. Em números, isto representa aproximadamente R$1.140.000,00 a cada semestre.  


## 6. Conclusão
O objetivo do projeto foi alcançado, resolvendo o problema inicial de previsibilidade de faturamento do CFO, bem como aumentando o lucro líquido da empresa dentro do esperado.

O funcionamento da previsão de vendas via bot do Telegram pode ser visto aqui: [Youtube] (https://www.youtube.com/shorts/XsvRzYXMBL4)

## 7. Próximos passos
Melhorias mapeadas:
* Reavaliação do conjunto de parâmetros utilizados para maximizar o aprendizado do modelo, incluindo mais parâmetros no Random Search, e avaliando a viabilidade de uso de Bayesian Search.
* Possibilidade de incluir além da previsão de vendas da loja atual, a previsão mais pessimista e a mais otimista. Exemplo: previsão para 6 semanas: R$ 200.000,00. Pessimista: R$ 186.000,00 (-7%). Otimista: R$ 214.000,00 (+7%).

## 8 Referências
* Este Projeto de Previsão de vendas é parte do curso "DS em Produção", da [Comunidade DS](https://www.comunidadedatascience.com/comunidade-ds/)
* O Dataset foi obtido no [Kaggle](https://www.kaggle.com/c/rossmann-store-sales)
* A imagem utilizada é de uso livre e foi obtida no [Pexels](https://www.pexels.com/)
