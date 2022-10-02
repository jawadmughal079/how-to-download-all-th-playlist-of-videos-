


print("How To Download The PlaylIST ")


from pytube import Playlist
link =input("Enter the Playlist  link : ")


linkStore = Playlist(link)




for video in linkStore.videos: 
    video.streams.get_highest_resolution().download()

    



