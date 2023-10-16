#!/usr/bin/python3


"""
Commandline interpreter Module
for AirBnB clone Application
"""
from models import storage, standard_models
import cmd
import re
import sys


class HBNBCommand(cmd.Cmd):
    """
    definition for airbnb clone shell console
    """
    prompt = '(hbnb) '
    file = None

    def do_create(self, line):
        """
        Create an object of named class
        usage: $ create <class_name>
        """
        args = parse_args(line)

        if not args:
            print("** class name missing **")
            return False
        if args[0] not in standard_models.keys():
            print("** class doesn't exist **")
            return False
        if len(args) > 1:
            print("** too many arguments **")
            return
        arg, *_ = args

        new_model = standard_models[arg]()
        print(new_model.id)
        new_model.save()

    def do_EOF(self, arg):
        """
        Exit shell with Ctrl-D
        """
        return True

    def emptyline(self):
        """
        Ignore empty line
        """
        pass

    def do_all(self, line):
        """
        Print all instances of a model
        usage: $ all <model_name>
        ex: $ all BaseModel
        """
        args = parse_args(line)
        if args and args[0] not in standard_models.keys():
            print("** class doesn't exist **")
            return False
        models = []
        if args:
            arg, *_ = args
            models = [model.__str__() for key, model in storage.objects.items()
                      if key.split(".")[0] == arg]
        else:
            models = [model.__str__() for key, model
                      in storage.objects.items()]
        print(models)

    def do_count(self, line):
        """
        Retrieve the number of instances of a class
        """
        pass

    def do_destroy(self, line):
        """
        Deletes an instance based on class name and id
        usage: $ destroy <model_name> <model_id>
        ex: $ destroy BaseModel 1234-1234-1234
        """
        args = parse_args(line)
        if not self.valid_args(args):
            return
        model_name, model_id, *_ = args
        key = "{}.{}".format(model_name.strip(), model_id.strip())
        del storage.objects[key]
        storage.save()

    def do_quit(self, arg):
        """
        Exit cmd console
        """
        return True

    def do_shell(self, arg):
        """
        Execute shell command
        """
        os.system(arg)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        usage: $ show <model_name> <model_id>
        ex: $ show BaseModel 1234-1234-1234
        """
        args = parse_args(line)
        if not self.valid_args(args):
            return
        model_name, model_id, *_ = args
        key = "{}.{}".format(model_name.strip(), model_id.strip())
        print(storage.objects.get(key))

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        usage: $ update <class name> <id> <attribute name> <attribute value>
        """
        args = parse_args(line)
        if not self.valid_args(args):
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        model_name, model_id, attribute_name, attribute_value, *_ = args
        key = "{}.{}".format(model_name.strip(), model_id.strip())
        setattr(storage.objects[key], attribute_name, attribute_value)
        storage.objects[key].save()

    def valid_args(self, args):
        """
        Check if class name is missing
        or if class name doesn't exit
        """
        if not args:
            print("** class name missing **")
            return False
        if args[0] not in standard_models.keys():
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        model_name, model_id, *_ = args
        key = "{}.{}".format(model_name.strip(), model_id.strip())
        try:
            storage.objects[key]
            return True
        except KeyError:
            print("** no instance found **")
            return False
        return True

    def default(self, line):
        """
        Default method
        """
        args = parse_args(line)
        if not args:
            return

        model_name = re.search(r"^([a-zA-Z]\w*?)\.", args[0])
        command = re.search(r"\.([a-zA-Z]\w*?)\(", args[0])
        new_args = re.search(r"\((.*?)\)", args[0])
        if not model_name or not command:
            print("** Unknown syntax: {}".format(args[0]))
            return
        commands = {'all': self.do_all,
                   'count': self.do_count,
                   'destroy': self.do_destroy,
                   'show': self.do_show,
                   'update':self.do_update}

        model_name = model_name.group(1)
        command = command.group(1)
        if new_args:
            new_args = new_args.group(1)
        else:
            new_args = ""
        new_line = "{} {}".format(model_name.strip(),
                                     new_args.strip())
        try:
            commands[command](new_line)
        except KeyError:
            print("** command {} not found **".format(command))
            return

def parse_args(line):
    """
    Split the args passed by Cmd
    in individual args
    """
    match_pattern = "( |\\\".*?\\\"|'.*?')"
    args = [arg.replace("'", "").replace('"', "")
            for arg in re.split(match_pattern, line) if arg.split()]
    return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()
