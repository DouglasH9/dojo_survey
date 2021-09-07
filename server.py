from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'omar comin!'

@app.route('/')
def render_page():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_info():
    session['name']=request.form['name']
    session['city']=request.form['city']
    session['language']=request.form['language']
    return redirect('/result')

@app.route('/result')
def show_result():
    return render_template('infoCard.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)