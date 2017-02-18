
import webapp2
from events import MainHandler
from events import EventHandler
from events import ShowEventHandler

# Router
routes = [
    ('/', MainHandler),
    ('/events', EventHandler),
    ('/events/<id>', ShowEventHandler)
]

# Set up application
app = webapp2.WSGIApplication(routes, debug=True)
