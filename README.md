<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&height=260&color=gradient&section=header&reversal=false&text=Pysh&textBg=false&fontSize=70&fontAlign=50&fontAlignY=50&animation=twinkling&rotate=0&strokeWidth=0&desc=A+Python+Shell+Project&descSize=22&descAlign=49&descAlignY=72" width="100%" alt="Pysh — A Python Shell Project" />

<br>

**A small shell built with Python, one command at a time.**

<br>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Project-Learning-16865B?style=for-the-badge" alt="Learning project" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-orange?style=for-the-badge" alt="In progress" />
  <img src="https://img.shields.io/badge/Purpose-Fun%20%26%20Practice-38BDF8?style=for-the-badge" alt="Fun and practice" />
</p>
</div>

<br>

---

## About

`pysh` is a personal project built for **fun**, **experimentation**, and **Python practice**.

The idea is simple: build a small command-line shell from scratch and gradually explore how command-line interfaces work, how files and directories are managed, and how different parts of a shell fit together.

The project also explores terminal presentation and user customization, including configurable colors, terminal styling, and a more structured interface.

> This project is **not** intended to be a production-ready replacement for existing shells.
> It is a space to learn by building, experiment with new ideas, and improve the code step by step.

---

## Goals

- Practice Python through a hands-on project
- Work with filesystem operations and path handling
- Learn how to organize commands and their behavior
- Explore command parsing and argument handling
- Experiment with terminal styling and customization
- Improve error handling and code organization
- Gradually expand the shell as new ideas come up

---

## Current Features

The project currently includes commands for filesystem navigation, file management, terminal output, environment information, command documentation, history tracking, and repeated command execution.

| Command    | Description                                                     |
| ---------- | --------------------------------------------------------------- |
| `ls`       | Lists files and directories in the current working directory    |
| `ls -a`    | Includes hidden files and directories                           |
| `ls -l`    | Displays file sizes and timestamps                              |
| `pwd`      | Displays the current working directory                          |
| `cd`       | Changes the current working directory                           |
| `mkdir`    | Creates a directory                                             |
| `touch`    | Creates a file without overwriting existing content             |
| `cat`      | Reads and displays a text file                                  |
| `cat -n`   | Displays file contents with line numbers                        |
| `rm`       | Removes a file                                                  |
| `rm -r`    | Removes a directory and its contents recursively                |
| `mv`       | Moves or renames a file or directory                            |
| `cp`       | Copies a file                                                   |
| `cp -r`    | Copies a directory recursively                                  |
| `echo`     | Displays text in the terminal                                   |
| `echo >`   | Writes text to a file, replacing its existing content           |
| `clear`    | Clears the terminal screen                                      |
| `printenv` | Displays selected environment information                       |
| `uname`    | Displays system information                                     |
| `uname -a` | Displays all available system information                       |
| `man`      | Displays the documentation of a supported command               |
| `history`  | Displays previously recorded commands                           |
| `watch`    | Repeatedly executes a supported command at a specified interval |

---

## Filesystem Navigation

### `ls`

Lists the contents of the current working directory.

- Directories are displayed in **green**
- Hidden entries are excluded by default
- `-a` includes hidden files and directories
- `-l` displays file sizes, creation timestamps, and modification timestamps

### `pwd`

Displays the current working directory maintained by `pysh`.

### `cd`

Changes the current working directory.

Supports:

- Moving to the parent directory with `cd ..`
- Returning to the home directory with `cd`
- Navigating to a directory when its path can be resolved

---

## File Management

### `mkdir`

Creates a directory inside the current working directory.

### `touch`

Creates a file if it does not exist. Uses append mode to preserve the contents of an existing file.

### `cat`

Reads and displays the contents of a text file.

The `-n` option displays line numbers alongside the file contents.

### `rm`

Removes a file from the filesystem.

The `-r` option enables recursive directory removal, allowing directories and their contents to be deleted.

**Examples:**

```bash
rm hello.txt
rm -r old_directory
```

### `mv`

Moves a file or directory to another location. It can also be used to rename files and directories.

**Examples:**

```bash
mv hello.txt documents/
mv old_name.txt new_name.txt
```

### `cp`

Copies a file to another location.

The `-r` option enables recursive directory copying.

**Examples:**

```bash
cp hello.txt backup.txt
cp -r projects backup_projects
```

---

## Terminal Output

### `echo`

Displays text in the terminal.

Also supports writing text to a file using the project's output-to-file option.

**Example:**

```bash
echo hello
```

**Output:**

```text
hello
```

**Writing to a file:**

```bash
echo hello > hello.txt
```

When writing to a file:

- A new file is created if it does not exist
- Existing content is replaced
- The text is written to the specified file instead of being displayed in the terminal

### `clear`

Clears the terminal screen using the system's `clear` command.

---

## Environment & System Information

### `printenv`

Displays selected environment information obtained from the project's `env` module.

| Key       | Description               |
| --------- | ------------------------- |
| `CWD`     | Current working directory |
| `USER`    | Username                  |
| `DESKTOP` | Desktop environment       |

### `uname`

Displays information about the operating system using Python's `os.uname()`.

Available options:

| Option | Description                                |
| ------ | ------------------------------------------ |
| `-a`   | Displays all available system information  |
| `-s`   | Displays the operating system name         |
| `-n`   | Displays the network node hostname         |
| `-v`   | Displays the operating system version      |
| `-m`   | Displays the machine hardware architecture |

**Example:**

```bash
uname
uname -a
uname -m
```

---

## Command Documentation

### `man`

Displays the Python docstring associated with a supported command.

Uses a command mapping to find the corresponding function and print its documentation.

---

## Command History

### `history`

Displays previously recorded commands.

Uses a shared dictionary to store commands alongside their execution counter. Each recorded command is associated with a number.

**Example:**

```text
1  ls
2  cd
3  pwd
```

> The history functionality is currently being developed as part of the shell's command management.

---

## Repeated Command Execution

### `watch`

Repeatedly executes a supported command at a specified time interval.

- Execution can be interrupted using `Ctrl + C`
- Useful for periodically checking information without manually running the same command multiple times

---

## Terminal Customization

`pysh` includes a customization module that allows users to personalize the terminal's appearance.

**Current options:**

- Prompt color
- Path color
- Command color
- Output color
- Muted text color
- Header title color
- Header subtitle color

Color settings use **Rich-compatible** color names and styles:

```text
green
bold green
dim cyan
bold bright_red
```

Users can choose whether to customize the default theme or keep the predefined settings.

---

## Tech Stack

| Technology   | Purpose                                      |
| ------------ | -------------------------------------------- |
| **Python**   | Core language                                |
| **OS**       | Filesystem and system information operations |
| **Shutil**   | File and directory copying and moving        |
| **Datetime** | File timestamps                              |
| **Colorama** | Colored terminal output                      |
| **Rich**     | Terminal styling and customizable UI         |

---

## Project Structure

```text
pysh/
├── pysh.py          # Main entry point
├── commands.py      # Command implementations
├── interface.py     # Terminal presentation
├── uisettings.py    # Theme colors & UI customization
├── env.py           # Shared environment variables
└── README.md        # Project documentation
```

---

## Roadmap

These are potential next steps — not claims about completed functionality.

### Completed

- [x] Implement directory listing
- [x] Add colored directory names
- [x] Display file metadata
- [x] Implement basic directory navigation
- [x] Add file and directory creation commands
- [x] Read text files and display line numbers
- [x] Display selected environment information
- [x] Add command documentation
- [x] Implement repeated command execution
- [x] Introduce terminal theme customization
- [x] Add configurable terminal colors
- [x] Add terminal screen clearing
- [x] Add terminal text output
- [x] Add basic output-to-file functionality
- [x] Introduce command history storage and display
- [x] Implement file and directory removal
- [x] Implement file and directory moving
- [x] Implement file and directory copying
- [x] Add operating system information command

### Planned

- [ ] Persist user settings between sessions
- [ ] Improve path handling
- [ ] Build an interactive command loop
- [ ] Implement command and argument parsing
- [ ] Improve error handling
- [ ] Expand command history functionality
- [ ] Organize commands into separate modules
- [ ] Explore executing system commands
- [ ] Experiment with pipes and output redirection

---

## Why This Project?

Because sometimes the best way to understand something is to build a small version of it yourself.

`pysh` is an opportunity to experiment, make mistakes, refactor, and learn along the way. There is no pressure to make everything perfect from the beginning.

The goal is to **keep building** and understand a little more with every step.

---

## Disclaimer

This is an **educational project** created for personal practice and experimentation.
It is **not** intended to replace Bash, Zsh, or other mature command-line shells.

---

<div align="center">
  <sub>Built with Python, curiosity, and a willingness to experiment.</sub>
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=gradient&section=footer&reversal=false&textBg=false&fontSize=70&fontAlign=50&fontAlignY=50&animation=twinkling&rotate=0&strokeWidth=0&descSize=22&descAlign=49&descAlignY=72" width="100%" alt="Gradient footer" />
</div>
