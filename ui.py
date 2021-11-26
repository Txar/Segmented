import math, pygame
from gameLogic import *
class ui:
	def checkButtons(buttons, gm, sx, sy, scaling, selectedLevel):
		mouse = ui.mouseXY(sx, sy, scaling)
		h = 0
		for i in range(0, len(buttons[0])):
			if buttons[4][i] == gm:
				if ui.mouseOn(buttons[0][i], buttons[1][i], mouse):
					return int(buttons[5][i]), selectedLevel #returns gamemode
		if gm == 1 or gm == 2:
			if ui.mouseOn(1216, 328, mouse):
				selectedLevel+=1
			if ui.mouseOn(0, 328, mouse):
				selectedLevel-=1
		return gm, selectedLevel

	def mouseXY(sx, sy, scaling):
		mousePos = list(pygame.mouse.get_pos())
		mousePos[0] = math.floor(abs(sx-mousePos[0])/scaling)
		mousePos[1] = math.floor(abs(sy-mousePos[1])/scaling)
		return mousePos

	def mouseOn(x, y, mouse, size = 64):
		if mouse[0] > x and mouse[0] < x + size:
			if mouse[1] > y and mouse[1] < y + size:
				return True
		return False

	def setSoundsVolume(soundButtonsList, sx, sy, scaling):
		mouse = ui.mouseXY(sx, sy, scaling)
		if ui.mouseOn(0, 680, mouse, 32):
			if soundButtonsList[0]:
				soundButtonsList[0] = False
			else:
				soundButtonsList[0] = True
		elif ui.mouseOn(32, 680, mouse, 32):
			if soundButtonsList[1]:
				soundButtonsList[1] = False
			else:
				soundButtonsList[1] = True
		return soundButtonsList

	def checkShopButtons(currentSkin, selectingSkin, skinsList, sx, sy, scaling):
		mouse = ui.mouseXY(sx, sy, scaling)
		if ui.mouseOn(576, 648, mouse):
			if gameLogic.progress() >= skinsList[selectingSkin] and currentSkin != selectingSkin:
				currentSkin = selectingSkin
		if ui.mouseOn(1216, 328, mouse) and selectingSkin < 3:
			selectingSkin+=1
		if ui.mouseOn(0, 328, mouse) and selectingSkin > 0:
			selectingSkin-=1
		return currentSkin, selectingSkin