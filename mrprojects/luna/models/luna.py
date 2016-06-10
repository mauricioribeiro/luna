# Luna Module
# Author: Mauricio Ribeiro
# Python: 3.4

# Luna Class
class Luna:

	def __init__(self, luna_command_classes):
		self.__command = luna_command_classes
		self.__luna_json_return = {'understood':False, 'message':'', 'data':None}

	def process(self, speech):
		for luna_command in self.__command:
			if luna_command.check(speech):
				self.__luna_json_return['understood'] = True
		return self.__luna_json_return

# Luna Command Abstract Class
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
		return True if self.__command in speech.split(' ') else False

	def process(self, speech):
		raise NotImplementedError('Your class has not "process" method implemented (LunaCommand Abstract Class)')