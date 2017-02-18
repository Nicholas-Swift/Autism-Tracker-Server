
import webapp2
import json
from event import Event

# Database
events_database = []

# MARK: - Routes
class EventHandler(webapp2.RequestHandler): # /events
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(get_all_events())

    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(create_event())

class ShowEventHandler(webapp2.RequestHandler): # /events/(event_id)
    def get(self, event_id):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(get_event(event_id))


# MARK: - Get All Events
def get_all_events():
    
    # Turn events to list of json
    all_events = list(map(lambda x: x.__dict__, events_database))

    # Return json version
    return json.dumps(all_events)

# MARK: - Get Event
def get_event(event_id):
    
    # Make sure event_id is an int
    event_id = int(event_id)

    # Find correct event
    for e in events_database:
        if e.id == event_id:

            # Return json version
            return json.dumps(e.__dict__)

    # Error if event is None
    return json.dumps({'Error': 'Did not find event'})

# MARK: - Create Event
def create_event():
    
    # Create new event
    new_event = Event()

    # Append to database
    events_database.append(new_event)

    # Return json version
    return json.dumps(new_event.__dict__)

