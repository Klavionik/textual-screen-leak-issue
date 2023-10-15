from textual.app import App, ComposeResult
from textual.widgets import Footer, DataTable, Label
from textual.screen import Screen

from pympler.summary import summarize
from pympler import muppy


def get_screens_summary():
    all_objects = muppy.get_objects()
    screens = muppy.filter(all_objects, Type=Screen)
    return summarize(screens)


class FirstScreen(Screen):
    BINDINGS = [("e", "second_screen", "Switch to the second screen")]

    def compose(self) -> ComposeResult:
        yield Label(f"[red bold]{self.__class__.__name__}[/]")
        table = DataTable()
        table.styles.margin = 2
        table.add_columns("Class name", "Instances", "Memory footprint (kb)")
        table.add_rows(get_screens_summary())
        yield table
        yield Footer()

    def action_second_screen(self):
        self.app.switch_screen(SecondScreen())

    def __del__(self):
        self.log.warning(f"{self.__class__.__name__} DELETED")


class SecondScreen(Screen):
    BINDINGS = [("e", "first_screen", "Switch to the first screen")]

    def compose(self) -> ComposeResult:
        yield Label(f"[red bold]{self.__class__.__name__}[/]")
        yield Label(f"[bold]Go back to see pympler report[/]")
        yield Footer()

    def action_first_screen(self):
        self.app.switch_screen(FirstScreen())

    def __del__(self):
        self.log.warning(f"{self.__class__.__name__} DELETED")


class TheApp(App):
    def on_mount(self):
        self.push_screen(FirstScreen())
