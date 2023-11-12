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
        """Prints string representation of instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{args[0]}.{obj_id}"
        objects = self.load_objects()

        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes instance based on the class name & id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{args[0]}.{obj_id}"
        objects = self.load_objects()

        if key in objects:
            del objects[key]
            self.save_objects(objects)
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{args[0]}.{obj_id}"
        objects = self.load_objects()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        obj = objects[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def do_all(self, arg):
            """Prints all string representations"""
            objects = self.load_objects()


    def load_objects(self):
        """Loads objects from JSON"""
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_objects(self, objects):
        """Save objects to JSON"""
        with open(self.file_path, 'w') as file:
            json.dump(objects, file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
