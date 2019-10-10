
import sharedlibs
sharedlibs.add_path_for('perm_utils')
from permuter import Permuter

class StringPermuter(object):
	def __init__(self, str, *args, **kwargs):
		self._permuter = Permuter(list(str), *args, **kwargs)
		
	def permute(self, *args, **kwargs):
		for perm in self._permuter.permute(*args, **kwargs):
			yield ''.join(perm)
			
if __name__ == '__main__':
	sp = StringPermuter('aaba')
	for p in sp.permute():
		print(p)
