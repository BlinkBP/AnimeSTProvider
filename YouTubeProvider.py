import __main__ as main

class YouTubeProvider():
    login = None

    def youtube_search(self, keywords, addStr):
        if (login != None):
            youtube = login
            searchResponse = youtube.search().list(
                q="{} {}".format(keywords, addStr),
                part="id, snippet",
                maxResults=30
            ).execute()

            videos = []
            for video in searchResponse.get("items", []):
                if video["id"]["kind"] == "youtube#video":
                    videos.append(
                        [video["snippet"]["title"],
                         video["snippet"]["thumbnails"]["medium"]["url"],
                         video["id"],
                         video["snippet"]["resourceId"]["videoId"]]))
            return videos
        else:
            main.window.showError("You are not logged in!")
            
    def get_user_playlists(self):
        if login != None:
            youtube = login
            playlistsList = youtube.playlists().list(
                part="snippet",
                mine=True
            ).execute()

            playlists = []
            for playlist in playlistsList.get("items", []):
                playlists.append(
                    playlist["snippet"]["localized"]["title"],
                    playlist["id"]])
            return playlists
    else:
        main.window.showError("You are not logged in!")

    def load_playlist(self, id):
        if login != None:
            youtube = login
            playlistItems = youtube.playlistItems().list(
                part="snippet, id",
                playlistId=id,
                maxResults=30
            ).execute()

            videos = []
            for video in playlistItems.get("items", []):
                videos.append(
                    [video["snippet"]["title"],
                     video["snippet"]["thumbnails"]["medium"]["url"],
                     video["id"],
                     video["snippet"]["resourceId"]["videoId"]])
            return videos
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
