command = ""
car_started = False
car_stopped = False
while True:
    command = input(">").lower()
    if command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif command == "start":
        if not car_started:
            print("Car started...Ready to go!")
            car_started = True
        else:
            print("Car has already started")

    elif command == "stop":
        if not car_stopped:
            print("Car stopped.")
            car_stopped = True
        else:
            print("Car has already stopped")
    elif command == "quit":
        break
    else:
     print("I don't understand that...")
