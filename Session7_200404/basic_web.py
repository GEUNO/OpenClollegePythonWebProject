from flask import Flask, render_template, request

app= Flask(__name__)


@app.route('/')
def index():
    return "welcome to my hompage!"

@app.route('/about')
def about():
    return render_template('introduce.html')

@app.route('/test')
def test():
    a= request.args.get('name')
    if a is None: return "hello!"
    else: return "hello" + a

count= 0

@app.route('/visit')
def visit():
    global count
    count +=1

    if count==1:
        return "the first visitor"
    else: return "you are the "+str(count)+" visitors"

if __name__=='__main__':
    app.run()
