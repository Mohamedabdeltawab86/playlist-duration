from pytube import YouTube, Playlist
import datetime


class mytimedelta(datetime.timedelta):
    def __str__(self):
        seconds = self.total_seconds()
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f'{int(hours)}:{int(minutes)}'


link = ["https://www.youtube.com/watch?v=yh0E1Vm0oHM&list=PLMESC_UFcDHKHeisGQSxCD3jsGGoDiDNP"]


duration_list = []
plylst = Playlist(link)

for video in plylst:
    v = YouTube(video)
    duration_list.append(v.length)

total_dur_in_sec = sum(duration_list)

td = mytimedelta(seconds=total_dur_in_sec)

print(str(td))
