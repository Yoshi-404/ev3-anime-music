# LEGO EV3 Anime Music Player

A Python script for the LEGO Mindstorms EV3 that randomly plays classic anime themes using the robot's speaker.

This project was developed to run on the **ev3dev** operating system using the **Pybricks** library.

## Included Songs
Whenever the script is executed, the EV3 randomly selects and plays one of the following songs:
1. **Neon Genesis Evangelion** (A Cruel Angel's Thesis)
2. **Naruto Shippuden** (Bluebird)
3. **One Piece** (We Are!)

## Prrequisites
* A LEGO Mindstorms EV3 brick.
* SD card with [ev3dev](https://www.ev3dev.org/) installed.
* Environment configured with the `pybricks` library.

## How to run
1. Connect to your EV3 via SSH or use the EV3 extension in VS Code
2. Transfer the `musicas.py` file to your robot.
3. Give execution permission to the file (if you are running it via terminal)
   ```bash
   chmod +x musicas.py
