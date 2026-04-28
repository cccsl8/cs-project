class Timing:
    def __init__(self, bpm):
        self.bpm = bpm
        self.sec_per_beat = 60 / self.bpm
    
    def beat_to_time(self, beat):
        return beat * self.sec_per_beat