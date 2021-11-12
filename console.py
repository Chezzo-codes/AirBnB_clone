#!/usr/bin/python3
"""
Module contains command line interpreter
for managing Airbnb
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand that inherits from Cmd class
    """
    prompt = "(hbnb)"

    def do_create(self, args):
        """
        Create command to create a new instance of Airbnb models
        Usage: Create <ClassName>
        """
        if args == None:
            print("** class name missing **")
        else:
            try:
                arg = args.split(" ")
                new_inst = eval("{}()".format(args[0]))
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
