
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored_print (string : str, num : int, end_with : str = '\n') -> None:
        dict = {0 : Colors.RESET, 1 : Colors.GREEN, 2 : Colors.YELLOW, 3 : Colors.RED}

        print (f"{dict[num]}{string}{dict[0]}", end = end_with)

def color_test ():
    print (f'{Colors.HEADER} header')
    print (f'{Colors.OKBLUE} okblue')
    print (f'{Colors.OKCYAN} okcyan')
    print (f'{Colors.OKGREEN} okgreen')
    print (f'{Colors.WARNING} warning')
    print (f'{Colors.FAIL} Fail')
    print (f'{Colors.ENDC} endc')
    print (f'{Colors.BOLD} bold')
    print (f'{Colors.UNDERLINE} underline')