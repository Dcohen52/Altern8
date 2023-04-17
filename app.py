import os
import datetime
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from io import StringIO
from contextlib import redirect_stdout
import altern8

app = Flask(__name__)


def get_upload_folder():
    return os.path.join(os.getcwd(), 'uploads')


@app.route('/playground.html', methods=['GET', 'POST'])
def index():
    now = datetime.datetime.now()
    formatted = now.strftime("%H:%M:%S")
    output = ""
    if request.method == 'POST':
        if 'code_file' not in request.files:
            code = request.form['code']  # get the code from the input field
            if not code:
                return render_template('playground.html', output=output)
            output_stream = StringIO()
            with redirect_stdout(output_stream):
                result, error = altern8.run('<stdin>', code)
            output = output_stream.getvalue()
            if error:
                output += error.as_string()
        else:
            code_file = request.files['code_file']
            if code_file.filename == '':
                return render_template('playground.html', output=output)
            filename = secure_filename(code_file.filename)
            file_path = os.path.join(get_upload_folder(), filename)
            code_file.save(file_path)
            output_stream = StringIO()
            with redirect_stdout(output_stream):
                result, error = altern8.run('<stdin>', f'run("{file_path}")')
            output = output_stream.getvalue()
            if error:
                output += error.as_string()
    return render_template('playground.html', output=output)


@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    code = data['code']
    output_stream = StringIO()
    with redirect_stdout(output_stream):
        result, error = altern8.run('<stdin>', code)
    output = output_stream.getvalue()
    if error:
        output += error.as_string()
    return jsonify({'output': output})

@app.route('/')

def get_started():
    return render_template('index.html')

@app.route('/downloads.html')
def downloads_page():
    return render_template('downloads.html')


@app.route('/alpin.html')
def alpin_page():
    return render_template('alpin.html')


@app.route('/documentation.html')
def docs_page():
    return render_template('documentation.html')


if __name__ == '__main__':
    app.run(debug=True)
