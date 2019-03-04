from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = 'vnlka123lkjfs#'
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/pen")
def pen():
        return "Would you like 15 Peruvian Nuevos?"

@app.route("/sessions")
def sessions():
    return render_template("session.html")


def messageReceived(methods=["GET", "POST"]):
    print("message was recieved!")


@socketio.on("my event")
def handle_my_custom_event(json, methods=["GET", "POST"]):
    print("received my event: " + str(json))
    socketio.emit("my response", json, callback=messageReceived)


if __name__ == "__main__":
    socketio.run(app, debug=True)
