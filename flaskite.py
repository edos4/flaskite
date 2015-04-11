import flask
app = flask.Flask("My Server")

@app.route("/")
def index():
	html = """
	<a href='%s'>Home</a><br>
	<a href='%s'>About</a><br>
	<a href='%s'>Contact Page</a><br>
	""" % (flask.url_for("Hello_World"),
		   flask.url_for("Joke"),
		   flask.url_for("Joke", name="Yourname"))
	#return html
	return flask.render_template("home.html")

@app.route("/hello")
def Hello_World():
	return "Hello World"

@app.route("/whoami")
def MyName():
	html = """
		<center>
			<strong>Edwin</strong>
		</center>"""
	return html

@app.route("/joke")
@app.route("/joke/<name>")
def Joke(name):
	#name = "edos"
	html = """
	<img src='%s' />
	Chuck Norris haha<br>
	has a live bear %ss<br>
	lying on the""" %(flask.url_for('static', filename='cat.jpg'), name)

	return html

@app.route("/form", methods=["GET", "POST"])
def form():
	#name = flask.request.form.get('name') #GET
	name = flask.request.form.get('name') #POST
	return flask.render_template("form.html", name=name)


if __name__ == "__main__":
	app.debug = True
	app.run()
