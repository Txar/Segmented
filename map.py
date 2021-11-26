import os
from gameLogic import *
class map:
	def getEl():
		el = 0
		f = open("gameData/progress.pgd", "r")
		i = f.readlines(1)
		f.close()
		el = int(i[0])
		return el

	def loadLevel(num):
		global el
		levelList = []
		levelList2 = []
		for i in range(0, 22):
			levelList2.append([])
		for i in range(0, 40):
			levelList.append([])
			for j in range(0, 22):
				levelList[i].append("00")
		"""for i in range(0, 24):
			levelList[i][0] = "01"
			levelList[i][24] = "01"""
		if num < 1:
			num = 1
		if num > map.getEl():
			num = map.getEl()
		filename = "levels/lvl"+str(num)+".plv"
		f = open(filename)
		for r in range(0, 22):
			levelList2[r].append(f.readlines(r + 1))
			levelList2[r] = str(levelList2[r]).replace("\\n", "")
			levelList2[r] = str(levelList2[r]).replace("[['", "") #yes, what?
			levelList2[r] = str(levelList2[r]).replace("']]", "") #i actually dont know
			levelList2[r] = levelList2[r].split(" ")
		f.close()
		for i in range(0, 40):
			for j in range(0, 22):
				levelList[i][j] = levelList2[j][i]
		return levelList

	def putCells(sldlvl, clls):
		clls = [[], [], []]
		for i in range(0, len(sldlvl)):
			for j in range(0, len(sldlvl[0])):
				if sldlvl[i][j] == "02":
					sldlvl[i][j] == "00"
					clls[0].append(i)
					clls[1].append(j)
					clls[2].append(0)
		return sldlvl, clls