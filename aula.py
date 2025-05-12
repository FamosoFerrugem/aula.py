/cadastro_professores/
│
├── app.py               # Código Python com Flask
├── templates/
│   └── index.html       # Página HTML com formulário e listagem
└── static/
    └── style.css        # Estilo da página
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista para armazenar os professores substitutos (temporariamente em memória)
professores = []

@app.route('/')
def index():
    return render_template('index.html', professores=professores)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    telefone = request.form['telefone']

    professores.append({
        'nome': nome,
        'disciplina': disciplina,
        'telefone': telefone
    })
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
