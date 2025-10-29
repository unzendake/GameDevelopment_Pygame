import pygame
import random

#inicializar a biblioteca e configurar o tamanho da nossa tela
pygame.init()

#configuração da janela
LARGURA_TELA = 800
ALTURA_TELA = 600

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("pong moments")

#cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

fonte_pontos = pygame.font.SysFont(None, 74)

PONTOS_J1 = 0
PONTOS_J2 = 0

#constantes do jogo
LARGURA_RAQUETE = 15
ALTURA_RAQUETE = 100
VELOCIDADE_RAQUETE = 7


RAIO_BOLA = 10
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_y = 5

#classes do jogo
class Bola:
    def _init_(self, x, y):
        self.rect = pygame.Rect(x - RAIO_BOLA, y - RAIO_BOLA, RAIO_BOLA * 2, RAIO_BOLA * 2)

        #velocidades/direção para x e y
        self.vel_x = VELOCIDADE_BOLA_X * random.choice((2, -1))
        self.vel_y = VELOCIDADE_BOLA_y * random.choice((2, -1))

    def desenhar(self, tela):
        pygame.draw.ellipse(tela, BRANCO, self.rect) #desenhado um circulo
    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    
    def verificar_colisao(self, raquete1, raquete2):
        global PONTOS_J1, PONTOS_J2
        #verificação da colisao das paredes
        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            self.vel_y *= -1 #inverter a direção Y

        
        #colisao com as raquetes
        if self.rect.colliderect(raquete1) or self.rect.colliderect(raquete2):
            self.vel_x *= -1 #inverter a direção X


        if minha_bola.rect.left < 0:
            minha_bola.resetar()
            PONTOS_J2 += 1

        if minha_bola.rect.right > 800:
            minha_bola.resetar()
            PONTOS_J1 += 1
        

    def resetar(self):
        #mover a bola de volta para o centro
        self.rect.x = LARGURA_TELA / 2 - RAIO_BOLA
        self.rect_y = ALTURA_TELA / 2 - RAIO_BOLA

        self.vel_x *= -1
        self.vel_y = VELOCIDADE_BOLA_y * random.choice((1, -1))

        pygame.time.delay(500)

class Raquete:
    # o construtor é chamado quando criamos uma raquete
    # 'self' se refere ao proprio objeto
    def _init_(self, x, y):
        # o 'rect' armazena a posição (x, y) e o tamanho
        self.rect = pygame.Rect(x, y, LARGURA_RAQUETE, ALTURA_RAQUETE)

    #metodo utilizado para desenhar a raquete
    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)
        
    def mover(self, tecla_cima, tecla_baixo):
        #captura o dicionario de todoas as teclas que tiveram pressionadas
        teclas = pygame.key.get_pressed()

        #verificar se a tecla foi pressionada
        if teclas[tecla_cima] and self.rect.top > 0:
            self.rect.y -= VELOCIDADE_RAQUETE

        if teclas[tecla_baixo] and self.rect.bottom < ALTURA_TELA:
            self.rect.y += VELOCIDADE_RAQUETE
#criando q raquete 1
#posição: 10 pixels a esquerda. centralizada na altura
raquete1 = Raquete(10, ALTURA_TELA / 2 - ALTURA_RAQUETE /2)
raquete2 = Raquete(775, ALTURA_TELA / 2 - ALTURA_RAQUETE /2)

minha_bola = Bola(LARGURA_TELA / 2, ALTURA_TELA / 2)



#criar o fluxo principal
relogio = pygame.time.Clock()
rodando = True

#1 - eventos
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    #2 - tela
    tela.fill(PRETO)

    #criando a raquete1
    raquete1.desenhar(tela)
    raquete2.desenhar(tela)
    minha_bola.desenhar(tela)

    texto_j1 = fonte_pontos.render(str(PONTOS_J1), True, BRANCO)
    tela.blit(texto_j1, (LARGURA_TELA / 4, 20))

        
    texto_j2 = fonte_pontos.render(str(PONTOS_J2), True, BRANCO)
    tela.blit(texto_j2, (LARGURA_TELA * 3/4 - texto_j2.get_width(), 20))

    #3 - atualização da tela
    pygame.display.flip()
    relogio.tick(60)

    #4 MOVENDO RAQUETE
    raquete1.mover(pygame.K_w, pygame.K_s)
    raquete2.mover(pygame.K_UP, pygame.K_DOWN)
    minha_bola.mover()

           
    #verificar colisoes
    minha_bola.verificar_colisao(raquete1.rect, raquete2.rect)

    

pygame.quit()
