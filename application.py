from flask import Flask, render_template, request, redirect

# app is an instance of class Flask
app = Flask(__name__)


# Root route
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        username = request.form.get('username')
        if username == '':
            username = 'Guest'
        return render_template('index.html', username=username, title='Index')
    return render_template('index.html', username="Guest", title='Index')


@app.route('/xyz')
def greeting():
    return render_template('greetings.html', title='Greetings')


# Run using app.run
if __name__ == '__main__':
    app.run(debug=True)
