class MusicTracker():

    def __init__(self):
        self.tracklist = []

    def add(self, track):
        self.tracklist.append(track)
    
    def get_tracklist(self):
        new_list = list(sorted(self.tracklist, key= lambda track : track['artist']))
        return new_list