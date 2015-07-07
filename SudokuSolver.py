def findNextCell(grid, i, j):
	for x in range(i,9):
		for y in range(j,9):
			if grid[x][y] == 0:
				return x,y
	for x in range(0,9):
		for y in range(0,9):
			if grid[x][y] == 0:
				return x,y
	return -1,-1

def isValid(grid, i, j, e):
	checkRows = all([e != grid[i][x] for x in range(9)])
	if checkRows:
		checkCols = all([e != grid[x][j] for x in range(9)])
		if checkCols:
			secTopX, secTopY = 3 *(i//3), 3 *(j//3)
			for x in range(secTopX, secTopX+3):
				for y in range(secTopY, secTopY+3):
					if grid[x][y] == e:
						return False
			return True
	return False

def solveSudoku(grid, i=0, j=0):	
	i,j = findNextCell(grid, i, j)
	if i == -1:
		return True
	for e in range(1,10):
		if isValid(grid, i, j, e):
			grid[i][j] = e
			if solveSudoku(grid, i, j):
				return True
			grid[i][j] = 0
	return False

def printBoard(grid):
	for i in grid:
		print(i)

def main(grid):
	board = grid
	solveSudoku( board )
	return board

if __name__ == '__main__': main()
