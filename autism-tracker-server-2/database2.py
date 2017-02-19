
from google.cloud import datastore


def create_client(project_id):
    return datastore.Client(project_id)

def add_task(client):

    task = datastore.Entity(client.key('Task'))
    task.update({
        'name': 'Nick',
        'testing': True,
        'desription': 'Very cool'
    })

    client.put(task)

    return task.key
