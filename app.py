from flask import Flask, render_template, request, jsonify
from game import TwentyFortyEight

app = Flask(__name__)
game = TwentyFortyEight()

@app.route('/restart', methods=['POST'])
def restart():
    global game
    game = TwentyFortyEight()
    return jsonify(success=True)

@app.route('/')
def index():
    combined_matrix = [
        [(int(cell), f'cell-{int(cell)}' if cell > 0 else 'cell-0') for cell in row]
        for row in game.matrix
    ]
    return render_template('index.html', combined_matrix=combined_matrix)

@app.route('/move', methods=['POST'])
def move():
    direction = request.json.get('direction')
    if direction == 'left':
        game.horizontal(1)
    elif direction == 'right':
        game.horizontal(-1)
    elif direction == 'up':
        game.vertical(1)
    elif direction == 'down':
        game.vertical(-1)
    return jsonify(game.matrix.tolist())

if __name__ == '__main__':
    app.run(debug=True)
