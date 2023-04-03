from flask import Flask, request, render_template
import pandas as pd
import json as js
from io import StringIO
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/csv_upload', methods=['POST'])
def csv_upload():
    # Get the uploaded file from the request
    file = request.files['file']
    filename = secure_filename(file.filename)
    # Check if the filename is safe
    if filename != file.filename:
        return 'Unsafe filename', 400
    
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file)
    csv_columns = df.columns.tolist()
    return js.dumps({'filename': filename, 'columns': csv_columns})

if __name__ == '__main__':
    app.run(debug=True)
