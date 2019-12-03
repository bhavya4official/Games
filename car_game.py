cmd = ""
started = False
print('Enter car command:\nhelp | start | stop | exit\n')
while True:
    cmd = input('|>').lower()
    if cmd == "start":
        if started:
            print('Car is already started.')
        else:
            started = True
            print('Car started...Ready to go!')
    elif cmd == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif cmd == "help":
        print("""
start - to start the car
stop  - to stop the car
exit  - to exit""")
    elif cmd == "exit":
        break
    else:
        print("Sorry! I don't understand.")
