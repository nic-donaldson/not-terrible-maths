import os
import tornado.ioloop
import tornado.web
import tornado.websocket

from chat_manager import ChatManager, Room, User
import configparser
import json

class ChatSocket(tornado.websocket.WebSocketHandler):

	def initialize(self, manager):
		self.manager = manager

	def open(self):

		# See if user has a cookie already
		if not self.get_secure_cookie("id"):
			self.write_message("ERROR: No cookie assigned yet")
			self.close()
		elif manager.user_exists(int(self.get_secure_cookie("id"))):
			# Assign socket to user
			# Disconnect them first just in case
			sock =  manager.disconnect_user(int(self.get_secure_cookie("id")))
			if sock != None:
				sock.close()

			print("User %s connected" % (self.get_secure_cookie("id")))
			manager.connect_user(int(self.get_secure_cookie("id")), self)
			self.write_message("ERROR: chat not implemented yet")
			self.close()
		else:
			self.write_message("ERROR: incorrect cookie, clear cookies")
			self.close()

	def on_message(self, message):
		print("Message received")
		try:
			msg = json.loads(message)
		except ValueError:
			print("Malformed message")


	def on_close(self):
		print("Some socket closed wow")
		if self.get_secure_cookie("id"):
			print("User %s disconnected" % (self.get_secure_cookie("id")))
			manager.disconnect_user(int(self.get_secure_cookie("id")))

class ChatHandler(tornado.web.RequestHandler):
	def get(self):
		if not self.get_secure_cookie("id"):
			self.redirect("/")
		else:
			self.render("templates/chat.html")

class RootHandler(tornado.web.RequestHandler):
	def get(self):
		if not self.get_secure_cookie("id"):
			print("new user connected, asking for name")
			self.render("templates/index.html")
		else:
			self.redirect("/chat")

	def post(self):
		name = self.get_argument("username")
		user_id = manager.add_user(None, name)
		self.set_secure_cookie("id", str(user_id))
		print("User %s given cookie" % (name))
		self.redirect("/chat")
		


manager = ChatManager()

config = configparser.ConfigParser()
config.read('config.ini')

settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "../client"),
	"cookie_secret" : config['DEFAULT']['secret'],
	"xsrf_cookies" : True
}



application = tornado.web.Application([
	(r"/connect", ChatSocket, dict(manager=manager)),
	(r"/", RootHandler),
	(r"/chat", ChatHandler),
], **settings)

if __name__ == "__main__":
	application.listen(9001)
	tornado.ioloop.IOLoop.instance().start()