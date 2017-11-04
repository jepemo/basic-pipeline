
class Pipe:
	def __init__(self, generator):
		self.generator = generator
		self.steps = []
		
	def next(self, step):
		self.steps.append(step)
		return self
		
	def start(self):
		for x in self.generator:
			result = x
			for step in self.steps:
				result = step(result)
	