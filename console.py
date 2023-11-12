#!/usr/bin/python3
"""hbnb  console"""
import cmd
import json
import shlex
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter

    Attributes:
        prompt (str): The command prompt
    """

    prompt = "(hbnb) "
    file_path = "file.json"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates an instance of BaseModel, saves and prints it"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
