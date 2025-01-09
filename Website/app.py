from flask import Flask, request, abort,render_template

app = Flask(__name__)

# Hardcoded credentials for simplicity
AUTHORIZED_USERNAME = "100bd919fc25d9aea85cf1400c52e6a1558357330a0b9f5550a521d41e5226c4"
AUTHORIZED_PASSWORD = "3394b4c8e567604828bc7d8f8ffed599d9821706b5a13c2dd3d64501a67dbf9c"
URL_PATH="url.txt"

def read():
    try:
        with open(URL_PATH, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No IP address stored yet."

@app.route('/write', methods=["POST"])
def write():
    # Get credentials and IP address from the request
    username = request.form.get('username')
    password = request.form.get('password')
    ip_address = request.form.get('ip_address')
    # Validate credentials
    if username != AUTHORIZED_USERNAME or password != AUTHORIZED_PASSWORD:
        abort(403)  # Forbidden if authentication fails

    # Update the IP address in the file
    try:
        with open(URL_PATH, "w") as file:
            file.write(ip_address)
        return "IP address updated successfully!"
    except Exception as e:
        return f"Error updating IP address: {e}", 500

@app.route('/')
def home():
    ip=read()
    return render_template("index.html",ip=ip)


if __name__ == "__main__":
    app.run(debug=True)
