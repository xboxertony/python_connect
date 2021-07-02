from flask import Flask,render_template,request
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from werkzeug.serving import run_with_reloader
from flask_cors import CORS


app = Flask(__name__)

sockets = Sockets(app)

cors = CORS(app,resources={r"/*": {"origins": "*"}})

@sockets.route("/actions")
def echo_socket(ws):
    while True:
        message = ws.receive()
        if(message=="socket open"):
            ws.send("歡迎使用客服機器人")
        elif(message=="photo"):
            ws.send("請幫我我我我")
        else:
            ws.send(message)
@app.route("/")
def home():
    return "hello"

@app.route("/echo_test",methods = ["GET"])
def echo_test():
    return render_template("index.html")

def run_server():
    server = pywsgi.WSGIServer(('', 3000), app, handler_class=WebSocketHandler)
    server.serve_forever()

if __name__=="__main__":
    run_with_reloader(run_server)

# if __name__ == "__main__":
#     app.run(debug=True)
#     from gevent import pywsgi
#     from geventwebsocket.handler import WebSocketHandler
#     server = pywsgi.WSGIServer(('', 8000), app, handler_class=WebSocketHandler)
#     server.serve_forever()