import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from seiri.utils import logging

WIDTH = 1024
HEIGHT = 800

logger = logging.getLogger(__name__)


class Seiri(toga.App):
    def startup(self):

        logger.info("Starting up the app...")

        self.main_window = toga.MainWindow(
            title=f"{self.formal_name} v{self.version}",
            size=(WIDTH, HEIGHT),
            resizable=False,
        )

        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window.content = self.main_box

        self.main_window.show()

        logger.info("App started.")


def main():
    return Seiri()
