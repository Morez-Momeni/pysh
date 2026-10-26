<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=180&color=0:0B3D2E,50:16865B,100:38BDF8&text=pysh&fontSize=72&fontColor=FFFFFF&fontAlignY=45&desc=A%20Python%20Shell%20Project&descAlignY=70&descSize=18" width="100%" alt="pysh gradient banner" />

  <p>
    <strong>A small shell built with Python, one command at a time.</strong>
  </p>

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

The project is in its early stages.

| Command | Description | Status |
|:---|:---|:---|
| `ls` | Lists files and directories | In progress |
| `ls -a` | Includes hidden entries | In progress |
| `ls -l` | Displays file details and timestamps | In progress |
| `pwd` | Displays the current working directory | Implemented |
| `cd` | Changes the working directory | In progress |

### `ls`

The current implementation can list directory contents, distinguish directories from files using colors, hide hidden entries by default, and collect additional file information.

The long-format output includes:
- File or directory name
- File size in bytes
- Creation time
- Last modification time

### `pwd`

Displays the current working directory maintained by the project.

### `cd`

The current implementation includes basic navigation behavior, such as moving to the parent directory and returning to the home directory.

Command handling and path resolution are still being developed.

## Tech Stack

- **Python** — Core language
- **OS module** — Filesystem and directory operations
- **Datetime** — File timestamps
- **Colorama** — Colored terminal output

## Project Structure

The project structure will evolve as new commands and features are added.

```text
pysh/
├── pysh.py
└── commands.py
└── README.md
```

*This structure represents the initial stage of the project and will be updated as the codebase grows.*

## Roadmap

The following are possible next steps, not completed features.

- [x] Implement initial directory listing
- [x] Add colored directory names
- [x] Collect basic file metadata
- [ ] Improve path handling
- [ ] Add a command input loop
- [ ] Parse commands and their arguments
- [ ] Implement `mkdir`, `touch`, and `cat`
- [ ] Add command history
- [ ] Improve error handling
- [ ] Organize commands into separate modules
- [ ] Explore executing system commands
- [ ] Experiment with pipes and output redirection

## Why This Project?

Because the best way to understand something is sometimes to build a small version of it yourself.

`pysh` is an opportunity to experiment, make mistakes, refactor, and learn along the way. There is no pressure to make everything perfect from the beginning; the goal is to keep building and understand a little more with every step.

## Disclaimer

This is an educational project created for personal practice and experimentation. It is not intended to replace Bash, Zsh, or other mature command-line shells.

---

<div align="center">
  <sub>Built with Python, curiosity, and a willingness to experiment.</sub>
  <br><br>
  <img src="https://capsule-render.vercel.app/api?type=rect&height=70&color=0:38BDF8,50:16865B,100:0B3D2E&section=footer" width="100%" alt="Gradient footer" />
</div>
