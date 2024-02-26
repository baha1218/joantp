from flask import Flask, render_template, request
from subprocess import check_output

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_command', methods=['POST'])
def execute_command():
    command = request.form['command']
    try:
        output = check_output(command, shell=True).decode('latin-1')
    except UnicodeDecodeError:
        output = "Unable to decode command output"
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
