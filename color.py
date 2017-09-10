from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsColor' 

@app.route('/')
def index():
    session['color'] = "rgb(255,255,255);"
    return render_template("color.html")

@app.route('/color', methods=['POST'])
def change_color():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    color = "rgb(" + str(red) + "," + str(green) + "," + str(blue) + ");" 
    #print color
    session['color'] = color
    return render_template("color.html")
    #return redirect('/')

app.run(debug=True) 