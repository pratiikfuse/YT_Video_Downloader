import os
import validators
from pytube import YouTube
import traceback
import time


def downloadvideo(link, quality):
	try:
		yt = YouTube(link)
		print("Downloading : ", yt.title)

		if quality == "360p":
			stream = yt.streams.get_by_itag(18)  # Selecting Quality

		elif quality == "720p":
			stream = yt.streams.get_by_itag(22)  # Selecting Quality

		elif quality == "1080p":
			stream = yt.streams.get_by_itag(137)  # Selecting Quality

		elif quality == "160kbps":
			stream = yt.streams.get_by_itag(251)  # Selecting Quality
		else:
			print("Choose Correct Option")
			exit()

		downloadpath = "C:\\Users\\Prati\\Desktop\\Music"

		if not os.path.isdir(downloadpath):
			os.mkdir(downloadpath)

		stream.download(downloadpath)

	except:
		print("Error Occured")
		traceback.print_exc()
		exit()

	return 1

def main():
	choice  =  -1;
	while(choice != 0):
		print("Enter option from below")
		print("1:download youtube video")
		print("0: exit application")
		choice  = int(input());
		if(choice == 1 ):
			print("paste video link")
			link = input()
			istrue  = validators.utl(link)
			if istrue:
				print("-" * 80)
				print("Choose Quality from below")
				print("360p")
				print("720p")
				print("1080p")
				print("For Audio only")
				print("160kbps")
				print("-" * 80)
				quality = input()
				if (
						quality != "480p" and quality != "360p" and quality != "720p" and quality != "1080p" and quality != "160kbps"):
					print("choose correct quality")
				else:
					starttime = time.time()
					success = downloadvideo(link, quality)
					if success == 1:
						endtime = time.time()
						print("Downloaded SuccessFully")
						print("Time Required to donwload: {:.2f} Minutes".format((endtime - starttime) / 60))
					else:
						print("url is not valid")




if __name__ == "__main__":
	main()
