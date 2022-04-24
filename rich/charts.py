from . import print
from .panel import Panel


class Bar:
    def __init__(self):
        self.renderable = """"""
        self.renderable_data = []
        self.data = []

    def add_sequence(self, data, label, color="black"):
        self.renderable_data.append(
            f"[{color}]"
            + "─" * (data - 1)
            + "┐"
            + "\n"
            + "─" * (data - 1)
            + "┘"
            + label
            + "\n\n"
            + "[/]"
        )

    def __rich__(self):
        for i in self.renderable_data:
            self.renderable = self.renderable + i.strip(" ")
        return self.renderable


if __name__ == "__main__":
    print("A [bold]bar[/bold] chart:")
    example_bar = Bar(40)
    example_bar.add_sequence(5, "test", "red")
    example_bar.add_sequence(7, "test2", "yellow")
    example_bar.add_sequence(40, "test3", "blue")
    print(example_bar)
