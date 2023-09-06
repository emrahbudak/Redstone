"""
import images and create board setup
"""
import pygame

# initialize pygame 
pygame.init()
screen_x = 150
screen_y = 150
screen = pygame.display.set_mode((screen_x, screen_y))

white_img = pygame.image.load("./assests/images/white.png")
white_img = pygame.transform.scale(white_img,(40,40))
black_img = pygame.image.load("./assests/images/black.png")
black_img = pygame.transform.scale(black_img,(40,40))
black_won_img = pygame.image.load("./assests/images/black_won.png")
black_won_img = pygame.transform.scale(black_won_img,(120,17))
white_won_img = pygame.image.load("./assests/images/white_won.png")
white_won_img = pygame.transform.scale(white_won_img,(120,17))


def drawBoard():
	# drawing lines
	bg_img = pygame.image.load("./assests/images/bg.jpg")
	# wood background
	screen.blit(bg_img,(0,0))
	for i in range(2):
		pygame.draw.line(screen, "black", (0, (screen_x // 3)*(i+1)),(screen_y,(screen_x // 3)*(i+1)),3)
		pygame.draw.line(screen, "black", ((screen_y // 3)*(i+1), 0),((screen_y // 3)*(i+1),screen_x),3)

def drawMessage(img):
	pygame.draw.rect(screen,"white",pygame.Rect(0,50,150,50))
	if img == 1:
		screen.blit(white_won_img,(15,68))
	elif img == -1:
		screen.blit(black_won_img,(15,68))

def screnUpdate(x,y,img):
	x= (x+5)+(x*50)
	y= (y+5)+(y*50)
	if img == -1:
		screen.blit(white_img,(x,y))
	elif img == 1:
		screen.blit(black_img,(x,y))