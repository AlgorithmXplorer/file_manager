import os
from datetime import datetime 
transactions_of_app = ["create a folder" , "create a file" , "list of folders and files" ,"go to up location ","enter the folder","out"]
files = ["text file .txt","word file .docx","excel file .xlsx","powerpoint file .pptx","cancel"]

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

#region #todo creating a file
def creating_a_file():
    def create_file(path,extension):
        name = input("file name: ")
        if  os.path.exists(f"{name}{extension}") == True:
            print("already there is a folder same name so please enter different name")
            return 0
        else:
            with open(f"{path}/{name}{extension}","a",encoding="utf-8") as file:
                pass
            print("folder has been created")
            return 1


    @prnt_location_for_normal_func
    def inner():
        num = choosing(files)
        file = files[num].split(" ")[-1]
        file_path = os.getcwd()
        if file == "cancel":
            pass
        else:
            number = create_file(file_path,file)
            while not(number == 1):
                number = create_file(file_path,file)
            inner()
            

    inner() 

#endregion

#region #todo list of folders and files
def listing(number):
    """
    ınput: ıf 1 
    output: list of folders
    ınput: ıf 2
    output: list of files
    ınput: ıf 3
    output: both of them
    
    """
    @prnt_location_for_normal_func
    def inner():
        folders = []
        files = []
        for i in os.listdir():
            if "." in i :
                files.append(i)
            else:
                folders.append(i)

        def list_of_folders():
            print("FOLDERS".center(30,"_"),end="\n\n")
            for i in folders:
                file_info = os.stat(i)
                second_of_create_date = file_info.st_ctime
                just_date = datetime.fromtimestamp(second_of_create_date)
                modded_date = datetime.strftime(just_date,"%x")
                print(f"{i}\t\t\t\tcreate date: {modded_date}")

        def list_of_files():
            print("FİLES".center(30,"_"),end="\n\n")
            for i in files:
                file_info = os.stat(i)
                second_of_create_date = file_info.st_ctime
                just_date = datetime.fromtimestamp(second_of_create_date)
                modded_date = datetime.strftime(just_date,"%x")
                print(f"{i}\t\t\t\tcreate date: {modded_date}")
    
        if number == 1:
            list_of_folders()
            print("-"*70)
        elif number == 2:
            list_of_files()
        elif number == 3:
            list_of_folders()
            list_of_files()
        else:
            raise ValueError("wrong number")
    inner()
#endregion

#region #todo move up
def move_up():
    os.chdir("..")
    def inner():
        pass
    inner()

#endregion

#region #todo entering to a folder
def enter_folder():
    def enter_folder(folder_name):
        path = f"{os.getcwd()}/{folder_name}"
        os.chdir(path)
    
    def inner():
        listing(1)

        folder_name = input("folder name: ")
        if os.path.isdir(folder_name) == True:
            enter_folder(folder_name)
            
        else:
            print("there is not a folder with this name. please try again")
            inner()
    inner()

#endregion
# @prnt_location_for_normal_func
def main():
    choice = choosing(transactions_of_app)
    if choice == 0:
        create_a_folder()
        main()

    elif choice == 1:
        creating_a_file()
        main()

    elif choice == 2:
        listing(3)
        main()
    
    elif choice == 3:
        move_up()
        main()

    elif choice == 4:
        enter_folder()
        main()

    elif choice == 5:
        print("exited")

main()