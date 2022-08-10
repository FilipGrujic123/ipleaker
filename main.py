import flask

app = flask.Flask(__name__)

@app.route('/')
def front_page():
    print(f'!!!!!!!! {str(flask.request.remote_addr)} !!!!!!!!')
    return flask.render_template('Wordle - The New York Times.html')

app.run(debug=True)