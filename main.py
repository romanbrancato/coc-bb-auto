from adbutils import adb
from bot import Bot
from client import Client
import os
import msvcrt
import sys
import time


def get_key():
    """Get a keypress on Windows."""
    if msvcrt.kbhit():
        key = msvcrt.getch()
        # Handle arrow keys
        if key == b'\xe0':  # Extended key
            key = msvcrt.getch()
            if key == b'H':  # Up arrow
                return 'UP'
            elif key == b'P':  # Down arrow
                return 'DOWN'
        elif key == b'\r':  # Enter key
            return 'ENTER'
        elif key == b'q' or key == b'Q':
            return 'QUIT'
    return None


def display_devices(devices, selected_idx):
    """Display available devices with the currently selected one highlighted."""
    os.system('cls')
    print("Available devices:")
    print("------------------")

    for i, device in enumerate(devices):
        prefix = "→ " if i == selected_idx else "  "
        print(f"{prefix} {device.serial}")

    print("\nUse ↑/↓ arrow keys to navigate, Enter to select, q to quit")


def select_device(devices):
    """Interactive device selection for Windows."""
    selected_idx = 0
    display_devices(devices, selected_idx)

    while True:
        key = get_key()
        # Small delay to prevent CPU hogging
        time.sleep(0.1)

        if key == 'UP':
            selected_idx = (selected_idx - 1) % len(devices)
            display_devices(devices, selected_idx)
        elif key == 'DOWN':
            selected_idx = (selected_idx + 1) % len(devices)
            display_devices(devices, selected_idx)
        elif key == 'ENTER':
            return devices[selected_idx].serial
        elif key == 'QUIT':
            print("\nExiting...")
            sys.exit(0)


def main():
    devices = adb.device_list()

    if not devices:
        print("No devices found. Make sure an emulator or device is connected.")
        sys.exit(1)

    # Auto-select if only one device is available
    if len(devices) == 1:
        device_serial = devices[0].serial
    else:
        # Show selection interface only when multiple devices are present
        device_serial = select_device(devices)

    client = Client(serial=device_serial)
    bot = Bot(client)
    bot.run()



if __name__ == '__main__':
    main()