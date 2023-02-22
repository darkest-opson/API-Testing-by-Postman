from flask import Flask,jsonify,request
import random 

app = Flask(__name__)

@app.route('/postman_data',methods = ['GET'])
def math_operation1():
    num = int(request.json['num'])
    rand = random.randint(1, 100)
    print(rand)
    if num == rand:
        r = "you predicted correct "
    elif num<rand:
        r = "you predicted lower value"
    else:
        r = "you predicted upper value"
    return jsonify(r)

if __name__=="__main__":
    app.run(host="0.0.0.0")
