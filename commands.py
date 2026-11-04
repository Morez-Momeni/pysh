import os
import time
from datetime import datetime
from colorama import Fore, Style
from env import CWD, USER, DESKTOP, COUNTER, HISTORY


def ls(l_flag=False, a_flag=False):
    """
    List files and directories in the current working directory.

    Args:
        l_flag (bool): Display detailed information, including file size,
                       creation time, and last modification time.
        a_flag (bool): Include hidden files and directories.

    Notes:
        Directories are displayed in green.
        Hidden entries are excluded by default.
        Detailed information is displayed when l_flag is True.
    """
    global COUNTER
    COUNTER += 1

    result = os.listdir(CWD)
    info_list = []

    if not l_flag:
        for r in result:
            full_path = os.path.join(CWD, r)

            if os.path.isdir(full_path) and a_flag == True:
                print(
                    Fore.GREEN + f"{r}" + Style.RESET_ALL,
                    end=" "
                )

            elif os.path.isdir(full_path) and a_flag == False:
                if r.startswith("."):
                    continue
                else:
                    print(
                        Fore.GREEN + f"{r}" + Style.RESET_ALL,
                        end=" "
                    )

            elif os.path.isfile(full_path) and a_flag == True:
                print(r, end=" ")

            elif os.path.isfile(full_path) and a_flag == False:
                if r.startswith("."):
                    continue
                else:
                    print(r, end=" ")

    else:
        for r in result:
            full_path = os.path.join(CWD, r)

            size = os.path.getsize(full_path)
            creation = datetime.fromtimestamp(
                os.path.getctime(full_path)
            )
            modification = datetime.fromtimestamp(
                os.path.getmtime(full_path)
            )

            info = {
                'name': r,
                'size': size,
                'creation': creation,
                'modification': modification
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

    Notes:
        Prints the current value of CWD.
        Increments the command counter.
    """
    global COUNTER
    COUNTER += 1

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
        Increments the command counter.
    """
    global COUNTER
    COUNTER += 1

    global CWD

    if dir.strip() == "..":
        CWD = os.path.abspath(
            os.path.join(CWD, os.pardir)
        )

    elif dir == "":
        CWD = os.path.expanduser("~")

    elif os.path.isdir(os.path.join(CWD, dir)):
        CWD = os.path.join(CWD, dir)
        print(CWD)

    else:
        print("no dir")


def mkdir(dir_name):
    """
    Create a new directory in the current working directory.

    Args:
        dir_name (str): The name of the directory to create.

    Notes:
        Creates the directory inside CWD.
        Displays an error message if the directory or file already exists.
        Increments the command counter.
    """
    global COUNTER
    COUNTER += 1

    try:
        os.mkdir(os.path.join(CWD, dir_name))

    except FileExistsError as e:
        print(f"File already existed, Erorr: {e}")


def printenv():
    """
    Display selected environment information.

    Notes:
        Prints the current working directory, username, and desktop
        environment using values imported from the env module.
        Increments the command counter.
    """
    global COUNTER
    COUNTER += 1

    print(f"PWD = {CWD}")
    print(f"USER = {USER}")
    print(f"DESKTOP = {DESKTOP}")


def touch(file_name):
    """
    Create a file if it does not exist.

    Args:
        file_name (str): The name or path of the file to create.

    Notes:
        Opens the file in append mode.
        Preserves existing content if the file already exists.
        Increments the command counter.
    """
    global COUNTER
    COUNTER += 1

    file = open(
        os.path.join(CWD, file_name),
        'a'
    )

    file.close()


def cat(file, n_flag=False):
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
        Increments the command counter.
    """
    global COUNTER
    COUNTER += 1

    if not file:
        return

    try:
        with open(
            os.path.join(CWD, file),
            'r'
        ) as f:

            if not n_flag:
                context = f.read()
                print(context)

            else:
                counter = 1
                context = f.readlines()

                for line in context:
                    print(f"{counter} -> {line}")
                    counter += 1

    except (FileNotFoundError, IsADirectoryError) as e:
        print(f"Erorr: {e}")


def man(command):
    """
    Display the documentation of a supported command.

    Args:
        command (str): The name of the command whose documentation
                       is requested.

    Notes:
        Displays the command's docstring.
        Supported commands include cd, ls, cat, pwd, touch, mkdir,
        printenv, man, watch, history, clear, and echo.
        Increments the command counter.
    """
    global COUNTER
    COUNTER += 1

    commands = {
        'cd': cd,
        'ls': ls,
        'cat': cat,
        'pwd': pwd,
        'touch': touch,
        'mkdir': mkdir,
        'printenv': printenv,
        'man': man,
        'watch': watch,
        'history': history,
        'clear': clear,
        'echo': echo
    }

    func = commands.get(command)

    if func is not None:
        print(func.__doc__)

    else:
        print(f"Unknown command: {command}")


def watch(command, n_flag=False, timer=1):
    """
    Execute a supported command repeatedly or once.

    Args:
        command (str): The name of the command to execute.
        n_flag (bool): Repeat the command when True.
        timer (int or float): Delay in seconds between executions.

    Notes:
        Currently supports cat, pwd, and printenv.
        Displays an error message for unsupported commands.
        Stops repeating when Ctrl+C is pressed.
        Increments the command counter.
    """
    global COUNTER
    COUNTER += 1

    commands = {
        'cat': cat,
        'pwd': pwd,
        'printenv': printenv
    }

    func = commands.get(command)

    if func is None:
        print(
            f"watch: {command}: "
            "command not found or not supported"
        )
        return

    try:
        if n_flag:
            while True:
                func()
                time.sleep(timer)

        else:
            func()

    except KeyboardInterrupt:
        print("\nWatch stopped.")


def history(command):
    """
    Display the recorded command history.

    Args:
        command (str): The command name to record.

    Notes:
        Stores the command in the shared HISTORY dictionary.
        Uses COUNTER as the command history index.
        Displays all commands currently stored in HISTORY.
    """
    HISTORY[COUNTER] = command

    for key, val in HISTORY.items():
        print(f"{key} {val}")


def clear():
    """
    Clear the terminal screen.

    Notes:
        Uses the system clear command.
    """
    os.system("clear")


def echo(text, file=None, to_file_flag=False):
    """
    Display text or write it to a file.

    Args:
        text (str): The text to display or write.
        file (str, optional): The destination file.
        to_file_flag (bool): Write text to a file when True.

    Notes:
        Prints text when file output is disabled.
        Writes text to the specified file when file output is enabled.
        Existing file content is overwritten when writing to a file.
    """
    if to_file_flag == True and file is not None:

        with open(file, 'w') as f:
            f.write(text)

    else:
        print(text)

def rm():
    pass
if __name__ == '__main__':
    print("Pysh Commands")
