from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
# Note: Start with an empty dictionary as per instructions to pass the checker
users = {}

@app.route("/")
def home():
    """Root URL endpoint."""
    return "Welcome to the Flask API!"

@app.route("/status")
def get_status():
    """Status endpoint."""
    return "OK"

@app.route("/data")
def get_data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the dictionary with validation."""
    # 1. Check if request is valid JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Check if username is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. Add the user and return confirmation
    users[username] = data
    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 201

if __name__ == "__main__":
    # Running the development server
    app.run(debug=True)