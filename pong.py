import pygame

pygame
    #inicializar a biblioteca e configurar o tamanho da nossa tela
pygame.init()

    #configuração da janela
LARGURA_TELA = 800
ALTURA_TELA = 600

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong!")

    #cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

    #----- constantes do jogo -----
LARGURA_RAQUETE = 15
ALTURA_RAQUETE = 100
VELOCIDADE_RAQUETE = 15
TAMANHO_BOLA = 20
VELOCIDADE_BOLA_X = 7
VELOCIDADE_BOLA_Y = 7
    
    #----- classes do jogo -----
class Raquete:
    def _init_(self, x, y):
    # O 'rect' armazena a posição (x,y) e o tamanho
        self.rect = pygame.Rect(x, y, LARGURA_RAQUETE, ALTURA_RAQUETE)
    
    #metodo utilizado para desenhar a raquete
    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)
    
    
    #metodo para mover
    def mover(self, tecla_cima, tecla_baixo):
        #captura um dicionário de todas as teclas que estão pressionadas
        teclas = pygame.key.get_pressed()
        
        #verificar se a tecla foi pressionada
        if teclas[tecla_cima] and self.rect.top > 0:
             self.rect.y -= VELOCIDADE_RAQUETE 
        
        if teclas[tecla_baixo] and self.rect.bottom < ALTURA_TELA:
             self.rect.y += VELOCIDADE_RAQUETE


class Bola:
    def _init_(self, x, y):
        # A bola será um quadrado pequeno (pode ser substituído por um círculo depois)
        self.rect = pygame.Rect(x, y, TAMANHO_BOLA, TAMANHO_BOLA)
        self.vel_x = VELOCIDADE_BOLA_X
        self.vel_y = VELOCIDADE_BOLA_Y
    
    def desenhar(self, tela):
        pygame.draw.ellipse(tela, BRANCO, self.rect)
    
    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        #colisão com o topo e o fundo da tela
        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            self.vel_y = -self.vel_y
    
    def verificar_colisoes(self, raquete1, raquete2):
        #colisão com as raquetes
        if self.rect.colliderect(raquete1.rect) or self.rect.colliderect(raquete2.rect):
            self.vel_x = -self.vel_x

        #se a bola sair da tela (pontuação)
        if self.rect.left <= 0 or self.rect.right >= LARGURA_TELA:
            #reposiciona no centro
            self.rect.center = (LARGURA_TELA / 2, ALTURA_TELA / 2)
            self.vel_x = -self.vel_x
            self.vel_y = VELOCIDADE_BOLA_Y
        

#criando a raquete 01 a partir da classe raquete
#posição 10 pixels a esquerda, e centralizada na altura
raquete1 = Raquete((10, ALTURA_TELA / 2 - ALTURA_RAQUETE / 2))

#criando a raquete 02 a partir da classe raquete
#posição 10 pixels a direita, e centralizada na altura
raquete2 = Raquete(LARGURA_TELA - LARGURA_RAQUETE - 10, ALTURA_TELA / 2 - ALTURA_RAQUETE / 2)

#criando a bola no centro
bola = Bola(LARGURA_TELA / 2 - TAMANHO_BOLA / 2, ALTURA_TELA / 2 - TAMANHO_BOLA / 2)
               

    #criar fluxo principal

relogio = pygame.time.Clock()
rodando = True

while rodando:
    #----- 1. eventos -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            
    #------- 2. movendo as raquetes e a bola -------
    raquete1.mover(pygame.K_w, pygame.K_s)
    raquete2.mover(pygame.K_UP, pygame.K_DOWN)
    bola.mover()
    bola.verificar_colisoes(raquete1, raquete2)
            
    #----- 3. tela -----
    #criação da tela (preto)
    tela.fill(PRETO)
    
    #----- 3.1 desenhar raquetes e bola -----
    raquete1.desenhar(tela)
    raquete2.desenhar(tela)
    bola.desenhar(tela)
    
    #----- 4. atualização da tela -----
    pygame.display.flip()
    relogio.tick(60)
    
pygame.quit()