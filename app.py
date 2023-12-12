from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Generate a random number for the game (between 1 and 100)
target_number = random.randint(1, 100)

@app.route('/')
def index():
    return "Welcome to the Number Guessing Game API!"

@app.route('/game', methods=['GET'])
def get_game():
    numbers_to_guess = list(range(1, 101))
    return jsonify({'numbers_to_guess': numbers_to_guess})

@app.route('/guess', methods=['POST'])
def make_guess():
    data = request.get_json()

    if 'number' not in data:
        return jsonify({'error': 'Please provide a "number" in the request body'}), 400

    guess_number = data['number']

    if guess_number == target_number:
        result = "Correct"
    elif guess_number < target_number:
        result = "Too Low"
    else:
        result = "Too High"

    response = {
        'guessed_number': guess_number,
        'result': result
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
