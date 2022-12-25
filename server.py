import random
from flask import Flask

random_number = random.randint(0, 9)


app = Flask(__name__)

@app.route('/')

def home_route():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<iframe src="https://giphy.com/embed/4Zo41lhzKt6iZ8xff9" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/4Zo41lhzKt6iZ8xff9">via GIPHY</a></p>'

@app.route("/<int:guess>")

def number_guessing(guess):
    if guess > random_number:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '<iframe src="https://giphy.com/embed/Y4pAQv58ETJgRwoLxj" width="384" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/dog-eyebleach-im-flying-Y4pAQv58ETJgRwoLxj">via GIPHY</a></p>'

    elif guess < random_number:
        return '<h1 style="color: red">Too low, try again!</h1>' \
               '<iframe src="https://giphy.com/embed/VTXzh4qtahZS" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/VTXzh4qtahZS">via GIPHY</a></p>'
    else:
        return '<h1 style="color: blue">You guessed it!</h1>' \
               '<iframe src="https://giphy.com/embed/1jWaJ8RgySqOaPjl45" width="384" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/jesseling-1jWaJ8RgySqOaPjl45">via GIPHY</a></p>'


if __name__ == "__main__":
    app.run(debug=True)
