
class Pipe:
	def __init__(self, generator):
		self.generator = generator
		self.steps = []
		self.error_callback = None
		self.abort_on_error = False
		
	def peek(self):
		def _peek(x):
			print(x)
			return x
			
		self.steps.append(_peek)
		return self
		
	def next(self, step):
		self.steps.append(step)
		return self
		
	def error(self, error_callback, abort_on_error=False):
		self.error_callback = error_callback
		self.abort_on_error = abort_on_error
		return self
		
	def run(self):
		for x in self.generator:
			result = x
			for step in self.steps:
				result = step(result)
	