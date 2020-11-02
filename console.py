#!/usr/bin/python3
"""
Console program
"""
import cmd


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
