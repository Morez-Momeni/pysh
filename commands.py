import os
from datetime import datetime
from colorama import Fore , Style


CWD = os.getcwd()

def ls(l_flag=False,a_flag=False):
    global CWD
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
        print(
            f"{Fore.GREEN}{inf['name']:<25}{Style.RESET_ALL}"
            f"{inf['size']:>10} bytes  "
            f"{inf['creation'].strftime('%Y-%m-%d %H:%M:%S')}  "
            f"{inf['modification'].strftime('%Y-%m-%d %H:%M:%S')}"
        )


def pwd():
    print(CWD)

def cd(dir):
    global CWD
    if dir.strip() == "..":
        CWD = os.path.abspath(os.path.join(CWD,os.pardir))
    elif dir ==  "":
        CWD = os.path.expanduser("~")
    elif os.path.isdir(dir):
        CWD = os.path.join(CWD,dir)
        print(CWD)
    else:
        print("no dir")

if __name__ == '__main__':
    print("Pysh Commands")