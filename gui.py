# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

screen_x = 150
screen_y = 150
screen = pygame.display.set_mode((screen_x, screen_y))

bg_img = pygame.image.load("./bg.jpg")
white_img = pygame.image.load("./white.png")
white_img = pygame.transform.scale(white_img,(40,40))
black_img = pygame.image.load("./black.png")
screen.blit(bg_img,(0,0))

clock = pygame.time.Clock()
running = True


def drawBoard():
	# Drawing Rectangle
	for i in range(2):
		pygame.draw.line(screen, "black", (0, (screen_x // 3)*(i+1)),(screen_y,(screen_x // 3)*(i+1)),3)
		pygame.draw.line(screen, "black", ((screen_y // 3)*(i+1), 0),((screen_y // 3)*(i+1),screen_x),3)

def playStone(state, player):
	#(state.reshape(-1) == 0).astype(np.uint8)
	screen.blit(white_img,((state[0]*(screen_x // 3))-22,(state[0]*(screen_x // 3))+22))

def guiStart(running):
	while running:
		drawBoard()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pressed = pygame.mouse.get_pressed()
				if pressed[0]:
					pos = pygame.mouse.get_pos()
					print(pos[0])
					if((pos[0] <= (screen_x // 3)) & (pos[1] <= (screen_y // 3))):
						screen.blit(white_img,(((screen_x // 3)-45),((screen_y // 3)-45)))
		pygame.display.update()
		clock.tick(60)  # limits FPS to 60
