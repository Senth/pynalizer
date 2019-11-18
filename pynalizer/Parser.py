import json
from .Message import Message
from .Participant import Participant

def parse_obj(dct):
    for key in dct:
        if isinstance(dct[key], str):
            dct[key] = dct[key].encode('latin1').decode('utf8')
        pass
    return dct

def parse_facebook(f):
    json_data = f.read()
    parsed_json = json.loads(json_data, object_hook=parse_obj)

    # Create participants
    participants = {}

    # Get participants
    for participant in parsed_json['participants']:
        name = participant['name']
        participants[name] = Participant(name)

    # Go through all messages
    for message in parsed_json['messages']:
        if 'content' in message:
            participant = participants[message['sender_name']]
            participant.add_message(Message(message['timestamp_ms'], message['content']))

    return participants
