from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Lab 2</h1>
    <h2>Containerized Flask Application</h2>
    <p>Application is running successfully inside Docker.</p>
    <p>Student: Aaryan Tandon</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
