from pynput.mouse import Controller

def mouseController():
    mouse = Controller()
    mouse.position = (500, 10)
    print("show mouse cursor to top left cornor")

mouseController()