import __main__ as main
import requests
import Image
import ImageQt

from io import BytesIO
from PySide.QtCore import (QRectF, Qt, QByteArray)
from PySide.QtGui import (QPixmap, QImage)

login = None
videos = []

def clear_list(tab):

    if tab == "anime":
        labels = main.window.animeLabels
        for i in range(0, 6):
            labels[i].setText("")
            main.window.animeScenes[i].clear()
            main.window.animeScenes[i].update()
    elif tab == "playlist":
        labels = main.window.videoLabels
        for i in range(0, 6):
            labels[i].setText("")
            main.window.videoScenes[i].clear()
            main.window.videoScenes[i].update()

def fill_thumbnails(thumbnails, tab):

    if tab == "anime":
        views = main.window.animeViews
        scenes = main.window.animeScenes
    else:
        views = main.window.videoViews
        scenes = main.window.videoScenes

    clear_list(tab)

    for i in range(0, len(thumbnails)):
        data = requests.get(thumbnails[i]).content
        image = QImage()
        image.loadFromData(data)
        scenes[i].addPixmap(QPixmap(image))
        views[i].fitInView(QRectF(0, 0, 320, 180), Qt.KeepAspectRatio)
        scenes[i].update()

def fill_labels(titles, tab):

    if tab == "anime":
        labels = main.window.animeLabels
    elif tab == "playlist":
        labels = main.window.videoLabels

    for i in range(0, len(titles)):
        labels[i].setText(titles[i])

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

        for searchResult in searchResponse.get("items", []):
            if searchResult["id"]["kind"] == "youtube#video":
                titles.append(searchResult["snippet"]["title"])
                thumbnails.append(searchResult["snippet"]["thumbnails"]["medium"]["url"])
                ids.append(searchResult["id"])

        fill_thumbnails(thumbnails, "anime")
        fill_labels(titles, "anime")

        return ids

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

        playlist = youtube.playlistItems().list(
            part="snippet, id",
            playlistId=id
            ).execute()

        for video in playlist.get("items", []):
            titles.append(video["snippet"]["title"])
            thumbnails.append(video["snippet"]["thumbnails"]["medium"]["url"])
            ids.append(video["id"])

        fill_thumbnails(thumbnails, "playlist")
        fill_labels(titles, "playlist")

        return ids

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