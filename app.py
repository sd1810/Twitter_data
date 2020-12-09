from flask import Flask,render_template,request
from poc1 import get_data
app = Flask(__name__)

urls=[]
# Route for the home page
@app.route("/")
def home():
    return render_template('home.html')

# Post Route for the tweets page
@app.route("/tweets",methods=['POST'])
def show_tweets():
    input_company = request.form['company_name']
    urls = get_data(input_company)
    return render_template('tweets.html',urls=urls)

# Get Route for tweets page
@app.route("/tweets",methods=['GET'])
def tweets():
    return render_template('tweets.html',urls=urls)

if __name__ == '__main__':
    app.run(debug=True)
