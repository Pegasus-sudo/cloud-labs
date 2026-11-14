from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/users/1', methods=['GET'])
def get_user():
    return jsonify({
        "user_id": 1,
        "name": "Alice Smith",
        "membership": "Gold"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
