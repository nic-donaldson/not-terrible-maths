import logging

class ChatManager():
	def __init__(self):

		self.rooms = {}
		self.users = {}
		self.waiting_users = {}
		self.id = 1

	def add_waiting_user(self, socket):
		self.waiting_users[socket] = None

	def transfer_user(self, socket, name):
		if socket in self.waiting_users:
			del self.waiting_users[socket]
			return self.add_user(socket, name)
		else:
			print("user not waiting")

	def add_user(self, socket, name):
		self.users[self.id] = User(self.id, name, socket)
		self.id += 1
		return (self.id-1)




class Room():
	def __init__(self, name):
		self.name = name
		self.users = {}

	def addUser(userObject):
		if userObject.id not in self.users:
			self.users[userObject.id] = userObject
			print("User %s added to room %s." % (userObject.name, self.name))
		else:
			raise RoomError("User already in room!")

	class RoomError(Exception):
		def __init__(self, value):
			self.value = value
		def __str__(self):
			return repr(self.value)

class User():
	def __init__(self, id, name, socket):
		self.id = id
		self.name = name
		self.socket = socket