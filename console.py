#!/usr/bin/python3
"""
Module contains command line interpreter
for managing Airbnb
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand that inherits from Cmd class
    """
    prompt = "(hbnb) "

    def do_all(self, arg):
        """
        All command to Prints all string representation of all instances
        based or not on the class name.
        Usage: all <Class_Name>  OR  all
        """
        pass

    def do_destroy(self, arg):
        """
        Destroy command to Deletes an instance based on the class name and id
        Usage: destroy <Class_Name> <obj_id>
        """
        pass

    def do_show(self, args):
        """
        Show string representation of an instance.
        Usage: Show <ClassName>
        """
        pass

    def do_create(self, args):
        """
        Create command to create a new instance of Airbnb models
        Usage: Create <ClassName>
        """
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                arg = args.split()
                # it will only work with module imported in the file source
                # else raise exception
                new_inst = eval("{}()".format(arg[0]))
                new_inst.save()
                print(new_inst.id)
            except Exception:
                print("** class doesn't exist **")

    def do_quit(self, args):
        """
        Quit command exits out of the command interpreter
        """
        quit()

    def do_EOF(self, args):
        """
        EOF command exits out of the command interpreter
        """
        quit()

    def do_help(self, args):
        """
        Command lists all help details for each command
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        Returns back to the prompt
        """
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
