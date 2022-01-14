import pickle
import pandas as pd
#from pacote [pasta.nome_arquivo] import nome classe
from rossmann.Rossmann import Rossmann
from flask             import Flask, request, Response

#carregar modelo em memória
model = pickle.load( open ('/Users/home/Documents/pharmacy_sales_forecast_files/model/model_rossmann.pkl', 'rb' ) )
             
app = Flask (__name__)

#criar o endpoint
@app.route( '/rossmann/predict', methods=['POST'] )
#ao receber chamada, executa:
def rossmann_predict():
    test_json = request.get_json()

    #conversão do json em dataframe
    if test_json: #se recebeu dados
        #se vier um só json
        if isinstance( test_json, dict ):
            test_raw = pd.DataFrame( test_json, index=[0] )
        # se vierem vários jsons
        else:
            #pega todas as chaves da primeira linha (json é um dicionário), e assume estas chaves como colunas 
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
            
        # Instanciar Rossmann class, pra ter acesso aos seus métodos.
        pipeline = Rossmann()
        
        #data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        #feature engineering
        df2 = pipeline.feature_engineering( df1 )
        
        #data preparation
        df3 = pipeline.data_preparation( df2 )
        
        #prediction                   #modelo, dados originais, dados preparados
        df_response = pipeline.get_prediction( model, test_raw, df3 )
            
        return df_response
    else:
        #requisição deu certo, mas retorna vazio pois recebeu vazio.
        return Response( '{}', status=200, mimetype='application/json' )
if __name__ == '__main__':  
    #rodar no localhost
    app.run ( '0.0.0.0' )
