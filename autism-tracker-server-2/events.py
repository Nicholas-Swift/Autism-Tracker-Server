import time
import webapp2
import json
from event import Event
import database

# MARK: - Routes
class EventHandler(webapp2.RequestHandler): # /events
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(get_all_events())

    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(create_event(self.request.POST))

    def delete(self):
        database.events = []
        self.response.write("Nuked bro")

class ShowEventHandler(webapp2.RequestHandler): # /events/(event_id)
    def get(self, event_id):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(get_event(event_id))

# MARK: Active Events

class ActiveEventHandler(webapp2.RequestHandler): # /active/events
    def post(self):
        print(self.requst.POST)
        self.response.write("")

# MARK: - Get All Events
def get_all_events():

    # Turn events to list of json
    all_events = list(map(lambda x: x.__dict__, database.events))

    # Return json version
    return json.dumps(all_events)


# MARK: - Get Event
def get_event(event_id):

    # Make sure event_id is an int
    event_id = int(event_id)

    # Find correct event
    for e in database.events:
        if e.id == event_id:

            # Return json version
            return json.dumps(e.__dict__)

    # Error if event is None
    return json.dumps({'Error': 'Did not find event'})


# MARK: - Create Event
def create_event(parameters):

    print(parameters)

    # Create new event
    new_event = Event(parameters['mood'], int(parameters['stress_level']), int(parameters['physical_activity_level']), int(parameters['self_harm_level']), parameters['trigger'], parameters['resolution'], parameters['additional_notes'], parameters['photo_url'], int(time.time()))

    # Append to database
    database.events.append(new_event)

    # Return json version
    return json.dumps(new_event.__dict__)
