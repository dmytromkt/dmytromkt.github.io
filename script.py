from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_note', methods=['POST'])
def play_note():
    key = request.form['key']
    note = request.form['note']
    # Здійсніть дії, щоб відтворити ноту за ключем
    # Наприклад, відправте відповідний звук на клієнтську сторону
    return 'Playing note {} for key {}'.format(note, key)

if __name__ == '__main__':
    app.run(debug=True)
