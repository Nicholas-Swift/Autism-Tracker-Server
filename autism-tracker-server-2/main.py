
import webapp2

# Import Events
from events import EventHandler
from events import ShowEventHandler
from webhooks import ActiveHookHandler

# MARK: - Router
routes = [

    # Events
    webapp2.Route('/events', handler=EventHandler),
    webapp2.Route('/events/<event_id>', handler=ShowEventHandler),
    webapp2.Route('/webhooks/events', handler=ActiveHookHandler)
]

# MARK: - Set up app
app = webapp2.WSGIApplication(routes, debug=True)
