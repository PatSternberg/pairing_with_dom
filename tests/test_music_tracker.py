from lib.music_tracker import *
import pytest


# """
# On initialise
# self.tracklist is a list
# """

def test_tracklist_type_is_a_list():
    new_music_tracker = MusicTracker()
    
    assert isinstance(new_music_tracker.tracklist, list)

# """
# Given a track name, album and artist
# #add adds the track to self.tracklist
# And #get_tracklist returns the tracklist
# """
    
def test_add_and_get_tracklist():    
    new_music_tracker = MusicTracker()
    new_music_tracker.add({'track_name': 'The Bay', 'artist': 'Metronomy', 'album': 'Selftitled' })
    new_music_tracker.add({'track_name': 'S.O.S.', 'artist': 'ABBA', 'album': 'Selftitled' })
    result = new_music_tracker.get_tracklist()

    assert result == [{'track_name': 'S.O.S.', 'artist': 'ABBA', 'album': 'Selftitled' }, {'track_name': 'The Bay', 'artist': 'Metronomy', 'album': 'Selftitled' }]

# """
# Given a track with incorrect type of elements
# #add raises an exception
# """
    
def test_add_incorrect_track_type():  
    new_music_tracker = MusicTracker()

    with pytest.raises(Exception) as e:
        new_music_tracker.add({'track_name': 45, 'artist': True, 'album': 'Selftitled' })
    error = str(e.value)

    assert error == "Can't add track information"


# """
# Given a track with an empty value
# add raises an exception
# """
    
def test_add_empty_track_information(): 
    new_music_tracker = MusicTracker()

    with pytest.raises(Exception) as e:
        new_music_tracker.add({'track_name': '', 'artist': 'Metronomy', 'album': 'Selftitled' })
    error = str(e.value)

    assert error == "Can't add empty track name"