from flask import Flask

app = Flask(__name__)

myMessages = []

@app.get("/hello")
def hello_world():
    print("Request received.")
    return "<p>Hello, World!</p>"

@app.post("/hello")
def goodbye_world():
    print("Request received.")
    myMessages.append("<p>Goodbye, World!</p>")
    return f"Messages len {len(myMessages)}"