#!/usr/bin/python3

"""command line interpretor module for the creation and 
manipulation of data"""


import cmd
import sys
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class that holds methods for my command line console"""

    prompt = '(hbnb) '

    definedClasses = {'BaseModel'}

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


    def do_create(self, line):
        """create a new instance of BaseModel and saves it
        to file and prints the id of the instance"""

        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in self.definedClasses:
            print("** class doesn't exist **")

        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """displays str rep of an instance based on the class name
        and id"""

        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in self.definedClasses:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            # need to create variable that points to
            # saved instances in order to check if or
            # not an instance has been saved
            objs = storage.all()

            # create a key that accesses these objects
            # via the arguments inputed
            key = f"{args[0]}.{args[1]}"

            if key not in objs:
                print("** no instance found **")

            else:
                print(objs[key])

    def do_destroy(self, line):
        """deletes an instance based on class name
        and id"""

        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in self.definedClasses:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            objs = storage.all()

            key = f"{args[0]}.{args[1]}"

            if key not in objs:
                print("** no instance found **")

            else:
                del objs[key]
                storage.save()

    def do_all(self, line):
        """prints all instances saved in string representation"""

        args = line.split()

        objs = storage.all()

        if len(args) == 0 or args[0] in self.definedClasses:
            for key, value in objs.items():
                print(str(f"{value}"))

        elif args[0] not in self.definedClasses:
            print("** class doesn't exist **")

    def do_update(self, line):
        """updates an instance based on class name and and id
        adds or even updates attributes and saves to json file
        """

        args = line.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in self.definedClasses:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            objs = storage.all()

            key = f"{args[0]}.{args[1]}"

            if key not in objs:
                print("** no instance found **")

            elif len(args) < 3:
                print("** attribute name missing **")

            elif len(args) < 4:
                print("** value missing **")

            else:

                obj = objs[key]

                attr_name = args[2]

                attr_value = args[3]

                try:
                    attr_value = eval(attr_value)

                except Exception:
                    pass

                setattr(obj, attr_name, attr_value)
                obj.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
