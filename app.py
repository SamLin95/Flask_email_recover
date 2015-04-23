from flask import Flask, request
from flask.ext.mail import Message, Mail

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'slin950205@gmail.com'
app.config['MAIL_PASSWORD'] = 'linsizhe123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

admin = ["slin950205@gmail.com"]
mail = Mail(app)


def sendMessage(recipient, password):
	try:
		msg = Message("Your Password", sender="Our Application", recipients=[recipient])
		msg.body = "your password is: %s \n\n\n\n Thank you for using our application\n best\n Sizhe Lin"%(password,)
		with app.app_context():
			mail.send(msg)
	except Exception:
		return "error occurs"	


@app.route("/recover", methods=["POST", "GET"])
def recover():
	if request.method=="POST":
		try 
			email = request.args.get("email")
			password = request.args.get("password")
			sendMessage(email, password)
		except Exception:
			return "error occurs"
		return "successful"
	return "error occurs"

app.run("0.0.0.0", port=8080)
