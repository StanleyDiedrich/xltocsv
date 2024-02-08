from flask import Flask , render_template

app=Flask (__name__)
@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html', title='title')

@app.route("/about")
def about():
    return "<h1>Поговорим?</h1>"

if __name__ == "__main__":
    app.run(debug=True)