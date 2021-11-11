from rich import print

print("Hello, [bold blue]Towards Data Science[/bold blue]!", ":thumbs_up:", "[u]By[/u]", "[i]Christopher Tao[/i]")

from rich import pretty
pretty.install()
a = {"bool1":True, "bool2":False, "number":123.45, "string":"Hello!", "dict":{"key":"value"}, "list":[1,2,3], "class":type(1)}

print(a)