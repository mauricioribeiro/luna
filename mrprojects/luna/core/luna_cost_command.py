# Luna Cost Command Module
# Author: Mauricio Ribeiro
# Python: 3.4

from luna import LunaCommand

# Luna Cost Command Class
class LunaCostCommand(LunaCommand):

	def __init__(self):
		self.__command = 'gastei'

	def process(self, speech):
		return 1 if self.__command in speech.split(' ') else 0