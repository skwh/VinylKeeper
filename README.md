# Vinyl Keeper App, v0.1.0
A webapp for storing information about vinyl records in a personal collection.

More of a personal experiment and project than a production-ready idea.

Front-end powered by Angular and many Angular Material components. Backend with Python and SQLite. 

### Planned Features:
* Have a persistent collection of records
* Add and remove records from your collection
* See a list of records with their cover art
* See a list of artists and the records they are associated with
* Download cover art from the internet rather than scan it or take photos of it
* Search & filter by artist and title
* Favorite records so they are shown immediately

#### Far-off features:
* Store a track list for each record
* Link to record / track on Spotify or other music service


### In-Progress Features:
* _List of records with cover art_ => Finalizing design
* _Persistent collection of records_ 
* _General design and concept_

## Testing 
I'm trying to go for full code coverage with this project.

Currently, tests are broken up into front end and back end tests. There is an Angular test suite in VinylKeeper/, and a
Python test suite seen in the `*_test.py` files. I run the tests in Intellij IDEA with a special run config.

I'm planning on adding a script which will run all the tests at once, without needing Intellij IDEA.
