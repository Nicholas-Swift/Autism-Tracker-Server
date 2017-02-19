import time
import webapp2
import json
import database


# MARK: Active Hooks

class ActiveHookHandler(webapp2.RequestHandler): # /active/events
    def post(self):
        print(self.request.POST)
        database.webhookdata.append(self.request.POST)
        print(database.webhookdata)
        self.response.write("")
