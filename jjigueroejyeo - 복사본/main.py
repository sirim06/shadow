import pygame

pygame.init()

screen_height = 768
screen_width = 1366
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Shadow")

background_M_image = pygame.image.load("data/back/background_main.png")
background_M_image = pygame.transform.scale(background_M_image, (1366, 768))
background_O_S_image = pygame.image.load("data/back/background_O_S.png")
background_O_S_image = pygame.transform.scale(background_O_S_image, (1366, 768))

title_image = pygame.image.load("data/image/title.png") 
title_image = pygame.transform.scale(title_image, (1000, 1000))

start_image = pygame.image.load("data/image/start.png")
start_image = pygame.transform.scale(start_image, (320, 100))
start_H_image = pygame.image.load("data/image/start_H.png")
start_H_image = pygame.transform.scale(start_H_image, (320, 100))

option_image = pygame.image.load("data/image/option.png")
option_image = pygame.transform.scale(option_image, (320, 100))
option_H_image = pygame.image.load("data/image/option_H.png")
option_H_image = pygame.transform.scale(option_H_image, (320, 100))

Return_image = pygame.image.load("data/image/return.png")
Return_image = pygame.transform.scale(Return_image, (54, 36))
Return_H_image = pygame.image.load("data/image/return_H.png")
Return_H_image = pygame.transform.scale(Return_H_image, (54, 36))

music_B_image = pygame.image.load("data/image/music_B.png")
music_B_image = pygame.transform.scale(music_B_image,(140, 140))
music_b_B_image = pygame.image.load("data/image/music_b_B.png")
music_b_B_image = pygame.transform.scale(music_b_B_image,(140, 140))

stage_1_image = pygame.image.load("data/image/stage_1.png")
stage_1_image = pygame.transform.scale(stage_1_image,(140,140))

cha_image = pygame.image.load("data/image/cha 1.png")
cha_image = pygame.transform.scale(cha_image,(50,50))

bar_image = pygame.image.load("data/image/bar.png")
bar_image = pygame.transform.scale(bar_image,(50,20))

main_sound = pygame.mixer.Sound("data/sound/main_sound.mp3")

main_sound.set_volume(0.5) 

class Button :
    def __init__(self,N,H,W,L,X,Y):
        self.N = N
        self.H = H
        self.W = W
        self.L = L
        self.X = X
        self.Y = Y
        self.rect = pygame.Rect((self.X, self.Y, self.W, self.L))
        self.state = self.N

    def draw(self):
        screen.blit(self.state, self.rect)

    def handle_hover(self, event):
        if self.rect.collidepoint(event.pos):
            self.state = self.H
        else:
            self.state = self.N


title = Button(title_image, title_image, 1000, 1000, 450, -100)
start = Button(start_image, start_H_image, 320, 100, 180, 350)
option = Button(option_image, option_H_image, 320, 100, 180, 500)
Return = Button(Return_image,Return_H_image, 54, 36, 10, 720)
music = Button(music_B_image,music_B_image, 140, 140, 220, 200)
music_b = Button(music_b_B_image,music_b_B_image, 140, 140, 220, 420)
stage_1_B = Button(stage_1_image,stage_1_image, 140, 140, 220, 200)


def button_reset():
    start.state = start.N
    option.state = option.N
    Return.state = Return.N
    music.state = music.N
    music_b.state = music_b.N
    stage_1_B.state = stage_1_B.N

class bar():
    def __init__(self,X,Y):
        self.X = self.X
        self.Y = self.Y
        self.rect = pygame.Rect(self.X,self.Y,50,20)
        self.drag = False
    def move (self,Y):
        if self.drag == True : 
            self.Y = pygame.mouse.set_pos

'''bar_A = bar(100,100,50,20)'''

Type= 'Menu'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Main

        if Type == 'Menu':

            main_sound.play(-1)

            screen.blit(background_M_image,(0,0))
            title.draw()
            start.draw()
            option.draw()

            button_reset()

            if event.type == pygame.MOUSEMOTION:
                start.handle_hover(event)

            if event.type == pygame.MOUSEMOTION:
                option.handle_hover(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start.rect.collidepoint(event.pos):
                    Type = 'Start'
                elif option.rect.collidepoint(event.pos):
                    Type = 'Option'

#Start

        if Type == 'Start':
            screen.blit(background_O_S_image,(0,0))
            Return.draw()
            stage_1_B.draw()

            button_reset()

            if event.type == pygame.MOUSEMOTION:
                Return.handle_hover(event)

            if event.type == pygame.KEYDOWN :
                if event.key == 27:
                    Type = 'Menu'

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Return.rect.collidepoint(event.pos):
                    Type = 'Menu'

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if stage_1_B.rect.collidepoint(event.pos):
                    Type = "Stage_1"

#Option

        if Type == 'Option':
            screen.blit(background_O_S_image,(0,0))
            Return.draw()
            music.draw()
            music_b.draw()
            

            button_reset()

            if event.type == pygame.MOUSEMOTION:
                Return.handle_hover(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if music.rect.collidepoint(event.pos):
                    main_sound.set_volume(0.5) 

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if music_b.rect.collidepoint(event.pos):
                    main_sound.set_volume(0) 

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Return.rect.collidepoint(event.pos):
                    Type = 'Menu'
                
            if event.type == pygame.KEYDOWN :
                if event.key == 27:
                    Type = 'Menu'

#stage - 1

        if Type == "Stage_1":
            screen.blit(background_M_image,(0,0))
            screen.blit(cha_image,(0,0))
            Return.draw()


            if event.type == pygame.MOUSEMOTION:
                Return.handle_hover(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Return.rect.collidepoint(event.pos):
                    Type = 'Start'
                
            if event.type == pygame.KEYDOWN :
                if event.key == 27:
                    Type = 'Start'


    pygame.display.update()

pygame.quit()
    