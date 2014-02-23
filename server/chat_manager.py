import logging

class ChatManager():
	def __init__(self):

		self.rooms = {}
		self.users = {}
		
		self.id = 1

	def user_exists(self, id):
		""" Checks to see if a user with id exists.

			(ChatManager, int) -> bool
		"""

		return id in self.users

	def add_user(self, socket, name):
		""" Adds a user to the user list with the given name. Returns
			a unique id for the user.

			(ChatManager, int, string) -> int
		"""

		self.users[self.id] = User(self.id, name, socket)
		self.id += 1
		return (self.id-1)

	def connect_user(self, id, socket):
		""" Attaches the socket to the user with the given id

			(ChatManager, int, int) -> None
		"""

		self.users[id].socket = socket

	def disconnect_user(self, id):
		""" Disconnects the user with the given id and returns
			their socket to be closed by the application.

			(ChatManater, int) -> int
		"""

		sock = self.users[id].socket
		self.users[id].socket = None
		return sock

	def __str__(self):
		return repr(self.rooms) + '\n' + repr(self.users)



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

	def __str__(self):
		return "Room: " + self.name

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