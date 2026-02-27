from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

PRESENTATION_FOLDER = 'static/presentations'

@app.route('/')
def index():
    files = os.listdir(PRESENTATION_FOLDER)
    return render_template('index.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(PRESENTATION_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)