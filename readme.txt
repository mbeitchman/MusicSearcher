Marc Beitchman
3/26/2014

The project was developed on Mac OS X using Python 2.7.4 and the Flask micro framework for a basic web server with routing and view templates. Testing was done in Chrome and Firefox on Mac OS X.

Installation:

Run ./setup.sh from the root directory of the app to set up. This script will setup a virtual python environment and install the necessecary Flask files.

Running the server:

Run ./run.py from bash shell and open localhost:5000 in your browser.

Architecture:

The design for my project is based on a microservices architecture (http://martinfowler.com/articles/microservices.html). Microservices are very suitable for scalable systems as they allow for decentralizaion of data storage and efficient scaling of infrastructure among other benefits.

The 'Services' folder in the app directory contains a playlist service and a search service. These classes implement the external endpoint API's for the services. For this application, the services are classes running on the same server as the rest of the app. In a production system, these services would be running on seperate servers. The services take a datastore parameter in the constructor. This is a testability feature as it provides a mechanism to inject a mock datastore into the service.

The 'DataLayer' folder in the app directory contains a playlist and search datalayer implementation. These components define the layer that the end points of the service call to manipulate and retrieve data. The datalayer is a nice abstraction because it can manage accessing data from multiple data sources. For example, the search datalayer, talks to the Spotify API and a local cache. This folder also contains datastore implementation. The datastore is a very simple datastore implemented with a dictionary. The datastore is used as search results cache for the search data layer and as the data store for the playlist service. In a production system, the datastore would be replaced by an interface to a more sophisticate caching system like Redis for the search cache or a document store like MongoDB for the playlist data.

The 'Models' folders in the app directory contains the implementation of the song and playlist classes for the core data objects of the application.

I used a micro framework called Flask for running the server, routing and view templating. I wanted to focus mainly on the backend and Flask provided a very modular, lightweight system that provided an elegant way to take care of the parts of the system that weren't the main focus of the project. I also got to experiment with a new framework which was a lot of fun!

The __init__ file in the app directory creates the instance of the app. The controller file contains the route methods and actions that respond to requests from the browser. The templates folder contains a base.html view template and the musicsearcher.html view template. The base template provides a commen shell for rendering views. The static directory contains the javascript, css and image assets for the application. I used the bootstrap 2.3.2 rendering framework to make the UI look a little nice.

Next Steps:

There are a few features I had in mind but did not have time to implent. 

The playlist service supports CRUD operations for multiple playlists. Unfortunaly, I did not have time to do the UI for multiple playlists. There is a lot more fun that I could have with playlists such as shuffling, recommendations from both an algorithm and from friends on social networks.

The search service only retrieves the first page of at max 100 results from the
Spotify service. I would have liked to implement a paging feature in order to get all of the possible results for a search. 

I am a HUGE fan of unit tests. I definitely implement unit test given more time.

I also would have liked to implement a cache datastore with an LRU replacement algorithm and capacity but did not have time to complete this.

Overall Thoughts:

I enjoyed the project overall. It was fun to brush up on my Python and learn a new framework that I have never used before. It was also a lot of fun to define a scalable service based architecture for a system. I have thought a lot about this so it was fun to put my ideas into code! I also thought the results from the spotify services were interesting. I felt it was a good system design and implementation test.
