from flask import Flask, render_template
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

app = Flask(__name__)

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"

def get_terms(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_quiz_info(quiz_id):
    url = "https://www.quizlet.com/es/" + quiz_id
    req = Request(
        url, 
        data=None, 
        headers={
            'User-Agent': USER_AGENT
        }
    )
    with urlopen(req) as response:
        html = response.read()
        return get_terms(html)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz/<quiz_id>")
def quiz(quiz_id):
    return get_quiz_info(quiz_id)

if __name__ ==  "__main__":
    app.run()