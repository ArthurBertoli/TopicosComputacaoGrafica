import cv2
import pygame
import numpy as np
import mediapipe as mp
import sys

print("\n=============================================")
print("=== INICIALIZANDO O MOTOR DO PULA-GERAÇÃO ===")
print("=============================================\n")

# 1. Configurações Iniciais
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("PulaGeração - Fase 2 (Modo Tutorial Clássico)")
relogio = pygame.time.Clock()

# 2. Inicialização do MediaPipe (Modo Clássico)
print("[INFO] Carregando o MediaPipe Pose...")
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_desenho = mp.solutions.drawing_utils

# 3. Inicialização da Câmera 
print("[INFO] Iniciando busca avançada pela câmera...")
cap = None

# Lista de tecnologias de captura (Automático, Media Foundation, DirectShow)
backends = [cv2.CAP_ANY, cv2.CAP_MSMF, cv2.CAP_DSHOW]

for backend in backends:
    if cap is not None: 
        break
    for indice in range(3): # Testa as portas 0, 1 e 2
        print(f"-> Testando câmera {indice} com a tecnologia {backend}...")
        cap_temp = cv2.VideoCapture(indice, backend)
        
        if cap_temp.isOpened():
            # Tenta ler um frame real para garantir que não é uma câmera "fantasma" ou travada
            sucesso, frame_teste = cap_temp.read()
            if sucesso:
                cap = cap_temp
                print(f"[SUCESSO] Câmera funcionando na porta {indice}!")
                break
            else:
                cap_temp.release()

if cap is None or not cap.isOpened():
    print("\n[ERRO FATAL] O Python não conseguiu roubar a imagem de nenhuma câmera.")
    print("Possíveis causas:")
    print("1. A câmera não está conectada.")
    print("2. Tem uma tampinha física de privacidade fechada na lente.")
    print("3. O antivírus (como Kaspersky) bloqueou o Python de usar a webcam.")
    print("4. Outro aplicativo já está com a câmera aberta.")
    sys.exit()

# 4. Loop Principal
print("[SUCESSO] Sistema pronto!")
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            rodando = False

    sucesso, frame = cap.read()
    if not sucesso: continue

    # Processamento visual
    frame = cv2.flip(frame, 1)                    
    frame = cv2.resize(frame, (LARGURA, ALTURA))  
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detecção do esqueleto
    resultados = pose.process(frame_rgb)
    if resultados.pose_landmarks:
        # pose_landmarker_lite
        mp_desenho.draw_landmarks(
            frame_rgb, 
            resultados.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

    # Renderização no Pygame
    frame_surface = pygame.surfarray.make_surface(np.rot90(frame_rgb))
    frame_surface = pygame.transform.flip(frame_surface, True, False)

    tela.blit(frame_surface, (0, 0))
    pygame.display.flip()
    relogio.tick(30)

# 5. Finalização Segura 
cap.release()
pygame.quit()
sys.exit()