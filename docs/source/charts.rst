Charts
======
You can add bar charts::

  from rich.charts import Bar
  from rich import print
  chart = Bar(40)
  chart.add_sequence(5, "test", "red")
  chart.add_sequence(7, "test2", "yellow")
  chart.add_sequence(40, "test3", "blue")
  print(chart)
Which will result in::

  ────┐
  ────┘test

  ──────┐
  ──────┘test2

  ───────────────────────────────────────┐
  ───────────────────────────────────────┘test3

