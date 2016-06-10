# Luna Command Abstract Class
# Author: Mauricio Ribeiro

class LunaCommand(object):

	def __init__(self):
		self.__command = None
		self.__luna_command_json_return = {'command':None, 'parameters':{}, 'return':None}

	def getLunaCommandJsonReturn(self, process_parameters, process_return):
		self.__luna_command_json_return['command'] = self.__command
		self.__luna_command_json_return['parameters'] = process_parameters
		self.__luna_command_json_return['return'] = process_return
		return self.__luna_command_json_return

	def check(self, speech):
		return if self.__command in speech.split(' ')

	def process(self, speech):
		raise NotImplementedError('Your class has not "process" method implemented (LunaCommand Abstract Class)')