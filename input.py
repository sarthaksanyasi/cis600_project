from flask import Flask, request,send_file, render_template, jsonify
import pandas as pd
import json as js
from io import StringIO
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/csv_upload', methods=['POST'])
def csv_upload():
    # Get the uploaded file from the frontend
    file = request.files['file']

    # Read the first line of the CSV file to get the header row
    #header = file.readline().decode().strip()

    # Get the name of the first column
    #first_column = header.split(',')[0]
    
    selected_column = request.form['csv_dropdown']
    
    df = pd.read_csv(file)

    # Return the name of the first column as a plain text response
    #return first_column
    
    df.to_csv('../cis600_project/uploaded_CSV_file/process_data.csv', encoding='utf-8', index=False)

    return jsonify({
        #'csv': df.to_dict(),
        #'first_column': first_column,
        'selected_column': selected_column
    })

if __name__ == '__main__':
    app.run(debug=True)
