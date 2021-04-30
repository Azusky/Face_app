import json

def loadConfig(settings):
    file_settings = open(f'{settings}.json')
    settings = json.load(file_settings)
    return settings
