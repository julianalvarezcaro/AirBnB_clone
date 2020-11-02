#!/usr/bin/python3
"""
Console program
"""
import cmd
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """
    Console class
    """
    prompt = '(hbnb) '
    file = None

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
        try:
            test = eval(words[0])()
            with open("file.json", "r") as file:
                dic = json.load(file)
            if len(words) >= 2:
                key = words[0] + "." + words[1]
                if key in dic:
                    inst = eval(words[0])(**dic[key])
                    print(inst)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """destroy command deletes an instance based on the class name and id
        """
        words = line.split()
        if not line:
            print("** class name missing **")
            return
        try:
            test = eval(words[0])()
            file = open("file.json", "r")
            dic = json.load(file)
            file.close()
            if len(words) >= 2:
                key = words[0] + "." + words[1]
                del dic[key]
                file = open("file.json", "w")
                jdic = json.dumps(dic)
                file.write(jdic)
                file.close()
            else:
                print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")
    
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
