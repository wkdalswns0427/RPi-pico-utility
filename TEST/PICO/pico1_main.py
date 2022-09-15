from pico1_functions import function1, function2

def main():
    selection = int(input("choose sensor : "))
    selecttime = int(input("config time : "))
    if selection == 1:
        function1(selecttime)
    elif selection == 2:
        function2(selecttime)
        
main()
