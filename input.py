from flask import Flask, request
import pandas as pd
import json as js

app = Flask(__name__)

@app.route('/csv', methods=['POST'])
def csv():
    # Get the uploaded file from the request
    csv_file = request.files['file']
    
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Perform some operation on the DataFrame
    # For example, let's calculate the sum of the first column
    sum_first_col = df.iloc[:, 0].sum()
    print('result is ', sum_first_col)
    # Return the result
    y = js.dumps(int(sum_first_col))
    #return {'sum_first_col': sum_first_col}
    return y

if __name__ == '__main__':
    app.run(debug=True)
