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

        print("POST")
        print(self.request.POST)
        print("\n\n\n")

        print("GET")
        print(self.request.GET)
        print("\n\n\n")

        print("PARAMS")
        print(self.request.params)
        print("\n\n\n")

        self.response.write(create_event(self.request.POST))

    def delete(self):
        database.events = []
        self.response.write("Nuked bro")

class ShowEventHandler(webapp2.RequestHandler): # /events/(event_id)
    def get(self, event_id):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(get_event(event_id))

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

    # TESTING TESTING TESTING PLEASE
    # client = database2.create_client('AIzaSyDa_7NPxtvNXM2Laz0j3cQ')
    # database2.add_task(client)

    # Find correct event
    for e in database.events:
        if e.id == event_id:

            # Return json version
            return json.dumps(e.__dict__)

    # Error if event is None
    return json.dumps({'Error': 'Did not find event'})


# MARK: - Create Event
def create_event(parameters):

    # new_params = {}
    # for key, value in parameters.items():
    #     new_params[key] = value
    #     print('\n\n\n\n')
    #     print(key)
    #     print(type(key))

    #     print(value)
    #     print(type(value))
    # print('new_params')
    # print(new_params)

    new_list = []
    for i in enumerate(parameters.items()):
        for j in i:
            print(j)
            new_list.append(j)

    new_list[1] = new_list[1][0] + '"}'
    new_list[3] = '{' + new_list[3][1][5:]

    print("WOWOWOOWW")

    wow1 = new_list[1].encode('ascii','ignore')
    print(wow1)
    wow1dict = json.loads(wow1)
    print(wow1dict)
    print("wow1dict succeeded")

    wow2 = new_list[3].encode('ascii','ignore')
    print(wow2)
    wow2dict = json.loads(wow2)
    print(wow2dict)
    print("wow2dict succeeded")

    # Merge the dictionaries
    wow1dict.update(wow2dict)

    # Create new event
    new_event = Event(wow1dict['mood'], wow1dict['stress_level'], wow1dict['physical_activity_level'], wow1dict['self_harm_level'], wow1dict['trigger'], wow1dict['resolution'], wow1dict['additional_notes'], wow1dict['photo_url'], int(time.time()))

    # Append to database
    database.events.append(new_event)

    # Return json version
    return json.dumps(new_event.__dict__)
