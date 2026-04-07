
\f0\fs24 \cf0 #!/usr/bin/env python3\
import time\
import random\
from pybricks.hubs import EV3Brick\
\
def tocar_evangelion(ev3):\
    \'93\'94\'94Play the Neon Genesis Evangelion theme song.\'94\'94\'94\
    ev3.speaker.play_notes(['C3/3', 'D#3/3', 'F3/4', 'D#3/4', 'F3/5', 'F3/3', 'A#3/5', 'G#3/5', 'G3/6', 'F3/6'], tempo=200)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['G3/2', 'G3/3', 'A#3/3', 'C4/4', 'F3/4', 'D#3/5', 'A#3/3'], tempo=200)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['G3/5', 'A#3/5', 'A#3/4', 'C4/2'], tempo=200)\
    time.sleep(0.1)\
\
def tocar_bluebird(ev3):\
    \'93\'94\'94Play Bluebird (Naruto Shippuden)."""\
    ev3.speaker.play_notes(['C#4/4', 'F#4/4', 'G#4/4', 'A4/2', 'G#4/2'], tempo=180)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['F#4/2', 'C#4/3', 'F#4/5'], tempo=180)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['G#4/4', 'A4/2', 'B4/3', 'A4/4'], tempo=180)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['B4/3', 'C#5/2', 'C#4/4', 'F#4/4', 'G#4/5'], tempo=180)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['A4/2', 'G#4/3', 'F#4/3'], tempo=180)\
    time.sleep(0.3)\
    ev3.speaker.play_notes(['F#4/4', 'C#5/4', 'B4/3'], tempo=180)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['F#4/4', 'C#5/4', 'B4/3', 'E4/3', 'E4/3', 'F#4/5'], tempo=180)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['F#4/1'], tempo=180)\
    time.sleep(0.1)\
\
def tocar_one_piece(ev3):\
    \'93\'94\'94Play the One Piece theme song.\'94\'94\'94\
    ev3.speaker.play_notes(['A#4/6','A#4/6', 'D#5/2'], tempo=192)\
    time.sleep(0.3)\
    ev3.speaker.play_notes(['A#4/3','D#5/6', 'F5/1'], tempo=192)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['D#5/6', 'F5/6', 'G#5/4', 'G5/2', 'D#5/2', 'G#4/6', 'G#4/6'], tempo=192)\
    time.sleep(0.1)\
    ev3.speaker.play_notes(['A#4/6', 'A#4/6', 'A#4/6', 'A#4/6', 'D#5/6', 'D#5/2', 'A#4/3', 'D#5/6', 'F5/6'], tempo=192)\
    time.sleep(0.2)\
    ev3.speaker.play_notes(['F4/3','G#4/3', 'G4/3', 'F4/6', 'D#4/6', 'F4/6', 'D#4/6'], tempo=192)\
    time.sleep(0.1)\
\
def main():\
    # Starts EV3\
    ev3 = EV3Brick()\
    \
    # Sort one number 1 to 3\
    escolha = random.randint(1, 3)\
    \
    # play the music\
    if escolha == 1:\
        print("Playing: Evangelion")\
        tocar_evangelion(ev3)\
    elif escolha == 2:\
        print("Playing: Bluebird (Naruto)")\
        tocar_bluebird(ev3)\
    else:\
        print(\'93Playing: One Piece")\
        tocar_one_piece(ev3)\
\
if __name__ == "__main__":\
    main()}
