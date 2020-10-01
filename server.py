# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
# The "@" decorator associates this route with the function immediately following
app = Flask(__name__)

@app.route('/')
def hello_world():    
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template('index.html', usertable = users)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Well now you dun 404'd.  Probably shouldn't be here.  Run along."

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
