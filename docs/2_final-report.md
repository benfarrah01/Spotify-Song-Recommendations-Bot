# Course project final report

## Final title

Daily Song Recommendations tweet

## If you used any data sources, what were they and why?

The only data sources that we use is the Spotify API. The reason why is because it provides a channel between the user and the cloud of data we want to access. The data that we want to access are the Client ID and the secret ID. This is created by using our spotify developer account.  

## How did the final project end up? Were you able to achieve your ideal (or close to it)?

Our final project ended up similar to our initial thoughts where the idea is to pull the most popular song out of a specific genre. This song will be changed everyday, where the bot will tweet out a daily recommendation songs out of spotify. This is done by randomly choosing tyhe genre, then pick a song out of that genre based of the popularity of the song. The statement will be formatted with the song name and the song artists.  

## Did your project change over time? If so, how?

The project does not change over time that much because the process of the project is simple. The only change that we make is not to make every single file for every genre because it allows to make all the work more efficient. For example, if we make a mistake on one part, it will affect the overall result. Therefore, if we solve the problem, it will be solved for the overall result. 

## Describe your approaches and experience with the project.

### What worked?

With this project we did a lot of splitting up work and then later checking eachothers work to catch possible errors. This was a very efficient way of going about the group work. Communication was key throughout the project. While working in diffrent branches, we would bounce ideas off of eachother and try diffrent methods we thought might work until we got one that we liked. We were almost always aware of what everyone was working on and we tried to be on the same page at all times. We would start with a very clumsy code and work on it till it was concise and ran smoothly. All of these approaches were very important to our success.

### What didn't?

We began the project by trying to create a few diffrent specific genre files that we would pull from. There were only 6 or so genres to pull from in this case. Therefore, when paired with our popularity identifier there was likely to be repeated songs for our tweets. This was also a much more difficult way to go about the issue. It had more moving parts and didn't run as well. Instead we created a single genre file that allowed us to utilize many more genres more efficiently.

### What would you have done differently?

We believe that there is always room for improvment when it comes to code. There is always something to add or to make more consise or make easier to use. Had we had more time I believe we would have added more ammenities to the bot in order to make it more appealing to users. We could have perhaps added extra astetics, explicit content protection, or even fun alternatives to just most popular. Maybe in the future we will be able to do so.


### What was the biggest challenge that you overcame? How did you do it?

One of the largest challenges we faced was feeling like we were getting close and then for the sake of improving our code and making our future progress easier, facing what seemed like set backs. We also had a difficult time creating our own empty dictionaries to use. We did solve that challenge only to be faced with new challenges in using those dictionaries. However, in the end we were able to overcome these challenges as a group and with a little help.

## How did you ensure that you were following best practice of ethical botmaking?

> Reflect on this using the list of potential ethical challenges highlighted in the [original ideas document](0_idea.md)

`In order to keep our bot as ethical as possible, it will require some upkeep on our part. If the bot suggests a song that is extremely explicit, we would remove the tweet and make sure it is removed from the pool of songs it could suggest. The Spotify API automatically removes songs from artists who are extraordinarily problematic or in the news due to their misconduct, so we do not have to worry about the bot recommending songs from unscrupulous artists. We also believe that bots should not try to appear human in any way. In order to make it obvious that our bot is NOT human, we will give it a name that implies it is a bot. We will also clearly state that it is a bot in the account's bio.`