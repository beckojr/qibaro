# My first flask applicaiton

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index/index.html')

@app.route('/inscription')
def inscription():
    return render_template('/index/inscription.html')

@app.route('/page-layout/')
def page_layout():
    return render_template('/content/page-layout.html')

@app.route('/home/')
def home():
    return render_template('/content/home.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000')
