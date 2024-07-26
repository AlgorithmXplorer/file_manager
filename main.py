import os

#region #todo decorator func
def prnt_location(func):
    def inner(*param,**params):
        print("-"*50)
        loc = os.getcwd().center(50," ")
        print(loc)
        print("-"*50)
        func(*param,**params)
    return inner
#endregion

#region #todo choosing
@prnt_location
def choosing():
    transactions = ["create a folder" , "list of folder" , "create a file","go to up location ","enter the folder","out"]
    def choices():
        for index,choice in enumerate(transactions,1):
            print(f"{index}-{choice}")
        print("-"*20)

    class choice:
        choices()    
        def __init__(self,choice):
            self.choice = choice
            if  not (self.choice in [1,2,3,4,5,6]):
                raise ValueError

    while True:
        try:
            inp = int(input("ENTER TRANSACTION: "))
            choice_object = choice(inp)
        except ValueError:
            print("please enter clearly")
            choices()
        else:
            break

    return choice_object.choice

#endregion


