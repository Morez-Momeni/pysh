import os
from datetime import datetime
from colorama import Fore , Style
from env import CWD , USER , DESKTOP

def ls(l_flag=False,a_flag=False):
    """
    List files and directories in the current working directory.

    Args:
        l_flag (bool): Display detailed information, including file size,
                       creation time, and last modification time.
        a_flag (bool): Include hidden files and directories.

    Notes:
        Directories are displayed in green.
        Hidden entries are excluded by default.
    """

    result = os.listdir(CWD)
    info_list = []
    if not l_flag:
        for r in result:
            full_path = os.path.join(CWD,r)

            if os.path.isdir(full_path) and a_flag == True:
                print(Fore.GREEN + f"{r}" + Style.RESET_ALL , end=" ")
            elif os.path.isdir(full_path) and a_flag == False:
                if r.startswith("."):
                    continue
                else:
                    print(Fore.GREEN + f"{r}" + Style.RESET_ALL , end=" ")
            elif os.path.isfile(full_path) and a_flag == True:
                print(r,end=" ")
            elif os.path.isfile(full_path) and a_flag == False:
                if r.startswith("."):
                    continue
                else:
                    print(r,end=" ")
    else:
        for r in result:
            full_path = os.path.join(CWD,r)
            size = os.path.getsize(full_path)
            creation = datetime.fromtimestamp(os.path.getctime(full_path))
            modification = datetime.fromtimestamp(os.path.getmtime(full_path))
            info = {
                'name' : r,
                'size' : size,
                'creation' : creation,
                'modification' : modification
            }
            info_list.append(info)
        
    for inf in info_list:
        if a_flag == True:
            print(
                f"{Fore.GREEN}{inf['name']:<25}{Style.RESET_ALL}"
                f"{inf['size']:>10} bytes  "
                f"{inf['creation'].strftime('%Y-%m-%d %H:%M:%S')}  "
                f"{inf['modification'].strftime('%Y-%m-%d %H:%M:%S')}"
            )
        else:
            if inf['name'].startswith("."):
                continue
            print(
                f"{Fore.GREEN}{inf['name']:<25}{Style.RESET_ALL}"
                f"{inf['size']:>10} bytes  "
                f"{inf['creation'].strftime('%Y-%m-%d %H:%M:%S')}  "
                f"{inf['modification'].strftime('%Y-%m-%d %H:%M:%S')}"
                        )


def pwd():
    """
    Display the current working directory of the shell.
    """
    print(CWD)

def cd(dir):
    """
    Change the current working directory.

    Args:
        dir (str): The target directory path.

    Notes:
        Passing '..' moves to the parent directory.
        Passing an empty string changes the directory to the user's home.
        Relative paths are resolved from the current working directory.
        The directory is changed only if the target exists.
    """
    global CWD
    if dir.strip() == "..":
        CWD = os.path.abspath(os.path.join(CWD,os.pardir))
    elif dir ==  "":
        CWD = os.path.expanduser("~")
    elif os.path.isdir(os.path.join(CWD,dir)):
        CWD = os.path.join(CWD,dir)
        print(CWD)
    else:
        print("no dir")


def mkdir(dir_name):
    """
    Create a new directory in the current working directory.

    Args:
        dir_name (str): The name of the directory to create.

    Notes:
        Displays an error message if the directory or file already exists.
    """
    try:
        os.mkdir(os.path.join(CWD,dir_name))
    except FileExistsError as e:
        print(f"File already existed, Erorr: {e}")


def printenv():
    """
    Display selected environment information.

    Notes:
        Prints the current working directory, username, and desktop
        environment using values imported from the env module.
    """
    print(f"PWD = {CWD}")
    print(f"USER = {USER}")
    print(f"DESKTOP = {DESKTOP}")


def touch(file_name):
    """
    Create a file if it does not exist.

    Args:
        file_name (str): The name or path of the file to create.

    Notes:
        Opens the file in append mode, preserving existing content.
    """
    file = open(os.path.join(CWD,file_name),'a')
    file.close()

def cat(file,n_flag=False):
    """
    Read and display the contents of a text file.

    Args:
        file (str): The name or path of the file to read.
        n_flag (bool): Display line numbers when True.

    Notes:
        Displays the entire file when line numbering is disabled.
        Displays each line with its corresponding number when enabled.
        Prints an error message if the file does not exist or the path
        points to a directory.
    """
    if not file:
        return
    try:
        with open(os.path.join(CWD,file),'r') as f:
            if not n_flag:
                context = f.read()
                print(context)
            else:
                counter = 1
                context = f.readlines()
                for line in context:
                    print(f"{counter} -> {line}")
                    counter += 1

    except (FileNotFoundError , IsADirectoryError) as e:
        print(f"Erorr: {e}")
    
def man(command):
    """
    Display the documentation of a supported command.

    Args:
        command (str): The name of the command whose documentation
                       is requested.

    Notes:
        Supported commands include cd, ls, cat, pwd, touch, mkdir,
        and printenv.
    """
    commands = {
        'cd' : cd,
        'ls' : ls,
        'cat' : cat,
        'pwd' : pwd,
        'touch' : touch,
        'mkdir' : mkdir,
        'printenv' : printenv
    }
    func = commands.get(command)

    if func is not None:
        print(func.__doc__)
    else:
        print(f"Unknown command: {command}")


if __name__ == '__main__':
    print("Pysh Commands")