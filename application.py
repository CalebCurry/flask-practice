from flask import Flask
application = Flask(__name__)
app = application


@app.route('/')
def hello_world():
    return 'Hello, World!'


"""
if __name__ == "__main__":
    application.debug = True
    application.run()
"""
