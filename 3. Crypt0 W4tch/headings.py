import pyfiglet

def cli_ascii_heading(text):
    banner = pyfiglet.figlet_format(text, font="standard")
    print(banner)
