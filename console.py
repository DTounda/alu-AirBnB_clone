#!/usr/bin/python3
"""Entry point of the AirBnB clone command interpreter."""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter managing AirBnB objects."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    @staticmethod
    def _split(arg):
        """Split arg into words, keeping double-quoted strings together."""
        try:
            return shlex.split(arg)
        except ValueError:
            return arg.split()

    def _check(self, args, need_id=True):
        """Validate class name (and id); return the key or None."""
        if not args:
            print("** class name missing **")
            return None
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return None
        if not need_id:
            return args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return None
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return None
        return key

    def do_create(self, arg):
        """Create a new instance: create <class name>
        """
        args = self._split(arg)
        if self._check(args, need_id=False):
            obj = self.classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show an instance: show <class name> <id>
        """
        key = self._check(self._split(arg))
        if key:
            print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance: destroy <class name> <id>
        """
        key = self._check(self._split(arg))
        if key:
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, arg):
        """Show all instances: all [<class name>]
        """
        args = self._split(arg)
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for k, obj in models.storage.all().items()
               if not args or k.split(".")[0] == args[0]])

    @staticmethod
    def _cast(current, value):
        """Cast value to the type of current (int, float) or infer it."""
        if isinstance(current, str):
            return value
        casters = [int, float]
        if type(current) in (int, float):
            casters = [type(current)]
        for caster in casters:
            try:
                return caster(value)
            except ValueError:
                pass
        return value

    def do_update(self, arg):
        """Update an instance:
        update <class name> <id> <attribute name> "<attribute value>"
        """
        args = self._split(arg)
        key = self._check(args)
        if not key:
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = models.storage.all()[key]
        current = getattr(obj, args[2], None)
        setattr(obj, args[2], self._cast(current, args[3]))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
