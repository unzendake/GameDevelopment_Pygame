import pygame
import random

pygame.init()

#configuração da janela do jogo
LARGURA_TELA = 1480
ALTURA_TELA = 800
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Acerte o Alvo")

#configuração das cores rgb
PRETO =(0,0,0)
BRANCO =(255,255,255)
VERMELHO =(255,0,0)

#fluxo principlal base
relogio = pygame.time.Clock()
rodando = True

TAMANHO_ALVO = 50
alvo_rect = pygame.Rect(275, 155, TAMANHO_ALVO, TAMANHO_ALVO) # (x e y , largura e altura)

#configuração da fonte de exibição
pontos = 0
fonte = pygame.font.SysFont("bahnschrift", 35)

while rodando:
    #capturar um evento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando =False

            #verifica se o evento foi um click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            #event.pos vai ser a cordenada do x,y do mouse
            #collidepoint verifica se o ponto está dentro do rect
            if alvo_rect.collidepoint(event.pos):
                
                alvo_rect.x = random.randrange(0, LARGURA_TELA - TAMANHO_ALVO)

                alvo_rect.y = random.randrange(0, ALTURA_TELA - TAMANHO_ALVO)

                pontos += 1

    #etapa 2 criação da logica


    #etapa 3 desenho da tela
    tela.fill(PRETO)

    #novo
    pygame.draw.rect(tela, VERMELHO, alvo_rect)

    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (10,10))
 
    #4 atualizações de tela
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()


