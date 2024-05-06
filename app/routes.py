from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/name/<name>')
def name(name):
    return f"Hello, {name}!"