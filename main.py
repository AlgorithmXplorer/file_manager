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

#region #todo creating a folder
def create_a_folder():
    @prnt_location
    def inner():
        name = input("name: ")
        os.mkdir(name)
    while True:
        try:
            inner()
        except FileExistsError:
            print("already there is a folder same name so please enter different name")
        else: 
            print("folder has been created")
            break

#endregion
#region #todo list od folders
@prnt_location
def listing():
    folders = []
    files = []
    for i in os.listdir():
        if "." in i :
            files.append(i)
        else:
            folders.append(i)
    print("FOLDERS".center(30,"_"))
    for i in folders:
        print(i)
    print("FİLES".center(30,"_"))
    for i in files:
        print(i)
   
#endregion

