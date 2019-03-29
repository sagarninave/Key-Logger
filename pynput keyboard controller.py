from pynput.keyboard import Controller

def keyboardController():
    
    keyboard = Controller()
    keyboard.type("i am typeing text")
    
keyboardController()