from pico2_functions import function3, function4

def main():
    selection = int(input("choose sensor : "))
    selecttime = int(input("config time : "))
    if selection == 3:
        function3(selecttime)
    elif selection == 4:
        function4(selecttime)
        
main()
