
import webapp2
from events import MainHandler
from events import EventHandler
from events import ShowEventHandler

# Router
routes = [
    # Main
    webapp2.Route('/', handler=MainHandler),

    # Events
    webapp2.Route('/events', EventHandler),
    webapp2.Route('/events/<event_id>', ShowEventHandler)
]

# Set up application
app = webapp2.WSGIApplication(routes, debug=True)
