from pytube import YouTube
#provide options for various for resolution
#provide options for sudio
#cipher
#handle exception

path = '/home/synced/Desktop/youtube/'
def download_video(url , download_dir):
	try:
		yt = YouTube(url)
		stream = yt.streams.first()
		print(f"Downloading {yt.title} ...")
		stream.download(download_dir)
	except:
		print("cant read url")


def download_whole_playlist_II(url , folder_name):
	import re
	from pytube import Playlist
	import os
	os.mkdir(folder_name)
	#download_dir = os.path.join(path , folder_name)
	#print(download_dir)
	#input()

	#YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
	#DOWNLOAD_DIR = '/home/synced/Desktop/youtube/FRONT END DEVELOPMENT/'
	playlist = Playlist(url)

	# this fixes the empty playlist.videos list
	playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

	print(len(playlist.video_urls))

	for url in playlist.video_urls:
	    download_video(url , (folder_name+"/"))

	# physically downloading the audio track
	'''
	for video in playlist.videos:
	    video = video.streams.get_by_itag('22')
	    print(f"Downloading {video.title}")
	    video.download(output_path=DOWNLOAD_DIR)
	'''

if __name__ == '__main__':
	while True:
		print("1)Download a video\n2)Download whole playlist:")
		choice = input("\n Enter choice to proceed:")
		if choice == "1":
			url = input("Enter Url:")
			download_video(url)
		else:
			url = input("Enter playlist url:")
			folder_name = input("enter folder name to save in :")
			download_whole_playlist_II(url , folder_name)


	 