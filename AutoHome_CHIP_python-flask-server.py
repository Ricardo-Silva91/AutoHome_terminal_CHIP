from flask import Flask, jsonify, request

app = Flask(__name__)

import json

import general_things
import controllers.gpio_control


@app.route('/', methods=['GET'])
def hello_world():
    return 'AutoHome Terminal ' + str(general_things.getMyInfo()['id']) + ' says: good evening...'


@app.route('/getMyInfo', methods=['GET'])
def get_my_info():
    return jsonify(general_things.getMyInfo())


@app.route('/setPinState', methods=['POST'])
def set_pin_state():

    requestBody = request.get_json()

    pin_number = requestBody["pinNumber"]
    new_pin_state = requestBody["newPinState"]

    res = general_things.makeOkRes()

    myInfo = general_things.getMyInfo()

    pin = general_things.getPinByNumber(myInfo, pin_number)

    if pin is not None and pin['op'] == 'out':
        if new_pin_state == 'HIGH' or new_pin_state == 'LOW':
            try:
                controllers.gpio_control.setPinState(pin['realName'], new_pin_state)
                pin['currentState'] = new_pin_state
                general_things.setPinByNumber(myInfo, pin)
                general_things.writeMyInfo(myInfo)
            except IOError:
                res = general_things.makeErrorRes(0, 'trouble using gpio', 'none')
        else:
            res = general_things.makeErrorRes(0, 'bad state', 'newPinState')
    else:
        res = general_things.makeErrorRes(0, 'bad pinNumber', 'pinNumber')

    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
