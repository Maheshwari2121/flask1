from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/new_page')
def new_page():
    sorted_integers = request.args.get('sorted_integers', '')
    sorted_integers = [int(num) for num in sorted_integers.split(',')]

    return render_template('new_page.html', sorted_integers=sorted_integers)

if __name__ == '__main__':
    app.run()
