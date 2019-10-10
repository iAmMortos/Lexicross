from tile import Tile
import random

class TileBag (object):
	def __init__(self):
		self._counts = {}
		self._bag = []
		
	def add(self, tile, num=1):
		for _ in range(num):
			self._counts[tile.char] = self._counts.get(tile.char, 0) + 1
			self._bag += [tile]
			
	def draw(self, num=1):
		tiles = []
		for _ in range(num):
			if self.num_tiles > 0:
				tile = random.choice(self._bag)
				c = tile.char
				self._bag.remove(tile)
				self._counts[c] = self._counts[c] - 1
				tiles += [tile]
		return (tiles) if (num != 1) else (tiles[0])
		
	def get_number_of(self, char):
		return self._counts.get(char, 0)
		
	def _print_counts(self):
		total = 0
		ak = sorted(self._counts.keys())
		for k in ak:
			c = self._counts[k]
			print('%s: %s' % (k, c))
		
	@property
	def num_tiles(self):
		return len(self._bag)
		
	@staticmethod
	def get_wwf_tile_bag():
		return TileBag.get_tile_bag_from_file('rsc/wwf_tiles.txt')
		
	@staticmethod
	def get_wwf_small_tile_bag():
		return TileBag.get_tile_bag_from_file('rsc/wwf_small_tiles.txt')
		
	@staticmethod
	def get_scrabble_tile_bag():
		return TileBag.get_tile_bag_from_file('rsc/scrabble_tiles.txt')
		
	@staticmethod
	def get_tile_bag_from_file(path):
		with open(path) as f:
			tb = TileBag()
			for line in [line.strip() for line in f.readlines()]:
				if not line.startswith('#'):
					try:
						c,n,v = line.split()
						tb.add(Tile(c, int(v)), int(n))
					except Exception as ex:
						raise Exception('Problem creating tile from line: "%s"' % line)
			return tb
						


if __name__ == '__main__':
	b = TileBag.get_wwf_tile_bag()
	b._print_counts()
