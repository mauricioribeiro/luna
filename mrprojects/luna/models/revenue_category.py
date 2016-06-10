# RevenueCategory Model Class
# Author: Mauricio Ribeiro
# Python: 3.4
# Lang: PT-BR

from django.db import models

class RevenueCategory(models.Model):

	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name