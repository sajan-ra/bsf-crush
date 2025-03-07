from flask import Flask, render_template, request
import random
from send_mail import send_email  # Import the email function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match_names():
    name1 = request.form['name1'].strip().capitalize()
    name2 = request.form['name2'].strip().capitalize()
    
    # Simple match percentage logic (Randomized for fun)
    match_percentage = random.randint(50, 100)
    
    # Format message
    message = f"💖 Match Percentage between {name1} and {name2}: {match_percentage}%"
    
    # Send email to you
    send_email("New Name Match!", message)
    
    return render_template('result.html', name1=name1, name2=name2, match_percentage=match_percentage)

if __name__ == '__main__':
    app.run(debug=True)
