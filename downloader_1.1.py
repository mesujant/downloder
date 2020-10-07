from pytube import YouTube
import re
from pytube import Playlist
import os

#handling various exception
#checking if file already exists.
#hadling various exception

def download_video(urls, download_dir="/home/synced/Desktop/YouTube/"):
	if isinstance(urls, str):
		urls = [urls]

	choice = input("1)video \n 2) audio \n Enter no. of your choice:")
	for url in urls:
		yt = YouTube(url)
		print(f"downloading {yt.title}...")
		if choice == "1":
			stream = yt.streams.first()
		else:
			stream = yt.streams.get_audio_only()

		stream.download(download_dir)

def download_playlist(url):
	
	# this fixes the empty playlist.videos list
	playlist = Playlist(url)
	playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
	print(len(playlist.video_urls))
	
	folder_name = input("Enter folder you want to save files in:")
	if not os.path.exists(folder_name):
		os.mkdir(folder_name)

	download_video(playlist.video_urls, folder_name+"/")
	
def download_video_from_playlist(url):
	playlist = Playlist(url)
	playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
	print(len(playlist.video_urls))
	download_video(playlist.video_urls[0])

def url_checker(url):
	#need to check the url with regex
	string_regex = "https://www.youtube.com/watch?v="#+"[a-zA-Z0-9@:%._\\+~#?&//=]+"
	if string_regex in url:
   		return True
	return False

if __name__ == '__main__':
	try:
		while True:
			choice = input("1)video download \n2)Playlist download\n3)exit\n")
			if choice ==  "3":
				print("exiting downloader:")
				break
			url = input("Enter url:")
			if url_checker(url):
				if choice == "1":
					if "list" not in url:
						download_video(url)
						print("Download successful:")
					else:
						download_video_from_playlist(url)
						print("url of the playlis but downloaded..:")
				elif choice == "2":
					if "list" in url:
						print("inside when list in url")
						download_playlist(url)
						print("Download successful:")
					else:
						download_video(url)
						print("url doesnt belong to the playlist but downloaded..")
			else:
				print(":INCOMPATIBLE URL:")
				input("press enter to continue..")
	except:
		print("exception occurs:")
		
				