#!/usr/bin/python3
""" This is the command line or console module """

import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ this is the console class """
    prompt = '(hbnb) '
    class_list = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }
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
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or updating attribute """

        args = arg.split(" ")
        all_objects = models.storage.all()

        if len(args) >= 1:
            if args[0] in HBNBCommand.class_list.keys():
                if len(args) >= 2:
                    if len(args) >= 3:
                        if len(args) >= 4:
                            # format the key
                            key = "{}.{}".format(args[0], args[1])
                            if key not in all_objects:
                                print("** no instance found **")
                                return
                            # prevent id, created_at and updated_at from being updated
                            if args[2] not in ['id', 'created_at', 'updated_at']:
                                setattr(all_objects[key], args[2], args[3])
                                models.storage.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** instance id missing **")
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
                    # format the key
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
