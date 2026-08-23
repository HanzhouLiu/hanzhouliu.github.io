import os
import json
from datetime import datetime
from scholarly import scholarly

scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID') or 'DYha9k0AAAAJ'

try:
    print(f"Fetching Google Scholar data for ID: {scholar_id}")
    author: dict = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    author['updated'] = str(datetime.now())
    if 'publications' in author and isinstance(author['publications'], list):
        author['publications'] = {v.get('author_pub_id', idx): v for idx, v in enumerate(author['publications'])}
    
    os.makedirs('results', exist_ok=True)
    with open('results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author.get('citedby', 0)}",
    }
    with open('results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)
    print("Successfully fetched and saved Google Scholar data.")
except Exception as e:
    print(f"Error fetching Google Scholar data: {e}")
    # Still write a valid minimal fallback if network or rate limit occurs
    os.makedirs('results', exist_ok=True)
    if not os.path.exists('results/gs_data.json'):
        with open('results/gs_data.json', 'w') as outfile:
            json.dump({"updated": str(datetime.now()), "scholar_id": scholar_id}, outfile)
    if not os.path.exists('results/gs_data_shieldsio.json'):
        with open('results/gs_data_shieldsio.json', 'w') as outfile:
            json.dump({"schemaVersion": 1, "label": "citations", "message": "280+"}, outfile)
