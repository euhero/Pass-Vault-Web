from flask import Flask, render_template, url_for, request
from generatepassword import GeneratePass

app = Flask(__name__,template_folder="templates")


# @app.route('/')
# def index():
# 	return 'Welcome To My Website'

@app.route('/', methods=['POST','GET'])
def passvault():
	if request.method == 'POST':
		password = request.form['password']
		website = request.form['website']
		username = request.form['username']
		genpass = GeneratePass(password,username,website.strip('https:').strip('http:').strip('/').strip('www.'))
		displayresponse = request.method

		return render_template('passvault.html',genpass=genpass,displayresponse=displayresponse,password=password,username=username,website=website)
	else:
		
		return render_template('passvault.html')



if __name__ == '__main__':
	app.run(debug=True)