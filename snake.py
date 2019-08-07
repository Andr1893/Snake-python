import pygame, random 


class snake:

    def __init__(self):
        # Direçoes de cobra sentido horario
        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3
        self.my_direction = self.LEFT # direção inicial cobra

        # Inicialização 
        pygame.init() # inicia pygame   
        self.screen = pygame.display.set_mode((600, 600)) # tamanho tela
        pygame.display.set_caption('Snake') # nome jogo


        #renicia as variaveis do jogo
        self.restartGame()

        self.clock = pygame.time.Clock() # clock jogo = FPS
        self.font = pygame.font.Font('freesansbold.ttf', 18) # tamanho e tipo letra 
        self.score = 0 # resultado jogo
        self.fps = 30 # fps velocidade do jogo
        

    
    def restartGame(self):
          # criar cobra inicial
        self.snake = [(200, 200), (210, 200), (220,200)] # tamanho da cobra inicial tamanho = 3 quadros
        # criar skin da cobra
        self.snake_skin = pygame.Surface((10,10)) # cada quadrado cobra = 5*5 pixel
        self.snake_skin.fill((255,255,255)) # cor inicinial = branco (rgb)

        # criar maçã inicial
        self.apple_pos = self.onGridRandom() # posição da maçã randomica
        # criar skin da maça
        self.apple_skin = pygame.Surface((10,10))# cada quadrado maça = 5*5 pixel
        self.apple_skin.fill((255,0,0)) # cor inicinial = vermelho (rgb)
        self.game_over = False # se jogo acabou
        self.score = 0
   


    # criar posição randomica da maçã
    def onGridRandom(self): 
        x = random.randint(0,59)
        y = random.randint(0,59)
        return (x * 10, y * 10)

    # se cobra colidir com maçã
    def collision(self):
         return (self.snake[0][0] == self.apple_pos[0]) and (self.snake[0][1] == self.apple_pos[1])
    
    # se cobra colidir com as paredes
    def snakeCollidedWithBoundaries(self):
        if self.snake[0][0] == 600 or self.snake[0][1] == 600 or self.snake[0][0] < 0 or self.snake[0][1] < 0: # se sim 
            # game over jogo acaba
            self.game_over = True 
            return True
        # se não jogo continua
        return False 
    
    # se cora bater nela mesma
    def snakeHasHitItself(self):
        for i in range(1, len(self.snake) - 1):
            if self.snake[0][0] == self.snake[i][0] and self.snake[0][1] == self.snake[i][1]:# se sim
                 # game over jogo acaba
                self.game_over = True
                return True
         # se não jogo continua
        return False

    # seleciona direção que cobra se move
    def insertSnakeMove(self):
        if self.my_direction == self.UP: # cima
            self.snake[0] = (self.snake[0][0], self.snake[0][1] - 10)
        if self.my_direction == self.DOWN: # baixo
            self.snake[0] = (self.snake[0][0], self.snake[0][1] + 10)
        if self.my_direction == self.RIGHT: # direita
            self.snake[0] = (self.snake[0][0] + 10, self.snake[0][1])
        if self.my_direction == self.LEFT: # esquerda
            self.snake[0] = (self.snake[0][0] - 10, self.snake[0][1])

    # jogador seleciona direção que cobra se move
    def selectDirection(self):
        for event in pygame.event.get(): # todos os eventos da tela
            if event.type == pygame.QUIT: # se o jogador sair
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN: # se jogador carregar numa teclas
                if event.key == pygame.K_UP and self.my_direction != self.DOWN:
                    self.my_direction = self.UP
                if event.key == pygame.K_DOWN and self.my_direction != self.UP: 
                    self.my_direction = self.DOWN
                if event.key == pygame.K_LEFT and self.my_direction != self.RIGHT:
                    self.my_direction = self.LEFT
                if event.key == pygame.K_RIGHT and self.my_direction != self.LEFT:
                    self.my_direction = self.RIGHT


    #movimento da cobra
    def snakeMove(self):
        for i in range(len(self.snake) - 1, 0, -1):# comprimento da cobra 
            self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])# Move o pixel anterior para nova posição fazendo movimento 
    
    # criar tabela score 
    def setScore(self):
        score_font = self.font.render('Score: %s' % (self.score), True, (255, 255, 255)) # criar uma label onde contem score , cor , fonte e tamnho de letra
        score_rect = score_font.get_rect() # cria um objecto retangulo
        score_rect.topleft = (600 - 120, 10) # marca posição do objecto (Topo direito)
        self.screen.blit(score_font, score_rect) # aparece na tela

    # posiciona na tela cobra
    def setSnake(self):
        for pos in self.snake:
            self.screen.blit(self.snake_skin,pos) # posiciona cobra + a sua posição

    # posiona na tela maça
    def setApple(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.apple_skin, self.apple_pos) # posiciona maçã + a sua posição

    # quando o jogador perder cria o evento
    def gameOver(self):
            game_over_font = pygame.font.Font('freesansbold.ttf', 75)
            game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
            game_over_rect = game_over_screen.get_rect()
            game_over_rect.midtop = (600 / 2, 10)
            self.screen.blit(game_over_screen,game_over_rect)
            pygame.display.update()
            pygame.time.wait(500)
            for event in pygame.event.get(): # todos os eventos da tela
                if event.type == pygame.QUIT: # se o jogador sair
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN: # se jogador carregar numa teclas
                    if event.key == pygame.K_KP_ENTER : # se o jogador carregar <ENTER> inicia novamento o jogo 
                        self.restartGame()
                    if event.key == pygame.K_ESCAPE: # se o jogar carregar <ESC> dai do jogo
                        pygame.quit()
                        exit()
                   

        
            
     

    def startGame(self):

            # fps jogo
        self.clock.tick(self.fps)

        # procura direção 
        self.selectDirection()

        # se apanhar maçã
        if self.collision():
            self.apple_pos = self.onGridRandom() # nova posição da maçã
            self.snake.append((0,0)) # aumenta cobra em 1 de tamanho
            self.score = self.score + 1 # aumenta o score em ele mesmo +1
        
        # se cobra colidir com as paredes, break sair do laço
        if self.snakeCollidedWithBoundaries():
            self.game_over = True

        # se cobra colidir com ela mesma, break sair do laço
        if self.snakeHasHitItself():
            self.game_over = True

        # função cobra mexer
        self.snakeMove()

        # insere nova direção da cobra
        self.insertSnakeMove()

        # aparece maça
        self.setApple()

        # aparece tabela score
        self.setScore()

        # aparece cobra
        self.setSnake()
        

        # faz refresh ao ecra
        pygame.display.update()
        
        
