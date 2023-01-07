from flask import Flask, render_template, request
app = Flask(__name__)

@app.route( '/', methods = ['POST', 'GET'])
def hei():
    if request.method == 'POST':
        name = request.form[ 'name']        
        return 'Hei ' + name + '!'
   
    return render_template( 'NameForm.html')
