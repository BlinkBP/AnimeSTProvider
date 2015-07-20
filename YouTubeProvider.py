import __main__ as main

login = None
videos = []

def youtube_search(keywords, results, addStr):

    if login != None:

        youtube = login

        searchResponse = youtube.search().list(
            q="{} {}".format(keywords, addStr),
            part="id, snippet",
            maxResults=results
            ).execute()

        titles = []
        thumbnails = []
        ids = []
        urls = []

        for video in searchResponse.get("items", []):
            if video["id"]["kind"] == "youtube#video":
                titles.append(video["snippet"]["title"])
                thumbnails.append(video["snippet"]["thumbnails"]["medium"]["url"])
                ids.append(video["id"])
                urls.append(video["id"]["videoId"])

        return titles, thumbnails, ids, urls

    else:
        
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")

def get_user_playlists():

    if login != None:

        youtube = login

        playlists = youtube.playlists().list(
            part="snippet",
            mine=True
            ).execute()

        titles = []
        ids = []

        for playlist in playlists.get("items", []):
            titles.append(playlist["snippet"]["localized"]["title"])
            ids.append(playlist["id"])

        return titles, ids

    else:
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")

def load_playlist(id):

    if login != None:

        youtube = login

        titles = []
        thumbnails = []
        ids = []
        urls = []

        playlist = youtube.playlistItems().list(
            part="snippet, id",
            playlistId=id
            ).execute()

        for video in playlist.get("items", []):
            titles.append(video["snippet"]["title"])
            thumbnails.append(video["snippet"]["thumbnails"]["medium"]["url"])
            ids.append(video["id"])
            urls.append(video["snippet"]["resourceId"]["videoId"])

        return titles, thumbnails, ids, urls

    else:
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")

def create_playlist(name):
    
    if login != None:

        youtube = login

        youtube.playlists().insert(
            part="snippet, status",
            body=dict(
            snippet=dict(
                title=name
                ),
            status=dict(
                privacyStatus="private"
                )
            )
        ).execute()

    else:
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")

def delete_playlist(playlistId):

    if login != None:
        youtube = login
        youtube.playlists().delete(id=playlistId).execute()

    else:
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")

def add_to_playlist(vidId, playId):
    
    if login != None:

        youtube = login

        struct = {
            'snippet':{
                'resourceId': vidId,
                'playlistId': playId
                }
            }

        youtube.playlistItems().insert(
            part="snippet",
            body=struct
        ).execute()

    else:
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")

def delete_from_playlist(Id):
    
    if login != None:

        youtube = login

        youtube.playlistItems().delete(id=Id).execute()

    else:
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")

def delete_playlist(playlistId):

    if login != None:

        youtube = login
        youtube.playlists().delete(id=playlistId).execute()

    else:
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")