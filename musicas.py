#!/usr/bin/env python3
"""LEGO Mindstorms EV3 - Anime Music Player.

Plays random anime theme songs using the EV3 Brick speaker and Pybricks.
"""

import random
import time

try:
    from pybricks.hubs import EV3Brick
except ImportError:
    # Fallback para testes de desenvolvimento fora do bloco EV3 (ex: no PC)
    class SpeakerMock:
        def play_notes(self, notes, tempo=120):
            print("  [Speaker] Tempo: {} BPM | Total de notas/pausas: {}".format(tempo, len(notes)))

    class EV3Brick:
        def __init__(self):
            self.speaker = SpeakerMock()


# Lista de músicas: cada item contém título, tempo (BPM) e notas (tom e duração)
MUSICAS = [
    {
        "nome": "Neon Genesis Evangelion (A Cruel Angel's Thesis)",
        "tempo": 200,
        "notas": [
            "C3/3", "D#3/3", "F3/4", "D#3/4", "F3/5", "F3/3", "A#3/5", "G#3/5", "G3/6", "F3/6",
            "R4/8",
            "G3/2", "G3/3", "A#3/3", "C4/4", "F3/4", "D#3/5", "A#3/3",
            "R4/8",
            "G3/5", "A#3/5", "A#3/4", "C4/2",
        ],
    },
    {
        "nome": "Naruto Shippuden (Bluebird)",
        "tempo": 180,
        "notas": [
            "C#4/4", "F#4/4", "G#4/4", "A4/2", "G#4/2",
            "R4/8",
            "F#4/2", "C#4/3", "F#4/5",
            "R4/8",
            "G#4/4", "A4/2", "B4/3", "A4/4",
            "R4/8",
            "B4/3", "C#5/2", "C#4/4", "F#4/4", "G#4/5",
            "R4/8",
            "A4/2", "G#4/3", "F#4/3",
            "R4/4",
            "F#4/4", "C#5/4", "B4/3",
            "R4/8",
            "F#4/4", "C#5/4", "B4/3", "E4/3", "E4/3", "F#4/5",
            "R4/8",
            "F#4/1",
        ],
    },
    {
        "nome": "One Piece (We Are!)",
        "tempo": 192,
        "notas": [
            "A#4/6", "A#4/6", "D#5/2",
            "R4/4",
            "A#4/3", "D#5/6", "F5/1",
            "R4/8",
            "D#5/6", "F5/6", "G#5/4", "G5/2", "D#5/2", "G#4/6", "G#4/6",
            "R4/8",
            "A#4/6", "A#4/6", "A#4/6", "A#4/6", "D#5/6", "D#5/2", "A#4/3", "D#5/6", "F5/6",
            "R4/8",
            "F4/3", "G#4/3", "G4/3", "F4/6", "D#4/6", "F4/6", "D#4/6",
        ],
    },
]


def tocar_musica(ev3, musica):
    """Toca uma música selecionada no alto-falante do bloco EV3."""
    print("Playing: " + musica["nome"])
    ev3.speaker.play_notes(musica["notas"], tempo=musica["tempo"])


def main():
    ev3 = EV3Brick()
    musica = random.choice(MUSICAS)
    tocar_musica(ev3, musica)


if __name__ == "__main__":
    main()
