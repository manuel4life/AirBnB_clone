#!/usr/bin/python3
""" This is the command line or console module """

import cmd
from statistics import mode
import sys
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ this is the console class """
    prompt = '(hbnb) '
    class_list = {'BaseModel': BaseModel}
    # obj_classes = [
    #     'BaseModel'
    # ]

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

    def do_create(self, args):
        """ Create a new instance of a class """

        if args:
            if args in HBNBCommand.class_list.keys():
                new_obj = HBNBCommand.class_list[args]()
                print("{}".format(new_obj.id))
                new_obj.save()  # create and save new class
                # models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """ Prints the string representation of an 
        instance based on the class name and id """

        args = arg.split(" ")
        all_objects = models.storage.all()
        if len(args) >= 1:
            if args[0] in HBNBCommand.class_list.keys():
                if len(args) == 2:
                    key = "{}.{}".format(args[0], args[1])
                    if key not in all_objects:
                        print("** no instance found **")
                        return
                    print(all_objects[key])
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """

        args = arg.split(" ")
        all_objects = models.storage.all()
        if len(args) >= 1:
            if args[0] in HBNBCommand.class_list.keys():
                if len(args) == 2:
                    key = "{}.{}".format(args[0], args[1])
                    if key not in all_objects:
                        print("** no instance found **")
                        return
                    del all_objects[key]
                    models.storage.save()
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """ Prints all string representation of all \
        instances based or not on the class name """

        all_objects = models.storage.all()

        if len(arg) >= 1:
            args = arg.split(" ")

            if args[0] in HBNBCommand.class_list.keys():
                for key, value in all_objects.items():
                    if args[0] == value.__class__.__name__:
                        print(all_objects[key])
            else:
                print("** class doesn't exist **")
        else:
            lst = [str(val) for val in all_objects.values()]
            print(lst)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
