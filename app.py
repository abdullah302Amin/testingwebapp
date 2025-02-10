from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def hello():
    # Return HTML with a link to the second page
    return """
        Hello, welcome to the homepage!<br>
        Good to see you!!<br>
        You are on the production slot.<br>
        <a href="/second_page">Go to the second page</a>
    """

# Define the route for the second page
@app.route('/second_page')
def second_page():
    # Return a message for the second page
    return "Hello to the second page!<br>good to see you on this page"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
