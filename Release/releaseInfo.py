
import os
import datetime
import json
import requests

url = "https://events.zahs.tv/pt_annotations"
event={"date": None, "component": "", "type": "", "tenant_id": 1, "version": ""}
annotations = {"events": [{}], "v": 1}
# Access environment variables
dateInfo = os.environ.get('DATE')
datetime_obj = datetime.datetime.fromisoformat(dateInfo)
# Convert datetime object to Unix epoch time
epoch_time = int(datetime_obj.timestamp())

event["date"] = int(epoch_time)
event["component"] = os.environ.get('COMPONENT')
event["type"]  = os.environ.get('TYPE')
event["tenant_id"] = int(os.environ.get('TENANT_ID'))
event["version"] = str(os.environ.get('VERSION'))
annotations["events"]= event

# Create a new dictionary with the desired format
new_data = {"events": [annotations["events"]], "v": annotations["v"]}
response = requests.post(url, json=new_data)

if response.status_code == 200:
        print("Data sent successfully to the endpoint.")
else:
        print("Failed to send data. Status code:", response.status_code)
