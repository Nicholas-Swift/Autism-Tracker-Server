
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

    # def to_dict(self):
    #     """Return a dictionary representation of this event"""

    #     return_dict = {}
    #     return_dict["id"] = self.id

    #     return_dict["mood"] = self.mood
    #     return_dict["stress_level"] = self.stress_level

    #     return_dict["physical_activity_level"] = self.physical_activity_level
    #     return_dict["self_harm_level"] = self.self_harm_level

    #     return_dict["trigger"] = self.trigger
    #     return_dict["resolution"] = self.resolution
    #     return_dict["additional_notes"] = self.additional_notes

    #     self.photo_url
    #     self.time