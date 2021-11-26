from map import *
class gameLogic:
	def checkPlayerCollisions(drct, pxy, sldlvl):
		if drct[0] == 1:
			if sldlvl[pxy[1]-1][pxy[0]] != "00":
				drct[0] = 0	
		if drct[1] == 1:
			if sldlvl[pxy[0]-1][pxy[1]] != "00":
				drct[1] = 0
		if drct[2] == 1:
			if sldlvl[pxy[0]+1][pxy[1]] != "00":
				drct[2] = 0
		if drct[3] == 1:
			if sldlvl[pxy[1]+1][pxy[0]] != "00":
				drct[3] = 0	
		return drct

	def movePlayer(drct, pxy):
		if drct[0] == 1:
			pxy[1]-=1
		if drct[1] == 1:
			pxy[0]-=1
		if drct[2] == 1:
			pxy[0]+=1
		if drct[3] == 1:
			pxy[1]+=1
		return pxy

	def checkIfDiagonal(drct):
		count = 0
		for i in range(0, 4):
			if drct[i] == 1:
				count+=1
		if count > 1:
			drct = [0, 0, 0, 0]
		return drct

	def areCellsNearPlayer(pxy, clls, sldlvl):
		s = False
		for i in range(0, 22):
			if s:
				break
			for j in range(0, 40):
				if pxy == [i, j]:
					continue
				if not sldlvl[j][i] == "02":
					continue
				if i == pxy[1] - 1 and j == pxy[0]:
					s = True
					clls[1].append(i)
					clls[0].append(j)
					sldlvl[j][i] = "00"
				if i == pxy[1] and j == pxy[0] - 1:
					s = True
					clls[1].append(i)
					clls[0].append(j)
					sldlvl[j][i] = "00"
				if i == pxy[1] + 1 and j == pxy[0]:
					s = True
					clls[1].append(i)
					clls[0].append(j)
					sldlvl[j][i] = "00"
				if i == pxy[1] and j == pxy[0] + 1:
					s = True
					clls[1].append(i)
					clls[0].append(j)
					sldlvl[j][i] = "00"
		return clls, sldlvl

	def moveCells(drct, clls, sldlvl):
		p = False
		if 1 in drct:
			clls = gameLogic.sortCells(clls, drct)
		if drct[0] == 1:
			for i in range(0, len(clls[1])):
				if clls[1][i]-1 in clls[1]:
					if clls[0][clls[1].index(clls[1][i]-1)] == clls[0][i]:
						continue
				try:
					if sldlvl[clls[0][i]][clls[1][i]-1] != "01":
						clls[1][i]-=1
						clls[2][i]=1
						p = True
				except:
					continue
		elif drct[1] == 1:
			for i in range(0, len(clls[0])):
				if clls[0][i]-1 in clls[0]:
					if clls[1][clls[0].index(clls[0][i]-1)] == clls[1][i]:
						continue
				try:
					if sldlvl[clls[0][i]-1][clls[1][i]] != "01":
						clls[0][i]-=1
						clls[2][i]=1
						p = True
				except:
					continue
		elif drct[2] == 1:
			for i in range(0, len(clls[0])):
				if clls[0][i]+1 in clls[0]:
					if clls[1][clls[0].index(clls[0][i]+1)] == clls[1][i]:
						continue
				try:
					if sldlvl[clls[0][i]+1][clls[1][i]] != "01":
						clls[0][i]+=1
						clls[2][i]=1
						p = True
				except:
					continue
		elif drct[3] == 1:
			for i in range(0, len(clls[1])):
				if clls[1][i]+1 in clls[1]:
					if clls[0][clls[1].index(clls[1][i]+1)] == clls[0][i]:
						continue
				try:
					if sldlvl[clls[0][i]][clls[1][i]+1] != "01":
						clls[1][i]+=1
						clls[2][i]=1
						p = True
				except:
					continue
		return clls, p

	def sortCells(lst, drct): #i want the most top cells to move up first, basically this is for sorting the list for that purpose
		a = []
		b = []
		c = [[], [], []]
		for i in range(0, len(lst[0])):
			a.append(lst[0][i])
			b.append(lst[1][i])
			c[2].append(lst[2][i])
		if drct[0] == 1:
			for i in range(0, len(lst[0])):
				h = b.index(min(b))
				c[0].append(a[h])
				c[1].append(b[h])
				b.pop(h)
				a.pop(h)
		elif drct[1] == 1:
			for i in range(0, len(lst[0])):
				h = a.index(min(a))
				c[0].append(a[h])
				c[1].append(b[h])
				b.pop(h)
				a.pop(h)
		elif drct[2] == 1:
			for i in range(0, len(lst[0])):
				h = a.index(max(a))
				c[0].append(a[h])
				c[1].append(b[h])
				b.pop(h)
				a.pop(h)
		elif drct[3] == 1:
			for i in range(0, len(lst[0])):
				h = b.index(max(b))
				c[0].append(a[h])
				c[1].append(b[h])
				b.pop(h)
				a.pop(h)
		return c

	def checkWin(sldlvl, clls):
		h = [[], []]
		cnt = 0
		for i in range(0, len(sldlvl)):
			cnt += sldlvl[i].count("03")
		for i in range(0, len(clls[0])):
			h[0].append(clls[0][i])
			h[1].append(clls[1][i])
		for i in range(0, len(sldlvl[0])):
			for j in range(0, len(sldlvl)):
				if sldlvl[j][i] == "03":
					if j in clls[0]:
						if clls[1][clls[0].index(j)] == i:
							cnt-=1
		if cnt < 1:
			return True
		return False

	def existingLevels():
		el = 1
		while True:
			filename = "levels/lvl" + str(el) + ".plv"
			if not os.path.exists(filename):
				break
			el = el + 1
		return el

	def saveProgress(level):
		if level >= gameLogic.existingLevels():
			level = gameLogic.existingLevels() - 1
		f = open("gameData/progress.pgd", "w")
		f.writelines(str(level))
		f.close()

	def passLevel(level, h = True):
		if h:
			gameLogic.saveProgress(level)
		l = map.loadLevel(level)
		clls = [[], [], []]
		l, clls = map.putCells(l, clls)
		return l, clls

	def progress():
		f = open("gameData/progress.pgd", "r")
		i = f.readlines(1)
		f.close()
		return int(i[0])

	def changeGameMode(gm, lvl = -1):
		if lvl == -1:
			lvl = gameLogic.progress()
		#if gm == 3:
		l, clls = gameLogic.passLevel(lvl, False)
		return l, clls

	def skin():
		f = open("gameData/skin.pgd", "r")
		i = f.readlines(1)
		f.close()
		return int(i[0])

	def saveSkin(i):
		if i > 3 or i < 0:
			i = 0
		f = open("gameData/skin.pgd", "w")
		f.writelines(str(i))
		f.close()
