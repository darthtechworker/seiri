import toga
from toga.style import Pack
from toga.style.pack import ROW

from seiri.ui.main import build_ui
from seiri.utils import logging

WIDTH = 1024
HEIGHT = 1000

logger = logging.getLogger(__name__)


class Seiri(toga.App):
    def startup(self):

        logger.info("Starting up the app...")

        # Directory paths
        self.output_directory = None
        self.working_directory = None
        self.pdf_path = None

        self.main_window = toga.MainWindow(
            title=f"{self.formal_name} v{self.version}",
            size=(WIDTH, HEIGHT),
            resizable=False,
        )

        self.main_box = toga.Box(style=Pack(direction=ROW))

        self.main_window.content = self.main_box

        build_ui(self)

        self.main_window.show()

        logger.info("App started.")


def main():
    return Seiri()
