# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker():

    def __init__(self):
        self.tracklist = []

    def add(self, track):
        # Side-effect:
        # Add track to tracklist
        # Track is a dictionary with three keys:
        # trackname, album, artist
    
    def get_tracklist(self):
        # Returns the tracklist as a list of dictionaries
        # sorted by artist

    # EXTRA
    def get_tracklist_filtered_by_artist(self, artist):
        # Returns only tracks by the supplied artist
        # as a list

    

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
On initialise
self.tracklist is a list
"""
new_music_tracker = MusicTracker()
isinstance(new_music_tracker.tracklist, list)

"""
Given a track name, album and artist
#add adds the track to self.tracklist
And #get_tracklist returns the tracklist
"""
new_music_tracker = MusicTracker()
new_music_tracker.add({'track_name': 'The Bay', 'artist': 'Metronomy', 'album': 'Selftitled' })
result = new_music_tracker.get_tracklist()

assert result == [{'track_name': 'The Bay', 'artist': 'Metronomy', 'album': 'Selftitled' }]

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
