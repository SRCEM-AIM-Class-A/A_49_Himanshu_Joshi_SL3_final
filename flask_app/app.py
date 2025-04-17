from flask import Flask, render_template, request, redirect, url_for, flash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user_info', methods=['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        
        # Error handling
        if not name:
            flash('Please enter a name')
            return redirect(url_for('user_info'))
        
        if not age:
            flash('Please enter an age')
            return redirect(url_for('user_info'))
            
        try:
            age = int(age)
            if age <= 0 or age > 120:
                flash('Please enter a valid age between 1 and 120')
                return redirect(url_for('user_info'))
        except ValueError:
            flash('Age must be a number')
            return redirect(url_for('user_info'))
            
        # Process valid inputs
        return render_template('greeting.html', name=escape(name), age=age)
        
    # GET request - show the form
    return render_template('user_form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)