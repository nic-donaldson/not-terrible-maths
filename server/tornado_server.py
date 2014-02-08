import os
import tornado.ioloop
import tornado.web
import tornado.websocket

from chat_manager import ChatManager, Room, User
import configparser
import json

class EchoWebSocket(tornado.websocket.WebSocketHandler):

	def initialize(self, manager):
		self.manager = manager

	def open(self):

		# See if user has a cookie already
		if not self.get_secure_cookie("id"):
			# Ask for a name and save user in manager
			print("new user connected, asking for name")
			msg = {
				"type":"request",
				"request":"name"
			}
			self.write_message(json.dumps(msg))
			manager.add_waiting_user(self)

	def on_message(self, message):
		msg = json.loads(message)

		if msg["type"] == "response" and msg["request"] == "name":
			# We now have the user's name
			# Remove from waiting list and add to users
			# Give cookie
			user_id = manager.transfer_user(self, msg["name"])
			self.set_secure_cookie("id", bytes(user_id))
			print("User %s transferred" % (msg["name"]))


	# def initialize(self, database):
	# 	self.database = database

	# def open(self):

	# 	if database['prior'] == None:
	# 		print("New user connected")
	# 		database['prior'] = self
	# 	else:
	# 		print("New user connected, connecting with previous user")
	# 		database['pairs'][database['prior']] = self
	# 		database['pairs'][self] = database['prior']
	# 		database['prior'].write_message("1:Connected to another!")
	# 		self.write_message("2:Connected to another!")
	# 		database['prior'] = None

	# def on_message(self, message):
	# 	if self in database['pairs']:
	# 		database['pairs'][self].write_message(message)
	# 	else:
	# 		self.write_message("No friend yet, :(")


	# def on_close(self):

	# 	if self in database['pairs']:
	# 		database['pairs'][self].write_message("Your friend has disconnected")
	# 		# if there is no-one else to talk to
	# 		if database['prior'] == None:
	# 			database['prior'] = database['pairs'][self]
	# 			del database['pairs'][self]
	# 			del database['pairs'][database['prior']]
	# 		# if there is someone else to talk to!
	# 		else:
	# 			old_friend = database['pairs'][self]
	# 			del database['pairs'][self]
	# 			database['pairs'][old_friend] = database['prior']
	# 			database['pairs'][database['prior']] = old_friend
	# 			database['prior'] = None

	# 			old_friend.write_message("New friend connected")
	# 			database['pairs'][old_friend].write_message("Friend connected!")
	# 	else:
	# 		if self == database['prior']:
	# 			database['prior'] = None

class RootHandler(tornado.web.RequestHandler):
	def get(self):
		self.redirect("/static/websockets.html")

manager = ChatManager()

config = configparser.ConfigParser()
config.read('config.ini')

settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "../client"),
	"cookie_secret" : config['DEFAULT']['secret'],
	"xsrf_cookies" : True
}



application = tornado.web.Application([
	(r"/connect", EchoWebSocket, dict(manager=manager)),
	(r"/", RootHandler),
], **settings)

if __name__ == "__main__":
	application.listen(9001)
	tornado.ioloop.IOLoop.instance().start()