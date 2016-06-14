# Luna Cost Command Module
# Author: Mauricio Ribeiro
# Python: 3.4

from core.luna import LunaCommand

import re

# Luna Cost Command Class
class LunaCostCommand(LunaCommand):

	def __init__(self):
		self._command = 'gastei'

	def process(self, speech):
		r = self.getLunaCommandJsonReturn()
		p = {'costs': [], 'category': None }
		costs = re.findall(r"\w\$\s([0-9,.]+)",speech)
		if 'r$' in speech.lower() and costs:
			for c in costs:
				self.save(float(c.replace('.','').replace(',','.')))
			p['costs'] = costs if len(costs) > 1 else costs[0]
			r['parameters'] = p
		return r

	def save(self, cost, category = None):
		# store on model
		print('cost %.2f saved' %cost)
		return False