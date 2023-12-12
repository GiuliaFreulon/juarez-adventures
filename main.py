import pygame
from pygame.locals import *
from pygame import mixer
import pickle
from os import path

#Inicia o mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

#Inicia o pygame
pygame.init()

clock = pygame.time.Clock()


#Variáveis
fps = 60

largura_tela = 800
altura_tela = 600

largura_player = 40
altura_player = 30

tamanho_bloco = 30

game_over = 0

menu = True

level = 1

offset = [0,0]



#Cria a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))



#Imagens
icone = pygame.image.load('imagens/icone.png')

titulo = pygame.image.load('imagens/titulo.png')
titulo = pygame.transform.scale(titulo, (600, 50))

mouse = pygame.image.load('imagens/mouse.png')
mouse = pygame.transform.scale(mouse, (20, 24))

balao = pygame.image.load('imagens/balao.png')
balao = pygame.transform.scale(balao, (800, 130))
balao1 = pygame.image.load('imagens/balao1.png')

controles = pygame.image.load('imagens/controles.png')
controles = pygame.transform.scale(controles, (200, 140))

historia = pygame.image.load('imagens/historinha.png')
historia = pygame.transform.scale(historia, (500, 300))

mapaFundo = pygame.image.load('imagens/fundo.png')
mapaFundo = pygame.transform.scale(mapaFundo, (810, 610))

inimigoImg = pygame.image.load('imagens/inimigo.png')
inimigoImg = pygame.transform.scale(inimigoImg, (18, 18))

espinhoImg = pygame.image.load('imagens/espinho.png')
espinhoImg = pygame.transform.scale(espinhoImg, (tamanho_bloco, tamanho_bloco))

player_morto = pygame.image.load('imagens/andar0.png')
player_morto = pygame.transform.flip(player_morto, False, True)
player_morto = pygame.transform.scale(player_morto, (largura_player, altura_player))

iniciarImg = pygame.image.load('imagens/iniciar.png')
iniciarImg = pygame.transform.scale(iniciarImg, (220, 120))

reiniciarImg = pygame.image.load('imagens/reiniciar.png')
reiniciarImg = pygame.transform.scale(reiniciarImg, (285, 90))

fecharImg = pygame.image.load('imagens/fechar.png')
fecharImg = pygame.transform.scale(fecharImg, (230, 130))

grama = pygame.image.load('imagens/grama.png')
grama = pygame.transform.scale(grama, (tamanho_bloco, tamanho_bloco))

terra = pygame.image.load('imagens/terra.png')
terra = pygame.transform.scale(terra, (tamanho_bloco, tamanho_bloco))

portaImg = pygame.image.load('imagens/porta.png')
portaImg = pygame.transform.scale(portaImg, (tamanho_bloco, tamanho_bloco))

porta_topo = pygame.image.load('imagens/porta_topo.png')
porta_topo = pygame.transform.scale(porta_topo, (tamanho_bloco, tamanho_bloco))

grama_cima_baixo = pygame.image.load('imagens/grama_cima_baixo.png')
grama_cima_baixo = pygame.transform.scale(grama_cima_baixo, (tamanho_bloco, tamanho_bloco))

grama_esquerda = pygame.image.load('imagens/grama_esquerda.png')
grama_esquerda = pygame.transform.scale(grama_esquerda, (tamanho_bloco, tamanho_bloco))

grama_direita = pygame.image.load('imagens/grama_direita.png')
grama_direita = pygame.transform.scale(grama_direita, (tamanho_bloco, tamanho_bloco))

grama_direita_baixo = pygame.image.load('imagens/grama_direita_baixo.png')
grama_direita_baixo = pygame.transform.scale(grama_direita_baixo, (tamanho_bloco, tamanho_bloco))

grama_esquerda_baixo = pygame.image.load('imagens/grama_esquerda_baixo.png')
grama_esquerda_baixo = pygame.transform.scale(grama_esquerda_baixo, (tamanho_bloco, tamanho_bloco))

terra_baixo = pygame.image.load('imagens/terra_baixo.png')
terra_baixo = pygame.transform.scale(terra_baixo, (tamanho_bloco, tamanho_bloco))

terra_esquerda = pygame.image.load('imagens/terra_esquerda.png')
terra_esquerda = pygame.transform.scale(terra_esquerda, (tamanho_bloco, tamanho_bloco))

terra_direita = pygame.image.load('imagens/terra_direita.png')
terra_direita = pygame.transform.scale(terra_direita, (tamanho_bloco, tamanho_bloco))

terra_canto_esquerdo = pygame.image.load('imagens/terra_canto_esquerdo.png')
terra_canto_esquerdo = pygame.transform.scale(terra_canto_esquerdo, (tamanho_bloco, tamanho_bloco))

terra_canto_direito = pygame.image.load('imagens/terra_canto_direito.png')
terra_canto_direito = pygame.transform.scale(terra_canto_direito, (tamanho_bloco, tamanho_bloco))

nuvem_meio = pygame.image.load('imagens/nuvem_meio.png')
nuvem_meio = pygame.transform.scale(nuvem_meio, (tamanho_bloco, tamanho_bloco))

nuvem_esquerda = pygame.image.load('imagens/nuvem_esquerda.png')
nuvem_esquerda = pygame.transform.scale(nuvem_esquerda, (tamanho_bloco, tamanho_bloco))

nuvem_direita = pygame.image.load('imagens/nuvem_direita.png')
nuvem_direita = pygame.transform.scale(nuvem_direita, (tamanho_bloco, tamanho_bloco))

cogumelo_meio = pygame.image.load('imagens/cogumelo_meio.png')
cogumelo_meio = pygame.transform.scale(cogumelo_meio, (tamanho_bloco, tamanho_bloco))

cogumelo_esquerda = pygame.image.load('imagens/cogumelo_esquerda.png')
cogumelo_esquerda = pygame.transform.scale(cogumelo_esquerda, (tamanho_bloco, tamanho_bloco))

cogumelo_direita = pygame.image.load('imagens/cogumelo_direita.png')
cogumelo_direita = pygame.transform.scale(cogumelo_direita, (tamanho_bloco, tamanho_bloco))

plataforma = pygame.image.load('imagens/plataforma.png')
plataforma = pygame.transform.scale(plataforma, (tamanho_bloco, tamanho_bloco))

caule = pygame.image.load('imagens/caule.png')
caule = pygame.transform.scale(caule, (tamanho_bloco, tamanho_bloco))

grama_coberta = pygame.image.load('imagens/grama_coberta.png')
grama_coberta = pygame.transform.scale(grama_coberta, (tamanho_bloco, tamanho_bloco))

terra_direita_esquerda = pygame.image.load('imagens/terra_direita_esquerda.png')
terra_direita_esquerda = pygame.transform.scale(terra_direita_esquerda, (tamanho_bloco, tamanho_bloco))


#Sons
pygame.mixer.music.load('sons/musica.mp3')
pygame.mixer.music.play(-1, 0.0, 5000)
pygame.mixer.music.set_volume(0.4)

morre_som = pygame.mixer.Sound('sons/morrer.wav')
morre_som.set_volume(0.2)

pular_som = pygame.mixer.Sound('sons/pular.wav')
pular_som.set_volume(0.3)

passar_level = pygame.mixer.Sound('sons/passar_level.wav')
passar_level.set_volume(0.2)





#Fonte
fonte = pygame.font.Font('bits.ttf', 70)
borda = pygame.font.Font('bits.ttf', 70)



#Título e ícone
pygame.display.set_caption('JUAREZ ADVENTURES')
pygame.display.set_icon(icone)



    #Classes e Funções
def desenhar_texto(texto, fonte, cor, x, y):
    imagem = fonte.render(texto, True, cor)
    tela.blit(imagem, (x,y))



def resetar_level(level):
    player.resetar(100, altura_tela - (largura_player + tamanho_bloco))
    inimigo_grupo.empty()
    espinho_grupo.empty()
    porta_grupo.empty()

    # Abrir levels
    if path.exists(f'level{level}.pkl'):
        with open(f'level{level}.pkl', 'rb') as f:
            mapa_matriz = pickle.load(f)
    mapa = Mapa(mapa_matriz)

    return mapa



class Botao():
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.retangulo = self.imagem.get_rect()
        self.retangulo.x = x
        self.retangulo.y = y
        self.click = False

    def desenhar(self):
        acao = False
        posicao = pygame.mouse.get_pos()

        if self.retangulo.collidepoint(posicao):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                acao = True
                self.click = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False

        tela.blit(self.imagem, self.retangulo)

        return acao



class Player():
    def __init__(self, x, y):
       self.resetar(x, y)

    def atualizar(self, game_over):
        #Desenha o player na tela
        tela.blit(self.imagem, self.rect)


        dx = 0
        dy = 0
        resistencia_andar = 7

        if game_over == 0:

            # Movimentação
            aperta = pygame.key.get_pressed()
            if aperta[pygame.K_SPACE] and self.pular == False and self.no_ar == False:
                self.vel_y = -9
                self.pular = True
                pular_som.play()
            if aperta[pygame.K_SPACE] == False:
                self.pular = False
            if aperta[pygame.K_a]:
                dx -= 2
                self.contador += 1
                self.direcao = -1
            if aperta[pygame.K_d]:
                dx += 2
                self.contador += 1
                self.direcao = 1
            if aperta[pygame.K_a] == False and aperta[pygame.K_d] == False:
                self.contador = 0
                self.index = 0
                if self.direcao == 1:
                    self.imagem = self.andar_direita[self.index]
                if self.direcao == -1:
                    self.imagem = self.andar_esquerda[self.index]

            self.vel_y += 0.5
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y


            #Animação
            if self.contador > resistencia_andar:
                self.contador = 0
                self.index += 1
                if self.index >= len(self.andar_direita):
                    self.index = 0
                if self.direcao == 1:
                    self.imagem = self.andar_direita[self.index]
                if self.direcao == -1:
                    self.imagem = self.andar_esquerda[self.index]


            #Colisão
            self.no_ar = True
            for bloco in mapa.lista_blocos:
                if bloco[1].colliderect(self.rect.x + dx, self.rect.y, self.largura, self.altura):
                    dx = 0
                if bloco[1].colliderect(self.rect.x, self.rect.y + dy, self.largura, self.altura):
                    if self.vel_y < 0:
                        dy = bloco[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = bloco[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.no_ar = False


            #Colisão com inimigos
            if pygame.sprite.spritecollide(self, inimigo_grupo, False):
                game_over = -1
                morre_som.play()
            if pygame.sprite.spritecollide(self, espinho_grupo, False):
                game_over = -1
                morre_som.play()


            #Colisão com porta
            if pygame.sprite.spritecollide(self, porta_grupo, False):
                game_over = 1
                passar_level.play()


            #Coordenadas do player
            self.rect.x += dx
            self.rect.y += dy

            #Limites verticais e horizontais
            if self.rect.bottom > altura_tela:
                self.rect.bottom = altura_tela
                dy = 0
            if self.rect.left <= 0:
                self.rect.left = 0
                dx = 0
            elif self.rect.right >= largura_tela:
                self.rect.right = largura_tela
                dx = 0


        elif game_over == -1:
            self.imagem = self.morto

        return game_over



    def resetar(self, x, y):
        self.andar_direita = []
        self.andar_esquerda = []
        self.index = 0
        self.contador = 0
        for num in range(0, 5):
            img_direita = pygame.image.load(f'imagens/andar{num}.png')
            img_direita = pygame.transform.scale(img_direita, (largura_player, altura_player))
            img_direita = pygame.transform.flip(img_direita, True, False)
            img_esquerda = pygame.transform.flip(img_direita, True, False)
            self.andar_direita.append(img_direita)
            self.andar_esquerda.append(img_esquerda)
        self.morto = player_morto
        self.imagem = self.andar_direita[self.index]
        self.rect = self.imagem.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.largura = self.imagem.get_width()
        self.altura = self.imagem.get_height()
        self.vel_y = 0
        self.pular = False
        self.direcao = 0
        self.no_ar = True


#Definições
inimigo_grupo = pygame.sprite.Group()
espinho_grupo = pygame.sprite.Group()
porta_grupo = pygame.sprite.Group()



class Mapa():
    #Cria o mapa
    def __init__(self, matriz):
        self.lista_blocos = []

        contador_linhas = 0
        for linha in matriz:
            contador_colunas = 0
            for bloco in linha:
                if bloco == 1:
                    inimigo = Inimigo(contador_colunas*tamanho_bloco, contador_linhas*tamanho_bloco + 14)
                    inimigo_grupo.add(inimigo)
                if bloco == 2:
                    espinho = Espinhos(contador_colunas*tamanho_bloco, contador_linhas*tamanho_bloco)
                    espinho_grupo.add(espinho)
                if bloco == 3:
                    porta = Porta(contador_colunas*tamanho_bloco, contador_linhas*tamanho_bloco)
                    porta_grupo.add(porta)
                if bloco == 4:
                    imagem = terra
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 5:
                    imagem = grama
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 6:
                    imagem = grama_esquerda
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 7:
                    imagem = grama_direita
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 8:
                    imagem = porta_topo
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 9:
                    imagem = plataforma
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 10:
                    imagem = grama_cima_baixo
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 11:
                    imagem = grama_esquerda_baixo
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 12:
                    imagem = grama_direita_baixo
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 13:
                    imagem = terra_baixo
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 14:
                    imagem = terra_esquerda
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 15:
                    imagem = terra_direita
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 16:
                    imagem = terra_canto_esquerdo
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 17:
                    imagem = terra_canto_direito
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 18:
                    imagem = terra_canto_esquerdo
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 19:
                    imagem = terra_canto_direito
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 20:
                    imagem = nuvem_meio
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 21:
                    imagem = nuvem_esquerda
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 22:
                    imagem = nuvem_direita
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 23:
                    imagem = cogumelo_meio
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 24:
                    imagem = cogumelo_esquerda
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 25:
                    imagem = cogumelo_direita
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 26:
                    imagem = caule
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 27:
                    imagem = grama_coberta
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)
                if bloco == 28:
                    imagem = terra_direita_esquerda
                    imagem_retangulo = imagem.get_rect()
                    imagem_retangulo.x = contador_colunas * tamanho_bloco
                    imagem_retangulo.y = contador_linhas * tamanho_bloco
                    bloco = (imagem, imagem_retangulo)
                    self.lista_blocos.append(bloco)


                contador_colunas += 1
            contador_linhas += 1

    #DesenharNaTela
    def desenhar(self):
        for bloco in self.lista_blocos:
            tela.blit(bloco[0], bloco[1])



class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = inimigoImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direcao = 1
        self.contador_movimento = 0

    def update(self):
        self.rect.x += self.direcao
        self.contador_movimento += 1
        if abs(self.contador_movimento) > 50:
            self.direcao *= -1
            self.contador_movimento *= -1



class Espinhos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = espinhoImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direcao = 1
        self.contador_movimento = 0



class Porta(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = portaImg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direcao = 1
        self.contador_movimento = 0



#Definições
player = Player(50, altura_tela - (largura_player + tamanho_bloco))



#Abrir levels
if path.exists(f'level{level}.pkl'):
    with open(f'level{level}.pkl', 'rb') as f:
        mapa_matriz = pickle.load(f)
mapa = Mapa(mapa_matriz)



#Botões
reiniciar = Botao(largura_tela // 2 - 150, altura_tela // 2 + 50, reiniciarImg)
iniciar = Botao(largura_tela // 2 - 300, altura_tela // 2 + 130, iniciarImg)
fechar = Botao(largura_tela // 2 + 80, altura_tela // 2 + 120, fecharImg)



'''Loop do jogo'''
running = True
while running:
    clock = fps

    tela.fill((255, 255, 255))
    tela.blit(mapaFundo, (0, 0))


    if menu == True:
        tela.blit(controles, (550, 180))
        tela.blit(historia, (10, 100))
        tela.blit(titulo, (100, 20))
        if fechar.desenhar():
            running = False
        if iniciar.desenhar():
            menu = False
    else:
        #Chamando funções
        mapa.desenhar()

            #continua igual
        if game_over == 0:
            inimigo_grupo.update()

        inimigo_grupo.draw(tela)
        espinho_grupo.draw(tela)
        porta_grupo.draw(tela)

        game_over = player.atualizar(game_over)

            #morre
        if game_over == -1:
            tela.blit(balao, ((largura_tela // 2) - 409, altura_tela // 2 - 90))
            desenhar_texto('Oh não! Juarez foi derrotado :(', fonte, (50, 49, 49), (largura_tela // 2) - 330, altura_tela // 2 - 60)
            if reiniciar.desenhar():
                mapa_matriz = []
                mapa = resetar_level(level)
                game_over = 0

            #passa de level
        if game_over == 1:
            level += 1
            if level <= 3:
                mapa_matriz = []
                mapa = resetar_level(level)
                game_over = 0

            #recomeça o jogo
            else:
                tela.blit(balao1, ((largura_tela // 2) - 280, altura_tela // 2 - 280))


                if reiniciar.desenhar():
                    level = 1
                    mapa_matriz = []
                    mapa = resetar_level(level)
                    game_over = 0


    #Fecha a tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse personalizado
    pygame.mouse.set_visible(False)
    mx, my = pygame.mouse.get_pos()
    loc = [mx, my]
    rot = 0
    tela.blit(pygame.transform.rotate(mouse, rot), (loc[0] + offset[0], loc[1] + offset[1]))

    #Atualiza a tela
    pygame.display.update()

    '''
    Finalmente terminei senhor oh glória! 
    Sim, a última fase é muito difícil, mas é possível, eu consegui passar uma vez
    '''