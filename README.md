# Pharmacy-Sales-Forecast


<img src="https://github.com/nortonvanz/Pharmacy-Sales-Forecast/blob/main/img/rossmann_sales_prediction_img.jpg?raw=true" width=70% height=70%/>

Projeto de Previsão de Vendas de uma rede de farmácias.

Contextualização:
A Rossmann é uma das maiores redes de farmácias da Europa, possuindo mais de 4.000 lojas, e 56 mil colaboradores até 2020.

Os dados utilizados neste projeto são reais, e foram disponibilizados pela própria Rossmanm através do site Kaggle, para uma competição de ciência de dados.
Foram disponibilizados 1.017.209 registros de vendas, contendo 18 características de cada venda.

O contexto de negócios é fictício, porém descreve um problema real de uma grande varejista: prever com assertividade suas vendas.

## 1. Problema de negócios
Em uma reunião mensal de resultados da Rossmann, o CFO solicitou aos gerentes das lojas a previsão de vendas (faturamento) para as próximas 6 semanas, pois ele precisa saber quanto cada loja pode contribuir financeiramente para uma reforma na rede, que está padronizando suas lojas.

## 2. Premissas de negócio
- A consulta da previsão de vendas deve estar diponível 24/7, e será acessível via dispositivos móveis.

## 3. Planejamento da solução
### 3.1. Produto final
O que será entregue efetivamente?
- Um bot (robô) no aplicativo de mensagens Telegram, que recebe o código da loja, e retorna em tempo real qual a sua previsão de vendas (faturamento) para as próximas 6 semanas.

### 3.2. Ferramentas
Quais ferramentas serão usadas no processo?
- Python 3.8.12;
- Jupyter Notebook;
- Git e Github;
- Heroku Cloud; 
- Algoritmos de Regressão;
- Pacotes de Machine Learning Sklearn e Scipy;
- Técnicas de Seleção de Features;
- Flask e Python API's.

### 3.3 Processo
#### 3.3.1 Estratégia de solução
Minha estratégia para resolver esse desafio, baseado na metodologia CRISP-DS, é:
1. Compreender com clareza o modelo e o problema de negócios, através da estatística descritiva;
2. Tratar os dados (formatos, dados faltantes, outliers), realizando a sua limpeza.
3. Levantar junto ao time de negócio quais são as features que impactam nas vendas. Formular e validar hipóteses gerando insights de negócio.
4. Preparar os dados para a criação do modelo de previsão de vendas, realizando transformações, separação do dataframe entre treino e teste, e seleção de features automatizada.   
5. Treinar algoritmos de aprendizado de máquina (lineares e não lineares), comparar sua performance, e selecionar o de melhor desempenho.
6. Encontrar o conjunto de parâmetros que maximiza o aprendizado do modelo selecionado, reduzindo o seu erro nas previsões.
7. Interpretar o erro do modelo e traduzir em resultado financeiro para a empresa.
8. Avaliar se a previsão de vendas construída já entrega valor ao time de negócios, publicando em produção em caso positivo, ou realizando um novo ciclo de melhorias pontuais em caso negativo.
9. Após a publicação, criar robô no Telegram que acesse a previsão em tempo real, de qualquer lugar.
10. Apresentar e disponibilizar o bot do Telegram aos gerentes e CFO, detalhando o funcionamento do modelo e esclarecendo as suas dúvidas.

## 4. Os 3 principais insights dos dados
Durante a análise exploratória de dados, foram gerados insights ao time de negócio. 

Insights são informações novas, ou que contrapõe crenças até então estabelecidas do time de negócios. São também acionáveis: possibilitam ação para direcionar resultados futuros.

#### 1 Lojas com promoções ativas por mais tempo deveriam vender mais.
Hipótese falsa. Foi observado que as vendas cairam em toda a rede em promoções extendidas ativas há mais de 220 semanas.

* Insight de negócio: Descontinuar as promoções extendidas ativas ao atingirem no máximo 220 semanas, mantendo apenas promoções pontuais, ou realizando novas campanhas promocionais.

#### 2 Lojas deveriam vender mais no segundo semestre do ano.
Hipótese falsa. Foi observado que com exceção do mês de julho, as vendas são aproximadamente 1/3 menores nos 5 últimos meses do ano. 

* Insight de negócio: Considerar o declínio sazonal histórico de vendas entre os meses de agosto a dezembro, compensando este fenômeno como ações de marketing adicionais.  

#### 3 Lojas deveriam vender menos durante os feriados escolares.
Hipótese verdadeira. Na média anual, as lojas vendem menos em feriados escolares. Avaliando mensalmente, a exceção é o mês de agosto.

* Insight de negócio: Considerar um maior aproveitamento deste aumento de vendas nos feriados escolares de agosto, elaborando promoções focadas em clientes nas faixas etárias escolares.

## 5. Resultados financeiros para o negócio
As previsões de vendas da Rossmann, eram até antes deste projeto realizadas por meio de planilhas de histórico de venda, através de uma média móvel.
A taxa de erros desta previsão de vendas de toda a rede ficava na média de 36%, chegando a até 60% nas lojas mais recentes.

Após a implementação deste modelo de previsão de vendas com machine learning, a taxa de erro média das previsões em toda a rede passou para 10%.

Essa redução do erro de 26% em média, propiciou que o CFO fosse muito mais assertivo nos empréstimos bancários que fará para a reforma das lojas da rede.

Os empréstimos estimados estavam na casa de €80 milhões antes do projeto. Considerando os juros de 2% ao ano em 2023 na zona do euro, com prazo de 3 ano, seriam gastos aprox. €4,5 milhões em juros.

Após o projeto, a necessidade de emprestimo foi reavaliada em 55 milhões de euros.
Considerando as mesmas condições de emprestimo, serão gastos agora aprox. €3,3 milhões em juros, uma economia de aprox. €1,2 milhões em 3 anos.


## 6. Conclusão
O objetivo do projeto foi alcançado, resolvendo o problema inicial de previsibilidade de faturamento enfrentado pelo CFO. 

Além disso, o projeto também viabiliou uma melhoria na gestão financeira da Rossmann, através de uma melhor gestão de fluxo de caixa.

O previsão de vendas implementada via bot do Telegram pode ser vista em funcionamento aqui: [Youtube](https://www.youtube.com/shorts/XsvRzYXMBL4)

## 7. Próximos passos
Melhorias mapeadas:
* - Aumentar o a quantidade de combinações de features no random search.
* - Implementar pipelines para preprocessing, ML e cross validation no projeto.

## 8 Referências
* O Dataset foi obtido no [Kaggle](https://www.kaggle.com/c/rossmann-store-sales)
* A imagem utilizada é de uso livre e foi obtida no [Pexels](https://www.pexels.com/pt-br/foto/mulher-adulta-elegante-usando-smartphone-na-rua-3774903/)
