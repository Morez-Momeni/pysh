from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.theme import Theme


theme = Theme({
    "prompt": "bold green",
    "path": "bold cyan",
    "command": "bold white",
    "output": "white",
    "muted": "dim white",
})

console = Console(theme=theme)


def show_interface():
    console.clear()

    # Header
    title = Text("PYSH", style="bold green", justify="center")
    subtitle = Text("A Python Shell Project", style="dim white")

    header = Text()
    header.append(title)
    header.append("\n")
    header.append(subtitle)

    console.print(
        Panel(
            Align.center(header),
            border_style="green",
            padding=(1, 2),
            title="[bold green]Terminal[/bold green]",
            subtitle="[dim]v0.1.0[/dim]",
        )
    )

    # Terminal body
    terminal_content = Text()
    terminal_content.append("Welcome to Pysh!\n", style="bold green")
    terminal_content.append("Type your commands below.\n\n", style="muted")

    terminal_content.append("morez", style="bold green")
    terminal_content.append("@pysh ", style="bold white")
    terminal_content.append("~/Projects/pysh", style="cyan")
    terminal_content.append(" $ ", style="bold green")
    terminal_content.append("ls\n", style="command")

    terminal_content.append("commands.py    pysh.py    README.md\n\n", style="output")

    terminal_content.append("morez", style="bold green")
    terminal_content.append("@pysh ", style="bold white")
    terminal_content.append("~/Projects/pysh", style="cyan")
    terminal_content.append(" $ ", style="bold green")

    console.print(
        Panel(
            terminal_content,
            border_style="bright_black",
            padding=(1, 2),
            title="[bold white]Pysh Shell[/bold white]",
        )
    )


if __name__ == "__main__":
    show_interface()