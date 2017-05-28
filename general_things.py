import os
import json

rootDir = os.path.dirname(__file__)

myInfoPath = rootDir + '/data/myInfo.json'


def getMyInfo():
    with open(myInfoPath) as data_file:
        return json.load(data_file)


def getPinByNumber(myInfo, pinNumber):
    res = None

    for pin in myInfo['pins']:
        if pin['number'] == pinNumber:
            res = pin
            break

    return res


def setPinByNumber(myInfo, piner):
    for index, pin in enumerate(myInfo['pins']):
        if pin['number'] == piner['number']:
            myInfo['pins'][index] = piner
            break

    return myInfo


def makeErrorRes(code, field, message):
    return {
        'code': code,
        'field': field,
        'message': message,
        'result': 'fail'
    }


def makeOkRes():
    return {
        'result': 'success'
    }


def writeMyInfo(newInfo):
    with open(myInfoPath, 'w') as outfile:
        json.dump(newInfo, outfile)
