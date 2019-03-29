from pynput.mouse import Listener

def mouseListener(x, y):
    print("position of mouse {0}", format((x, y)))
    
    
with Listener(on_move=mouseListener) as l:
    l.join()