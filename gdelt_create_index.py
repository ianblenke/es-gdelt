import requests
import os

from requests.auth import HTTPBasicAuth

ES_HOST_URL = os.environ.get("ES_HOST_URL")
ES_USER = os.environ.get("ES_USER")
ES_PASSWORD = os.environ.get("ES_PASSWORD")
ES_GDELT_INDEX = os.environ.get("ES_GDELT_INDEX")
ES_DELETE_INDEX = os.environ.get("ES_DELETE_INDEX")
URL = ES_HOST_URL + ES_GDELT_INDEX

def create_indice(delete=None):

    if delete:
        res = requests.delete(URL + "-events", auth=HTTPBasicAuth(ES_USER, ES_PASSWORD))
        print res.content
        res = requests.delete(URL + "-gkg", auth=HTTPBasicAuth(ES_USER, ES_PASSWORD))
        print res.content
        res = requests.delete(URL + "-mentions", auth=HTTPBasicAuth(ES_USER, ES_PASSWORD))
        print res.content

    template = open("elasticsearch/gdelt-events-template.json").read()
    res = requests.put(URL + "-events", data=template, auth=HTTPBasicAuth(ES_USER, ES_PASSWORD), headers={'Content-type': 'application/json'})
    print res.content

    template = open("elasticsearch/gdelt-gkg-template.json").read()
    res = requests.put(URL + "-gkg", data=template, auth=HTTPBasicAuth(ES_USER, ES_PASSWORD), headers={'Content-type': 'application/json'})
    print res.content

    template = open("elasticsearch/gdelt-mentions-template.json").read()
    res = requests.put(URL + "-mentions", data=template, auth=HTTPBasicAuth(ES_USER, ES_PASSWORD), headers={'Content-type': 'application/json'})
    print res.content

if __name__ == "__main__":
    if ES_DELETE_INDEX:
        delete = ES_DELETE_INDEX == 'Y'
    else:
        delete = raw_input("Want to delete the actual '{0}' index? Y/N: ".format(ES_GDELT_INDEX)) == "Y"
    create_indice(delete)
