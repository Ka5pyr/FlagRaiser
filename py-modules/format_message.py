import textwrap
from rich.console import Console

def print_title(title):
    console = Console()
    # Add a blank line to the beginning of the output
    print("")
    console.print(f"[bold blue]{title}[/bold blue]")

def print_check_pass(check):
    if check["print_success"] is False:
        return
        
    console = Console()
    console.print(f"  [bold green][✔] Success:[/bold green] {check['name']}")
    if check["success_flag"] != "":
        console.print(f"{' '*6}🎉 [bold green]Flag:[/bold green]"
                      f"{check['success_flag']} 🎉")
        
def print_check_fail(check, issue):
    console = Console()
    console.print(f"  [bold red][✘] Failure:[/bold red] {check['name']}")
    console.print(f"{' '*6}[bold]Description:[/bold]")
    console.print(textwrap.fill(f"{' '*8}• {check['description']}",
                    width=70, subsequent_indent=' '*10))
    console.print(f"{' '*6}[bold]Issue:[/bold]")
    console.print(textwrap.fill(f"{' '*8}• {issue}",
                    width=70, subsequent_indent=' '*10))
    console.print(f"{' '*6}[bold]Suggestions:[/bold]")
    for suggestion in check['suggestions']:
        console.print(textwrap.fill(f"{' '*8}• {suggestion}",
                    width=70, subsequent_indent=' '*10))
    # Add a blank line to the end of the progam output
    print("")