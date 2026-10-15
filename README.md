*[Read this in English](README_EN.md)*

# LEGO EV3 Anime Music Player

Um tocador de músicas de animes clássicos para o robô LEGO Mindstorms EV3 desenvolvido em Python com a biblioteca **Pybricks** no sistema operacional **ev3dev**.

A cada execução, o robô escolhe aleatoriamente uma trilha sonora da lista de músicas e sintetiza a melodia no alto-falante interno do bloco EV3.

---

## Demonstração

![LEGO EV3 Anime Music Player](assets/robot_playing.gif)

> 🎥 **Vídeo com áudio:** Assista ao [vídeo gravado com áudio (MP4)](assets/robot_playing.mp4) sintetizado no robô.

---

## Músicas Inclusas

| Música | Anime | Andamento (BPM) | Formato das Notas |
| :--- | :--- | :---: | :--- |
| **A Cruel Angel's Thesis** | Neon Genesis Evangelion | 200 BPM | Tom/Oitava e fração de duração (ex: `C3/3`, `D#3/3`, `R4/8`) |
| **Bluebird** | Naruto Shippuden | 180 BPM | Tom/Oitava e fração de duração (ex: `C#4/4`, `F#4/4`, `A4/2`) |
| **We Are!** | One Piece | 192 BPM | Tom/Oitava e fração de duração (ex: `A#4/6`, `D#5/2`, `F5/1`) |

---

## Como Funciona

O script [`musicas.py`](musicas.py) organiza as músicas em uma estrutura de dados declarativa (`MUSICAS`), onde cada faixa possui:
* `nome`: Nome da faixa e anime.
* `tempo`: Andamento da música em batidas por minuto (BPM).
* `notas`: Lista de notas musicais e pausas no formato Pybricks (`[nota][oitava]/[duração]`).

A seleção é realizada de forma concisa via `random.choice(MUSICAS)`. Além disso, o script inclui fallback para testes no computador (PC/Mac/Linux) sem travar por falta da biblioteca de hardware do EV3.

---

## Pré-requisitos

* Bloco inteligente LEGO Mindstorms EV3.
* Cartão MicroSD com [ev3dev](https://www.ev3dev.org/) instalado.
* Ambiente com a biblioteca [Pybricks](https://pybricks.com/) (inclusa nas imagens ev3dev MicroPython).

---

## Como Executar

### No Bloco LEGO EV3 (ev3dev)

1. Conecte-se ao seu EV3 via SSH ou pela extensão **LEGO MINDSTORMS EV3 MicroPython** no VS Code.
2. Transfira o arquivo `musicas.py` para a pasta do projeto no robô.
3. Conceda permissão de execução (se executar via terminal):
   ```bash
   chmod +x musicas.py
   ```
4. Execute o script:
   ```bash
   ./musicas.py
   ```
   *Ou execute diretamente pelo menu "File Browser" na tela do EV3.*

### Teste Local no Computador (Modo Simulação)

Caso queira testar a lógica e o sorteio aleatório antes de enviar ao robô:
```bash
python3 musicas.py
```

---

## Licença

Distribuído sob a licença [MIT](LICENSE). Consulte o arquivo `LICENSE` para mais detalhes.
