from time import sleep

from detection import *

ATTACK_BUTTON = (60, 475)
FIRST_TROOP_SLOT = (100, 485)
GRASS = (730, 85)
TROOP_SLOTS = 6


class Bot:
    def __init__(self, client):
        self.client = client

    def await_images(self, image_name, confidence=0.9, delay=0.2):
        while True:
            found = locate_image(self.client.capture_screen(), image_name, confidence)
            if found: return found
            sleep(delay)

    def handle_matching(self):
        self.client.device.click(*ATTACK_BUTTON)
        match = self.await_images(["match.png"], delay=1)
        if match:
            self.client.device.click(*match)
            self.await_images(["match_begin.png"])
            return

    def handle_battle(self):
        self.client.device.click(*FIRST_TROOP_SLOT)
        for _ in range(TROOP_SLOTS):
            self.client.device.click(*GRASS)
        sleep(1)  # CANNOT BE LOWER AS TROOPS WON'T REGISTER AS DEPLOYED

    # def handle_surrender(self):
    #     if surrender := locate_image(self.client.capture_screen(),["surrender.png"], 0.6):
    #         self.client.device.click(*surrender)
    #     sleep(0.2)
    #     if surrender_confirm := locate_image(self.client.capture_screen(), ["surrender_confirm.png"], 0.6):
    #         self.client.device.click(*surrender_confirm)
    #     sleep(0.5)
    #     if return_home := locate_image(self.client.capture_screen(), ["return_home.png"], 0.6):
    #         self.client.device.click(*return_home)
    #         self.await_images(["attack.png"])
    #         return

    def handle_restart(self):
        self.client.device.app_stop('com.supercell.clashofclans')
        self.client.device.app_start(package_name='com.supercell.clashofclans', activity='com.supercell.titan.GameApp')
        self.await_images(["attack.png"])

    def handle_elixir(self):
        while True:
            if cart := locate_image(self.client.capture_screen(),
                                    ["elixir_cart_empty.png", "elixir_cart_third.png", "elixir_cart_half.png", "elixir_cart_full.png"], 0.6):
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
