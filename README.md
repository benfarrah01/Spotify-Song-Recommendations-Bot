# CMPSC 100: Fall 2021, Course Project

* Distributed: 3 November
* Due: Various dates (see [requirements](#Requirements) below)

## Follow the test bot!

* https://twitter.com/chomp_bot

The bot is a private account. The reason for this: if, at any time, folks tweet any information that would identify them, this protects against other folks discovering that. If you're already on Twitter, follow the account and the instructor will approve you to follow and view the timeline.

This is helpful for verification that your bot is _actually_ doing something. At least one member of your team should follow the bot; you can create a "throw-away" account to do so, should you need to.

## Table of Contents

* [Overview](#Overview)
* [Supporting Readings](#Supporting-readings)
* [Supporting Examples](#Supporting-examples)
* [Evaluation](#Evaluation)
  * [Requirements](#Requirements)
    * [The docs](#The-docs)
    * [The code](#The-code)
    * [The repository](#The-repository)
* [Some resources](#Some-resources)

## Overview

This semester, in the course of learning fundamental computational concepts using Python, you've been using structured, semi-guided exercises to explore topics. This project invites you to explore and expand your knowledge in greater detail by applying your skills to a different kind of "problem": one of creating a Twitter bot which engages in some sort of creative expression which _could include_ (but is not limited to):

* drawing
* interactive chat
* analysis
* "read-only" posts

## Supporting readings

### Working definitions

* [Wooley et al. - How to Think about Bots](https://points.datasociety.net/how-to-think-about-bots-1ccb6c396326)
* [Parrish - Bots: A Definition...](https://points.datasociety.net/bots-a-definition-and-some-historical-threads-47738c8ab1ce)

### Ethics

* [O'Leary - Ethical bot-making](http://mewo2.com/notes/bot-ethics/)
* [Kazemi - Basic Twitter bot etiquette](http://tinysubversions.com/2013/03/basic-twitter-bot-etiquette/)
* [Jeong - How to Make a Bot That Isn't Racist](https://www.vice.com/en/article/mg7g3y/how-to-make-a-not-racist-bot)
* [Daly - Ethical Imperatives in AI and Generative Art](https://worldwritable.com/ethical-imperatives-in-ai-and-generative-art-b8cf51af4c5)

## Supporting examples

* [Magical Realism Bot](https://twitter.com/MagicRealismBot)
* [Olivia Taters](https://twitter.com/oliviataters)
* [Crooked Cosmos](https://twitter.com/CrookedCosmos)
* [Soft Landscapes](https://twitter.com/softlandscapes)
* [Emoji Mashup Bot](https://twitter.com/EmojiMashupBot)
* [Weird Spy Satellite](https://twitter.com/WeirdSatellite)
* [DoDEdits](https://twitter.com/DoDEdits)
* [Last 100 Bills](https://twitter.com/last100bills)
* [Buoy Pix](https://twitter.com/buoypix)
* [Various dictator air travel alert bots](https://twitter.com/i/lists/1230069925504520194)
* [Real Time Bus](https://twitter.com/realtimebus)

And many, many more on [BotWiki](https://botwiki.org/bots/) and elsewhere.

## Evaluation

|Type                      |Point value |
|--------------------------|------------|
|Documentation             |120 pts.    |
|Working code and output   |80 pts.     |
|                          |            |
|Total                     |200 pts.     |
|                          |20% of course|

Though being a completely arbitrary measure, your creative intent with this project is the goal.

Simply put, the outcome of this project should be one of the following:

But those general goals are a bit too easy. There exist more requirements.

### Requirements

|Component              |Due Date       | Weight |
|:----------------------|:--------------|:-------|
|Idea                   | 12 November    |40 pts. |
|Progress report        | 19 November   |40 pts. |
|Final report           | 10 December   |40 pts. |
|Final code and output  | 10 December   |80 pts. |
|                       |               |        |
|Total                  |               |200 pts.|

<div class="alert alert-block alert-danger">
    <p><b>You must be able to run your program when it's graded</b>. If it can't run, the "<b>Working code and output</b>" category will be assessed a <b>0</b>, which means that the maximum score for any project <em>not</em> running will be a <b>60%</b> (120 out of 200).
</div>

<div class="alert alert-block alert-warning">
<p>This project assumes a very high level of autonomy. Meeting due dates is a key way to demonstrate that you're on track and that you're doing well with this kind of "free-range" project. Some advice: work iteratively (that is, in pieces over time) to complete the work and not let the due date sneak up on you. A project like this is no fun if you start it the night before.</p>
<p>Plus, by that time, you've already missed a bunch of deadlines.</p>
<p>(And have upset your group.)</p>
</div>

#### The docs

Each of these documents already exists in the `docs` directory. It is up to your team to complete them.

##### Ideas

Especially as your group considers ideas that you'd like to implement, try not to think too much about _how_ you're going to do it. Use the bots we're going to study as a guide toward thinking about _what's possible_, and we can scale up or back from there. Conceptualize freely -- don't get mired in the details yet.

* An `idea` of _no fewer_ than 100 words which:
  * Proposes a tentative/working/permanent title for your project
  * Describes the project you intend to create
  * Categorizes the project using Allison Parrish's four-class system
  * Your motivation or interest in doing so
  * Potential roadblocks or perceived challenges
  * A description of the _ideal_ outcome/output

<div class="alert alert-block alert-danger">
    <p>The instructor must approve your idea!</p>
</div>

##### Progress report

* A `progress report` of _no fewer_ than 200 words that:
  * Describes the state of your project: where are you at? What do you still need to complete?
    * This should take the form of a Markdown list of outstanding tasks and a brief paragraph describing your progress
  * Summarizes your current challenges: where are you stuck? What could you use help with?
  * Celebrates your successes: surely you have some.
  
##### Final report  

* A `final report` of _at least_ 300 words which:
  * Contains the final title
  * Summarizes your end-of-project thoughts: how do you feel about the outcome of your project?
  * Describes how your project changed over time -- did you need to make it more complex? Simpler? How/why?
  * Contains a "post-mortem" which thinks about: 
    * what worked? 
    * what didn't? 
    * what would you have done differently?
    * what was the biggest challenge that you overcame? How did you do it?

#### The code

<div class="alert alert-block alert-danger">
<p>All code must be placed in the `src` directory.</p>
</div>

While there's no objective rule or law of what makes a project complex enough, the instructor will

##### `main.py`

The `main.py` file is _only responsible for sending messages to Twitter_. Any additional functionality _must_ be written in a separate `class` (i.e. a `module`). These `module`s need to be `import`ed from the `main.py` file.

##### `module`s

You may create new modules by right-clicking in the `File Explorer` and selecting the `New Python File` menu item. This will create a new file which you can rename by right-clicking the file and choosing the `Rename` option.

<div class="alert alert-block alert-warning">
    <p>Do not name files using <b>spaces</b> or <b>dashes</b>. Follow all Python variable naming rules when creating these files.</p>
</div>

###### A note on external libraries and modules

As you conceptualize what you'd like to do with this project, it's likely that there's a module out there that could help you. While you're more than able to find one to tell me about, it's more probable that I'll be able to tell you about something that could speed along your work.

You do not have the ability to install additional libraries on the server. However, if you request an additional module, the instructor _can_. **However, the instructor reserves the right to choose not to install a requested module _and_ provide a reason why**. We do have some additional functionality already on the server:

* `markovify`
  * Generates fake text from a set of sources you provide
* `PIL`
  * Draws and edits images
* `opencv`
  * Does "computer vision"
* `spaCy`
  * Performs natural language processing (NLP)
  
As much as we can, we'll look at these during our lab and at the end of the week.

Some of these we haven't seen or discussed. Odds are, if there's a module you'd like to use, we haven't. Though glad to talk with you about using any "non-standard" modules, it's up to you to really integrate them into your project through exploration or trial-and-error. A suggested start: reviewing documentation or reading about how other folks solved similar problems.

**This project can be completed with interesting output using only the modules we already have.**

#### The repository

Because this work should take place iteratively, this repository requires at least _20_ `commit`s.

## Some resources

Struggling for what to do with a text or with images? Here are two resources which may help:

* Darius K.'s corpora madness
  * A group of many, many `JSON` files located in the `src/data/corpora` directory
* [Project Gutenberg](https://www.gutenberg.org/)
* [Unsplash API](https://unsplash.com/developers)
* [Flickr API](https://www.flickr.com/services/api/)

## Note about the conclusion of the project

It's possible that some teams will want their automated account to live in perpetuity on its own. For groups interested in doing this, the instructor will guide interested students through creating a "bot" account on Twitter and automating it.