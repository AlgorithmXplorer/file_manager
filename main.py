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



