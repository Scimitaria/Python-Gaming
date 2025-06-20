from pynput.keyboard import Key, Controller, Listener # type: ignore

#keyboard command center

keyboard = Controller()
listener = Listener()

listener.start()
while True:
    #print('a')
    def on_press(key):
        print(f'Key pressed: {key.char}')
