def display_inputs(*args, **kwargs):
    if len(args) == 0 or len(kwargs) == 0:
        print("je moet iets meegeven")
    else:
        print("Je gebruikte volgende positionele argumenten: \n")
        for element in args:
            print(element)
        print("\n")
        print("Je gebruikte volgende benoemde argumenten: \n")
        for key, value in kwargs.items():
            print(f"{key}: {value}")




display_inputs("a", 7, "test", foo="bar", getalwaarde= 12)