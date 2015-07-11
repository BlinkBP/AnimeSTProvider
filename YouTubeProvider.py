login = None
videos = []

def youtube_search(keywords, results):

    if login != None:
        youtube = login

        searchResponse = youtube.search().list(
            q=keywords,
            part="id, snippet",
            maxResults=results
            ).execute()

        videos = []

        for searchResult in searchResponse.get("items", []):
            if searchResult["id"]["kind"] == "youtube#video":
                videos.append("%s (%s)" % (searchResult["snippet"]["title"],
                                        searchResult["id"]["videoId"]))

        print("Videos:\n", "\n".join(videos), "\n")

    else:

        print("You are not logged in!")
