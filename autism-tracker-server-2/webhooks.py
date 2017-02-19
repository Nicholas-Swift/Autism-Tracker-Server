import time
import webapp2
import json
import database


# MARK: Active Hooks

class ActiveHookHandler(webapp2.RequestHandler): # /active/events
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(database.webhookdata))

    def post(self):
        print(self.request.POST)
        database.webhookdata.append(dict(self.request.POST))
        print(database.webhookdata)
        self.response.write("")
