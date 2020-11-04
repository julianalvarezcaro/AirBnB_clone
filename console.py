#!/usr/bin/python3
"""Console program module
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Console class
    """
    prompt = '(hbnb) '
    file = None
    classes =\
        ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program
        """
        self.close()
        return True

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        self.close()
        return True

    def do_create(self, line):
        """create command creates a instance of the especified class
        """
        if not line:
            print("** class name missing **")
        try:
            inst = eval(line)()
            inst.save()
            print(inst.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """show command prints the string representation of \
an instance based on the class name and id
        """
        words = line.split()
        if not line:
            print("** class name missing **")
            return
        if words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(words) < 2:
            print("** instance id missing **")
            return
        try:
            with open("file.json", "r") as file:
                dic = json.load(file)
            key = words[0] + "." + words[1]
            if key in dic:
                inst = eval(words[0])(**dic[key])
                print(inst)
            else:
                print("** no instance found **")
        except FileNotFoundError:
            print("** no instance found **")

    def do_destroy(self, line):
        """destroy command deletes an instance based on the class name and id
        """
        words = line.split()
        if not line:
            print("** class name missing **")
            return
        if words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(words) == 1:
            print("** instance id missing **")
            return
        obj = storage.all()
        key = words[0] + "." + words[1]
        if key in obj:
            del obj[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances \
based or not on the class name
        """
        strs = []
        if line:
            words = line.split()
            if words[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        dic = storage.all()
        for key, value in dic.items():
            strs.append(str(value))
        print(strs)

    def do_update(self, line):
        """update instance of all"""
        string1 = line.split()
        string = shlex.split(line)
        all_objs = models.storage.all()
        if len(string) < 1:
            print("** class name missing **")
        elif string[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(string) < 2:
            print("** instance id missing **")
        elif len(string) < 3:
            print("** attribute name missing **")
        elif len(string) < 4:
            print("** value missing **")
        else:
            key = string[0] + "." + string[1]
            if key in all_objs:
                object1 = all_objs.get(key)
                word = string1[3]
                if string[3].isdigit() and word[0] is not '"':
                    setattr(object1, string[2], eval(string[3]))
                else:
                    setattr(object1, string[2], string[3])
                storage.save()
            else:
                print("** no instance found **")

# ---------------Implementation methods---------------

    def close(self):
        """close process
        """
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        """empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
