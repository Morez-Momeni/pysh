<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=260&color=gradient&section=header&reversal=false&text=Pysh&textBg=false&fontSize=70&fontAlign=50&fontAlignY=50&animation=twinkling&rotate=0&strokeWidth=0&desc=A+Python+Shell+Project&descSize=22&descAlign=49&descAlignY=72" width="100%" alt="Pysh — A Python Shell Project" />

  <p><strong>A small shell built with Python, one command at a time.</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Project-Learning-16865B?style=flat-square" alt="Learning project" />
    <img src="https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square" alt="In progress" />
    <img src="https://img.shields.io/badge/Purpose-Fun%20%26%20Practice-38BDF8?style=flat-square" alt="Fun and practice" />
  </p>
</div>

---

## About

`pysh` is a personal project built for fun, experimentation, and Python practice.

The idea is simple: build a small command-line shell from scratch and gradually explore how command-line interfaces work, how files and directories are managed, and how different parts of a shell fit together.

This project is not intended to be a production-ready replacement for existing shells. It is a space to learn by building, experiment with new ideas, and improve the code step by step.

## Goals

- Practice Python through a hands-on project.
- Work with filesystem operations and path handling.
- Learn how to organize commands and their behavior.
- Explore command parsing and argument handling.
- Improve error handling and code organization.
- Gradually expand the shell as new ideas come up.

## Current Features

The project currently includes basic commands for filesystem navigation, file management, and environment information.

| Command | Description |
|:---|:---|
| `ls` | Lists files and directories in the current working directory. |
| `ls -a` | Includes hidden files and directories. |
| `ls -l` | Displays file sizes and timestamps. |
| `pwd` | Displays the current working directory. |
| `cd` | Changes the current working directory. |
| `mkdir` | Creates a directory. |
| `touch` | Creates a file without overwriting existing content. |
| `cat` | Reads and displays a text file. |
| `cat -n` | Displays file contents with line numbers. |
| `printenv` | Displays selected environment information. |
| `man` | Displays the documentation of a supported command. |

### Filesystem Navigation

#### `ls`

Lists the contents of the current working directory.

- Directories are displayed in green.
- Hidden entries are excluded by default.
- `-a` includes hidden files and directories.
- `-l` displays file sizes, creation timestamps, and modification timestamps.

#### `pwd`

Displays the current working directory maintained by `pysh`.

#### `cd`

Changes the current working directory.

The current implementation supports moving to the parent directory with `cd ..`, returning to the home directory with `cd`, and navigating to a directory when its path can be resolved.

### File Management

#### `mkdir`

Creates a directory inside the current working directory.

The current implementation handles the case where the target already exists.

#### `touch`

Creates a file if it does not exist. It uses append mode to preserve the contents of an existing file.

#### `cat`

Reads and displays the contents of a text file.

The `-n` option displays line numbers alongside the file contents.

### Environment Information

#### `printenv`

Displays selected environment information obtained from the project's `env` module:

- Current working directory (`CWD`)
- Username (`USER`)
- Desktop environment (`DESKTOP`)

### Command Documentation

#### `man`

Displays the Python docstring associated with a supported command.

The current implementation uses a command mapping to find the corresponding function and print its documentation.

## Tech Stack

- **Python** — Core language
- **OS module** — Filesystem operations and path handling
- **Datetime** — File timestamps
- **Colorama** — Colored terminal output

## Project Structure

The current project uses a simple structure that can evolve as more commands and features are added.

```text
pysh/
├── pysh.py
├── commands.py
└── README.md
```

- `pysh.py` — Main entry point for the project.
- `commands.py` — Contains the command implementations.
- `README.md` — Project documentation.

## Roadmap

These are potential next steps, not claims about completed functionality.

- [x] Implement directory listing
- [x] Add colored directory names
- [x] Display file metadata
- [x] Implement basic directory navigation
- [x] Add file and directory creation commands
- [x] Read text files and display line numbers
- [x] Display selected environment information
- [x] Add command documentation
- [ ] Improve path handling
- [ ] Build an interactive command loop
- [ ] Implement command and argument parsing
- [ ] Improve error handling
- [ ] Add command history
- [ ] Organize commands into separate modules
- [ ] Explore executing system commands
- [ ] Experiment with pipes and output redirection

## Why This Project?

Because sometimes the best way to understand something is to build a small version of it yourself.

`pysh` is an opportunity to experiment, make mistakes, refactor, and learn along the way. There is no pressure to make everything perfect from the beginning. The goal is to keep building and understand a little more with every step.

## Disclaimer

This is an educational project created for personal practice and experimentation. It is not intended to replace Bash, Zsh, or other mature command-line shells.

---

<div align="center">
  <sub>Built with Python, curiosity, and a willingness to experiment.</sub>
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=gradient&section=footer&reversal=false&textBg=false&fontSize=70&fontAlign=50&fontAlignY=50&animation=twinkling&rotate=0&strokeWidth=0&descSize=22&descAlign=49&descAlignY=72" width="100%" alt="Gradient footer" />
</div>