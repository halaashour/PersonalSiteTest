from flask import Flask, render_template

#import random from randit 
app=Flask(__name__)
@app.route("/")

def loadweb():
	return render_template("Introducingmyself.html")

if __name__=="__main__":
	app.run(port = 4000,debug=True)
