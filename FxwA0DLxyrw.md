# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=FxwA0DLxyrw
- **Duration:** 21:25
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 3877
- **Transcript Generated:** 2025-03-30 23:49:05

## Transcript


### Minute 0

[00:00] if you want to win any generative AI age
[00:03] you must have a vision with every
[00:05] release it's 100% clear anthropic has a
[00:09] vision so much Vision that they gave it
[00:12] to our computers with the brand new
[00:14] computer use tools by now you've already
[00:17] seen how the computer tool Works running
[00:19] on the new claw 3.5 Sonet let's go
[00:22] deeper and explore the less disgusted
[00:24] tools Engineers are sleeping on because
[00:27] it's not flashy and it's not cool at
[00:30] first glance but make no mistake the
[00:32] text editor and The Bash tool are
[00:35] critical infrastructure for asymmetric
[00:38] software engineering in the age of
[00:40] generative AI why because Engineers that
[00:43] fully control their terminal and their
[00:46] editor can ingest and synthesize
[00:48] information like no other I've wired up
[00:51] a proof of concept of these tools and
[00:53] have started putting them to work
[00:55] already let's walk through productivity
[00:57] gains you can get using these tools

### Minute 1

[01:00] today and then we'll speculate on the
[01:02] question where is Claude 3.5 Opus I
[01:05] don't know if you've noticed but any
[01:07] mention of claw 3.5 Opus has been
[01:10] removed from anthropics Models page Why
[01:13] has anthropic completely removed any
[01:16] mention of it from their
[01:20] documentation so in this proof of
[01:22] concept you can see I have three classes
[01:25] here we have a logger we have the editor
[01:27] class and then we have the bash session
[01:29] let's go ahead and start start with
[01:30] anthropics new bash tools in the
[01:32] terminal I'm using astrals UV python
[01:35] package manager so I'll type UV run Main
[01:38] and then I'll specify my prompt so let's
[01:41] just start with something simple and
[01:42] work our way up I'll say list all files
[01:45] in current D tree form depth 2 and I'll
[01:50] use the mode bash so before we run this
[01:53] we'll open up the file explorer so you
[01:54] can just see a couple of files we have
[01:56] in this directory and now let's go ahead
[01:58] and run our tool

### Minute 2

[02:04] so we have a bunch of information here
[02:05] let's go ahead and review the log if you
[02:07] open up sessions you can see a couple
[02:08] previous sessions here and now you can
[02:10] see our logging for this run so this is
[02:13] really interesting right we have our
[02:15] bash command logging everything that's
[02:17] happening and you can see our output for
[02:19] the tool run right so output for tree-
[02:23] L2 and remember I asked for list all
[02:27] files in the current dur tree form depth
[02:29] 2 and that's exactly what we got we open
[02:31] up AI docs we have those files exactly
[02:34] and of course we have read me we have
[02:36] backup we have an app database that
[02:39] we'll look at here in a second we have
[02:41] our editor dur and then we have our
[02:42] images and of course we have these
[02:44] session dispatch tool converted our
[02:47] natural language command into the
[02:49] correct bash command let's go ahead and
[02:51] push this further let's clear and run
[02:53] another command so let's just add on to
[02:56] it right so we're on UV run main list
[02:58] all files Tre form depth 2 so just

### Minute 3

[03:01] running that same prompt and then we'll
[03:02] say first five lines of the newest log
[03:06] file and let's make sure we get our D-
[03:08] mode bash so let's kick this off open up
[03:11] our file explorer you can
[03:14] see okay so let's check out our log
[03:16] let's see what we have now so you can
[03:18] see same as before or tree command Rand
[03:21] just as before right so we can see here
[03:22] the new claw 3.5 model is consistent
[03:25] that's good to see and now if we move
[03:28] down to our second command we can see
[03:30] here that plot is picking up on this
[03:32] command here right so it's saying here
[03:34] let's go ahead and collapse this now
[03:36] let's find the newest log file and read
[03:39] the first five lines you can see here
[03:41] there's some type of Chain of Thought
[03:43] some type of iterative process happening
[03:46] within claud's thought process it's
[03:48] thinking through what it needs to do to
[03:50] accomplish the next task we've given it
[03:53] now it's referring to the files in the
[03:55] sessions directory it's looking at our
[03:57] newest file and interestingly right the

### Minute 4

[04:00] newest file is the file that's getting
[04:02] logged actively so it's getting a little
[04:04] meta here but what we end up with here
[04:06] is Claude properly printing out you can
[04:09] see here here's the actual run CLA is
[04:12] properly printing out its previous brand
[04:15] new messages and if we go ahead and
[04:17] search right first let's list all the
[04:20] files in tree form and scroll up you can
[04:23] see that line exactly I'm running
[04:25] commands in natural language and not
[04:27] only is Claude getting the order of the
[04:30] commands properly it's getting all the
[04:31] commands right you can see here we have
[04:33] our pricing calculations set up here so
[04:36] far no hiccups really impressed things
[04:38] are looking really good we are running
[04:40] arbitrary bash commands with a brand new
[04:43] bash tool let's just keep pushing this
[04:46] tool further so inside of this codebase
[04:48] I have this data app DB and this is a
[04:51] simple SQL light database with a single
[04:54] table inside of it so we can go ahead
[04:55] and see exactly what's in this SQL light
[04:58] database with

### Minute 5

[05:00] 3 we'll pass the path to this and then
[05:03] we'll say schema so you can see here we
[05:06] have a simple logging table so let's
[05:08] have the cloud bash computers tool
[05:11] modify this database let's go ahead and
[05:12] reuse the same command and I'll say
[05:15] using SQ light 3 update existing data/
[05:19] app. DB read schemas then insert these
[05:24] five lines in our SQL like database
[05:27] logging table okay so I'm giving it all
[05:30] the information it needs to complete
[05:31] this request without going through any
[05:33] of the Motions of actually writing these
[05:35] commands out myself so let's see how
[05:37] well this does here we'll fire this off
[05:40] and we'll load up that log file you can
[05:42] see it's running that tree command again
[05:44] let's go ah and get a refresh here you
[05:46] can see it is looking at the definitions
[05:50] right so this it's automatically looking
[05:51] at that right it ran that schema method
[05:54] and fantastic and it selected back out
[05:58] the rows here so you can see a summary

### Minute 6

[06:00] here at the end of the log I have
[06:02] completed all the requested tasks listed
[06:05] files in tree form with depth two found
[06:07] and display the first five lines read
[06:09] the schema inserted five lines into the
[06:12] logging table and then verified the
[06:14] insertions okay you can see the pricing
[06:16] here that cost us a total of 4 cents
[06:18] mostly input costs right you can see all
[06:20] the input tokens from ingesting the
[06:23] relevant information to make the
[06:24] commands right we can search our output
[06:26] for observability is ultra important
[06:29] when you're working working with these
[06:30] tools I always like to start with a
[06:31] simple loging file and then progress
[06:33] from there we can just search these
[06:34] right you can see we have a total of
[06:35] four outputs tree- L2 let's go ahead and
[06:39] look at that next command ls-t sessions.
[06:42] log tar agent has read this content and
[06:46] now it's checking our sqlite database
[06:49] schemas right so you can see here
[06:51] executing bash command it's first
[06:53] reading in the database structure just
[06:55] like we asked and then if we scroll down
[06:56] you can see here now it's going to
[06:58] actually execute this statement this is

### Minute 7

[07:00] not a trivial bash statement writing
[07:02] this command and then it's doing some
[07:04] wonderful said string parsing
[07:07] automatically for us grabbing those
[07:09] lines placing it inside our database
[07:12] then Claude is going back in and
[07:14] verifying that these items are in there
[07:16] right so we're saying select star from
[07:17] logging order by ID descending limit
[07:20] five and it's getting those items right
[07:22] back out and you know we can manually
[07:25] just go in and run this exact same
[07:27] command to verify because because you
[07:29] know with great logging again
[07:31] observability is really important you
[07:32] can always just backtrack and see what
[07:33] your agents and see what your prompts
[07:35] are doing so we're just going to
[07:37] literally copy paste to send and you can
[07:39] see there we're getting our new previous
[07:42] logging messages so this is really cool
[07:44] right if you want to you can also run
[07:46] this entire chain again with this-- no
[07:50] AGI flag and all this is going to do is
[07:53] it'll run and instead of actually
[07:55] executing the subprocess commands it
[07:58] will just return a mock response and

### Minute 8

[08:00] that'll be fed back into the AI agent
[08:02] obviously it won't completely work
[08:04] because it's not running the real
[08:05] commands and it's not getting the real
[08:07] results but you know just a test you can
[08:09] pass in this flag if you want so that
[08:11] you know Claude doesn't fully take over
[08:13] your computer this is pretty incredible
[08:14] stuff we have a simple Loop giving
[08:17] Claude the space to call tools get
[08:19] feedback from the tool and then rerun
[08:21] the next command right so it's a really
[08:23] simple process of letting Claude in just
[08:26] a prompt and then it runs the llm
[08:28] decides what tool to run it passes us
[08:30] the tool we execute the tool and then we
[08:32] give the response back to Claude and it
[08:34] just repeats in that Loop and if you
[08:36] were to build a real application or a
[08:38] real agent around this what you would
[08:40] actually do is after you finish an
[08:42] execution you would simply create some
[08:44] type of human in the loop feedback the
[08:46] simplest version of this is to run a
[08:49] while loop or set up a personal AI
[08:50] assistant to control the history and to
[08:53] interact with you with voice commands
[08:55] right so that this Loop would continue
[08:57] you can also set up user interfaces to

### Minute 9

[09:00] interact with this or any other
[09:03] [Music]
[09:05] agent so as always let's start simple
[09:07] you can see we have our editor directory
[09:10] here with this ping pong. text I'll say
[09:14] UV run Main and I'll pass in the prompt
[09:16] update pong to Ping in our ping pong.
[09:21] txt file okay and we'll run this the
[09:24] default mode is text so we can just kick
[09:26] this off you can see we're in file
[09:27] editor mode here and we should be able
[09:30] to see that value Kate update to Ping so
[09:32] that just happened in real time um you
[09:34] know we didn't do or say anything let's
[09:37] go ahead and just you know play with
[09:38] this a little bit add 30 more pings 30
[09:41] pongs ping pong. update okay so this is
[09:44] like the dumbest simplest thing we can
[09:46] do with this file but it's a good place
[09:47] to start right so we're just literally
[09:49] saying update this file in some silly
[09:51] arbitrary way okay great so now we have
[09:53] you know 30 ping 30 pong fantastic so
[09:56] let's do something more legitimate with
[09:57] this tool right we'll run UV run main

### Minute 10

[10:00] write a detailed three use case document
[10:04] for llms to a LM use cases markdown then
[10:10] into three going into detail about each
[10:14] use case so here we have two highle
[10:17] commands that we want done right we want
[10:19] an original use case Doc and then we
[10:21] want Claud to break it up into three
[10:24] additional files so let's kick that off
[10:26] eyes on the editor directory here as
[10:28] Cloud's going to be generating these
[10:30] files for
[10:33] us okay you can see LM use case here we
[10:36] can hop into this and get a nice
[10:39] breakdown view here right content
[10:41] generation code development programming
[10:43] data analysis you can see content
[10:45] generation now has its own file very
[10:47] very nice right that is one of the goto
[10:50] use cases for llms and of course code
[10:52] development this is a big one and all
[10:55] all these documents are happening
[10:56] they're getting generated on the fly
[10:58] live and here's our data analysis that

### Minute 11

[11:00] was really incredible let's go ahead and
[11:02] backtrack you can see the cost here that
[11:03] cost around 8 cents to fire off and a
[11:06] lot of this is the input tokens right
[11:08] after every tool call we're always
[11:10] passing back the response from the tool
[11:12] back into Claud right so that's going to
[11:14] see our our cost stack up over time
[11:16] let's go ahead and just break down the
[11:18] exact calls so if we search command you
[11:22] can see all the commands that Claud is
[11:24] running we should just have for create
[11:27] command and that's exactly what we have
[11:28] right so for create commands you can see
[11:30] all the content for every single
[11:31] creation statement you can see the exact
[11:34] path right we're always getting back
[11:35] this SL repo SL file and the SL repo is
[11:40] what you'll update or replace to be the
[11:42] true path that you're writing to so we
[11:45] update and replace that to be our editor
[11:46] dur that's configurable via an
[11:48] environment variable and you can see
[11:50] just like the bash tool the file editor
[11:52] tool is just doing all of this work for
[11:55] us right so you can imagine you're
[11:56] passing in a lot more important
[11:58] information and you're treating this

### Minute 12

[12:00] tool like an agent I hope it's becoming
[12:02] really really clear what's happening
[12:04] with every video release we have on the
[12:05] channel every Monday we're getting
[12:08] closer to having these pieces of
[12:10] software that are operating for us and
[12:13] with this release anthropic is pushing
[12:15] us into the future with these
[12:17] opinionated domain specific set of tools
[12:20] to solve a specific set of problems now
[12:23] I hope that sounds familiar because it
[12:25] is we've been talking about on the
[12:26] channel when you canst prompts around a
[12:28] specific ific use case and you compose
[12:31] those tools that your prompt can call
[12:33] what do you get you get an AI agent this
[12:36] is where everything's going this is
[12:38] what's coming next AI agents are here in
[12:40] 2025 they're going mainstream you're
[12:43] here early we're talking about this
[12:45] early get your hands on these tools and
[12:47] start utilizing these we can now craft
[12:49] arbitrary prompts pass any information
[12:51] we want to and instead of a text to text
[12:54] prompt what we're getting now is text to
[12:57] action prompt these are text to action

### Minute 13

[13:00] prompts with bash commands and with file
[13:03] editing and with computer use our llms
[13:06] are starting to control things they're
[13:08] starting to manipulate things create
[13:10] read update delete they're modifying
[13:13] information they're running concrete
[13:15] commands that allow them to do more now
[13:17] my llm can operate on all of my files
[13:21] with and for me this is a huge huge deal
[13:24] this is why I wanted to emphasize these
[13:26] two tools because it's a great way to
[13:28] work up to where everything is going as
[13:31] an engineer the file editor and the
[13:33] terminal are critical tools for us and
[13:36] if you have agents operating in your
[13:38] terminal and your file editor for you in
[13:41] parallel to you you're going to get
[13:43] asymmetric Returns on your time so this
[13:46] is awesome let's go ahead and make a
[13:47] couple tweaks and just show off a couple
[13:49] other things you can do with this be run
[13:51] Main and we'll say read llm use cases
[13:55] right so we'll have it fire off it's
[13:57] read functionality then update
[13:59] to contain a mermaid

### Minute 14

[14:02] diagram of the use cases and we'll say
[14:05] LR flow chart okay now we're going to
[14:09] read this file in right so this is an
[14:12] existing file it already exists and it's
[14:15] going to modify you can see there that
[14:16] modification came right in automatically
[14:18] we now have a flowchart right it
[14:20] ingested the file it reread the file and
[14:23] then it made a modification to it right
[14:25] if we go into preview mode here we can
[14:27] see our mermaid chart so now we're
[14:29] rapidly creating this documentation this
[14:31] markdown file you know this plan
[14:33] whatever you're working on you now have
[14:35] these agents to help you operate on it
[14:38] very very quickly it's so important to
[14:39] be wiring these tools up and to be
[14:41] keeping track of what's important this
[14:44] is an important tool the file editing
[14:46] tool and The Bash tool are Ultra
[14:48] important I'm going to be wiring these
[14:49] up in my CLI in Ada the personal AI
[14:52] assistant for engineering we've been
[14:54] building on the channel I'm going to be
[14:55] using and deploying these tools every
[14:57] single day so this code base is is going
[14:59] to be in the description for you to

### Minute 15

[15:00] check out and to get yourself up and
[15:02] running with your text editor and your
[15:04] bash AI
[15:08] agents I want to hop back to the high
[15:11] level here and just discuss where things
[15:13] are going so you might have noticed
[15:15] these are just tool calls right there's
[15:19] actually nothing super sophisticated
[15:21] going on here at least not at first site
[15:24] right not at first glance what they're
[15:25] doing here is actually really
[15:27] interesting the value composition of
[15:29] these tools is that claw 3.5 Sonet has
[15:32] been fine-tuned to operate these tools
[15:35] very well what we're seeing with this is
[15:38] an interesting direction for model
[15:40] providers like open aai Google Facebook
[15:42] and anthropic to release sets of tools
[15:45] to perform specific tasks very well with
[15:49] a model fine tune to excel at their
[15:52] tools and I hope this sounds familiar
[15:55] these tool belts built to solve a
[15:57] specific set of problems s are
[15:59] effectively pre-baked AI agents we dove

### Minute 16

[16:03] into the composability of prompts into
[16:06] AI agents in our previous video and it
[16:08] looks like we're right on track this is
[16:10] a great direction from a business
[16:11] perspective because now anthropic can
[16:13] build models and sets of tools that
[16:15] perform well on specific benchmarks and
[16:18] sell that tool belt as an AI agent so
[16:22] these companies are starting to turn all
[16:24] their work with llms into concrete value
[16:27] into concrete output they're saying
[16:29] fantastic we've built these next
[16:30] generation tools let's actually solve
[16:33] real problems with them and they're
[16:35] starting at a great place they're
[16:36] starting at the bottom level of where
[16:38] all software problems are solved the
[16:40] engineers tool belt these tools stood
[16:42] out to me right away for that reason
[16:45] text editor and Bash this is where
[16:48] Engineers live this is where great
[16:50] engineers get tons of work done quickly
[16:53] their computer tool obviously very
[16:55] flashy very cool great for RPA but the
[16:58] real world work for engineering happens

### Minute 17

[17:00] with these two tools as a side note
[17:03] these companies are trying to create
[17:04] vendor lockin with their specific sets
[17:07] of tools and they're you know fine-tuned
[17:10] models that are built to use those tools
[17:11] well so keep your eyes on releases like
[17:14] this this is a trade-off and it's a risk
[17:16] we just kind of have to accept and the
[17:18] generative AI age because these
[17:19] companies are leading the way for what's
[17:21] possible this is fantastic I'm loving
[17:24] Claude 3.5 upgraded or clae 3.5 new
[17:28] definitely could named that a little bit
[17:30] better but that's old news what is
[17:33] interesting is the question where is
[17:37] Opus where is claw 3.5 Opus I always
[17:40] keep a close eye on the big three model
[17:44] pages and AMA to you know just kind of
[17:47] see where the models are what's going on
[17:50] and also I've referenced these documents
[17:52] a lot one thing I noticed right away
[17:54] during this upgrade and one of my
[17:56] favorite Engineers Simon Willison also o
[17:58] pointed out claw 3.5 Opus has been

### Minute 18

[18:01] completely removed from their
[18:02] documentation what is going on why have
[18:05] they done this is Opus 3.5 off the table
[18:08] I have a couple ideas as to why
[18:09] anthropic removed it let's just walk
[18:11] through them and I want to get your
[18:13] thoughts on what you think is going on
[18:15] here so my first kind of prediction is
[18:18] that claw 3.5 Sonet is claw 3.5 Opus and
[18:23] they've just rebranded it although this
[18:26] model is a massive Improvement I don't
[18:28] think it perform forms like we would
[18:29] expect an opus 3.52 so they just
[18:32] rebranded it to claw 3.5 in a
[18:36] panic and you know this is not the most
[18:38] glamorous case you don't want a Top
[18:40] Model provider making strategic
[18:43] decisions like this but it's an
[18:45] interesting prediction I think this is a
[18:47] probably mid to low probability so you
[18:49] know maybe 10 to 30% possible the other
[18:52] prediction is that they just deleted it
[18:54] on purpose right they just got rid of it
[18:56] claw 3.5 is a great model with great
[18:59] speed great performance it follows

### Minute 19

[19:01] instructions better than any model it
[19:03] writes the best and minus 01 preview it
[19:06] it's also the best for coding more on AI
[19:09] coding with these models and future
[19:10] videos Cloud 3.5 basically wins in every
[19:13] category this isn't really interesting
[19:15] case if they just simply delete it but
[19:16] then we have to ask the next logical
[19:18] question why did they delete it right is
[19:21] it a funding issue do they not have the
[19:23] compute or is it again is it just a
[19:25] positive strategic decision are are they
[19:28] just FOC focusing on one powerful model
[19:31] and one fast model right which is going
[19:33] to be 3.5 ha cou I don't really see
[19:36] anthropic being short on ideas and
[19:38] Innovation to push on and it seems more
[19:41] likely that it's just a decision that
[19:43] they made more than a funding or compute
[19:45] issue because they're firing on all
[19:46] cylinders right all public sources State
[19:49] anthropic performing really really well
[19:51] so the last case and this is the
[19:53] prediction that's the most grounded in
[19:55] reality is that they simply remove the
[19:57] documentation because it's just not
[19:59] ready yet I put this at like mid-tier

### Minute 20

[20:01] probability they just need more time
[20:02] with it they're expanding it they're
[20:05] adding pieces of Chain of Thought or you
[20:07] know next level prompt chaining inside
[20:10] the model who really knows only they
[20:12] really know what's coming next on the
[20:14] Innovation side of things they're one of
[20:16] three leaders in model Innovation so
[20:19] only they really could know what's
[20:20] coming next to be fair though CLA 3.5
[20:23] Sonic is an incredible model especially
[20:25] after the upgrade so I'm not super
[20:28] worried about where 3.5 Opus is and if
[20:31] it comes out I'll be happy to see it if
[20:33] they move on from it and just go right
[20:34] to Cloud 4 that's fine too let me know
[20:37] what you think in the comments where do
[20:39] you think Claude 3.5 Opus has gone why
[20:42] is it not on their model page anymore so
[20:45] I hope you can see this theme AI agents
[20:47] are here in 2025 they're growing
[20:48] mainstream if you're here if you're
[20:50] watching this video you're here early
[20:52] it's time to capitalize as Engineers the
[20:55] question we must ask ourselves now is
[20:58] how quickly how much and how often are

### Minute 21

[21:00] we deploying compute in our development
[21:03] workflows right now this takes the form
[21:05] of prompts AI agents and personal AI
[21:08] assistants these are the big three you
[21:10] need to be focusing your time and effort
[21:12] on if you want those asymmetric results
[21:15] follow the channel to stay locked in to
[21:17] what you can do with this incredible
[21:19] generative AI technology available to
[21:20] you stay focused and keep building