from flask import Flask, app

HWApp = Flask(__name__) # Create a Flask application instance

@HWApp.route("/")       # Define a route for the root URL
def home():                     # Define the function to be called when the root URL is accessed
    return "Hello, Flask!"      # Return a simple greeting message

@HWApp.route("/about")
def about():
    return "About"

if __name__ == "__main__":      # Check if the script is being run directly
    HWApp.run(host="127.0.0.1", port=5000, debug=True)  # Run the Flask application on localhost at port 5000 with debug mode enabled    
    