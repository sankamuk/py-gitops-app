from flask import Flask, request, jsonify, abort
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
  time_now = datetime.now().strftime("%Y%m%d-%H%M%S")
  hst_nm = os.uname()[1]
  app_vrsn = ([ l for l in open('pom.xml') if '<version>' in l ][0]).split('<version>')[1].split('</version>')[0]
  return "Date: {0}, Host: {1}, Version: {2}".format(time_now, hst_nm, app_vrsn)

if __name__ == '__main__' :
  app.run(debug=True, host='0.0.0.0', port=8000)
