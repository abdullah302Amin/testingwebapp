from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def hello():
    return "Hello, welcome to the homepage!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
