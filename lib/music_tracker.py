class MusicTracker():

    def __init__(self):
        self.tracklist = []

    def add(self, track):
        values = track.values()
        for value in values:
            if type(value) != str:
                raise Exception('Can\'t add track information')
            elif value == '':
                raise Exception('Can\'t add empty track name')    
        
        self.tracklist.append(track)
    
    def get_tracklist(self):
        new_list = list(sorted(self.tracklist, key= lambda track : track['artist']))
        return new_list