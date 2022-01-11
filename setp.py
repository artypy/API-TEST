from flask import *
import json
import time

app = Flask(__name__)

@app.route('/', methods=['get'])

def home_page():
    data_set ={'page': 'home' , 'Msg': '200' , 'time': time.time()}

    jsonlol = json.dumps(data_set)

    return jsonlol

@app.route('/oogabooga/', methods=['get'])
 
def BOOGA():
    user = str(request.args.get('user'))    #/?user=LOL
    data_set ={'page': 'nothome' , 'Msg': 'OOGABOOGA'+ (user)}
    jsonlol = json.dumps(data_set)

    return jsonlol
if __name__ == '__main__':
    app.debug = True
    app.run()
