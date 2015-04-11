import flask
app = flask.Flask("My Server")

@app.route("/")
def index():
	html = """
	<a href='%s'>Home</a> | <a href='%s'>About</a> | <a href='%s'>Contact Page</a><br>
	""" % (flask.url_for("index"),
		   flask.url_for("about"),
		   flask.url_for("contact")
		   )
	return html+flask.render_template("home.html")

@app.route("/about")
def about():
	#name = "edos"
	html = """
		<a href='%s'>Home</a> | <a href='%s'>About</a> | <a href='%s'>Contact Page</a><br><br>I am a mini website done in Python and Flask. See me at <a href="https://github.com/edos4/flaskite">Flasksite</a>
	""" % (flask.url_for("index"),
		   flask.url_for("about"),
		   flask.url_for("contact")
		   )

	return html

@app.route("/contact")
def contact():
	html = """
	<a href='%s'>Home</a> | <a href='%s'>About</a> | <a href='%s'>Contact Page</a><br>
	""" % (flask.url_for("index"),
		   flask.url_for("about"),
		   flask.url_for("contact")
		   )
	return html+flask.render_template("form.html")

@app.route("/form", methods=["GET", "POST"])
def form():
	html = """
	<a href='%s'>Home</a> | <a href='%s'>About</a> | <a href='%s'>Contact Page</a><br>
	""" % (flask.url_for("index"),
		   flask.url_for("about"),
		   flask.url_for("contact")
		   )
	#name = flask.request.form.get('name') #GET
	name = flask.request.form.get('name') #POST
	email = flask.request.form.get('email') #POST
	message = flask.request.form.get('message') #POST
	return html+flask.render_template("form.html", name=name, email=email, message=message)


if __name__ == "__main__":
	app.debug = True
	app.run()
