import os
import tornado.ioloop
import tornado.web
import tornado.websocket

class EchoWebSocket(tornado.websocket.WebSocketHandler):
	def initialize(self, database):
		self.database = database

	def open(self):

		if database['prior'] == None:
			print("New user connected")
			database['prior'] = self
		else:
			print("New user connected, connecting with previous user")
			database['pairs'][database['prior']] = self
			database['pairs'][self] = database['prior']
			database['prior'].write_message("1:Connected to another!")
			self.write_message("2:Connected to another!")
			database['prior'] = None

	def on_message(self, message):
		if self in database['pairs']:
			database['pairs'][self].write_message(message)
		else:
			self.write_message("No friend yet, :(")


	def on_close(self):

		if self in database['pairs']:
			database['pairs'][self].write_message("Your friend has disconnected")
			# if there is no-one else to talk to
			if database['prior'] == None:
				database['prior'] = database['pairs'][self]
				del database['pairs'][self]
				del database['pairs'][database['prior']]
			# if there is someone else to talk to!
			else:
				old_friend = database['pairs'][self]
				del database['pairs'][self]
				database['pairs'][old_friend] = database['prior']
				database['pairs'][database['prior']] = old_friend
				database['prior'] = None

				old_friend.write_message("New friend connected")
				database['pairs'][old_friend].write_message("Friend connected!")
		else:
			if self == database['prior']:
				database['prior'] = None

class RootHandler(tornado.web.RequestHandler):
	def get(self):
		self.redirect("/static/websockets.html")


database = {'pairs' : {}, 'prior' : None}

settings = {
	"static_path": os.path.join(os.path.dirname(__file__), "../client")
}

application = tornado.web.Application([
	(r"/connect", EchoWebSocket, dict(database=database)),
	(r"/", RootHandler),
], **settings)

if __name__ == "__main__":
	application.listen(9001)
	tornado.ioloop.IOLoop.instance().start()