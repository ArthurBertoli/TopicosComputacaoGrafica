import pygame
import sys

print("\n=============================================")
print("=== PULA-GERAÇÃO: TABULEIRO OFICIAL (GDD) ===")
print("=============================================\n")

# --- 1. Configurações Iniciais ---
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("PulaGeração - Tabuleiro Oficial")
relogio = pygame.time.Clock()

# --- 2. Definição do Tabuleiro Baseado no Slide 6 ---
TAM = 80 
X_ESQ, X_CENTRO, X_DIR = 280, 360, 440

# Lista com a ordem exata que o jogador deve pular
ordem_jogo = ["1", "Saber", "3", "4", "5", "6", "Desafio", "8", "Bônus", "Coroa"]

# Dicionário do mapa: pygame.Rect(X, Y, Largura, Altura)
quadrados = {
    "1": pygame.Rect(X_CENTRO, 500, TAM, TAM),
    "Saber": pygame.Rect(X_ESQ, 420, TAM, TAM),
    "3": pygame.Rect(X_DIR, 420, TAM, TAM),
    "4": pygame.Rect(X_CENTRO, 340, TAM, TAM),
    "5": pygame.Rect(X_ESQ, 260, TAM, TAM),
    "6": pygame.Rect(X_DIR, 260, TAM, TAM),
    "Desafio": pygame.Rect(X_ESQ, 180, TAM * 3, TAM), # Retângulo largo vermelho
    "8": pygame.Rect(X_ESQ, 100, TAM, TAM),
    "Bônus": pygame.Rect(X_DIR, 100, TAM, TAM),
    "Coroa": pygame.Rect(X_ESQ, 20, TAM * 3, TAM)     # Retângulo largo amarelo
}

# Paleta de Cores do Documento
CORES = {
    "fundo": (240, 240, 240),     # Cinza bem clarinho (cor do slide)
    "normal": (255, 228, 196),    # Laranja clarinho (1, 3, 4, 5, 6, 8)
    "saber_bonus": (30, 144, 255),# Azul (Saber, Bônus)
    "desafio": (220, 20, 60),     # Vermelho (Desafio)
    "coroa": (255, 215, 0),       # Amarelo (Coroa)
    "colisao": (50, 205, 50),     # Verde (Quando pisa)
    "texto": (0, 0, 0)
}

fonte = pygame.font.SysFont(None, 45)

# --- 3. Loop Principal ---
indice_alvo = 0 # Começa no índice 0 (que é a casa "1")
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            rodando = False

    tela.fill(CORES["fundo"])
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Descobre qual é a casa que o jogador precisa pisar agora
    if indice_alvo < len(ordem_jogo):
        casa_alvo = ordem_jogo[indice_alvo]
    else:
        casa_alvo = "FIM"

    # --- 4. Renderização e Lógica ---
    for nome_casa, retangulo in quadrados.items():
        pisou = retangulo.collidepoint(mouse_x, mouse_y)
        
        # Lógica de Progressão
        if pisou and nome_casa == casa_alvo:
            print(f"Pisou no {nome_casa}! Avançando...")
            indice_alvo += 1
            if indice_alvo >= len(ordem_jogo):
                print("🏆 RODADA CONCLUÍDA! 🏆")
                indice_alvo = 0 # Reinicia para testar de novo
                
        # Define a cor base da casa conforme o seu tipo no GDD
        if nome_casa in ["Saber", "Bônus"]:
            cor_base = CORES["saber_bonus"]
        elif nome_casa == "Desafio":
            cor_base = CORES["desafio"]
        elif nome_casa == "Coroa":
            cor_base = CORES["coroa"]
        else:
            cor_base = CORES["normal"]

        # Efeito visual de pisar (fica verde temporariamente)
        cor_atual = CORES["colisao"] if pisou else cor_base
            
        # Desenha o quadrado e a borda
        pygame.draw.rect(tela, cor_atual, retangulo)
        pygame.draw.rect(tela, CORES["texto"], retangulo, 2, border_radius=10) # Bordas arredondadas!
        
        # Renderiza o texto
        texto = fonte.render(nome_casa, True, CORES["texto"])
        texto_rect = texto.get_rect(center=retangulo.center)
        tela.blit(texto, texto_rect)

    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
sys.exit()