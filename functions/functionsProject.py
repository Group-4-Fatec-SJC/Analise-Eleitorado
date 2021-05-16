from operator import itemgetter
import pandas as pd


def anoEleicao(ano):
    if ano == '':
        baseDados = 'base_Dados_Vale_Paraiba.csv'
        df = pd.read_csv(baseDados, encoding='UTF-8', sep=';')
    elif ano == '2020':
        baseDados = 'base_Dados_Vale_Paraiba.csv'
        df = pd.read_csv(baseDados, encoding='UTF-8', sep=';')
    elif ano == '2018':
        baseDados = 'base_Dados_Vale_Paraiba_2018.csv'
        df = pd.read_csv(baseDados, encoding='UTF-8', sep=';')

    return pd.DataFrame(df)

def pesquisaEscolaridade(cidade, genero, estadoCivil, graph,ano, anoSelecionado):

    df = anoSelecionado

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

    tituloGraph += f' NO ANO DE {ano}'




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
        "tipoGrafico": graph
    }

    return dic

def divisaoGenero():
    baseDados = 'base_Dados_Vale_Paraiba.csv'
    df = pd.read_csv(baseDados, encoding='UTF-8', sep=';')

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

def divisaoGeneroCidade(cidade, genero, estadoCivil, graph, ano, anoSelecionado):

    df = anoSelecionado

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

    tituloGraph += f' NO ANO DE {ano}'

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
        "tipoGrafico": graph
    }

    return dic

def maioresCidades(cidade, genero, estadoCivil, graph, ano, anoSelecionado):

    df = anoSelecionado

    if genero != "":
        pass

    if estadoCivil != "":
       pass

    if cidade != "":
        pass


    cidades = df.groupby(df['NM_MUNICIPIO']).NM_MUNICIPIO.count()
    cidades2 = dict(cidades.sort_values(ascending=False))

    nomeCidade = []
    qtdeCidade = []

    for k, v in cidades2.items():
        nomeCidade.append(k)
        qtdeCidade.append(v)

    nome5maiores = nomeCidade[:5]
    qtde5maiores = qtdeCidade[:5]

    totalPessoas = 0
    for x in qtde5maiores:
        totalPessoas += x

    tituloGraph = '5 MAIORES CIDADES VOTANTES'
    tituloGraph += f' NO ANO DE {ano}'

    dic = {
        "eixoX": nome5maiores,
        "eixoY": qtde5maiores,
        "qtdGenNaoInfo": 0,
        "totalPessoas": totalPessoas,
        "tituloGraph": tituloGraph,
        "tipoGrafico": graph
    }

    return dic

def populacaoIdosa(cidade, genero, estadoCivil, graph, ano, anoSelecionado):

    df = anoSelecionado

    tituloGraph = "ELEITORES ACIMA DE 60 ANOS"

    if genero != "":
        dfCidade = df.loc[df['DS_GENERO'] == genero]
        tituloGraph += f' DO GÊNERO {genero}'
    else:
        dfCidade = df

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

    tituloGraph += f' NO ANO DE {ano}'

    var60a64 = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == 6064])
    var65a69 = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == 6569])
    var70a74 = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == 7074])
    var75a79 = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == 7579])
    var80a84 = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == 8084])
    var85a89 = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == 8589])
    var90a94 = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == 9094])
    var95a99 = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == 9599])
    varAcima100 = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == 9999])
    naoInfo = len(dfCidade.loc[dfCidade['CD_FAIXA_ETARIA'] == -3])

    labelsIdoso = ['60 a 64 anos' , '65 a 69 anos' , '70 a 74 anos' , '75 a 79 anos' , '80 a 84 anos' ,
                   '85 a 89 anos' , '90 a 94 anos' , '95 a 99 anos' , '100 anos ou mais']
    qtdIdoso = [var60a64, var65a69, var70a74, var75a79, var80a84, var85a89, var90a94, var95a99, varAcima100]
    totalPessoas = var60a64 + var65a69 + var70a74 + var75a79 + var80a84 + var85a89 + var90a94 + var95a99 + varAcima100



    dic = {
        "eixoX": labelsIdoso,
        "eixoY": qtdIdoso,
        "qtdGenNaoInfo": naoInfo,
        "totalPessoas": totalPessoas,
        "tituloGraph": tituloGraph,
        "tipoGrafico": graph
    }

    return dic

def pesquisaIdade(cidade, genero, estadoCivil, graph, ano, anoSelecionado):

    df = anoSelecionado

    tituloGraph = "DIVISÃO POR IDADE"

    if genero != "":
        dfCidade = df.loc[df['DS_GENERO'] == genero]
        tituloGraph += f' DO GÊNERO {genero}'
    else:
        dfCidade = df

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

    tituloGraph += f' NO ANO DE {ano}'

    var16 = len(df.loc[df['CD_FAIXA_ETARIA'] == 1600])
    var17 = len(df.loc[df['CD_FAIXA_ETARIA'] == 1700])
    var18 = len(df.loc[df['CD_FAIXA_ETARIA'] == 1800])
    var19 = len(df.loc[df['CD_FAIXA_ETARIA'] == 1900])
    var20 = len(df.loc[df['CD_FAIXA_ETARIA'] == 2000])
    var21a24 = len(df.loc[df['CD_FAIXA_ETARIA'] == 2124])
    var25a29 = len(df.loc[df['CD_FAIXA_ETARIA'] == 2529])
    var30a34 = len(df.loc[df['CD_FAIXA_ETARIA'] == 3034])
    var35a39 = len(df.loc[df['CD_FAIXA_ETARIA'] == 3539])
    var40a44 = len(df.loc[df['CD_FAIXA_ETARIA'] == 4044])
    var45a49 = len(df.loc[df['CD_FAIXA_ETARIA'] == 4549])
    var50a54 = len(df.loc[df['CD_FAIXA_ETARIA'] == 5054])
    var55a59 = len(df.loc[df['CD_FAIXA_ETARIA'] == 5559])
    var60a64 = len(df.loc[df['CD_FAIXA_ETARIA'] == 6064])
    var65a69 = len(df.loc[df['CD_FAIXA_ETARIA'] == 6569])
    var70a74 = len(df.loc[df['CD_FAIXA_ETARIA'] == 7074])
    var75a79 = len(df.loc[df['CD_FAIXA_ETARIA'] == 7579])
    var80a84 = len(df.loc[df['CD_FAIXA_ETARIA'] == 8084])
    var85a89 = len(df.loc[df['CD_FAIXA_ETARIA'] == 8589])
    var90a94 = len(df.loc[df['CD_FAIXA_ETARIA'] == 9094])
    var95a99 = len(df.loc[df['CD_FAIXA_ETARIA'] == 9599])
    varAcima100 = len(df.loc[df['CD_FAIXA_ETARIA'] == 9999])
    varInvalido = len(df.loc[df['CD_FAIXA_ETARIA'] == -3])

    totalPessoas = var16 + var17 + var18 + var19 + var20 + var21a24 + var25a29 + var30a34 + var35a39 + var40a44 + var45a49 + var50a54 + var55a59 + var60a64 + var65a69 + var70a74 + var75a79 + var80a84 + var85a89 + var90a94 + var95a99 + varAcima100 + varInvalido
    labelIdades = ['16 Anos', '17 Anos', '18 Anos', '19 Anos', '20 Anos', '21 a 24 Anos', '25 a 29 Anos',
                   '30 a 34 Anos', '35 a 39 Anos', '40 a 44 Anos', '45 a 49 Anos', '50 a 54 Anos', '55 a 59 Anos',
                   '60 a 64 anos', '65 a 69 anos', '70 a 74 anos', '75 a 79 anos', '80 a 84 anos',
                   '85 a 89 anos', '90 a 94 anos', '95 a 99 anos', '100 anos ou mais']

    qtdPessoas = [var16, var17, var18, var19, var20, var21a24, var25a29, var30a34, var35a39, var40a44, var45a49,
                  var50a54, var55a59, var60a64, var65a69, var70a74, var75a79, var80a84, var85a89, var90a94, var95a99,
                  varAcima100]

    dic = {
        "eixoX": labelIdades,
        "eixoY": qtdPessoas,
        "qtdGenNaoInfo": varInvalido,
        "totalPessoas": totalPessoas,
        "tituloGraph": tituloGraph,
        "tipoGrafico": graph
    }

    return dic