import json
import ./Message
import ./Participant


def parseFacebook(f):
    json_data = f.read()
    parsed_json = json.loads(json_data)

    # Create participants
    participants = list()

    for participant in parsed_json["participants"]:
        participants.append(participant["name"])

    return participants
