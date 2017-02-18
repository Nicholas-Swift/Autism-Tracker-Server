
import webapp2
import json
from event import Event

# Database
events = []

# Routes
class MainHandler(webapp2.RequestHandler): # /
    def get(self):
        self.response.write('Welcome to the api. Please do /events and /events/<id>')

class EventHandler(webapp2.RequestHandler): # /events
    def get(self):

        # Get all events
        all_events = list(map(lambda x: x.__dict__, get_all_events()))

        # Turn to json
        return_json = json.dumps(all_events)

        # Set up headers
        self.response.headers['Content-Type'] = 'application/json'

        # Return response
        self.response.write(return_json)

    def post(self):
        """Post to server to create a new event"""

        # Create new event
        new_event = create_event("nil")

        # Turn to json
        return_json = json.dumps(new_event.__dict__)

        # Set up headers
        self.response.headers['Content-Type'] = 'application/json'

        # Return response
        self.response.write(return_json)

class ShowEventHandler(webapp2.RequestHandler): # /events/(event_id)
    def get(self, event_id):

        # Find the event
        return_event = get_event(event_id)

        # Error handling
        if return_event is None:
            self.response.write("Fuck dude doesn't work")
            return

        # Turn to json
        return_json = json.dumps(return_event.__dict__)

        # Set up headers
        self.response.headers['Content-Type'] = 'application/json'

        # Return response
        self.response.write(return_json)

# Helper Functions
def get_all_events():
    
    # Return all events
    return events

def get_event(event_id):
    
    # Find correct event
    for i in events:
        if events.id == event_id:
            return i

def create_event(stuff):
    
    # Create new event
    new_event = Event()

    # Append to database
    events.append(new_event)

    # Return event
    return new_event
