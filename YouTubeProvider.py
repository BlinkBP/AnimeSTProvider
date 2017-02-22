import __main__ as main

class YouTubeProvider():
    login = None
    videos = []

    def youtube_search(self, keywords, addStr):
        if (login != None):
            youtube = login
            searchResponse = youtube.search().list(
                q="{} {}".format(keywords, addStr),
                part="id, snippet",
                maxResults=30
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
            main.window.showError("You are not logged in!")
            
    def get_user_playlists(self):
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
        main.window.showError("You are not logged in!")

    def load_playlist(self, id):
        if login != None:
            youtube = login

            titles = []
            thumbnails = []
            ids = []
            urls = []

            playlist = youtube.playlistItems().list(
                part="snippet, id",
                playlistId=id,
                maxResults=30
            ).execute()

            for video in playlist.get("items", []):
                titles.append(video["snippet"]["title"])
                thumbnails.append(video["snippet"]["thumbnails"]["medium"]["url"])
                ids.append(video["id"])
                urls.append(video["snippet"]["resourceId"]["videoId"])

                return titles, thumbnails, ids, urls

        else:
            main.window.showError("You are not logged in!")
        
    def create_playlist(self, name):
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
            main.window.showError("You are not logged in!")
            
    def delete_playlist(self, playlistId):
        if login != None:
            youtube = login
            youtube.playlists().delete(id=playlistId).execute()
        else:
            main.window.showError("You are not logged in!")

    def add_to_playlist(self, vidId, playId):    
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
            main.window.showError("You are not logged in!")
            
    def delete_from_playlist(self, ID):
        if login != None:
            youtube = login
            youtube.playlistItems().delete(id=ID).execute()
        else:
            main.window.showError("You are not logged in!")
        
    def delete_playlist(self, playlistId):
        if login != None:
            youtube = login
            youtube.playlists().delete(id=playlistId).execute()
        else:
            main.window.showError("You are not logged in!")
