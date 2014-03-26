from flask import render_template, redirect, request
from app import app
from timeit import default_timer as timer
from app.DataLayer import datastore
from app.Services import searchservice
from app.Services import playlistservice
from app.Models import song

## controller for the music searcher app

## initialize the services and the default global playlist for the application
ps = playlistservice.PlaylistService(datastore.DataStore())
ps.create_playlist("default")
ss = searchservice.SearchService(datastore.DataStore())

# controller action for rendering the app
# uses query string paramater 'q' to pass in search request text
@app.route('/', methods = ['GET'])
def main():
	playlist = ps.get("default")
	search_request = ""
	search_results = None
	elapsed_time = None

	if request.args.get('q'):
		search_request = request.args.get('q')
		start = timer()
		search_results = ss.search(search_request)
		elapsed_time = timer() - start

	return render_template("musicsearcher.html", search_request = search_request, search_results = search_results, playlist = playlist, elapsed_time = elapsed_time)

# controller action for adding songs to a playlist
@app.route('/addsong', methods = ['POST'])
def addsong():
	s = song.Song(name = request.form['name'], album = request.form['album'], 
			artist = request.form['artist'], url = request.form['url'])
	ps.set_song("default", s)

	redirect_url = "/"
	if request.form['search_request']:
		redirect_url = redirect_url + "?q=" + request.form['search_request'] 

	return redirect(redirect_url)

# controller action for removing songs from a playlist
@app.route('/removesong', methods = ['POST'])
def removesong():
	s = song.Song(name = request.form['name'], album = request.form['album'], 
			artist = request.form['artist'], url = request.form['url'])
	
	ps.remove_song("default", s)

	redirect_url = "/"
	if request.form['search_request']:
		redirect_url = redirect_url + "?q=" + request.form['search_request'] 

	return redirect(redirect_url)