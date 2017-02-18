
import webapp2
import database

class Event:

    def __init__(self, mood, stress_level, physical_activity_level, self_harm_level, trigger, resolution, additional_notes, photo_url, time):
        """Initialize this event with the given variables"""

        self.id = len(database.events)
        
        self.mood = mood
        self.stress_level = stress_level

        self.physical_activity_level = physical_activity_level
        self.self_harm_level = self_harm_level

        self.trigger = trigger
        self.resolution = resolution
        self.additional_notes = additional_notes

        self.photo_url = photo_url
        self.time = time
