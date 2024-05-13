import os
import datetime
import json
import requests

def send_event_to_endpoint(url, event):
    """
    Send event data to the specified endpoint.

    Args:
        url (str): The URL of the endpoint.
        event (dict): Dictionary containing event data.

    Returns:
        bool: True if the data is sent successfully, False otherwise.
    """
    try:
        response = requests.post(url, json=event)
        response.raise_for_status()  # Raise exception for bad response status
        print("Data sent successfully to the endpoint.")
        return True
    except requests.exceptions.RequestException as e:
        print("Failed to send data. Error:", e)
        return False

def send_telemetry_annotation():
        # Endpoint URL for both staging and production
        # url_production = "https://events.zahs.tv/pt_annotations"
        url_staging  =  "https://events-staging.zahs.tv/pt_annotations"
        event = {"date": None, "component": "", "type": "", "tenant_id": None, "version": ""}

        # Environment variables
        dateInfo = os.environ.get('DATE')
        datetime_obj = datetime.datetime.fromisoformat(dateInfo)
        # Convert datetime object to Unix epoch time
        epoch_time = int(datetime_obj.timestamp())

        # Convert datetime object to Unix epoch time and in milliseconds
        epoch_time_ms = int(datetime_obj.timestamp() * 1000)
        event["date"] = int(epoch_time)
        event["component"] = os.environ.get('COMPONENT')
        event["type"]  = os.environ.get('TYPE')
        event["tenant_id"] = int(os.environ.get('TENANT_ID'))
        event["version"] = str(os.environ.get('VERSION'))

        # Create annotations dictionary
        annotations = {"events": [event], "v": 1}

        # Send data to the endpoint
        # send_event_to_endpoint(url_production, annotations)
        # time.sleep(90)
        send_event_to_endpoint(url_staging, annotations)


if __name__ == "__main__":
    send_telemetry_annotation()
