from pytube import YouTube
link = "https://www.youtube.com/watch?v=wy3PFkngtUs&ab_channel=Nh%E1%BA%A1cnh%C6%B0Music"
class ytb:
    def __init__(self, link):
        self.link = link
        self.yt = YouTube(self.link)
    def mp3(self, name):
        audio = self.yt.streams.filter(only_audio=True).first()
        audio.download(filename=f'{name}.mp3')
    def mp4(self, name):
        video = self.yt.streams.filter(progressive=True, file_extension="mp4").first()
        video.download(filename=f'{name}.mp4')
a = ytb(link)
a.mp3('hojc')