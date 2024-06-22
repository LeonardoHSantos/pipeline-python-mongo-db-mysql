import pandas as pd
import urllib.parse

from configs_db import *
from extract_and_save_data import connect_mongo, create_connect_db, create_connect_collection

def  visualize_collection(col):
    for doc in col.find():
        print(doc)

def rename_column(col, col_name, new_name):
    col.update_many({}, {"$rename": {f"{col_name}": f"{new_name}"}})

def select_category(col, category):
    query = { "Categoria do Produto": f"{category}"}

    lista_categoria = []
    for doc in col.find(query):
        lista_categoria.append(doc)
    
    return lista_categoria

def make_regex(col, regex):
    """
    return: documentos que correspondam a uma expressão regular específica.
    """
    lista_regex = []
    query = {"Data da Compra": {"$regex": f"{regex}"}}

    for doc in col.find(query):
        lista_regex.append(doc)

    return lista_regex


def create_dataframe(lista):
    """
        return: cria um dataframe a partir de uma lista de documentos.
    """
    return pd.DataFrame(lista)

def format_date(df, nome_coluna):
    """
        return: formata a coluna de datas do dataframe para o formato "ano-mes-dia".
    """
    df[nome_coluna] = pd.to_datetime(df[nome_coluna], format="%d/%m/%Y")
    df[nome_coluna] = df[nome_coluna].dt.strftime("%Y-%m-%d")
    return df

def save_csv(df, path):
    """
        return: salva o dataframe como um arquivo CSV no caminho especificado.
    """
    df.to_csv(path, index=False)
    print(f"\n Arquivo salvo: {path} ")



if __name__ == "__main__":
    parse_password = urllib.parse.quote(PASSWORD_MONGODB)
    uri = f"mongodb+srv://{USERNAME_MONGODB}:{parse_password}@cluster-pipeline.jcgyaej.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-pipeline"
    client = connect_mongo(uri=uri)
    db = create_connect_db(client=client, db_name="db_produtos_teste")
    collection = create_connect_collection(db=db, col_name="produtos")
    visualize_collection(col=collection)

    rename_column(col=collection, col_name="lat", new_name="Latitude")
    rename_column(col=collection, col_name="lon", new_name="Longitude")

    df_category_livros = create_dataframe(select_category(col=collection, category="livros"))
    format_date(df=df_category_livros, nome_coluna="Data da Compra")
    save_csv(df=df_category_livros, path="../data/tabela_livros_2.csv")

    vendas_a_partir_de_2021 = make_regex(col=collection, regex="/202[1-9]")
    df_venda_a_partir_de_2021 = create_dataframe(lista=vendas_a_partir_de_2021)
    format_date(df=df_venda_a_partir_de_2021, nome_coluna="Data da Compra")
    save_csv(df=df_venda_a_partir_de_2021, path="../data/tabela_2021_em_diante_2.csv")

    client.close()


