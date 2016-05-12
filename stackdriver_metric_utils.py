import datetime
import pprint
import time
import random
from apiclient import discovery
from oauth2client.client import GoogleCredentials
import requests
metadata_server = "http://metadata/computeMetadata/v1/instance/"
metadata_flavor = {'Metadata-Flavor' : 'Google'}


def format_rfc3339(datetime_instance=None):
    """Formats a datetime per RFC 3339.
    :param datetime_instance: Datetime instanec to format, defaults to utcnow
    """
    return datetime_instance.isoformat("T") + "Z"
def get_start_time():
    # Return now- 5 minutes
    start_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=5)
    return format_rfc3339(start_time)
def get_now_rfc3339():
    # Return now
    return format_rfc3339(datetime.datetime.utcnow())
def get_first_day_of_current_month_rfc3339():
    today = datetime.date.today()
    first_of_month_date = datetime.date(today.year, today.month, 1)
    first_of_month_datetime = datetime.datetime.combine(first_of_month_date, datetime.time.min)
    return format_rfc3339(first_of_month_datetime)
def get_http_client():
    """Builds an http client authenticated with the service account credentials"""
    credentials = GoogleCredentials.get_application_default()
    client = discovery.build('monitoring', 'v3', credentials=credentials)
    return client
def get_project_id():
    project_id = requests.get(metadata_server + 'hostname', headers = metadata_flavor).text.split('.')[2]
    return project_id
def get_instance_id():
    instance_id = requests.get(metadata_server + 'hostname', headers = metadata_flavor).text.split('.')[0]
    return instance_id
def delete_metric(metric_name):
    project_id = get_project_id()
    project_resource = "projects/{0}".format(project_id)
    metric = get_metric(metric_name)
    metric_name = project_resource + "/metricDescriptors/" + metric["type"]
    client = get_http_client()
    client.projects().metricDescriptors().delete(name = metric_name).execute()
def write_metric(custom_metric_name, value):
    project_id = get_project_id()
    instance_id = get_instance_id()
    custom_metric = get_metric(custom_metric_name)
    client = get_http_client()
    project_resource = "projects/{0}".format(project_id)
    value = get_dummy_data_point()
    print value
    start_time = get_now_rfc3339()
    end_time = get_now_rfc3339()
    metric_type = custom_metric["type"]
    metric_value_type = custom_metric["valueType"]
    point_value_type = ""
    metric_kind = custom_metric["metricKind"]
    if metric_kind == "CUMULATIVE":
        start_time = get_first_day_of_current_month_rfc3339()
    if metric_value_type == "DOUBLE":
        point_value_type = "doubleValue"
    elif metric_value_type == "INT64":
        point_value_type = "int64Value"
    elif metric_value_type == "BOOL":
        point_value_type = "boolValue"
    timeseries_data = {
        "metric": {
            "type": metric_type,
            "labels": {
            }
        },
        "resource": {
            "type": "gce_instance",
            "labels": {
                "zone": "us-east1-b",
                "instance_id": instance_id
            }
        },
        "valueType": metric_value_type,
        "points": [
            {
                "interval": {
                    "startTime": start_time,
                    "endTime": end_time
                },
                "value": {
                    point_value_type : value
                }
            }
        ],
        "metricKind": metric_kind
    }
    request = client.projects().timeSeries().create(
        name=project_resource, body={"timeSeries":[timeseries_data]})
    request.execute()
def create_metric(project_id, metric_name):
    custom_metric = get_metric(metric_name)
    client = get_http_client()
    project_id = "projects/{0}".format(project_id)
    client.projects().metricDescriptors().create(
        name=project_id, body=custom_metric).execute()
def get_dummy_data_point():
    number = random.randint(0,100)
    print "dummy data point " + str(number)
    return number
def get_metric(metric_name):
    all_metrics = {}
    with open("custom_metrics_dictionary.txt", "r") as inf:
        all_metrics = eval(inf.read())
    return all_metrics[metric_name]
def get_seconds(start_time, end_time):
    diff = end_time - start_time
    diff = diff//1000
    return diff
def get_gigabytes(bytes):
    return bytes//1000000000
all_metrics = {}
with open('custom_metrics_dictionary.txt', 'r') as inf:
    all_metrics = eval(inf.read())
for metric in all_metrics:
    try:
        create_metric(metric)
        print "created " + metric
        time.sleep(3)
        write_metric(metric, 10)
    except Exception:
        pass