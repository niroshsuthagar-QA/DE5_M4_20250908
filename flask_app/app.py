from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# The function to check if the price is above 300000
def checkValue(fields):
    price = fields.get('price')
    try:
        price = float(price)
        if price > 300000:
            return True
        return False
    except ValueError:
        return False  # Handle invalid input gracefully

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract form data
        fields = {
            'field1': request.form['field1'],
            'field2': request.form['field2'],
            'field3': request.form['field3'],
            'field4': request.form['field4'],
            'field5': request.form['field5'],
            'price': request.form['price']
        }
        
        # Check if the price is above 300,000
        result = checkValue(fields)
        
        # Return the result to the user
        return render_template('index.html', result=result, fields=fields)

    return render_template('index.html', result=None)

if __name__ == "__main__":
    app.run(debug=True)
