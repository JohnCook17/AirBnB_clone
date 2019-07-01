#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    ''' Entry for HBNBCommand Console

        Attributes:
        prompt: overwrite default prompt with custom prompt
    '''

    prompt = '(hbnb) '

    def do_create(self, arg):
        ''' creates a new instance of BaseModel, saves it to a JSON and prints the ID
        '''
        from models.base_model import BaseModel
        from models import storage

        if len(arg) < 1:
            print ('** class name missing **')

        # make more better
        elif arg != "BaseModel":
            print ("** class doesn't exist **")

        else:
            new_ins = eval("{}()".format(arg))
            storage.new(new_ins)
            storage.save()
            print(new_ins.id)

    def do_show(self, arg):
        ''' Prints the string representation of an instance based on the
            class name and id
        '''
        from models import storage
        from shlex import split

        token = arg.split()

        if len(arg) == 0:
            print ("** class name missing **")

        else:
            name_id = "{}.{}".format(token[0], token[1])
            print(storage.all()[name_id])

    def do_EOF(self, arg):
        ''' EOF argument that exits out of the console
        '''
        return True

    def do_quit(self, arg):
        ''' quit command that quits out of the console
        '''
        return True

    def emptyline(self):
        ''' overwrites emptyline method to not execute previous command
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
