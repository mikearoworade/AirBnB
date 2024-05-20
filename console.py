"""This file contains the entry point of the command interpreter (console)"""
import cmd
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

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
         "BaseModel",
         "User",
         "State",
         "City",
         "Place",
         "Amenity",
         "Review"
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

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        pattern = r'\(.*?\)'
        parentheses = re.search(pattern, line) # search for parentheses
        if parentheses:
            line_sub = re.sub(pattern, '', line) # Remove parentheses
            outside_parentheses = line_sub.split(".")
            outside_parentheses.reverse() #1 args[0], args[1](<action>, <class>)
        else:
            print("** Unknown syntax: {} **".format(line))
            return False
        parentheses_values = re.findall(r'\((.*?)\)', line) # Search for id in parentheses
        clean_parentheses_value = re.sub(r'[\'"\[\]\\]', '', str(parentheses_values)) #remove quotes and brackets

        curly_braces = re.findall(r'\{(.*?)\}', clean_parentheses_value)
        if(curly_braces):
            id = []
            id.append(clean_parentheses_value.split(', ')[0]) # args[2] <id>
            clean_curly_braces = re.sub(r'[\'"\[\]]', '', str(curly_braces)) #remove quotes and brackets
            key_value_pairs =  clean_curly_braces.split(', ')
            for key_value_pair in key_value_pairs:
                each_key_value = key_value_pair.split(': ') # args[3], args[4](<key> <value>)
                args = outside_parentheses + id + each_key_value
                if(args[0] in argdict.keys()):
                    merged_list = ' '.join(args[1:])
                    argdict[args[0]](merged_list)
                else:
                    print("** Unknown syntax: {} **".format(args))

        else:
            inside_parentheses =  clean_parentheses_value.split(', ')
            # print(inside_parentheses) # args[2], args[3], args[4](<id>, <key>, <value>)
            if inside_parentheses == ['']:
                args = outside_parentheses
            else:
                args = outside_parentheses + inside_parentheses

            if(args[0] in argdict.keys()):
                if len(args) == 2:
                    return argdict[args[0]](args[1])
                else:
                    merged_list = ' '.join(args[1:])
                    return argdict[args[0]](merged_list)
            else:
                print("** Unknown syntax: {} **".format(args))

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
        elif n > 2:
            print("** Too many arguments **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, args):
        """Delete an Instance based on class name and id"""
        args, n = parse(args)
        objdict = storage.all()

        if n == 0:
            print("** class name missing **")
        elif args[0] not in HugeBnBCommand.__classes:
             print("** class doesn't exit **")
        elif n == 1:
             print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
        elif n > 2:
            print("** Too many arguments **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            print("{}.{} destroyed successfully".format(args[0], args[1]))
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances of a given class. If no class is specified, displays all instantiated objects."""
        args, n = parse(args)
        objdict = storage.all()
        objstr = []

        if n == 1 and args[0] not in HugeBnBCommand.__classes:
            print("** class doesn't exist **")
        elif n > 1:
            print("** To many argument **")
        elif n == 0:
            for val in objdict.values():
                objstr.append(val.__str__())
        else:
            for val in objdict.values():
                if n == 1 and args[0] == val.__class__.__name__:
                   objstr.append(val.__str__())
        if objstr != []: 
            print(objstr)

    def do_update(self, args):
        """update: update [ARG] [ARG1] [ARG2] [ARG3]
        ARG = Class
        ARG1 = ID #
        ARG2 = attribute name
        ARG3 = value of new attribute
        SYNOPSIS: updates or adds a new attribute and value of given Class
        EXAMPLE: update City 1234-abcd-5678-efgh name Chicago
        """
        args, n =  parse(args)
        objdict = storage.all()

        if n == 0:
            print("** class name missing **")
            return False
        if args[0] not in HugeBnBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if n == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if n == 2:
            print("** attribute name missing **")
            return False
        if n == 3:
            if(type(eval(args[2])) != dict): #{"name":"value"}
                print("** value missing **")
            return False
        if n == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            # print(obj.__class__.__dict__.keys())
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                if(args[3].isdigit()):
                    args[3] = int(args[3])
                    obj.__dict__[args[2]] = args[3]
                else:
                    obj.__dict__[args[2]] = args[3]
        storage.save()

    def do_count(self, args):
        """Function to get the number of instances"""
        args, n = parse(args)
        objdict = storage.all()
        count = 0

        if n == 0:
            print("** class name missing **")
        elif n > 1:
            print("** Too many arguments **")
        else:
            for obj in objdict.values():
                if args[0] == obj.__class__.__name__:
                    count += 1
            print(count)


if __name__ == '__main__':
    HugeBnBCommand().cmdloop()