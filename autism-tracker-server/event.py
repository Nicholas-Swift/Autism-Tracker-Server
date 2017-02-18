
import webapp2

class Event:

    def __init__(self):
        """Initialize this event with the given variables"""

        self.id = 7
        
        self.mood = "Happy"
        self.stress_level = 5

        self.physical_activity_level = 8
        self.self_harm_level = 9

        self.trigger = "the trigger was something"
        self.resolution = "Resolved by this solution"
        self.additional_notes = "Here are some additional notes about the situation"

        self.photo_url = "url_to_photo"
        self.time = "Friday"
        