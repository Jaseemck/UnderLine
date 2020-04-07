from flask import Flask 

application = Flask(__name__)

@application.route("/")
def homepage():
    return("Hello World!")

if __name__ == "__main__":
    application.run()
