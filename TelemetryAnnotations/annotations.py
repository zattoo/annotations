import requests
import os
import datetime
import logging

class TelemetryAnnotation:
    def __init__(self, url_production, url_staging):
        self.url_production = url_production
        self.url_staging = url_staging
        self.logger = logging.getLogger(__name__)

    def send_event_to_endpoint(self, url, annotations):
        """
        Send event data to the specified endpoint.
        """
        try:
            response = requests.post(url, json=annotations)
            response.raise_for_status()  
            self.logger.info("Annotations are sent to the endpoint successfully.")
            return True
        except requests.exceptions.RequestException as e:
            self.logger.info("Failed to send Annotations. Error:", e)
            return False

    def send_telemetry_annotation(self):
        event = {}
        # Environment variables
        dateInfo = os.environ.get('date')
        datetime_obj = datetime.datetime.fromisoformat(dateInfo)

        # Convert datetime object to Unix epoch time and in milliseconds
        epoch_time_ms = int(datetime_obj.timestamp())
        event["date"] = int(epoch_time_ms * 1000)
        event["component"] = os.environ.get('component')
        event["type"] = os.environ.get('type')
        event["tenant_id"] = int(os.environ.get('tenantId'))
        event["version"] = str(os.environ.get('version'))

        # Create annotations dictionary
        annotations = {"events": [event], "v": 1}

        # Send data to the endpoints
        self.send_event_to_endpoint(self.url_production, annotations)
        self.send_event_to_endpoint(self.url_staging, annotations)

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    # Endpoint URL for both staging and production
    URL_PRODUCTION = os.environ.get('urlProduction')
    URL_STAGING = os.environ.get('urlStaging')
    print(URL_PRODUCTION,URL_STAGING)
   # sender = TelemetryAnnotation(URL_PRODUCTION, URL_STAGING)
    #sender.send_telemetry_annotation()
