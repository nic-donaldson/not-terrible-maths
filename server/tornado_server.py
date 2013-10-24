import tornado.ioloop
import tornado.web
import tornado.websocket

prior = None
pairs = {}

class EchoWebSocket(tornado.websocket.WebSocketHandler):

	def open(self):
		global prior
		global pairs

		if prior == None:
			print("New user connected")
			prior = self
		else:
			print("New user connected, connecting with previous user")
			pairs[prior] = self
			pairs[self] = prior
			prior.write_message("1:Connected to another!")
			self.write_message("2:Connected to another!")
			prior = None

	def on_message(self, message):
		global prior
		global pairs

		if self in pairs:
			pairs[self].write_message(message)
		else:
			self.write_message("No friend yet, :(")


	def on_close(self):
		global prior
		global pairs

		if self in pairs:
			pairs[self].write_message("Your friend has disconnected")
			# if there is no-one else to talk to
			if prior == None:
				prior = pairs[self]
				del pairs[self]
				del pairs[prior]
			# if there is someone else to talk to!
			else:
				old_friend = pairs[self]
				del pairs[self]
				pairs[old_friend] = prior
				pairs[prior] = old_friend
				prior = None

				old_friend.write_message("New friend connected")
				pairs[old_friend].write_message("Friend connected!")
		else:
			if self == prior:
				prior = None

application = tornado.web.Application([
	(r"/connect", EchoWebSocket),
])

if __name__ == "__main__":
	application.listen(9001)
	tornado.ioloop.IOLoop.instance().start()