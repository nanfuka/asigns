from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello_name():
    li = []
    thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    for x in thisdict:
        r =thisdict[x]
    li.append(r)
            
    


    # i = 0
    # while i<len(user):
    #     fr = user[i]
    return render_template('nop.html', name = li)

if __name__ == '__main__':
   app.run(debug = True)