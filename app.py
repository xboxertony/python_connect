from flask import Flask, json,render_template,request
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from werkzeug.serving import run_with_reloader
from flask_cors import CORS
import config

# import logging
# logger = logging.getLogger(__name__)

app = Flask(__name__)
app.debug=True

logger = app.logger

sockets = Sockets(app)

cors = CORS(app,resources={r"/*": {"origins": "*"}})

@sockets.route("/actions")
def echo_socket(ws):
    while True:
        message = ws.receive()
        mes = json.loads(message)
        if(mes.get("ok")=="socket open"):
            ws.send("歡迎使用客服機器人")
        elif(mes.get("ok")=="photo"):
            ws.send("請幫我")
        else:
            ws.send("請問有甚麼問題呢?")
@app.route("/")
def home():
    return "hello"

@app.route("/echo_test",methods = ["GET"])
def echo_test():
    return render_template("index.html",host=config.host)

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