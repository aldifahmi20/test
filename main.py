from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        tasks.append({"title": title, "description": description})
    return redirect(url_for("index"))

@app.route("/delete_task/<int:index>", methods=["GET"])
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
