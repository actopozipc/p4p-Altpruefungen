import operations as op
import sys as sus
def PrintOperation(operation):
    '''Function to print the text given after selecting a number
    Args:
        operation (string):  the name of the operation

    Returns:
        null
    Example:
    >>>PrintOperation("subtract")
    <<<Operation subtract selected
    <<<Please give two numbers:
    '''
    print("Operation '{}' selected:".format(operation))


def SetAB(args):
    '''
    Function that returns a tuple of float values
    Depending on if there are arguments on the console or not, the function asks for an input or just returns the values of the command line arguments
    Args:   
        args (array): Array with command line arguments
    Returns:
        a,b (tuple): Values a,b
    '''
    if len(args) == 4: #If command line arguments persist of the operation number and two values
        a=args[2]
        b=args[3]
    else: #If the command line does not have arguments or not enough, read them from the console 
        print("Please give two numbers:")
        a = input("a=")
        b = input("b=")
    return (a,b)

def main(args=[]):
    '''Main-Function
        Displays a menu and takes a user input to call an operation from operations.py
        Args:
            args (array) (optional): Array with potential arguments from the commandline
        Returns:
            Null
        Example:
            >>>main(['simplemath.py','1','2','3'])
            <<<Welcome to simplemath!
            <<<Operation 'add' selected:
            <<<5.0
            >>>main()
            <<<Please select an operation:
            <<<.....
            <<<Please give two numbers:
            >>>2
            >>>3
            <<<5.0
    '''
    print("Welcome to simplemath!")
    argsExists = len(args)>1; #True if called with commandline arguments
    while(True): #while(True) so one can use another operation as sonn as one is done
        if not argsExists: #Display the menu if !argsExists
            print("Please select an operation:")
            print("-0: quit")
            print("-1: add")
            print("-2: subtract")
            print("-3: multiply")
            print("-4: divide")
            print("-5: Pow")
            operation = input();
        else: #else the operator is just the first value in the commandline argument after the file name
            operation = args[1];
        if operation == "0": #quit
            print("Good bye!")
            exit();
        if operation == "1": #add
            PrintOperation("add")
            a,b = SetAB(args);
            try:
                erg = op.add(float(a), float(b))
                print(erg)
            except ValueError:
                print("Please only use integer values")

        elif operation == "2": #subtraction
            PrintOperation("subtract")
            a,b = SetAB(args);
            try:
                erg = op.sub(float(a), float(b))
                print(erg)
            except ValueError:
                print("Please only use integer values")
        elif operation == "3": #multiplication
            PrintOperation("multiply")
            a,b = SetAB(args);
            try:
                erg = op.mult(float(a), float(b))
                print(erg)
            except ValueError:
                print("Please only use integer values")
        elif operation == "4": #division
            PrintOperation("division")
            a,b = SetAB(args);
            try:
                erg = op.div(float(a), float(b))
                print(erg)
            except ValueError:
                print("Please only use integer values")
            except ZeroDivisionError: #divison with 0 is not allowed
                print("Please dont divide by zero")
        elif operation == "5":
            PrintOperation("pow")
            a,b = SetAB(args);
            try:
                erg = op.pow(float(a), float(b))
                print(erg)
            except ValueError:
                print("Please only use integer values")
        else:
            print("No valid number selected")

        if argsExists: #if main is called from the terminal with arguments, break the while(True) loop after its done
            quit()


if __name__ == "__main__":
    if(len(sus.argv)>1):
        main(sus.argv);
    else:
        main();
