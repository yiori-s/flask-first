#coding:utf-8
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method=='POST':
		return render_template('index.html',title="Flask test POST", body=request.form['message'], nums=[3,4,5], dict={'a':1, 'b':2})
	else:
		return render_template('index.html',title="Flask test GET", body="Welcome", nums=[0,1,2], dict={'a':3, 'b':4})

if __name__ == "__main__":
	app.run()
