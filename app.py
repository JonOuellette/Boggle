from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "bogglesmymind123"
app.config['TESTING'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def home_page():
    board = boggle_game.make_board()
    session['board'] = board
    
    return render_template("base.html", board=board)

@app.route("/check-word")
def check_word():
        word = request.args["word"]
        board = session["board"]
        response = boggle_game.check_valid_word(board,word)

        return jsonify({'result': response})

@app.route("/post-score", methods= ["POST"])
def post_score():
      