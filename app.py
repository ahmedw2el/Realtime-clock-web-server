from flask import Flask, render_template
import time
app = Flask(__name__)

cc= time.ctime()
@app.route('/')
def home():
   cc= time.ctime()
   return render_template('index.html', out=cc)
if __name__ == '__main__':
   app.run()

