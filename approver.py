
import pandas as pd
import pymongo
import json
import os
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings = json.loads(open(BASE_DIR+'/Approver/settings.json').read())

data = pd.read_csv(settings['CSV'])
data['priority'] = data['priority'].fillna(0)
data['exposition'] = data['exposition'].fillna(0)
data['asset_value'] = data['asset_value'].fillna(0)

resources_list = list()
for index, row in data.iterrows():
    res = {
        'domain': row['domain'],
        'subdomain': row['subdomain'],
        'url': row['url'],
        'ip': row['ip'],
        'isp': row['isp'],
        'asn': row['asn'],
        'country': row['country'],
        'region': row['region'],
        'city': row['city'],
        'org': row['org'],
        'geoloc': row['geoloc'],
        'first_seen': row['first_seen'],
        'last_seen': row['last_seen'],
        'is_alive': row['is_alive'],
        'has_urls': row['has_urls'],
        'approved': row['approved'],
        'type': row['scan_type'],
        'priority': row['priority'],
        'exposition': row['exposition'],
        'asset_value': row['asset_value']
        }
    resources_list.append(res)

data = {'data': resources_list}

requests.post(settings['VM-Orchestrator']+'/approve_resources/', json=data)