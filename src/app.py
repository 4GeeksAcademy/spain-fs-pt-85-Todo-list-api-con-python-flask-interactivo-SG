from flask import Flask, request, jsonify
app = Flask(__name__)
todos = [{"label": "My first task", "done": False}]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = todos
    return jsonify(json_text), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    deleted_todo = todos.pop(position)
    print("This is the position to delete", deleted_todo)
    return jsonify(todos), 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
