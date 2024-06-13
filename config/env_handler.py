import json

def get_env(env_selected='dev'):
    with open('config/app.json') as f:
        environment_list = {
            'dev': json.load(f)
        }
    return environment_list.get(env_selected, environment_list['dev'])
