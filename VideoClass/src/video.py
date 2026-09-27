
class Video:
    def __init__(self):
        self.title = "Avatar"
        self.duration = 90
        self.playback = 0

    def play(self): return "Now Playing: "+ self.title

    def advance(self, minutes):
        if minutes >= 0 and self.playback < self.duration : self.playback += minutes

    def is_finished(self): return self.playback == self.duration

    def restart(self): self.playback = 0

    def time_remaining(self): return self.duration - self.playback



