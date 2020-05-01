from flask import Flask, request, redirect
app = Flask(__name__,  static_url_path='')

@app.route('/',methods=["POST", "GET"])
def index():
    return app.send_static_file('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if (request.method == "POST"):
       req=request.form
       print(req)
       if req['lpw']=="asdf":
           return redirect('minecraft.html')

    return app.send_static_file('index.html')