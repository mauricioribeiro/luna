# Luna Module
# Author: Mauricio Ribeiro
# Python: 3.4

# Luna Class
class Luna:

	def __init__(self, luna_command_classes):
		self.__command = luna_command_classes

	def getLunaJsonReturn(self):
		return {'understood':False, 'data':None}

	def process(self, speech):
		r = self.getLunaJsonReturn()
		for luna_command_class in self.__command:
			luna_command = luna_command_class()
			if luna_command.check(speech):
				r['understood'] = True
				r['data'] = luna_command.process(speech)
		return r

# Luna Command Abstract Class
class LunaCommand(object):

	def __init__(self):
		self._command = None

	def getLunaCommandJsonReturn(self, process_parameters = {}, process_return = None):
		return {'command':self._command, 'parameters':process_parameters, 'return':process_return}

	def check(self, speech):
		return True if self._command in speech.split(' ') else False

	def process(self, speech):
		raise NotImplementedError('Your class has not "process" method implemented (LunaCommand Abstract Class)')