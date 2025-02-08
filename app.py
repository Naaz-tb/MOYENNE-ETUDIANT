from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculer', methods=['POST'])
def calculer():
    try:
        notes = [float(request.form[f'note{i}']) for i in range(1, 6)]
        moyenne = sum(notes) / len(notes)
        return render_template('result.html', moyenne=round(moyenne, 2))
    except ValueError:
        return "Erreur : Veuillez entrer uniquement des nombres."

if __name__ == '__main__':
    app.run(debug=True)
