from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Itomaru!'

@app.route('/contents')
def contents():
    return 'Itomaru Contents!'

@app.route('/news')
def news():
    return 'Itomaru News!'
    
@app.route('/about')
def about():
    return 'About Itomaru!'

@app.route('/contact')
def contact():
    return 'Contact Itomaru!'

if __name__ == '__main__':
    app.run(debug=True)