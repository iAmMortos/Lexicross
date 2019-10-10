
import sharedlibs
sharedlibs.add_path_for('word_utils')
from word_tree import WordTree
from word_loader import load_wwf_words

class Dictionary (object):
	def __init__(self):
		self._word_tree = WordTree
