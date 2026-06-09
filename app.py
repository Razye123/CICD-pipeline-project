from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<h1>CICD pipeline working </h1>
<p>Auto deployed via github actions</p>
<p>Docker image built Automatically</p>
"""

@app.route("/health")
def health():
    return {"Status": "healthy", "pipeline": "active"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

