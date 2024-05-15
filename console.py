"""This file contains the entry point of the command interpreter (console)"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel

def parse(line):
        """Split a line by spaces into a list"""
        args = shlex.split(line)
        return args, len(args)

class HugeBnBCommand(cmd.Cmd):
    """
    The Console based driver of the HugeBnB.
    All interaction is done via this class.
    """
    prompt = "(hugebnb) "
    __classes = {
         "BaseModel"
    }

    """Commands"""
    def do_EOF(self, args):
        """Exit the program in non-interactive mode"""
        return True
    
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_create(self, args):
        """Usage: create <class>
        Create a new class instance and print its id
        """
        args, n = parse(args)

        if n == 0:
            print("** class name missing **")
        elif args[0] not in HugeBnBCommand.__classes:
             print("** class name does not exit **")
        elif n == 1:
            obj = eval(args[0])()
            print(obj.id)
            obj.save()
        else:
             print("** To many argument **")

    def do_show(self, args):
        """Print the string representation of an instance based on class name and id"""
        args, n = parse(args)
        objdict = storage.all()

        if n == 0:
            print("** class name missing **")
        elif args[0] not in HugeBnBCommand.__classes:
             print("** class does'nt exit **")
        elif n == 1:
             print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])


if __name__ == '__main__':
    HugeBnBCommand().cmdloop()