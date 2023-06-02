from flask import Flask,render_template
import parsMain

app=Flask(__name__,template_folder='templates')

headings=('Name','Photo')

data = parsMain.get()

@app.route('/')
def table():
    return render_template('index.html',headings=headings,data=data)

if __name__=='__main__':
    app.run(debug=True)

