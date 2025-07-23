# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=dDbfmRDWAv0
- **Duration:** 28:51
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 5579
- **Transcript Generated:** 2025-03-30 23:48:52

## Transcript


### Minute 0

[00:00] what's up Engineers welcome back Andy
[00:02] Deb danan here 12 days of open AI went
[00:05] out with a bang they announced 03 and
[00:07] Next Generation Benchmark breaking
[00:10] reasoning model Google's Gemini 2.0
[00:13] flash is very clearly absolutely cracked
[00:16] and it's still 100% free the sleeping
[00:19] giant has awoken I have no idea how
[00:22] Google is able to offer this at scale oh
[00:25] wait I do they're rich and they want to
[00:27] get developers like you and I on their
[00:29] side not going to lie it's working
[00:31] meanwhile we have anthropic to me they
[00:34] seem like the cool guy in the corner at
[00:36] the party having a good time like it
[00:38] knows something everyone else does not
[00:41] I'm confident we'll see something
[00:42] absolutely insane out of anthropic
[00:44] relatively soon last but not least of
[00:46] course we have Lama 4 right around the
[00:50] corner it's going to have multiple
[00:51] releases really really excited for this
[00:53] tons and tons of models released are
[00:55] fine tunes on top of the Llama series
[00:58] with these next generation models right

### Minute 1

[01:01] around the corner the question for you
[01:03] and I as engineers and product Builders
[01:05] Remains the Same how can we use as much
[01:08] compute as possible with powerful models
[01:12] and the best AI coding assistance and AI
[01:14] tooling to build tons of software at
[01:17] higher rates than ever while maintaining
[01:20] high quality in this video I want to
[01:22] showcase a powerful promp chain built
[01:25] into my favorite AI coding assistant AER
[01:28] this promp chain is called architect
[01:30] mode architect mode is simple it's a
[01:32] prompt chain of length two where you
[01:34] have one model that drafts your code
[01:37] second model is the editor the editor
[01:39] takes the draft from the architect and
[01:41] generates real working code this
[01:44] workflow is the best way to understand
[01:47] what's coming next a topic we'll discuss
[01:49] more in this video with all the hype
[01:51] around Gemini 2.0 flash I thought it
[01:54] would be cool to pit it up against the
[01:56] reigning Undisputed Champion Claude 3.5

### Minute 2

[02:00] son it in this video we're going to boot
[02:01] up two AI coding assistants and see if
[02:04] Gemini 2.0 flash can code like the
[02:07] champion near the end of the video I
[02:08] have a massive announcement and a new
[02:10] opportunity for you I'm insanely excited
[02:12] to finally release if you ride code with
[02:15] AI stay tuned so you don't miss
[02:19] that what are we working on to show off
[02:22] this powerful prompt chaining technique
[02:24] using AER let's open up vs code let's
[02:26] break down what's happening here so on
[02:28] the left I have an AER setup command
[02:31] that is going to start our AI coding
[02:32] assistant in architect mode where we're
[02:35] running two models the architect is
[02:38] going to be Gemini 2.0 Flash and the
[02:41] editor is going to be Gemini 2.0 Flash
[02:44] the model is effectively talking to
[02:46] itself one time it's thinking the other
[02:48] time it's editing and then on the right
[02:50] we have that exact same thing with the
[02:52] reigning Champion the best llm for AI
[02:56] coding hands down the only exception to
[02:58] this now is the brand new 01 series

### Minute 3

[03:01] that's slowly rolling out we're going to
[03:03] be covering that on the channel in the
[03:04] future yes always this is going to
[03:06] accept the architext changes anytime
[03:09] they're suggested and then we have a
[03:11] brand new loading feature out of Aer
[03:13] that lets you save and reload sets of
[03:16] context all I'm going to do here is copy
[03:18] this paste it inside a terminal and what
[03:22] you'll see here is AER will boot up in
[03:24] architect mode and it will add every one
[03:28] of these files in this .or file to the
[03:31] context we're going to do the exact same
[03:33] thing on the left side so we're going to
[03:35] boot up Gemini and you can see we have
[03:37] the exact same context if we type SL
[03:39] tokens Gemini 2.0 flash is completely
[03:42] free with a million tokens in available
[03:46] context window if we run tokens on the
[03:47] red side claw 3.5 Sonet of course has a
[03:50] price tag to it we're running at about 1
[03:52] cent per prompt this is of course well
[03:55] within the bounds of what we're willing
[03:57] to pay to get a lot done in fraction of

### Minute 4

[04:00] the time it used to take so here are two
[04:02] sets of models we're running two Geminis
[04:04] on the left and two Cloud 3.5 sonets on
[04:07] the right so this is great we have our
[04:08] AI coding assistant but what are we
[04:10] actually updating what is this code what
[04:12] are these files I have this project that
[04:14] I've been building up is a personal
[04:15] knowledge base for your AI agents this
[04:18] is going to become more relevant we're
[04:19] going to talk about this code base more
[04:21] on this channel in 2025 but you can see
[04:24] here you can do a couple very simple
[04:26] things you can add arbitrary content
[04:28] list all of your cont content you can
[04:30] find similar content via embeddings
[04:32] remove content and back up the database
[04:35] everything here runs on a private local
[04:37] SQL light database if we open up the
[04:39] terminal we can easily run one of these
[04:41] commands let's go ahead and run our list
[04:43] command we just have a couple of items
[04:45] so what are the changes we're going to
[04:47] make right we have this personal
[04:48] knowledge based system that we're
[04:49] building up what are we going to add to
[04:51] this so we need to add a couple new
[04:52] commands and we're going to do that by
[04:54] firing a large spec prompt so what is
[04:58] the spec prompt it is essentially a plan

### Minute 5

[05:00] for the work you want done it's a
[05:01] specification document except this
[05:04] specification document is built for your
[05:06] AI coding assistance you can see here we
[05:09] have four sections the headline of the
[05:11] changes we want changed the objective
[05:13] context and low-l tasks so the objective
[05:16] is of course what we want changed at a
[05:18] high level you can see here I want to
[05:19] add these three new commands I want the
[05:22] ability to quickly add YouTube scripts
[05:25] so pull down YouTube videos get a
[05:28] transcript for the YouTube video and
[05:30] then save that into the knowledge base
[05:31] this will help me run arbitrary queries
[05:34] and prompts on my existing YouTube
[05:36] content we also have ADD site basically
[05:38] you scrape down a website and then you
[05:40] store that in your personal knowledge
[05:41] base and then we're adding a Syle
[05:42] command this is just something that's
[05:44] missing from the knowledge base if we
[05:45] open up main you can see all of our
[05:47] current commands if we collapse add
[05:49] remove list similar and backup this is
[05:52] going to give us the ability to grab a
[05:54] knowledge based item by ID what's
[05:57] context context is of course every file
[05:59] file you need to get the change done you

### Minute 6

[06:02] can see how this spec document is
[06:03] starting to drill in to the changes and
[06:06] detail out more information for AI
[06:08] coding assistant if we go back to our vs
[06:11] code Windows you can see we've added all
[06:13] of those files into our AER instances on
[06:16] the left and on the right we're almost
[06:18] ready to run this prompt the last thing
[06:19] we need to look at is of course the
[06:21] lowlevel tasks what I have written here
[06:23] is a list of prompts so a whole set of
[06:26] information Rich prompts I'm not going
[06:29] to go into much detail here of how this
[06:30] works I'll add some links to how some of
[06:33] this stuff works in the description but
[06:35] effectively what we have in our low-l
[06:36] tasks is a list of prompts that our AI
[06:39] cing assistants can execute top to
[06:41] bottom to get the work done you can see
[06:43] there's more detail in here than you're
[06:45] probably used to I'm writing very
[06:47] accurate very precise AI coding prompts
[06:50] we'll talk more about these prompts in
[06:52] the future on the channel so let's close
[06:55] everything and let's execute this
[06:56] spending all this time explaining this
[06:58] let's go ahead and fire this off we'll

### Minute 7

[07:00] open up VSCO I want to measure success
[07:02] in the most blunt forward way the only
[07:04] thing that really matters of course I'm
[07:06] being a bit reductive here but there are
[07:08] only three things that really matter as
[07:10] a software engineer first did you
[07:12] accomplish the task two how much time
[07:14] did it take you and lastly what did it
[07:17] cost we're going to judge our two AI
[07:19] coding assistants by the same metrics so
[07:22] let going go ah and pce this in both
[07:23] sides here so after this prompt runs we
[07:26] fully expect to be able to run these
[07:29] three commands on both code bases
[07:31] without flaw so here we go on the left
[07:34] we're going to run Gemini on the right
[07:35] we're going to run Sonic we want to know
[07:37] if they built the three features we
[07:39] asked for the three new commands how
[07:41] quickly they did it what it cost
[07:42] obviously Gemini wins automatically on
[07:44] the cost but let's go ahead fire these
[07:46] off and check out the
[07:51] results okay so right away you can see
[07:53] flash is Off to the Races so right now
[07:56] both aing assistant they're in architect
[07:58] mode so they're just drafting all the

### Minute 8

[08:00] changes that need to happen here um you
[08:03] can see on the left here Gemini flash is
[08:05] quite a bit faster the architect just
[08:07] finished now the editor is going on the
[08:09] right Sonet just finished the architect
[08:11] just finished and now the editor model
[08:13] is firing off on the right side I think
[08:15] Sonet no no I think I think flash is
[08:17] coming up to the finishing line here um
[08:19] it's writing tests we have a prompt for
[08:22] writing tests in there um let's see
[08:24] where is Sonet right now Sonet is oh man
[08:27] Sonet is updating the read me okay so
[08:29] son it actually finished a little bit
[08:30] faster no so flash has finished now they
[08:33] both ran into linting errors I have yes
[08:35] always so they're going to both
[08:37] automatically fix the linting error
[08:39] let's see how they perform here so Sonet
[08:41] is Sonet is finished Sonet has finished
[08:43] first I'm actually quite surprised Here
[08:46] and Now flash is finished okay so that
[08:49] was exciting a lot of stuff happened
[08:51] there if we just analyze the results
[08:53] here this costs us a total of 12 cents
[08:56] for this session and there's no cost for
[08:59] flash so on speed surprisingly son it

### Minute 9

[09:02] won I think it won because it received a
[09:06] much fewer tokens um I think on a token
[09:08] by token basis flash would have won but
[09:10] let's go ahead and actually see if our
[09:13] AI coding assistants accomplished the
[09:15] task right this is the most important
[09:16] thing if they haven't accomplished the
[09:18] task we asked them to complete then all
[09:20] the other side metrics like cost and
[09:22] speed don't matter at all so let's go
[09:24] ahead and see if we can run our new
[09:26] knowledgebase command so what I'll do is
[09:29] I'll open open up new terminals on both
[09:31] sides if I type get status you can see
[09:34] all the changes that are model made here
[09:35] and get status on the left side here
[09:38] same deal right just clear this let's go
[09:41] ahead and start with sonnet so if we
[09:44] open up main we should be able to see
[09:47] all of our new commands all collapse and
[09:49] you can see we do have three brand new
[09:52] typer methods let's go ahead and run our
[09:55] add YouTube script method so we also
[09:58] asked for usage docs so we have this

### Minute 10

[10:00] exact command that we can just copy out
[10:02] and run what we expect here is a new
[10:04] knowledge based item with this YouTube
[10:07] script and if we just open this up you
[10:08] know this YouTube script is going to be
[10:10] I want to share my our AI engineering
[10:12] 2025 plan max out compute super relevant
[10:16] this is the video we want to pull the
[10:17] transcript from so I'm going to copy
[10:19] nearly all this command I'm going to
[10:20] start from the python since we already
[10:22] are running in a virtual environment
[10:24] I'll paste the send so let's see if our
[10:26] Sonic 3.5 prompt chain completed our ad
[10:29] YouTube script command for us
[10:31] automatically so this is good as
[10:32] thinking we do get this bad recognized
[10:35] option so we do get an issue here all
[10:37] I'm going to do here is copy I'm going
[10:38] to copy the entire output here typer
[10:40] gives us a nice output block here I'm
[10:42] going to come back to our air coding
[10:44] assistant I'm just going to paste this
[10:45] in so I'm giving Sonic one shot to
[10:48] correctly resolve the issue so I'm going
[10:50] to hit enter there and then we're going
[10:52] to move over to the left side so let's
[10:53] see if Gemini properly wrote that
[10:55] command so if we do the same thing we go
[10:56] to main while our Claude and is running
[10:59] on the right um let's go ahead and

### Minute 11

[11:02] collapse and let's see our commands here
[11:05] we do have git at the top add YouTube
[11:08] script and then we have ADD site so this
[11:10] looks good let's open this up we do have
[11:13] some nice usage docs from the Gemini
[11:15] flash model let's go ahead and see if
[11:17] this command will execute for us so same
[11:20] deal and let's see if Gemini created
[11:23] this command properly for us okay so we
[11:25] ran into an issue right away definitely
[11:27] disappointed here I'm going to copy all
[11:29] this and do the same thing we're going
[11:30] to give both Gemini and Sonet a chance
[11:33] I'm just going to come to the instance
[11:35] I'm going to paste this in execute let's
[11:37] hop back over to our Claude AI coding
[11:40] assistant in architect mode and let's
[11:42] just rerun to see if it resolved the
[11:44] issues it had so I'm just going to hit
[11:46] enter here and let's see if it can get
[11:47] it right okay fantastic so you can see
[11:50] we have added YouTube transcript 12
[11:52] let's go ahead and test the new git
[11:55] method right so we should have this new
[11:57] git command here let's let's open this
[11:59] up and let's go ahead and fire it off so

### Minute 12

[12:03] you can see here we created this new
[12:04] YouTube transcript with id2 let's go
[12:07] ahead and just run git with id2 so if we
[12:10] hit enter here wonderful so we can see
[12:12] our new git command gave us back that
[12:14] exact instance if we open this up here
[12:16] you can see we have this transcript so
[12:18] this worked really really well so we
[12:20] have one more command to test here for
[12:22] our Claude AER prompt chain running in
[12:25] architect mode and that is going to be
[12:27] our site method so let's go ahead and
[12:29] see add site just copy this from python
[12:32] so you can see here python main.py add
[12:35] site and we're going to pull from the
[12:37] anthropic research building effective
[12:39] agents blog post if we click into this
[12:41] we can see exactly what this looks like
[12:42] there's a great rundown um a lot of the
[12:45] ideas discussed here we have discussed
[12:47] on the channel of course building blocks
[12:49] workflows agents we can search prompt
[12:51] chains you know this is a really popular
[12:53] idea we have and quite literally are
[12:55] discussing right now great posts it's
[12:57] weird cuz it kind of feels like you know
[12:59] on the channel we've discussed so many

### Minute 13

[13:00] of these ideas long ago frankly but it's
[13:03] cool to see this collected by a you know
[13:05] big player in the a agent space so this
[13:07] is great so anyway so let's go ahead and
[13:09] use this URL and let's see if our Sonet
[13:13] instance was able to build up this
[13:15] command end to end right and you can see
[13:17] some of the details here right we
[13:18] download the site generate embeddings
[13:20] and then we run our ad KB row command
[13:22] which inserts it into our sqlite
[13:24] database and so let's go ahead and fire
[13:26] this off and let's see if we can add
[13:28] this new site to our personal knowledge
[13:30] base no issue so far that's a good sign
[13:32] so we're probably scraping right now
[13:34] generating embeddings and there it is so
[13:37] added website content at id13 if we just
[13:40] type our list command here U main list
[13:43] and we actually need to drop UV there
[13:45] since we're already in a virtual
[13:46] environment we can just fire this off
[13:48] and we should see both our website and
[13:52] our um new site content so that looks
[13:54] good let me actually just go ahead and
[13:55] use the git command that we were just
[13:57] using and this is going to be ID3
[13:59] fantastic so check this out so we have

### Minute 14

[14:02] the markdown formatted version of
[14:05] anthropics agent post right so this is
[14:07] fantastic it's it's working perfectly we
[14:09] have this inside of our knowledge base
[14:11] and we can use some quick similarity
[14:13] search if I just highlight workflow
[14:16] routing and we have this similarity
[14:18] Search Command here I was using it
[14:20] earlier we just clear this out paste
[14:22] this here it's going to be the top hit
[14:24] so we're looking for the similar items
[14:26] with this text and you can see there
[14:29] that is of course our top hit so we got
[14:31] that knowledge based row returned
[14:33] immediately so this is fantastic we had
[14:35] one issue here with the Claude 3.5 Sonet
[14:39] prompt chain running in AER in architect
[14:42] mode but overall the changes went
[14:44] through you know we can see we can do a
[14:45] get diff here and if we want to we can
[14:48] even run get diff and then write the
[14:51] diff to a file so def. text and then we
[14:53] can see exactly how much was changed
[14:55] here right so you know about 2,000
[14:57] tokens worth of file change
[14:59] so this is fantastic um we should have a

### Minute 15

[15:02] readme update as well yeah so we have
[15:03] this readme update which is really cool
[15:05] part of our spec prompt asked for
[15:07] changes to the read me so you can see
[15:09] here um we have new documentation around
[15:12] adding YouTube content adding website
[15:14] content and getting content by ID so you
[15:16] can see we have great usage documents
[15:18] here let's switch back over to our
[15:20] Gemini flash AI coding assistant and
[15:22] let's see if it was able to correct the
[15:25] mistake it had let's go ah a and just
[15:26] open this up a little bit more too the
[15:28] issue happened on the add YouTube script
[15:30] call so we'll just hit up and let's see
[15:33] if this issue was resolved so let's run
[15:35] this okay uh same deal let's give it
[15:38] even more grace we'll copy this and
[15:42] again we'll let Gemini flash attempt to
[15:45] fix its issue it runs really quickly but
[15:48] it seems to get things wrong from time
[15:51] to time um to be fair this is a three
[15:55] feature spec prompt where we're asking
[15:57] for three changes right we want three

### Minute 16

[16:00] concrete things modified so there's room
[16:03] for confusion for a large language model
[16:04] but it's pretty clear even with this
[16:07] small AI coding sample here you know
[16:09] it's taking us an additional AI coding
[16:10] prompt uh to get Gemini flash where
[16:14] Sonic 3.5 is so let's go ahead and just
[16:16] rerun this again let's see if Gemini
[16:19] flash has resolved its issue this is
[16:21] good it's taking some time to load here
[16:23] added item 12 that's looking good so far
[16:25] let's go ahead and look for get there it
[16:27] is we have our new git command so it did
[16:30] successfully create this you can see we
[16:31] have that new git knowledge based row
[16:34] function call and if we open that up you
[16:36] can see here diving into the layers of
[16:38] this code base we also have that called
[16:40] there so that looks great let's go ahead
[16:42] and run this so we'll copy this command
[16:45] from the python and this is item 12 so
[16:48] let's see if we can get item 12 from our
[16:51] knowledge
[16:52] base fantastic you can see we have that
[16:55] entire YouTube transcript from that
[16:56] video we were able to add this to our
[16:58] knowledge base right so this looks great

### Minute 17

[17:00] we have one more command to run here on
[17:02] the Gemini flash a coding assistant code
[17:05] base let's look at add site method here
[17:09] everything looks relatively good let's
[17:11] copy this paste let it run right now
[17:14] it's scraping the site so that's good it
[17:16] got to that point so if we run the git
[17:18] for item 13 so let's just quick search
[17:21] git update this to item 13 we should see
[17:24] that anthropic building effective agents
[17:26] blog post nice and we can go ahead run
[17:29] that again and save this to a file we
[17:31] can say um AI
[17:33] docs building F uh agents and throp and
[17:37] markdown right so we can run that again
[17:40] and now we have that loaded out of our
[17:42] knowledge base we should have this new
[17:44] AI dock here and you can see we have
[17:47] that post from open AI exactly if we
[17:49] search prompt
[17:50] chain you can see that exact
[17:53] same uh search here from the site right
[17:57] so really really cool to see these two
[17:59] models perform up against each other

### Minute 18

[18:01] it's pretty clear that flash it's a
[18:03] great model it's free there's a lot of
[18:06] intelligence there it definitely is not
[18:08] on par with cl 3.5 Sonet but it is still
[18:12] a fantastic model so you'd be surprised
[18:14] how many times I've done this I run a
[18:16] large prompt in a code base and then
[18:19] I'll revert the code base duplicate it a
[18:22] couple times and see if another set of
[18:24] AI coding assistants with different
[18:26] models can get to that same place in the
[18:28] exact same amount of time speed cost so
[18:31] on and so forth so you know jury Zen um
[18:34] Claude ran the fastest it made fewer
[18:37] mistakes right it made two fewer
[18:39] mistakes than Gemini and it did cost so
[18:41] we're going to give Claude two points
[18:44] Gemini did not run the fastest it had
[18:46] two additional errors but it was free
[18:50] right and we did get there eventually to
[18:51] be fair so we're going to give Gemini
[18:54] one point this is just a simple
[18:56] comparison these models are both great
[18:58] we still need to see a little bit more

### Minute 19

[19:00] juice coming out of Gemini in order for
[19:02] it to be on par with Sonet uh for the
[19:05] longest time Sonet has been on the top
[19:08] of the leaderboards it is the most
[19:09] effective model for the most use cases
[19:12] but that is definitely changing with the
[19:14] release of 01 through the API which
[19:17] we're going to be looking at in upcoming
[19:18] videos and of course 03 mini and 03 so
[19:21] it's going to be super super wild to see
[19:24] you know model combinations and models
[19:27] like this roll out in the future I
[19:28] wanted to share aer's architect mode AER
[19:32] and prompt chaining again here with you
[19:35] just because it's going to be a very
[19:37] important pattern as we get access to
[19:39] more powerful models and we start really
[19:42] building out our AI agents and agentic
[19:44] workf flows in 2025 I highly recommend
[19:47] you read through anthropics blog post
[19:49] here it's a lot of what we've talked
[19:51] about in the past but when a big company
[19:53] backs up everything we've been talking
[19:55] about on the channel and writes about it
[19:57] in detail you know that tells you a
[19:58] things uh on the channel we are on the

### Minute 20

[20:00] right track we have been for a while and
[20:02] we're going to continue with that Trend
[20:04] but also there's a lot of really key
[20:06] ideas here one of them being prompt
[20:08] chaining that's going to be increasingly
[20:10] important as reasoning models allow us
[20:13] to plan and execute large amounts of
[20:16] work you know just to kind of call that
[20:18] out explicitly here again this spec
[20:21] prompt um detailed everything I wanted
[20:24] done in detail right that change pushed
[20:26] out uh tokens on both Gemini and Claud
[20:30] 3.5 sonit in a very very kind of precise
[20:33] way across multiple files I mean you saw
[20:35] that context window right which is you
[20:37] know not something I normally suggest
[20:39] unless it's required by the change you
[20:41] have we have over 10 files here and you
[20:43] know on both sides we edited over 2 or
[20:46] 3,000 tokens changed how were we able to
[20:48] do this we're able to do this by scaling
[20:50] our efforts with a larger prompt right
[20:54] this is a theme that's going to be
[20:56] really important as we move into 2025
[20:58] the amount of work you can hand off to

### Minute 21

[21:01] your AI tooling is going to increase as
[21:04] models improve so that means we need
[21:07] better patterns like the spec prompt to
[21:09] allow us to pass off more work to our AI
[21:12] coding tools and our AI Tooling in
[21:14] general this technique and other AI
[21:17] coding techniques and the speed and Pace
[21:19] in which AI tools and models are
[21:22] improving and increasing it's all part
[21:24] of the reason why I created something
[21:26] I'm really excited to share with you
[21:28] right now this has been a long time
[21:29] coming I want to introduce you
[21:34] to principled AI coding principal AI
[21:38] coding is my take on the best way to
[21:42] learn AI coding for 2025 and Beyond the
[21:45] whole point the whole theme with this
[21:47] course is to learn principles of AI
[21:49] coding that will help you you know not
[21:52] just stay relevant but Excel with the AI
[21:54] coding tools of today and tomorrow okay
[21:58] so this is my official AI coding course

### Minute 22

[22:01] link is going to be in the description
[22:03] for you uh the theme here is really
[22:04] simple you can read through this but
[22:06] I'll just scroll down to kind of the key
[22:08] takeaway um here right AI coding is the
[22:12] new standard so 2024 I think is the last
[22:15] year where if you are not using AI
[22:17] coding tools it's fine it's it's going
[22:20] to be okay I can no longer say that with
[22:22] confidence this is going to be the
[22:24] fastest way to fall behind and deprecate
[22:26] your career this is a course built for
[22:28] Engineers this is engineering focused
[22:30] and the entire goal of this is to really
[22:34] address the fact that we are hitting
[22:36] that threshold point where if you're not
[22:38] engineering with AI you are not
[22:40] engineering just plain and simple full
[22:43] stop so I created this course to help
[22:46] you and other Engineers not just survive
[22:49] this transition but to thrive in a
[22:51] principled based way this is not a
[22:54] course about a specific tool or a
[22:57] specific model but this is really about
[22:59] the underlying principles of AI coding

### Minute 23

[23:02] of software engineering with language
[23:05] models and AI coding assistant that's
[23:07] the focus for this entire course and it
[23:09] centers around mastering the big three
[23:12] the context prompt and the model if
[23:15] you've written code with AI you likely
[23:17] already know this is what matters your
[23:20] context model and your prompt this is a
[23:23] theme for generative AI you want to
[23:26] collect context select the mod model and
[23:29] create prompts and then hand off all the
[23:32] hard work to your AI coding assistant
[23:34] there's a lot of value here it's
[23:35] available to you um just to quickly go
[23:37] over what's in the course we have eight
[23:39] lessons in here so we're going to start
[23:40] from beginner move to intermediate and
[23:42] then end with Advanced I can only do
[23:44] this in course form because I have
[23:47] enough time I have the flexibility and
[23:49] the control to really create a guided
[23:51] experience for you so this is all here
[23:54] um I think the price is great you know
[23:56] we all want a good deal from someone we
[23:57] trust get in here early the price will

### Minute 24

[24:00] go up I am putting this at the end of
[24:03] the video here for you know the true
[24:05] viewers of the channel the you know the
[24:07] die hards you know I want to give you
[24:09] guys a big thanks so we just crossed 30k
[24:11] Subs last week I think and YouTube let
[24:14] me know that we hit uh 1 million views
[24:18] in total just the other day which is
[24:20] absolutely insane so again I just want
[24:22] to say thank you I want you to have this
[24:24] course at the best cheapest price before
[24:26] it goes up there are some pretty
[24:28] bleeding edge ideas here they were
[24:30] likely going to become mainstream as
[24:32] people start taking the course and
[24:33] sharing some of the key ideas here so
[24:35] anyway I don't want to preach on this
[24:36] too much a lot of YouTubers a lot of
[24:39] content creators they go the sponsorship
[24:41] route but you know that doesn't feel
[24:43] real to me and I don't want to give you
[24:45] something that I wouldn't want Myself by
[24:47] creating this course by owning you know
[24:50] the IP by owning the ideas behind this
[24:52] and being able to share it with you I've
[24:53] created content 100% relevant to the
[24:56] channel and to engineers and to you know
[24:59] you and I this is the course that I wish

### Minute 25

[25:01] I had when I started AI coding two years
[25:04] ago now once you sign up the dashboard
[25:06] looks like this super clean super simple
[25:08] you'll be able to see all of your
[25:10] courses your course progress you'll be
[25:12] able to uh you know leave a review
[25:14] report any issues you see ask questions
[25:17] so on and so forth you'll start out with
[25:18] the first three lessons unlocked and
[25:20] then once you cross the 50% threshold
[25:23] you'll unlock the next lesson and the
[25:25] next and the next and the next all the
[25:27] way till the end um this is principal AI
[25:29] coding this is my take on teaching AI
[25:33] coding in a indepth principled way where
[25:36] we don't just focus on the tool we focus
[25:38] on the principles underneath the tool
[25:40] principles not
[25:44] tools I think if we look at the
[25:46] ecosystem at a high level what we're
[25:48] seeing is new series of models new
[25:51] reasoning capabilities we see 03
[25:54] completely smashing and just saturating
[25:56] benchmarks just d destroying benchmarks
[25:59] into ashes for us you know I want to

### Minute 26

[26:02] Full Circle back to the beginning here
[26:04] and talk about the question that I think
[26:06] about every single day now how can I use
[26:09] as much compute as possible with
[26:12] powerful models and the best AI tooling
[26:15] AI coding assistants to build more
[26:18] software at higher qualities faster than
[26:21] ever right that's that's where my head's
[26:23] at right you want to be solving more
[26:24] problems higher scale higher rate with
[26:27] these powerful models right we have the
[26:29] old1 series we have the new Gemini 2
[26:32] Series we're going to have llama 4 soon
[26:35] that's going to shatter the open source
[26:38] ecosystem once again and kind of reset
[26:40] it and then of course we have whatever
[26:41] anthropic is cooking up so our potential
[26:44] is limited by what we can do with these
[26:47] incredible tools language models are
[26:50] superpowers now the question is how can
[26:52] we access them how can we tap into them
[26:55] and for AI coding specifically that is a
[26:57] big part of why I built principled AI

### Minute 27

[27:00] coding toward the end toward the
[27:01] advanced lessons the question is really
[27:02] about unlocking as much compute as
[27:06] possible learning to build context the
[27:08] right way so that we can pass off as
[27:10] much work as possible to our AI coding
[27:13] assistant this is a huge theme as we say
[27:16] AI agents roll out more and more this
[27:19] theme will continue long video today I
[27:21] hope you enjoyed it I hope you
[27:23] understand where things are going and I
[27:25] hope this technique you know prompt
[27:26] chaining AER Arch Tech I hope it all
[27:29] makes sense to you in upcoming videos
[27:31] we're going to be talking about the 2025
[27:33] predictions and we're also going to be
[27:34] looking at the new o1 series that is
[27:37] getting rolled out right now we have
[27:39] some interesting things happening on
[27:40] that same theme um the creator of Aer
[27:44] has rolled out a brand new Benchmark a
[27:47] polyglot leaderboard that is a much
[27:50] harder AI coding Benchmark 01 is already
[27:53] at the top of this and you can see the
[27:55] incredible gap between claw through 5
[27:58] son it the you know current kind of or

### Minute 28

[28:00] the previous I guess state-ofthe-art
[28:02] model and the new 01 coming out of the
[28:05] API this is really incredible we're
[28:07] going to be covering this as soon as we
[28:09] get API access I'm hoping that rolls out
[28:11] over the next week really incredible
[28:12] stuff here really excited to see some
[28:14] new harder benchmarks um I'm going to
[28:16] link this blog post in the description
[28:18] as well Paul aers Creator is one of the
[28:21] best Engineers to be following right now
[28:23] his writing and his benchmarks are
[28:25] something that I reference often in
[28:27] order to understand
[28:28] how the AI coding ecosystem is evolving
[28:30] we had to pick a tool in the principal
[28:32] AI coding course for me it was an
[28:34] absolute no-brainer to choose AER
[28:37] because it is foundational AI coding
[28:38] software thanks for watching next week
[28:40] we're going to be looking at our
[28:41] predictions for 2025 it's going to be a
[28:43] big year like comment subscribe to stay
[28:46] plugged into that stay focused and keep
[28:48] building