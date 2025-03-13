from adbutils import adb
from numpy import asarray


class Client:
    def __init__(self, serial):
        self.device = adb.device(serial)

    def capture_screen(self):
        return asarray(self.device.screenshot())
