from flask import Flask,render_template
from flask_sockets import Sockets

app = Flask(__name__)

sockets = Sockets(app)

@sockets.route("/WebSocketHome/actions")
def echo_socket(ws):
    while True:
        message = ws.receive()
        if(message=="socket open"):
            ws.send("歡迎使用客服機器人")
        else:
            ws.send(message)
@app.route("/")
def home():
    return "hello"

@app.route("/echo_test",methods = ["GET"])
def echo_test():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)