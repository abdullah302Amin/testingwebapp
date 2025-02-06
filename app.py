from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def hello():
    # Return HTML with a line break between the messages
    return "Hello, welcome to the homepage!<br>Good to see you!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
