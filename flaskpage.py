# First flask webpage

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('light bulb test.html')

@app.route('/p2')
def haha():
    return render_template('fell for it.html')

@app.route('/p3')
def galp():
    return render_template('Gallery.html')
if __name__ == '__main__':
    app.run()
    