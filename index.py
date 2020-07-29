from flask import Flask
from flask import request
# from requests.api import request
app = Flask(__name__)

@app.route('/',methods=["POST"])
def get_sensor_data():
    print(request.headers)
    data=request.get_json()
    print(data["rot_x"])
    print(data["rot_y"])
    print(data["rot_z"])
    return request.get_data()