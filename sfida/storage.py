import json
import os
import uuid
from datetime import datetime

DB_FILE = 'db.json'

def load_db():
    if not os.path.exists(DB_FILE):
        return {'links': [], 'categories': []}
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {'links': [], 'categories': []}

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_link(original_url, short_url, alias=None, category=None, description=None):
    data = load_db()
    
    new_link = {
        'id': str(uuid.uuid4()),
        'original_url': original_url,
        'short_url': short_url,
        'alias': alias,
        'category': category,
        'description': description,
        'created_at': datetime.now().isoformat()
    }
    
    data['links'].append(new_link)
    
    if category and category not in data['categories']:
        data['categories'].append(category)
        
    save_db(data)
    return new_link

def get_links():
    data = load_db()
    return data['links']

def find_link(query):
    data = load_db()
    results = []
    for link in data['links']:
        if query in link['original_url'] or (link['alias'] and query in link['alias']):
            results.append(link)
    return results

def delete_link(identifier):
    # identifier can be id or alias
    data = load_db()
    original_count = len(data['links'])
    data['links'] = [l for l in data['links'] if l['id'] != identifier and l['alias'] != identifier]
    
    if len(data['links']) < original_count:
        save_db(data)
        return True
    return False
