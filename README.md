*[Read this in English](README_EN.md)*

# LEGO EV3 Anime Music Player

Um script em Python para o LEGO Mindstorms EV3 que toca aleatoriamente temas clássicos de animes utilizando o speaker do robô. 

Este projeto foi desenvolvido para rodar no sistema operacional **ev3dev** utilizando a biblioteca **Pybricks**.

## Músicas Inclusas
Sempre que o script é executado, o EV3 sorteia e toca uma das seguintes músicas:
1. **Neon Genesis Evangelion** (A Cruel Angel's Thesis)
2. **Naruto Shippuden** (Bluebird)
3. **One Piece** (We Are!)

## Pré-requisitos
* Um bloco LEGO Mindstorms EV3.
* Cartão SD com o [ev3dev](https://www.ev3dev.org/) instalado.
* Ambiente configurado com a biblioteca `pybricks`.

## Como executar
1. Conecte-se ao seu EV3 via SSH ou utilize a extensão do EV3 no VS Code.
2. Transfira o arquivo `musicas.py` para o seu robô.
3. Dê permissão de execução ao arquivo (caso execute via terminal):
   ```bash
   chmod +x musicas.py
