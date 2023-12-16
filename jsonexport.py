import json

def export_to_json(release_note, filename="release_note.json"):
    with open(filename, 'w') as file:
        json.dump(release_note.__dict__, file, indent=4)

# Export the release note as JSON
export_to_json(release_note)
