import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    #return 'Hello'
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name-socker.gethostname(), color=color_codes[new_color])

@app.route('/read_file')
def read_file():
    f = open("data/testfile.txt")
    contents = f.read()
    return render_template('hello.html', name=socket.gethostname(). contents=contents, color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
