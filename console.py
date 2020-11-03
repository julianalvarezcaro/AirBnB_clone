#!/usr/bin/python3
"""
Console program
"""
import cmd
from models.base_model import BaseModel
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Console class
    """
    prompt = '(hbnb) '
    file = None
    classes = ["BaseModel"]

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
        try:
            obj = storage.all()
            if words[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            file = open("file.json", "r")
            dic = json.load(file)
            file.close()
            if len(words) >= 2:
                key = words[0] + "." + words[1]
                del dic[key]
                del obj[key]
                storage.save()
            else:
                print("** instance id missing **")
        except KeyError:
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
        """Updates an instance based on the class name and \
id by adding or updating attribute
        """
        if not line:
            print("** class name missing *")
            return
        words = line.split()
        if words[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(words) < 2:
            print("** instance id missing **")
            return
        dic = storage.all()
        key = words[0] + "." + words[1]
        if key not in dic:
            print("** no instance found **")
            return
        if len(words) < 3:
            print("** attribute name missing **")
            return
        if len(words) < 4:
            print("** value missing **")
            return
        obj = dic[key]
        val = words[3]
        if val[0] == '"':
            val = val.replace("\"","")
        try:
            val = int(val)
        except ValueError:
            try:
                val =  float(val)
            except ValueError:
                val = str(val)
        setattr(obj, words[2], val)
        storage.save()

# ------------Implementation methods----------------

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