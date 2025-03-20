# cc-bb-auto
A simple script to automate builder base farming in Clash of Clans.


https://github.com/user-attachments/assets/68ca8fc3-78ce-4a6e-8762-7089a9c8fe75



## Setup
- [Python](https://www.python.org/downloads/)
- [LDPlayer](https://www.ldplayer.net/) emulator (Might work on any emulator but all testing was done on LDPlayer)
- 960x540 resolution
- Settings > Others > ADB Debugging = Enable local connection
- Install requirements with `pip install -r requirements.txt`.

## How to use
1. Go to the builder base village and ensure your townhall is centered.
2. Zoom out as far as possible (ctrl + mouse wheel down).
3. Go to main base then back to builder base to center the screen. The elixir cart should be visible, similar to the demo.
4. Run the script with `python main.py`.

## Notes
- The troop placement coordinate can be adjusted in `bot.py`
- If the bot is stalling, its due to a reference image detection problem.
