#!/usr/bin/python3
""" This is the command line or console module """

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ this is the console class """
    prompt = '(hbnb)'

    def do_exit(self, arg):
        """ exit the command line """

        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        pass

    def do_EOF(self, arg):
        """ response to EOF and exit prompt """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
