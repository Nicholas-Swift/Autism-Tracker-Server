
import webapp2

# Import Events
from events import EventHandler
from events import ShowEventHandler

# MARK: - Router
routes = [

    # Events
    webapp2.Route('/events', handler=EventHandler),
    webapp2.Route('/events/<event_id>', handler=ShowEventHandler)
    webapp2.Route('active/events', handler=ActiveEventHandler)
]

# MARK: - Set up app
app = webapp2.WSGIApplication(routes, debug=True)
