# PulaGeração

> Projeto da disciplina **Tópicos Especiais em Computação Gráfica** — Ciência da Computação, UDESC.

## Sobre

O PulaGeração é a proposta de um *exergame* (jogo sério com atividade física) de chão projetado que reinventa a amarelinha tradicional. Segundo o documento de conceito, o público é formado por crianças de 5 a 10 anos e idosos com 65 anos ou mais, jogando sozinhos, em dupla (idoso + jovem) ou em equipes 2×2. Os objetivos são estimular saltos, equilíbrio e coordenação, aproximar as gerações, exercitar memória e atenção e apresentar tecnologia de forma lúdica aos idosos.

Este repositório contém protótipos iniciais em Python: a captura do corpo pela câmera e a lógica do tabuleiro.

## Funcionalidades

**`main.py` — rastreamento do corpo pela câmera**
- Procura uma câmera funcional testando as portas 0, 1 e 2 com diferentes *backends* do OpenCV (automático, Media Foundation e DirectShow), e mostra possíveis causas caso nenhuma funcione.
- Detecta o esqueleto do jogador com MediaPipe Pose e desenha os pontos e as conexões sobre a imagem espelhada da câmera, exibida em uma janela Pygame de 800×600.
- Fecha com `Esc` ou fechando a janela.

**`simulacao.py` — tabuleiro**
- Desenha o tabuleiro de 10 casas: casas normais, **Saber**, **Desafio**, **Bônus** e **Coroa**, cada tipo com sua cor.
- O cursor do mouse representa o pé do jogador: a casa sob o cursor fica verde e, se for a próxima da sequência, o jogo avança.
- Ao chegar à Coroa, informa no terminal que a rodada foi concluída e reinicia a sequência.
- Fecha com `Esc` ou fechando a janela.

## Tecnologias

Python, Pygame, OpenCV, MediaPipe, NumPy, Aseprite (artes).

## Estrutura

| Arquivo | Descrição |
|---|---|
| `main.py` | Protótipo de captura da câmera e detecção de pose. |
| `simulacao.py` | Protótipo do tabuleiro controlado pelo mouse. |
| `requirements.txt` | Dependências com versões fixas (MediaPipe com `mp.solutions`). |
| `pose_landmarker_lite.task` | Modelo do MediaPipe Pose Landmarker. Está incluído no projeto, mas a versão atual de `main.py` usa a API clássica `mp.solutions.pose` e não carrega este arquivo. |
| `TelaInicial`, `Fase1`, `Fase2` (`.aseprite` / `.png`) | Artes da tela inicial e das fases. Ainda não são carregadas pelo código. |
| `PulaGeração (1).pdf` | Apresentação do conceito do jogo (visão geral, objetivos, mecânicas MDA, tabuleiro e modos). |

## Como executar

Use Python 3.11 ou 3.12.

```bash
pip install -r requirements.txt
python main.py        # câmera + detecção de pose (requer webcam)
python simulacao.py   # tabuleiro controlado pelo mouse
```

`main.py` usa a API clássica `mp.solutions`, que foi removida das versões mais novas do MediaPipe; por isso o `requirements.txt` fixa o `mediapipe==0.10.21`, que ainda a inclui. O MediaPipe já instala o `opencv-contrib-python`; não instale também o `opencv-python`.

## Autores

- Arthur Bertoli
- Monique
- Mateus Unulino dos Passos (autor indicado no documento de conceito)

Professor: Marcelo da Silva Hounsell.
