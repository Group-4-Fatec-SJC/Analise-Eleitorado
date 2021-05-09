from flask import Flask , request, render_template, url_for
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




    if filtro == 'DS_GRAU_ESCOLARIDADE':
        resultado = fp.pesquisaEscolaridade(cidade, genero, estadoCivil)

    if filtro == 'DS_GÊNERO':
        resultado = fp.divisaoGeneroCidade(cidade, genero, estadoCivil)

    return render_template('resultSearch.html', result=resultado)

@app.route('/pages/team.html')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)