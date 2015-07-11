import httplib2
import argparse
import YouTubeProvider

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client import tools
from oauth2client.tools import run_flow

loggedIn = False
login = None

def json_log_in(json):

    YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    flow = flow_from_clientsecrets(json, scope=YOUTUBE_READ_WRITE_SCOPE)
    storage = Storage("{}-oauth2.json".format(json[:len(json)-5]))
    credentials = storage.get()

    parser = argparse.ArgumentParser(parents=[tools.argparser])
    flags = parser.parse_args()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, flags)

    login = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, http=credentials.authorize(httplib2.Http()))

    YouTubeProvider.login = login