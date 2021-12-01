# Course project progress

## Using a Markdown `list`, detail the tasks you've completed and describe your progress.

* Create a spotify developer account. Only one person needs to create the account. The reason being is because we just need 1 client ID and secret ID to reference into the spotify account. 
* Download the spotify API to the Jupyter Notebook. Importing Spotipy. This allows to get all the spotify data from each user. 
* Create a python file for each genres we are going to use for the recommendations. 7 genres assigned for each day. There are Pop, R&B, Jazz, Country, Rock, EDM and Rap. 
* The python file will import the spotify playlist to the Jupyter Notebook 
* Create a main function which randomly choose a song from the assigned playlist for that day. 


## Using a Markdown `list`, detail the tasks you still have yet to do. Where are you stuck? Where do you need help?

* Getting the actual name of the song and artist. We have gotten the playlist for each day and genre but right now we are just getting random letters and numbers. We think that they are different songs but get more confused becuase there are only 15 lines that show up when there are definitly more than 15 songs in the plylist.
* To break it down a little more is that we need to get the name of the song and the name of the artist
* Another things that we need to figure out is how to post on a certain days for the certain genres. We have decide that for each day of the week that we will use a different file and post from a different song. This is somethign we plan to do when we get from break. 
* We need to be able to pick a random song from the selected playlist as well.


## Celebrate your successes. What are they?

So far in this project we have had many successes. We created python files for all of our diffrent genres to pick random songs. We figured out how to put the spodify API into jupider and pull our playlist selections from this source. We are getting more efficient at merging files together in the main. Finally, we are doing very well at splitting up work, communicating, and working as a group.

## Highlight your group's most significant on-going challenge. How do you think you might solve it?

The most significant ongoing challenge is how we can actually pick the songs from the playlists to recommend daily. We had issues figuring out how to change the names of the songs from the playlist to the actual name because they ended up printing in code. We will still have to figure out this part that we have come across. We also had a challenge where the playlist was not printing fully and only printing a certain number of songs. We will have to solve these issues by getting help from stackoverflow or other spotify developers themselves. Another on-going challenge is how to actually get the bot to recommend the song at a specific time of the day and every day. We will also have to solve this by possibly using stackoverflow or getting help from TL or Professor Luman.