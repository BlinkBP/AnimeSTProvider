import __main__ as main
import requests
import Image
import ImageQt

from io import BytesIO
from PySide.QtCore import (QRectF, Qt, QByteArray)
from PySide.QtGui import (QPixmap)

login = None
videos = []

def fill_thumbnails(thumbnails):

        views = [main.window.animeView0, main.window.animeView1, main.window.animeView2,
                main.window.animeView3, main.window.animeView4, main.window.animeView5]

        for i in range(0, 6):
            views[i].setScene(main.window.scenes[i])
            main.window.scenes[i].clear()
            pixmap = QPixmap(480, 360)
            ok = pixmap.loadFromData(QByteArray(requests.get(thumbnails[i]).content))
            if ok:
                main.window.scenes[i].addPixmap(pixmap)
                views[i].fitInView(QRectF(0, 0, 480, 360), Qt.KeepAspectRatio)
                main.window.scenes[i].update()
            else:
                print("Thumbnail error!")

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
                videos.append(u"{}".format(searchResult["snippet"]["title"]))
                thumbnails.append(searchResult["snippet"]["thumbnails"]["medium"]["url"])

        fill_thumbnails(thumbnails)

    else:
        
        main.window.statusBar().showMessage("You are not logged in!")
        print("You are not logged in!")