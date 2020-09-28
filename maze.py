from random import randint

class Maze:
	wallRGB, wayRGB = (0, 0, 0), (255, 255, 255)
	offset = [(0, 2), (0, -2), (-2, 0), (2, 0)]

	def __init__(self, width, heigth):
		if width % 2 == 0: width += 1
		if height % 2 == 0: height += 1

		self.width = width
		self.height = height

		sx, sy = randint(1, self.width - 2), randint(1, self.height - 2)
		if not sx % 2: sx += 1
		if not sy % 2: sy += 1

		# Generate an empty maze
		self.frontier = set()
		self.visited() = set()
		self.to_draw = set()
		self.maze = []

		self.visited.add((sy, sx))
		self.to_draw((sy, sx))
		
		for y in range(self.height):
			row = []
			for x in range(self.width):
				if y % 2 + x % 2 < 2:
					row.append(Maze.wallRGB)
				else:
					row.append(Maze.wayRGB)
			self.maze.append(row)
		
		# Starting position
		self._add_walls(sy, sx)
		
		# print(sy, sx, self.maze[sy][sx])
	
	def _clamp(self, n, min_n, max_n):
		return min(max(min_n, n), max_n)
	
	def _add_walls(self, y, x):
		for o in Maze.offset:
			cell = (y + o[0], x + o[1])
			if self._range(cell[0], cell[1]) and cell not in self.visited and cell not in self.frontier and \
					self.maze[cell[0][cell[1]] == Maze.wayRGB:
				self.frontier.add(cell)
