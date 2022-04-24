import rich.charts

def test_bar():
    chart = rich.charts.Bar()
    chart.add_sequence(10, "test")
    assert chart.__rich__() == """[black]─────────┐
─────────┘test

[/]"""
def test_bar_multiple_sequences():
    chart = rich.charts.Bar()
    chart.add_sequence(10, "test")
    chart.add_sequence(20, "test2")
    chart.add_sequence(30, "test3")
    assert chart.__rich__() == """[black]─────────┐
─────────┘test

[/][black]───────────────────┐
───────────────────┘test2

[/][black]─────────────────────────────┐
─────────────────────────────┘test3

[/]"""
def test_bar_colors():
    chart = rich.charts.Bar()
    chart.add_sequence(5, "test", "red")
    chart.add_sequence(10, "test2", "green")
    assert chart.__rich__() == """[red]────┐
────┘test

[/][green]─────────┐
─────────┘test2

[/]"""
