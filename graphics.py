import pygame, random, math
from gameLogic import *
height = 720
width = 1280
floorTileSprite = pygame.image.load("floor.png")
wallTileSprite = pygame.image.load("wall.png")
playerSprite = pygame.image.load("player0.png")
buttonsSprite = pygame.image.load("buttons.png")
soundButtonsSprite = pygame.image.load("soundButtons.png")
exitButtonSprite = pygame.image.load("exitButton.png")
background = pygame.image.load("background.png")
endImage = pygame.image.load("end.png")
logo = pygame.image.load("logo.png")
class graphics:
	def drawFloor(s):
		s.fill((0, 0, 0))
		for i in range(0, 40):
			for j in range(0, 22):
				variant = random.randint(0, 4)
				variant = 0
				cfs = pygame.Surface((32, 32))
				cfs.blit(floorTileSprite, (0, 0), (0, variant * 32, 32, variant * 32 + 32))
				rotation = random.randint(0, 360)
				rotation = 0
				#s.blit(pygame.transform.rotate(cfs, int(90 * math.ceil(float(rotation) / 90) - 90)), (i*32, 8+j*32))
				s.blit(floorTileSprite, (i*32, 8+j*32))
		return s

	def drawPlayer(s, x, y):
		s.blit(playerSprite, (x*32, 8+y*32))
		return s

	def renderWalls(lst, srf = pygame.Surface((width, height)).fill((0, 0, 0, 0))):
		for i in range(0, 40):
			for j in range(0, 22):
				mask = 0
				x = i * 32
				y = j * 32
				if lst[i][j] == "01":
					if i + 1 < 40:
						if lst[i + 1][j] == "01":
							mask = mask + 1
					if lst[i][j - 1] == "01":
						mask = mask + 2
					if lst[i - 1][j] == "01":
						mask = mask + 4
					if j + 1 < 22:
						if lst[i][j + 1] == "01":
							mask = mask + 8
					srf.blit(wallTileSprite, (x, 8+y), (mask*32, 0, 32, 32))
		return srf

	def renderExitButtons(lst, srf = pygame.Surface((width, height)).fill((0, 0, 0, 0))):
		for i in range(0, 40):
			for j in range(0, 22):
				if lst[i][j] == "03":
					srf.blit(exitButtonSprite, (i*32, 8+j*32))
		return srf

	def drawCells(clls, srf):
		for i in range(0, len(clls[0])):
			srf.blit(playerSprite, (clls[0][i]*32, 8+clls[1][i]*32))
		return srf

	def drawUi(buttons, gm, soundButtonsList, srf = pygame.Surface((width, height)).fill((0, 0, 0, 0))):
		for i in range(0, len(buttons[0])):
			if buttons[4][i] == gm:
				srf.blit(buttonsSprite, ((buttons[0][i], buttons[1][i])), ((0, 0, 64, 64)))
				srf.blit(buttonsSprite, ((buttons[0][i], buttons[1][i])), ((buttons[2][i], buttons[3][i], 64, 64)))
		srf.blit(soundButtonsSprite, (0, 680), (0, 0, 64, 32))
		if not soundButtonsList[0]:
			srf.blit(soundButtonsSprite, (0, 680), (64, 0, 32, 32))
		if not soundButtonsList[1]:
			srf.blit(soundButtonsSprite, (32, 680), (64, 0, 32, 32))
		return srf

	def drawArrowButtons(gm, srf = pygame.Surface((width, height)).fill((0, 0, 0, 0))):
		if gm == 1 or gm == 2:
			srf.blit(buttonsSprite, ((0, 328)), ((0, 0, 64, 64)))
			srf.blit(buttonsSprite, ((1216, 328)), ((0, 0, 64, 64)))
			srf.blit(buttonsSprite, ((0, 328)), ((192, 0, 64, 64)))
			srf.blit(buttonsSprite, ((1216, 328)), ((256, 0, 64, 64)))
		return srf

	def drawCellsAnimations(lst1, lst2, srf): #lst 1 is current cells, lst 2 is previous
		lst3 = [[], [], []]
		for i in range(0, len(cells[0])):
			for j in range(0, 3):
				lst3[j].append(lst1[j][i])
		for i in range(0, len(lst1[0])):
			if lst1[2][i] == 0:
				lst1[0].pop(i)
				lst1[1].pop(i)
				lst1[2].pop(i)
				lst2[0].pop(i)
				lst2[1].pop(i)
				lst2[2].pop(i)
				continue

	def drawBackground(srf = pygame.Surface((width, height)).fill((0, 0, 0, 0))):
		srf.blit(background, (0, 0))
		return srf

	def drawSkin(i, srf = pygame.Surface((width, height)).fill((0, 0, 0, 0))):
		img = pygame.transform.scale2x(pygame.image.load("player"+str(i)+".png"))
		srf.blit(img, ((576, 296)))
		return srf

	def drawShopButtons(skinsList, selectingSkin, currentSkin, srf = pygame.Surface((width, height)).fill((0, 0, 0, 0))):
		if selectingSkin != currentSkin:
			if gameLogic.progress() >= skinsList[selectingSkin] and currentSkin != selectingSkin:
				srf.blit(buttonsSprite, ((576, 648)), ((0, 0, 64, 64)))
				srf.blit(buttonsSprite, ((576, 648)), ((192, 64, 64, 64)))
		img = pygame.image.load("player"+str(currentSkin)+".png")
		srf.blit(buttonsSprite, ((1088, 8)), ((0, 0, 64, 64)))
		srf.blit(img, ((1104, 24)))
		return srf

	def setSkin(i):
		global playerSprite
		playerSprite = pygame.image.load("player"+str(i)+".png")

	def drawEnd(srf = pygame.Surface((width, height)).fill((0, 0, 0, 0))):
		srf.blit(endImage, ((0, 0)))
		return srf

	def drawLogo(srf = pygame.Surface((width, height)).fill((0, 0, 0, 0))):
		srf.blit(logo, ((408, 128)))
		return srf