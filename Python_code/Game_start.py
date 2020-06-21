started = False
name=input("Enter your name: ")
print(f"Hii {name} let's play a game")
command = ""
while command != "quit":
    input_command= input("> ")
    if input_command.upper() == "HELP":
        print('''
start - to start the car
stop  - to stop the car
quit  - to exit
        ''')
    elif input_command.upper() == "START":
        if started  :
            print("Car is alreay started ... what are doing")
        else :
            started = True
            print("Car started... Ready to go!")
    elif input_command.upper() == "STOP" :
        if not started:
            print("you already stop ... what are you doing")
        else :
            started = False
            print("Car stopped")


    elif input_command.upper() == "QUIT" :
        exit_command = input('''
do u want to quit 
 (y)es and (N)o
 > '''  ).lower()
        if exit_command == "y" :
           command = 'quit'
    else :
        print("I don't understand that ...")



