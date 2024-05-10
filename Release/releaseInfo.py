
import os
import datetime
import json
import requests

url = "https://events.zahs.tv/pt_annotations"
annotations = {"events" : {},"v": 1}
event = {"date": None, "component": "", "type": "", "tenant_id": "","version": ""}
# Access environment variables
release = os.environ.get('RELEASE_TAG')
dateInfo = os.environ.get('RELEASE_DATE')
datetime_obj = datetime.datetime.fromisoformat(dateInfo)
# Convert datetime object to Unix epoch time
epoch_time = int(datetime_obj.timestamp())

event["date"] = int(epoch_time)
event["component"] = "zolagus"
event["type"]  = "release"
event["tenant_id"] = 1
event["version"] = str(release)
annotations["events"]= event

print(annotations)
reponse = requests.post(url, json=annotations)

if response.status_code == 200:
        print("Data sent successfully to the endpoint.")
else:
  print("Failed to send data. Status code:", response.status_code)

