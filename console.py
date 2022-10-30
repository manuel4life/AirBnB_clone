#!/usr/bin/python3
""" This is the command line or console module """

import cmd
from nis import match
import re
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

    def do_count(self, arg):
        """ Retrieves the number of instances of a class """

        all_objects = models.storage.all()
        count = 0

        # split the argument arg
        args = arg.split(".")
        class_name = args[0]

        if class_name in HBNBCommand.class_list.keys():
            for key, obj in all_objects.items():
                if key.startswith(class_name):
                    count += 1
        else:
            print("** class doesn't exist **")
        print("{}".format(count))

    def default(self, arg):
        """ Defualt method """

        class_name = None
        method_name = None
        obj_id = None
        class_attribute = None
        class_attribute_value = None
        arg_string = None

        # retrieve the class_name
        match_1 = re.match(r"([A-Z][a-zA-Z_]+)", arg)
        if match_1:
            class_name = match_1.group()

        # check if class_name is in the class name list
        if class_name in HBNBCommand.class_list.keys():

            # retrieve the method
            match_2 = re.match(r".+\.([a-zA-Z_]+)\(?", arg)
            if match_2:
                method_name = match_2.groups()[0]

            # retrieve the instance id
            match_3 = re.search(r"(?<=\").+(?=\"\))", arg)
            if match_3:
                obj_id = match_3.group().split('", ')[0]

            if method_name == "update":
                # check if there's a dict
                match_a_dict = re.search(r"({.+})", arg)
                if match_a_dict:
                    dict_rep = eval(match_a_dict.group(0))
                    if type(dict_rep) == 'dict':
                        pass
                else:
                    # retrieve the attribute name
                    match_4 = re.search(r"(?<=\").+(?=\"\))", arg)
                    if match_4:
                        class_attribute = match_4.group().split('", ')[
                            1].split('"')[1]

                    # retrieve the attribute value
                    match_5 = re.search(r"(?<=\").+(?=\"\))", arg)
                    if match_5:
                        class_attribute_value = match_5.group().split('", ')[
                            2].split('"')[1]

            # dict for method selection
            method_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
            }

            if method_name in method_dict.keys():
                if match_3:  # check if instance id is not None
                    if method_name == 'update':
                        arg_string = "{} {} {} {}".format(
                            class_name, obj_id, class_attribute, class_attribute_value)
                    else:
                        arg_string = "{} {}".format(class_name, obj_id)
                    method_dict[method_name](arg_string)
                else:
                    method_dict[method_name](class_name)
            else:
                print("command: not found".format(method_name))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
