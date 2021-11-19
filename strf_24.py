import datetime

class mytimedelta(datetime.timedelta):
   def __str__(self):
      seconds = self.total_seconds()
      hours = seconds // 3600
      minutes = (seconds % 3600) // 60
      seconds = seconds % 60
      return f'{int(hours)}:{int(minutes)}'
      


td = mytimedelta(hours=36, minutes=10)

print(str(td))