from flask import Flask, request
import pandas as pd
import json as js
import csv as csvtest
from io import StringIO
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/csv_upload', methods=['POST'])
def csv_upload():
    # Get the uploaded file from the request
    
    ###### intial logic for printing headers start ######
    #csv_file = pd.read_csv(request.files['file'], index_col=0, nrows=0).columns.tolist()
    
    #print('headers were: ', csv_file)
    #y = '\n'.join(csv_file)
    ###### intial logic for printing headers end ########

    # Load the CSV file into a pandas DataFrame
    #df = pd.read_csv(csv_file)

    #testcols = pd.read_csv(StringIO(request.files['file']), index_col=0, nrows=0).columns.tolist()

    #csv_file = request.files['file']
    
    #csv_file = pd.read_csv(request.files['file'])
    #file_data = csv_file.read().decode("utf-8")
    
    #with open(file_data, newline='') as file:
    #    reader = csvtest.reader(file, delimiter = ' ')
    #    headings = next(reader)
    
    ## Perform some operation on the DataFrame
    ## For example, let's calculate the sum of the first column
    #sum_first_col = df.iloc[:, 0].sum()
    
    #print('result is ', sum_first_col)
    ## Return the result
    #y = js.dumps(int(sum_first_col))

    #test comment
    #return {'sum_first_col': sum_first_col}
    #return y
    
    # Code Changes for safe file :: Start : Sarthak ###########################

    file = request.files['file']
    filename = secure_filename(file.filename)
    # Check if the filename is safe
    if filename != file.filename:
        return 'Unsafe filename', 400
    # Process the file
    # ...
    return 'File uploaded successfully'

    # Code Changes for safe file :: End : Sarthak #############################

    

if __name__ == '__main__':
    app.run(debug=True)
