class Context(object):

	def __init__(self,name):
		self.lifespan = 2
		self.name = name
		self.active = False

	def activate_context(self):
		self.active = True

	def deactivate_context(self):
		self.active = False

		def decrease_lifespan(self):
			self.lifespan -= 1
			if self.lifespan==0:
				self.deactivate_context()

class FirstGreeting(Context):

	def __init__(self):
		self.lifespan = 1
		self.name = 'FirstGreeting'
		self.active = True

class GetShowtime(Context):

	def __init__(self):
		print('Hi')
		self.lifespan = 1
		self.name = 'GetShowtime'
		self.active = True
        
class Getnooftickets(Context):

	def __init__(self):
		print('Hi')
		self.lifespan = 1
		self.name = 'Getnooftickets'
		self.active = True

class Getconfirmation(Context):

	def __init__(self):
		print('Hi')
		self.lifespan = 1
		self.name = 'Getconfirmation'
		self.active = True

class GetLocation(Context):
	def __init__(self):
		print('Hi')
		self.lifespan = 1
		self.name = 'GetLocation'
		self.active = True

class GetRestaruntLocation(Context):
	def __init__(self):
		print('Hi')
		self.lifespan = 1
		self.name = 'GetRestaruntLocation'
		self.active = True

class GetCostType(Context):
	def __init__(self):
		print('Hi')
		self.lifespan = 1
		self.name = 'GetCostType'
		self.active = True

class GetCuisine(Context):
	def __init__(self):
		print('Hi')
		self.lifespan = 1
		self.name = 'GetCuisine'
		self.active = True

		
class IntentComplete(Context):

	def __init__(self):
		self.lifespan = 1
		self.name = 'IntentComplete'
		self.active = True

class SpellConformation(Context):

	def __init__(self,index,CorrectWord,user_input,context):
		self.lifespan = 1
		self.name = 'SpellConformation'
		self.active = True
		self.index = index
		self.correct = CorrectWord
		self.tobecorrected = user_input
		self.contexttobestored = context
