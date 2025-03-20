from time import sleep
from detection import *

ATTACK_BUTTON = (60, 475)
HERO_SLOT = (95, 485)
FIRST_TROOP_SLOT = (180, 485)
GRASS = (730, 85)
TROOP_SLOTS = 6


class Bot:
    def __init__(self, client):
        self.client = client

    def await_image(self, image_name):
        while True:
            found = locate_image(self.client.capture_screen(),[image_name], 0.9)
            if found: return found
            sleep(0.1)

    def handle_matching(self):
        while True:
            self.client.device.click(*ATTACK_BUTTON)
            sleep(0.2)
            if match := locate_image(self.client.capture_screen(), ["match.png"], 0.9):
                self.client.device.click(*match)
                self.await_image("match_begin.png")
                return

    def handle_battle(self):
        self.client.device.click(*HERO_SLOT)
        self.client.device.click(*GRASS)
        self.client.device.click(*FIRST_TROOP_SLOT)
        for _ in range(TROOP_SLOTS):
            self.client.device.click(*GRASS)
        sleep(1)  # CANNOT BE LOWER AS TROOPS WON'T REGISTER AS DEPLOYED

    def handle_restart(self):
        self.client.device.app_stop('com.supercell.clashofclans')
        self.client.device.app_start(package_name='com.supercell.clashofclans', activity='com.supercell.titan.GameApp')
        self.await_image("attack.png")

    def handle_elixir(self):
        while True:
            if cart := locate_image(self.client.capture_screen(), [ "elixir_cart_full.png", "elixir_cart_empty.png"], 0.5):
                self.client.device.click(*cart)
            sleep(0.2)
            if collect := locate_image(self.client.capture_screen(), ["elixir_collect.png"], 0.9):
                self.client.device.click(*collect)
                self.client.device.shell("input keyevent KEYCODE_BACK")
                return

    def run(self):
        while True:
            self.handle_elixir()
            self.handle_matching()
            self.handle_battle()
            self.handle_restart()
