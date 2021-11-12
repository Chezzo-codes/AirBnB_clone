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
