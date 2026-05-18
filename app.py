from flask import Flask, request, render_template_string
import yaml, os, subprocess

app = Flask(__name__)

@app.route("/search")
def search():
    q = request.args.get("q", "")
    return render_template_string(f"<h1>Results for {q}</h1>")

@app.route("/config", methods=["POST"])
def load_config():
    data = request.get_data()
    config = yaml.load(data, Loader=yaml.Loader)
    return str(config)

@app.route("/run")
def run_cmd():
    cmd = request.args.get("cmd")
    result = subprocess.check_output(cmd, shell=True)
    return result

if __name__ == "__main__":
    app.run(debug=True)
