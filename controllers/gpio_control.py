import platform

onCHIP = True if platform.machine() == 'armv7l' else False


if onCHIP:
    import CHIP_IO.GPIO as GPIO


def setPinState(pinName, newState):
    if onCHIP:
        GPIO.setup(pinName, GPIO.OUT)
        GPIO.output(pinName, GPIO.HIGH if newState == 'HIGH' else GPIO.LOW)
