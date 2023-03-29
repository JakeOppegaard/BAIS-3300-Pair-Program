from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# a. Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# b. /add route to collect and process data from the form
@app.route('/add', methods=['POST'])
def add():
    # Extract data from the form
    field1 = request.form.get('field1')
    field2 = request.form.get('field2')
    # Add other fields as needed

    # Process the data (example: sum of two numbers)
    result = int(field1) + int(field2)

    # Redirect to the desired page (example: result page) with the result
    return redirect(url_for('result', result=result))

# c. About route
@app.route('/about')
def about():
    return render_template('about.html')

# Route to display the result of the /add route
@app.route('/result/<int:result>')
def result(result):
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
