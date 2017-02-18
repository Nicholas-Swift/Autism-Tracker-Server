
import webapp2
from events import MainHandler
from events import EventHandler

# Router
routes = [
    ('/', MainHandler),
    ('/events', EventHandler)
    ('/events/<id>', EventHandler)
]

# Set up application
app = webapp2.WSGIApplication(routes, debug=True)
