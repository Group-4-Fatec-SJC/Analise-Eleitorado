from operator import itemgetter
import pandas as pd

baseDados = 'base_Dados_Vale_Paraiba.csv'
df = pd.read_csv(baseDados, encoding='UTF-8', sep=';')

def pesquisaEscolaridade(cidade, genero, estadoCivil):

    tituloGraph = ""

    if genero != "":
        dfCidade = df.loc[df['DS_GENERO'] == genero]
        tituloGraph += f'GÊNERO {genero}'
    else:
        dfCidade = df
        tituloGraph = 'DIVISÃO POR ESCOLARIDADE'

    if estadoCivil != "":
        dfCidade = dfCidade.loc[dfCidade['DS_ESTADO_CIVIL'] == estadoCivil]
        tituloGraph += f', {estadoCivil}(A)'
    else:
        pass

    if cidade != "":
        dfCidade = dfCidade.loc[dfCidade['NM_MUNICIPIO'] == cidade]
        tituloGraph += f' DA CIDADE {cidade}'
    else:
        pass




    dicEscolaridade = dict(dfCidade['DS_GRAU_ESCOLARIDADE'].value_counts())


    listEscolaridade = []
    listQTDEscolaridade = []

    for k, v in dicEscolaridade.items():
        listEscolaridade.append(k)
        listQTDEscolaridade.append(v)

    totalPessoas = 0
    for valor in listQTDEscolaridade:
        totalPessoas += valor

    dic = {
        "eixoX": listEscolaridade,
        "eixoY": listQTDEscolaridade,
        "totalPessoas": totalPessoas,
        "tituloGraph": tituloGraph,
    }

    return dic



def divisaoGenero():
    totalPessoas = len(df)

    # Definindo as informações do eixo X, passando os Gêneros
    labels = ['Masculino', 'Feminino']

    # Definindo as informações do eixo Y, passando a quantidade de cada gênero
    masc = len(df.loc[df['DS_GENERO'] == 'MASCULINO'])
    fem = len(df.loc[df['DS_GENERO'] == 'FEMININO'])
    ni = len(df.loc[df['DS_GENERO'] == 'NÃO INFORMADO'])
    pessoas = []

    # Armazenando os dados na ordem do eixo X (labels), na ordem do eixo Y "Labels" ('Não Informado', 'Masculino', 'Feminino')
    pessoas.append(masc)
    pessoas.append(fem)

    dic = {
        "labelsGenero": labels,
        "qtdGenero": pessoas,
        "qtdGenNaoInfo": ni,
        "totalPessoas": totalPessoas,
    }

    return dic

def divisaoGeneroCidade(cidade, genero, estadoCivil):

    tituloGraph = ""

    if genero != "":
        dfCidade = df.loc[df['DS_GENERO'] == genero]
        tituloGraph += f'GÊNERO {genero}'
    else:
        dfCidade = df
        tituloGraph = 'DIVISÃO POR GÊNERO'

    if estadoCivil != "":
        dfCidade = dfCidade.loc[dfCidade['DS_ESTADO_CIVIL'] == estadoCivil]
        tituloGraph += f', {estadoCivil}(A)'
    else:
        pass

    if cidade != "":
        dfCidade = dfCidade.loc[dfCidade['NM_MUNICIPIO'] == cidade]
        tituloGraph += f' DA CIDADE {cidade}'
    else:
        pass

    totalPessoas = len(dfCidade)

    labels = ['Masculino', 'Feminino']

    masc = len(dfCidade.loc[dfCidade['DS_GENERO'] == 'MASCULINO'])
    fem = len(dfCidade.loc[dfCidade['DS_GENERO'] == 'FEMININO'])
    ni = len(dfCidade.loc[dfCidade['DS_GENERO'] == 'NÃO INFORMADO'])
    pessoas = []

    pessoas.append(masc)
    pessoas.append(fem)

    dic = {
        "eixoX": labels,
        "eixoY": pessoas,
        "qtdGenNaoInfo": ni,
        "totalPessoas": totalPessoas,
        "tituloGraph": tituloGraph,
    }

    return dic
