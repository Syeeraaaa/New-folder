from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nama = None
    if request.method == 'POST':
        nama = request.form.get('nama')
    return render_template('index.html', nama=nama)

if __name__ == '__main__':
    app.run(debug=True)