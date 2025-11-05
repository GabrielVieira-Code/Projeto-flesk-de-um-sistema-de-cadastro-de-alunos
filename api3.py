from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

alunos=[{
    'nome':'Gabriel',
    'idade':26,
    'telefone':'12312312'
},
{
    'nome':'fernando',
    'idade':12,
    'telefone':'2312322'
}
]

# caminho a ser seguido pelo ususario
@app.route('/')
def index():
    return render_template('register.html',alunos=alunos)

@app.route('/adicionar',methods=['POST'])
def adicioar():
    nome = request.form['nome']
    idade = request.form['idade']
  
 
    alunos.append( {'nome':nome,'idade':idade})
    return redirect(url_for('index'))




app.run(debug=True)
