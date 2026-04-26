from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data")
def data():
    # Returns a list of all keys (usernames)
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # 1. Parse JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # 2. Check for username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # 3. Check if exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # 4. Process the data
    # Create a copy of the data and remove the username key 
    # so it matches the storage format: {"name": "John", "age": 30, "city": "New York"}
    user_info = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    users[username] = user_info
    
    # 5. Return confirmation with the data
    # Standard format: {"message": "User added successfully", "user": {...}}
    return jsonify({
        "message": "User added successfully",
        "user": data  # Returns the full input data as confirmation
    }), 201

if __name__ == "__main__":
    app.run()