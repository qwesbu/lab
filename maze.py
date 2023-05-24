import pygame
pygame.init()



class Hero(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,img,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(w,h))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=speed
        self.gameover=0
    def draw(self,win):
        win.blit(self.image,self.rect)
    def update(self):
        x_old=self.rect.x
        y_old=self.rect.y
        kase=pygame.key.get_pressed()
        if kase[pygame.K_LEFT]:
            self.rect.x-=5
        elif kase[pygame.K_RIGHT]:
            self.rect.x+=5
        elif kase[pygame.K_UP]:
            self.rect.y-=5
        elif kase[pygame.K_DOWN]:
            self.rect.y+=5
        is_catch=pygame.sprite.spritecollide(self,walls,False)
        if is_catch:
            self.rect.x=x_old
            self.rect.y=y_old
        is_catch1=pygame.sprite.collide_rect(self,enemy)
        if is_catch1:
            self.gameover=1
            shoot_music1.play()
        is_catch2=pygame.sprite.collide_rect(self,door)
        if is_catch2:
            self.gameover=2
            shoot_music.play()


class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,img,speed,xend):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(w,h))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.direction='right'
        self.speed=speed
        self.xend=xend
        self.xstart=x
        
        
    def draw(self,win):
        win.blit(self.image,self.rect)
    def update(self):
        if self.direction=='right' and self.rect.x<self.xend:
            self.rect.x+=self.speed
        elif self.direction=='right' and self.rect.x>=self.xend:
            self.direction='left'

        elif self.direction=='left' and self.rect.x>self.xstart:
            self.rect.x-=self.speed
        elif self.direction=='left' and self.rect.x<=self.xstart:
            self.direction='right'
        

            

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,color):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([w,h])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=x,y
    def draw(self,win):
        win.blit(self.image,self.rect)

         
            



class Door():
    def __init__(self,x,y,w,h,img):
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(w,h))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def draw(self,win):
        win.blit(self.image,self.rect)


def game():
    hero.draw(win)
    walls.draw(win)
    door.draw(win)
    enemy.draw(win)

    hero.update()
    enemy.update()


W,H=900,500
win=pygame.display.set_mode((W,H))
pygame.display.set_caption('лабиринт')
clock=pygame.time.Clock()
FPS=60
run=True
hero=Hero(50,400,80,80,'hero.png',5)
door=Door(750,80,100,100,'treasure.png')
enemy=Enemy(470,305,80,80,'cyborg.png',4,680)
walls=pygame.sprite.Group()
walls.add(Wall(10,30,900,10,(0,0,0)))
walls.add(Wall(10,30,10,460,(0,0,0)))
walls.add(Wall(150,260,10,220,(0,0,0)))
walls.add(Wall(160,260,150,10,(0,0,0)))
walls.add(Wall(150,160,310,10,(0,0,0)))
walls.add(Wall(300,260,10,150,(0,0,0)))
walls.add(Wall(460,160,10,320,(0,0,0)))
walls.add(Wall(600,30,10,270,(0,0,0)))
walls.add(Wall(750,200,10,280,(0,0,0)))
walls.add(Wall(750,200,200,10,(0,0,0)))
walls.add(Wall(10,480,900,10,(0,0,0)))





font=pygame.font.SysFont('arial',70)
text_gameover=font.render('вы проиграли!',1,(189, 183, 107))
text_win=font.render('вы выиграли!',1,(189, 183, 107))

pygame.mixer.music.load('890796b2b460d45.mp3')
pygame.mixer.music.play(-1)
shoot_music=pygame.mixer.Sound('stopka-monet-30616.ogg')
shoot_music1=pygame.mixer.Sound('kick.ogg')
shoot_music.set_volume(1)
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    win.fill((150, 114, 122))
    if hero.gameover==0:
        game()
    elif hero.gameover==1:
        
        win.blit(text_gameover,(250,200))
    elif hero.gameover==2:
        
        win.blit(text_win,(250,200))

    

    
   
    pygame.display.update()
    clock.tick(FPS)