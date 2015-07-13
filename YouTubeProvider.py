import __main__ as main
import requests
import Image
import ImageQt

from io import BytesIO
from PySide.QtCore import (QRectF, Qt, QByteArray)
from PySide.QtGui import (QPixmap, QImage)

login = None
videos = []

def fill_thumbnails(thumbnails):

    views = [main.window.animeView0, main.window.animeView1, main.window.animeView2,
            main.window.animeView3, main.window.animeView4, main.window.animeView5]

    for i in range(0, 6):
        views[i].setScene(main.window.scenes[i])
        main.window.scenes[i].clear()
        data = requests.get(thumbnails[i]).content
        image = QImage()
        image.loadFromData(data)
        main.window.scenes[i].addPixmap(QPixmap(image))
        views[i].fitInView(QRectF(0, 0, 320, 180), Qt.KeepAspectRatio)
        main.window.scenes[i].update()

def fill_labels(videos):

    labels = [main.window.animeLabel0, main.window.animeLabel1, main.window.animeLabel2,
             main.window.animeLabel3, main.window.animeLabel4, main.window.animeLabel5]
			 
    for i in range(0, 6):
	    labels[i].setText(videos[i])
	
def youtube_search(keywords, results):

    if login != None:
        youtube = login

        searchResponse = youtube.search().list(
            q=keywords,
            part="id, snippet",
            maxResults=results
            ).execute()

        videos = []
        thumbnails = []

        for searchResult in searchResponse.get("items", []):
            if searchResult["id"]["kind"] == "youtube#video":
                videos.append(searchResult["snippet"]["title"])
                thumbnails.append(searchResult["snippet"]["thumbnails"]["medium"]["url"])

        fill_thumbnails(thumbnails)
        fill_labels(videos)

    else:
        
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")

def get_user_playlists():

    if login != None:
        youtube = login

        playlists = youtube.playlists().list(part="snippet", mine=True).execute()

        titles = []
        ids = []

        for playlist in playlists.get("items", []):
            titles.append(playlist["snippet"]["localized"]["title"])
            ids.append(playlist["id"])

        return titles, ids

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