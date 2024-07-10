from flask import Flask, render_template # Importing the Flask module
app = Flask(__name__) # Creating a Flask object

@app.route('/') # Defining the home page of our site
def home(): # Defining the home function
    return render_template('index.html') # Returning the index.html file

@app.route('/viewmoreamericana') # Defining the /more-images page of our site
def more_images(): # Defining the more_images function
    return render_template('seemore-americana.html') # Returning the more-images.html file

if __name__ == '__main__': # Checking if the script is run directly
    app.run(host="0.0.0.0", debug=True, port=5001) # Running the Flask app