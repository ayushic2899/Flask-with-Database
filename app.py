from flask import Flask,render_template,request,redirect

from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_table'

mysql = MySQL(app)

@app.route("/")

def home():
	return render_template("home.html")

@app.route("/display",methods=["POST","GET"])

def display():
	if request.method=="POST":
		data=request.form
		name=data["name"]
		email=data["email"]
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
		mysql.connection.commit()
		cur.close()		
		return redirect('/users')
	return "<h1>Ayushi</h1>"

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
	app.run(debug=True)
