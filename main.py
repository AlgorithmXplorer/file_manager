import os
transactions_of_app = ["create a folder" , "list of folder" , "create a file","go to up location ","enter the folder","out"]
files = ["text file .txt","word file .docx","excel file .xlsx","powerpoint file .pptx","pdf file .pdf","cancel"]

#region #todo decorator func
def prnt_location_for_ret_func(func):
    def inner(*param,**params):
        print("-"*50)
        loc = os.getcwd().center(50," ")
        print(loc)
        print("-"*50)
        return func(*param,**params)
    return inner

def prnt_location_for_normal_func(func):
    def inner(*param,**params):
        print("-"*50)
        loc = os.getcwd().center(50," ")
        print(loc)
        print("-"*50)
        func(*param,**params)
    return inner

#endregion

#region #todo choosing
@prnt_location_for_ret_func
def choosing(transactions):
     
    def choices():
        for index,choice in enumerate(transactions,1):
            print(f"{index}-{choice}")
        print("-"*20)

    class choice:
        choices()    
        def __init__(self,choice):
            self.choice = choice
            if  not (0 <= self.choice and  self.choice < len(transactions) ):
                raise ValueError

    def inner():
        while True:
            try:
                inp = int(input("ENTER TRANSACTION: "))
                choice_object = choice(inp-1)
            except ValueError:
                print("please enter clearly".center(50,"*"))
                choices()
            else:
                break 
        
        return choice_object.choice 
    
    return inner()


#endregion

#region #todo creating a folder
def create_a_folder():
    @prnt_location_for_normal_func
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

#region #todo list of folders
@prnt_location_for_normal_func
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

#region #todo creating a file
def creating_a_file():
    num = choosing(files)
    def create_file():
        file_str = files[num].split(" ")[-1]
        name = input("file name: ")
        path = os.getcwd()
        with open(f"{path}\{name}{file_str}","x",encoding="utf-8") as file:
            pass

    @prnt_location_for_normal_func
    def inner():
        while True: 
            try: 
                create_file()
            except FileExistsError :
                print("already there is a file same name so please enter different name")
            else:
                print("file has been created succesfully")
                break
    if files[num] != "cancel":
        inner()
    else:
        pass

#endregion
