from flask import Flask , request, render_template, url_for, redirect
from functions import functionsProject as fp



app = Flask(__name__, template_folder='pages')

@app.route('/pages/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pages/dashboard.html')
def dashboard():

    dic = fp.divisaoGenero()

    return render_template('dashboard.html', result=dic)

@app.route('/pages/compara.html')
def compara():
    return render_template('compara.html')

@app.route('/pages/documentation.html')
def decumentation():
    return render_template('documentation.html')

@app.route('/pages/dowload.html')
def dowload():
    return render_template('dowload.html')

@app.route('/pages/resultSearch.html')
def resultSearch():
    cidade = request.args.get('cidade')
    genero = request.args.get('genero')
    estadoCivil = request.args.get('estadoCivil')
    filtro = request.args.get('filtro')
    graph = request.args.get('grafico')
    ano = request.args.get('ano')

    anoSelecionado = fp.anoEleicao(ano)

    if graph != 'bar' and graph != 'line':
        return redirect(
            url_for('resultSearchOthers', cidade=cidade, genero=genero, estadoCivil=estadoCivil, filtro=filtro,
                    graph=graph))

    if filtro == 'DS_GRAU_ESCOLARIDADE':
        resultado = fp.pesquisaEscolaridade(cidade, genero, estadoCivil, graph, ano,anoSelecionado)
    elif filtro == 'DS_GÊNERO':
        resultado = fp.divisaoGeneroCidade(cidade, genero, estadoCivil, graph,ano, anoSelecionado)
    elif filtro == '5MAIORES':
        resultado = fp.maioresCidades(cidade, genero, estadoCivil, graph, ano,anoSelecionado)
    elif filtro == 'POPIDOSO':
        resultado = fp.populacaoIdosa(cidade, genero, estadoCivil, graph,ano, anoSelecionado)
    elif filtro == 'IDADES':
        resultado = fp.pesquisaIdade(cidade, genero, estadoCivil, graph,ano, anoSelecionado)


    return render_template('resultSearch.html', result=resultado)



@app.route('/pages/resultSearchOthers.html')
def resultSearchOthers():
    cidade = request.args.get('cidade')
    genero = request.args.get('genero')
    estadoCivil = request.args.get('estadoCivil')
    filtro = request.args.get('filtro')
    graph = request.args.get('graph')
    ano = request.args.get('ano')

    anoSelecionado = fp.anoEleicao(ano)

    if filtro == 'DS_GRAU_ESCOLARIDADE':
        resultado = fp.pesquisaEscolaridade(cidade, genero, estadoCivil, graph, ano,anoSelecionado)
    elif filtro == 'DS_GÊNERO':
        resultado = fp.divisaoGeneroCidade(cidade, genero, estadoCivil, graph,ano, anoSelecionado)
    elif filtro == '5MAIORES':
        resultado = fp.maioresCidades(cidade, genero, estadoCivil, graph, ano,anoSelecionado)
    elif filtro == 'POPIDOSO':
        resultado = fp.populacaoIdosa(cidade, genero, estadoCivil, graph, ano,anoSelecionado)
    elif filtro == 'IDADES':
        resultado = fp.pesquisaIdade(cidade, genero, estadoCivil, graph,ano, anoSelecionado)

    return render_template('resultSearchOthers.html', result=resultado)


@app.route('/pages/team.html')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)