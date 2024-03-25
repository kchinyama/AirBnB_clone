#!/usr/bin/python3

"""command line interpretor module for the creation and 
manipulation of data"""


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """class that holds methods for my command line console"""

    prompt = '(hbnb) ' 

    def do_quit(self, line):
        """quits the command interpretor"""

        return True

    def do_EOF(self, line):
        """quits the command line gently"""

        return True

    def onecmd(self, line):
        """overide to print emptyline and prompt for
        new command"""

        if not line:
            return False
        
        else:
            return super().onecmd(line)

    def help_quit(self):
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
