# from scholarly import scholarly
# import jsonpickle
# import json
# from datetime import datetime
# import os
# 
# author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
# scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
# name = author['name']
# author['updated'] = str(datetime.now())
# author['publications'] = {v['author_pub_id']:v for v in author['publications']}
# print(json.dumps(author, indent=2))
# os.makedirs('results', exist_ok=True)
# with open(f'results/gs_data.json', 'w') as outfile:
#     json.dump(author, outfile, ensure_ascii=False)
# 
# shieldio_data = {
#   "schemaVersion": 1,
#   "label": "citations",
#   "message": f"{author['citedby']}",
# }
# with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
#     json.dump(shieldio_data, outfile, ensure_ascii=False)


from scholarly import scholarly
import json
from datetime import datetime
import os

scholar_id = os.environ['GOOGLE_SCHOLAR_ID']

print(f"Fetching Google Scholar profile: {scholar_id}")

author = scholarly.search_author_id(scholar_id)

print("Profile found. Fetching citation statistics...")

author = scholarly.fill(
    author,
    sections=['basics', 'indices']
)

print(f"Citations: {author.get('citedby', 'N/A')}")

author['updated'] = str(datetime.now())

os.makedirs('results', exist_ok=True)

with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldsio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(author['citedby']),
}

with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldsio_data, outfile, ensure_ascii=False)

print("Google Scholar data saved successfully.")
