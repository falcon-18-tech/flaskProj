from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/postint', methods = ['POST'])
def post_integer():
    data = request.get_json()
    value = data.get('value')
    with open('output.txt', 'a') as f:
        f.write(str(value))
    return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)