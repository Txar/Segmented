import pygame, math, os
from gameLogic import *
from map import *
from ui import *
from graphics import *
from random import randint
"""
4 types of tiles so far
00 - floor
01 - wall
02 - cell
03 - exit button
"""
height = 720
width = 1280
refresh = False

buttons = [[396, 576, 768, 1216, 1088, 1216, 1216, 576], [304, 304, 304, 8, 8, 8, 8, 648], [64, 128, 128, 128, 64, 128, 128, 128], [0, 64, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 3, 2, 5], [1, 2, 4, 0, 3, 1, 0, 0]] #first two are x and y, second 2 are x and y on the sprite, fifth is game mode, sixth is game mode its changing to
skins = [0, 5, 10, 15]
playMoveSound = False
selectedLevel = 0
currentSkin = 0
selectingSkin = 0
gameMode = 0 #0 is main menu, 1 is level select, 2 is skin shop mode, 3 is play mode, 4 is just exit, 5 is ending screen
#playerXY = [0, 0]
cells = [[], [], []] #first is x, second is y, third is if it has moved in the previous frame
previousCells = [[], [], []] #previous frame of cells
solidLevel = []
pygame.mixer.init()
moveSound = pygame.mixer.Sound('moveSound.wav')
pygame.mixer.music.load("incoming.mp3")
gameIcon = pygame.image.load("player0.png")
songPlaying = False
soundButtons = [True, True]
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
for i in range(0, 22):
	solidLevel.append([])
windowCaption = "Segmented"
if not os.path.exists("gameData/progress.pgd"):
	firstTime = True
	f = open("gameData/progress.pgd", "w")
	f.writelines("1")
	f.close()
level = gameLogic.progress()
currentSkin = gameLogic.skin()
selectingSkin = gameLogic.skin()
if skins[currentSkin] > level or currentSkin < 0:
	currentSkin = 0
	selectingSkin = 0
selectedLevel = gameLogic.progress()
gameOver = False
direction = [0, 0, 0, 0]
screen = pygame.Surface((width, height))
floorSurface = pygame.Surface((width, height))
wallsSurface = pygame.Surface((width, height))
pygame.init()
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption(windowCaption)
pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()
"""solidLevel = map.loadLevel(1)
solidLevel, cells = map.putCells(solidLevel, cells)"""
while not gameOver:
	#controls
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				direction[0] = 1
			if event.key == pygame.K_a:
				direction[1] = 1
			if event.key == pygame.K_d:
				direction[2] = 1
			if event.key == pygame.K_s:
				direction[3] = 1
			if event.key == pygame.K_h:
				pygame.image.save(screen, "screenshot.png")
			if event.key == pygame.K_r:
				solidLevel, cells = gameLogic.passLevel(selectedLevel, False)
		if event.type == pygame.MOUSEBUTTONDOWN:
			gm, selectedLevel = ui.checkButtons(buttons, gameMode, sx, sy, scaling, selectedLevel)
			soundButtons = ui.setSoundsVolume(soundButtons, sx, sy, scaling)
			pygame.mixer.music.set_volume(int(soundButtons[1]))
			moveSound.set_volume(int(soundButtons[0]))
			if gameMode != 3:
				refresh = True
			if gameMode != gm:
				gameMode = gm
				if gameMode == 3:
					level = selectedLevel
					solidLevel, cells = gameLogic.changeGameMode(gameMode, level)
					floorSurface = graphics.drawFloor(floorSurface)
					wallsSurface = graphics.renderWalls(solidLevel, floorSurface)
					wallsSurface = graphics.renderExitButtons(solidLevel, wallsSurface)
		if event.type == SONG_END:
			songPlaying = False

	#game logic
	if refresh:
		if gameMode == 1:
			solidLevel, cells = gameLogic.passLevel(selectedLevel, False)
		if len(solidLevel[0]) > 0:
			floorSurface = graphics.drawFloor(floorSurface)
			wallsSurface = graphics.renderWalls(solidLevel, floorSurface)
			wallsSurface = graphics.renderExitButtons(solidLevel, wallsSurface)
		if gameMode == 2:
			currentSkin, selectingSkin = ui.checkShopButtons(currentSkin, selectingSkin, skins, sx, sy, scaling)
		graphics.setSkin(currentSkin)
		gameLogic.saveSkin(currentSkin)
		refresh = False
	if gameMode == 4:
		gameOver = True
	if gameMode != 3:
		direction = [0, 0, 0, 0]
	if 1 in direction:
		direction = gameLogic.checkIfDiagonal(direction)
		#direction = gameLogic.checkPlayerCollisions(direction, playerXY, solidLevel)
		#playerXY = gameLogic.movePlayer(direction, playerXY)
		playMoveSound = False
		cells, playMoveSound = gameLogic.moveCells(direction, cells, solidLevel)
		if playMoveSound:
			moveSound.play()
		if gameLogic.checkWin(solidLevel, cells):
			if level == 15:
				gameMode = 5
			level+=1
			h = level > gameLogic.progress()
			solidLevel, cells = gameLogic.passLevel(level, h)
			refresh = True
		direction = [0, 0, 0, 0]
		if cells[0] != previousCells[0] and cells[1] != previousCells[1]:
			previousCells = [[], [], []]
			for i in range(0, len(cells[0])):
				for j in range(0, 3):
					previousCells[j].append(cells[j][i])
		if 1 in cells[2]:
			for i in range(0, len(cells[2])):
				cells[2][i] = 0

	#displaying, scaling, music
	wh = pygame.display.get_surface().get_size()
	w, h = wh[0], wh[1]
	scaling = min(w/width, h/height)
	sx = abs(w-width*scaling)/2
	sy = abs(h-height*scaling)/2
	screen.fill((0, 0, 0))
	if gameMode == 3:
		if not songPlaying:
			i = randint(0, 1000)
			if i == 300:
				pygame.mixer.music.play()
				songPlaying = True
	if gameMode == 3 or gameMode == 1:
		#screen.blit(floorSurface, (0, 0))
		screen.blit(wallsSurface, (0, 0))
		#screen = graphics.drawPlayer(screen, playerXY[0], playerXY[1])
		screen = graphics.drawCells(cells, screen)
	if gameMode == 0 or gameMode == 2:
		screen = graphics.drawBackground(screen)
	if gameMode == 0:
		screen = graphics.drawLogo(screen)
	if gameMode == 2:
		screen = graphics.drawShopButtons(skins, selectingSkin, currentSkin, screen)
		screen = graphics.drawSkin(selectingSkin, screen)
	if gameMode == 5:
		screen = graphics.drawEnd(screen)
	screen = graphics.drawUi(buttons, gameMode, soundButtons, screen)
	screen = graphics.drawArrowButtons(gameMode, screen)
	window.fill((0, 0, 0))
	window.blit(pygame.transform.smoothscale(screen, (math.floor(width*scaling), math.floor(height*scaling))), (sx, sy))
	pygame.display.update()
	clock.tick(60)