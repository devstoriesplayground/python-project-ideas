import yt_dlp


def main():
    print("WELCOME TO DEVSTORIES PLAYGROUND - YOUTUBE DOWNLOADER")
    try:
        youtube_url = input('Enter your youtube URL: ')
        if 'https' in youtube_url:
            ydl_opts = {}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])
    except Exception as ex:
        print(f"Error encountered -- {ex}")


if __name__ == "__main__":
    main()