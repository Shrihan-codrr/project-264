# Import Libraries below
import os 
from flask import  Flask, request, redirect, url_for, render_template , send_file
from werkzeug.utils import secure_filename
# Define flask 
app = Flask(__name__)


@app.route('/')
def load_form():
    return render_template('upload.html')

# Define upload_form() and route the webapp 
@app.route('/gray', methods=['POST'])
def upload_form():
    return render_template('upload.html')
# Define upload_video() to get video in defined folder and route the webapp  
@app.route('/' , methods = ['POST'])
def upload_video():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/', filename))
    return render_template('upload.html', filename=filename, message = display_message)

@app.route('/display/<filename>')
def display_video(filename):
    return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run(debug=True)
