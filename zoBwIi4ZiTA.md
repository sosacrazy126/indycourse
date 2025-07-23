# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=zoBwIi4ZiTA
- **Duration:** 23:21
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 4146
- **Transcript Generated:** 2025-03-30 23:48:46

## Transcript


### Minute 0

[00:05] Ada list all
[00:14] users command executed successfully Dan
[00:17] let me know what's
[00:18] next fantastic Ada create a new user
[00:22] named Steve give him the admin role and
[00:24] then list all users that are admins
[00:34] command executed successfully Dan let me
[00:36] know what's
[00:39] next a show our config in verbose mode
[00:43] and then show files in the current
[00:52] directory command executed successfully
[00:54] Dan let me know what's next

### Minute 1

[01:02] [Music]
[01:07] welcome back Engineers Andy Deb Dan here
[01:10] so we have something really really
[01:12] interesting here I have an always on
[01:16] personal AI assistant as you can see
[01:18] here I'm still talking and my personal
[01:20] AI assistant is still active this
[01:23] assistant is always on this is a massive
[01:26] step forward toward the always on
[01:29] compute system systems we talk about on
[01:31] the channel why is this important it's
[01:33] extremely valuable because it adds
[01:36] another dimension for you to get work
[01:38] done with compute if I stop talking here
[01:41] for just a moment we're going to see
[01:44] this transcript come
[01:47] through awesome so we can see we had
[01:49] that transcription come through it took
[01:52] 1.12 seconds this is running locally on
[01:55] my M2 and you can see here we picked up
[01:58] on every piece of text welcome back

### Minute 2

[02:00] Engineers Andy Dev Dan here so we have
[02:03] something really really interesting here
[02:05] blah blah blah blah blah you can see
[02:06] here that my personal a assistant did
[02:08] not do anything a did not do anything
[02:11] she did not get activated but I just
[02:13] literally just said a so now she's going
[02:16] to look for a command to run on this
[02:19] incoming transcription that will
[02:21] complete and execute when I stop talking
[02:23] so you know this is known as the
[02:25] activation keyword for your personal AI
[02:27] assistant now I need to give a a command
[02:30] to run um if we go ahead and you know
[02:32] just keep talking here so she doesn't
[02:34] execute anything if we look at our
[02:36] template. py file we have a whole list
[02:38] of commands that you can execute let's
[02:40] go ahead and run one here Ada generate a
[02:43] report for our tasks
[02:51] table command executed successfully Dan
[02:55] let me know what's
[02:58] next as you can see here that executed

### Minute 3

[03:01] perfectly we have this you know really
[03:03] long transcription ad was able to take
[03:06] that you know powered by Deep seek V3
[03:09] and generate the proper command for us
[03:12] right here we took that command and we
[03:14] executed it using our you know entire
[03:17] Suite of commands here and we got a
[03:20] awesome output here the technology has
[03:22] lined up for us to have an always on
[03:26] personal AI assistant that's what we're
[03:28] going to break down in this video I'm
[03:29] going to walk through a working version
[03:32] of a useful personal AI assistant for
[03:35] your engineering work that's built on
[03:37] incredible open source Tech as well as
[03:39] the insane coste effective deep seek V3
[03:43] language model so I'm going to clear and
[03:45] just boot a back up there's no problem
[03:47] having her just on listening in the
[03:50] background as long as we don't say our
[03:51] activation keyword she won't look for
[03:53] commands she won't try to execute
[03:55] anything there are three and a half and
[03:58] really three Essential Elements to any

### Minute 4

[04:01] personal AI assistant let's go ahead and
[04:04] focus in here if I open up our
[04:06] configuration file we can see all these
[04:08] items really clearly so there are three
[04:10] elements to the personal AI assistant
[04:12] speech to text language model and we
[04:15] have the text to speech there's a
[04:17] simplified version of this that I like
[04:19] to use we have the ears the brain and
[04:22] the voice just by looking at our
[04:24] configuration file here you can see all
[04:26] the tooling we're using for our personal
[04:28] AI assistant we have our assistant name
[04:31] we have our human companion name this is
[04:33] of course you or I and then we have
[04:35] those three key components right ears
[04:37] brain voice and then the actual voice
[04:41] configuration we're using a very very
[04:43] powerful open source Library I'm really
[04:45] excited to share with you here there are
[04:47] tons of tools in the open source
[04:49] ecosystem every once in a while a
[04:51] foundational piece of generative AI
[04:54] technology comes out AER is that tool
[04:56] for the AI coding ecosystem and realtime
[04:59] speech text is a key piece for the

### Minute 5

[05:01] personal AI assistant ecosystem I'm
[05:04] going to talk about this more in this
[05:05] video so as the ears we have a realtime
[05:08] speech to text tooling as the brain we
[05:11] have the Deep seek V3 language model
[05:13] this is an absolutely incredible model
[05:16] for an always on AI assistant why is
[05:19] that it's because as you know this model
[05:21] is insanely powerful while being
[05:24] extremely cheap we then of course have
[05:26] the voice um I like to use 11 laps for
[05:29] this now sponsored not an affiliate or
[05:31] anything like that but they are my
[05:33] favorite and they have the classic voice
[05:35] that I like to use for Ada you can then
[05:37] of course select the specific voice and
[05:40] that's our configuration we in this code
[05:42] base I'll be sharing with you here we
[05:44] have two assistants we have the typer
[05:46] assistant which wraps our typer AI agent
[05:49] functionality we'll double click into
[05:51] that in just a second and then we have a
[05:53] base assistant where where we're just
[05:54] running speech to text a language model
[05:57] and then the language model is simply
[05:58] responding the great part about the

### Minute 6

[06:00] tooling here is that when you combine
[06:02] them with a local llm provider like AMA
[06:06] we can now use 100% local private
[06:10] personal AI assistants that run right on
[06:12] your hardware for instance you can do
[06:14] something like this brain to AMA colon
[06:17] 54 Microsoft just recently released the
[06:20] official 54 version we can set that
[06:23] there and then we can also update the
[06:24] voice to just local with this
[06:27] configuration this AI assistant runs
[06:31] 100% locally obviously the voices and
[06:34] the Brain will take a performance hit
[06:36] there are things you just cannot do with
[06:38] these small slms they are getting there
[06:40] as we saw in our previous video when
[06:42] you're benchmarking these local models
[06:44] we can see that the performance is
[06:46] constantly increasing while the size of
[06:48] the models are coming down lumo 4 is
[06:50] like you're going to shake things up
[06:51] quite a bit like subscribe comment to
[06:53] stay plugged into that I'm really
[06:54] excited for the next wave of local
[06:56] models coming out I have the M4 Max over
[06:59] here in the corner that uh we're going

### Minute 7

[07:01] to be testing and benchmarking local and
[07:04] Cloud models on in the future with this
[07:06] configuration we can now run a version
[07:09] of a personal AI assistant fully local
[07:12] right now let's run our powerful version
[07:15] with deeps V3 and 11 Labs these are the
[07:18] three essential elements of the personal
[07:21] AI assistant before we dig into the
[07:23] realtime speech DET text functionality
[07:26] where you can have your assistant always
[07:28] on always listening awaiting to hear
[07:30] their activation keyword let's look at
[07:33] this brand new scratch Pad
[07:37] pattern so this is something that's
[07:39] really important that I think has been
[07:40] missing from the personal AI assistant
[07:42] it's been hard for me to really get True
[07:44] Value out of the personal AI assistant
[07:46] without this so every time our AI
[07:49] assistant ran it was generating output
[07:51] and attaching it to the scratch Pad this
[07:54] is a super important pattern because it
[07:56] gives your personal AI assistant active
[07:59] memory this is why I was saying three

### Minute 8

[08:01] and a half Essential Elements the active
[08:03] memory lets your personal AI assistant
[08:06] be updated with information that it
[08:08] gives but also really importantly
[08:10] information that you give this is key
[08:12] for engineering tasks because we're
[08:14] often learning discovering and tweaking
[08:16] our mental model of the problem or
[08:19] feature we're building as we go we're
[08:21] literally updating our active memory as
[08:23] we solve the problem I've found that in
[08:26] order to make personal AI assistance
[08:27] useful we need a similar structure for a
[08:30] personal AI assistant this scratch Pad
[08:33] serves that purpose very well there are
[08:35] many permutations of this pattern but
[08:38] this gives us the parto 80% so let's
[08:41] look at a concrete example of how this
[08:43] works Ada list users that are
[08:47] viewers command executed successfully
[08:49] Dan let me know what's next all right so
[08:51] if I pause a here if I open this up and
[08:54] let's edit this scratch Pad right so a
[08:57] ran a command she saw our request here's

### Minute 9

[09:00] our run command and then here's the
[09:03] output so this scratch Pad is fully
[09:05] updatable right so if I just come in
[09:06] here and I take a couple of these IDs
[09:09] and I create something new update user
[09:12] block and I'm going to have another
[09:14] block here create user
[09:17] block and then we'll have a delete user
[09:20] block okay in the create user block I'm
[09:23] going to say this
[09:24] Alex viewer Mary editor and then Steve
[09:31] admin and then for the delete user block
[09:34] all I'm going to do here is give a list
[09:36] of a couple of these IDs right so paste
[09:39] a couple of these user IDs in so that's
[09:41] great we now have this you know updated
[09:44] active memory okay our personal a
[09:46] assistant Ada can see this entire
[09:48] scratch Pad she can work with everything
[09:49] here she can also see all of her
[09:51] commands here right so we have a couple
[09:53] key commands here you know list users
[09:55] create user delete user let's go ahead
[09:57] give a reference to this blog I hope you
[09:59] can see where this is going I'm going to

### Minute 10

[10:01] give her a reference to this block and
[10:03] then I just want her to execute and do
[10:04] all the work that we would normally do
[10:07] much faster and all we're doing is kind
[10:09] of thinking at a high level we're
[10:10] updating our active memory our scratch
[10:12] pad and then letting our always on
[10:14] personal AI assistant do the work for us
[10:16] so I'll kick her off right here Ada go
[10:19] ahead and look at the update user block
[10:21] and run the respective create user and
[10:25] delete user commands
[10:31] command executed Dan let me know what's
[10:32] next okay so check this out so this is
[10:35] really cool right she created the
[10:36] command she you know created this giant
[10:38] execution statement and we got a couple
[10:41] of outputs here our created commands and
[10:43] then we also have our delete commands
[10:46] that failed so something went wrong here
[10:49] and I think it's because let me look at
[10:51] exactly how this delete user Works user
[10:54] ID might just be a single ID so yeah
[10:57] that looks right so what I'm going to do
[10:59] is I'm just going to ask a to to correct

### Minute 11

[11:01] this for us right so I'll say a rerun
[11:05] the delete commands but only use the
[11:08] actual um user ID so not the user undor
[11:12] prefix just use the numbers for the
[11:22] deletion command executed successfully
[11:24] Dan let me know what's next okay so
[11:27] really cool stuff here right we're
[11:28] talking natural language we're talking
[11:30] to our personal AI assistant and so I
[11:32] want to be able to say her name so I'm
[11:33] going to shut it down here so we're
[11:35] talking to our personal AI assistant Ada
[11:37] and she is taking this let me go ahead
[11:39] and go into formatted mode Let's Go full
[11:41] screen she's taking the entire scratch
[11:43] pad that we have set up here and she has
[11:45] access to all of it right so this is a
[11:47] dynamic variable inside of our prompt
[11:49] which we can take a look at in a second
[11:51] you know a can see everything in this
[11:52] prompt for her brain she's running the
[11:55] powerful deep seek version 3 so she's
[11:57] able to really reason about this and
[11:59] take our natural language request and

### Minute 12

[12:01] really work through it right it also
[12:03] helps that she's seeing my entire stream
[12:05] of thought as I'm you know talking to
[12:07] you here the key is at the ending here
[12:10] right where we just say you know rerun
[12:12] the delete commands only use the actual
[12:13] ID do not use the user prefix right so
[12:16] she picked up on that rewrote all the
[12:18] commands and then executed them right
[12:21] this is really powerful this is
[12:23] something that has been stopping me from
[12:24] using personal AI assistance and I think
[12:27] this pattern is finally going to enable
[12:30] you know a more fluid experience for
[12:32] myself and for you which is why I'm
[12:34] sharing it with you here if this makes
[12:36] sense if you can see where this is going
[12:37] if you can see the value of having an
[12:39] active memory and a personal AI
[12:42] assistant that can execute commands on
[12:43] your behalf hit the luck hit the sub
[12:45] follow the journey personal AI
[12:47] assistants AI coding AI agents this is
[12:50] what we're focused on on the channel our
[12:52] North Star is to build living software
[12:54] software that works for us while we
[12:56] sleep a big milestone and a big pattern
[12:58] toward that we're working toward is

### Minute 13

[13:00] having these always on compute systems
[13:04] and with some of the key technology that
[13:05] we're breaking into right now if we open
[13:07] up that config file once again we are
[13:09] moving closer to this goal every single
[13:12] day with every single video release you
[13:14] can see here ears brain voice we turn
[13:17] this on and it's always on the real key
[13:20] is that you know it costs nothing to
[13:22] have our ears always on right and
[13:25] whenever we want to we can say our
[13:26] activation keyword to activate our brain
[13:28] so so I hope you can see where this is
[13:29] all going right the scratchpad ACT
[13:32] memory pattern is going to be really
[13:34] important for rolling out useful
[13:36] personal AI assistance we ran that
[13:39] command she generated all of the output
[13:41] for us part of the command worked part
[13:43] of it didn't and then we you know asked
[13:46] her again to correct it to make some
[13:48] modifications to it I think the scratch
[13:49] Pad is going to be a really important
[13:51] powerful pattern for the personal AI
[13:53] assistant so before we talk about the
[13:56] actual prompt that's feeling it and you
[13:57] can see it right here right before we
[13:59] talk about this there's another key

### Minute 14

[14:00] piece of this that I I want to dig into
[14:02] for a moment here the real time speech
[14:05] to text
[14:09] libraries there are tons of Open Source
[14:11] tools released you know every single day
[14:13] most of them aren't super important most
[14:15] of them don't move the needle but this
[14:17] is a library that absolutely changes the
[14:19] game for personal AI assistants that are
[14:22] always on this is a library called real
[14:24] time St realtime speech to text massive
[14:27] shout out to the author this is
[14:29] incredible technology the key here is
[14:31] that you can just leave this on running
[14:34] all the time it has several models that
[14:36] you can work with if we search
[14:39] tiny this is the one I'm using this is
[14:41] what you can use for maximum speed the
[14:43] trade-off here is that the
[14:45] transcriptions are not going to be as
[14:47] accurate you can scale this up as much
[14:49] as you want you can use basan small uh
[14:52] and medium if we hop back over to our
[14:54] assistant here open up the typer Main
[14:58] typers assistant and search for tiny Ian

### Minute 15

[15:00] you can see I'm playing with these model
[15:02] settings here if we boost this up to a
[15:04] small Ian model or even a larger right
[15:06] we can go super big we can use large V3
[15:09] and if we boot adaa up again and if we
[15:12] just you know talk a little bit uh get
[15:14] some content here for Ada to transcribe
[15:17] for a personal AI assistant to
[15:18] transcribe it's coming in the ears which
[15:20] is powered by real-time speech of text
[15:22] and then if we pause for a moment the
[15:24] transcription process will actually kick
[15:25] off and notice how much slower this is
[15:27] than our previous execution
[15:30] okay so where was that you can see here
[15:32] the large V3 running on my device
[15:35] locally took 18 seconds okay the
[15:38] transcription was I think perfect right
[15:41] you know you can play with these models
[15:42] the larger models are going to be more
[15:44] accurate but you're going to lose a lot
[15:45] of speed right if we bump all the way
[15:47] back to our
[15:48] tiny and we restart this this is really
[15:51] incredible and we just you know say a
[15:52] couple things here we just want to pick
[15:54] up on some new information for a real
[15:57] time speech detects to transcribe for us
[15:59] and then if we

### Minute 16

[16:02] pause bam that ran insanely quickly
[16:05] right less than a second to transcribe
[16:08] and I have my post speech silence
[16:10] duration set to 1.5 I like to have a you
[16:13] know a little bit larger of a gap
[16:15] between the commands I'm running and you
[16:17] know ending my speech so you can adjust
[16:19] this U as much as you want that's the
[16:21] key here I think this is one of the most
[16:23] important you know pieces you can set
[16:25] the tiny model will give you those you
[16:27] know super fast uh but of course not as
[16:30] accurate transcriptions if we pause here
[16:32] we'll get another one out of this there
[16:33] we go right so again really incredible
[16:36] stuff 1.28 seconds for you know one kind
[16:40] of full paragraph of text let's go ahead
[16:42] and pause this really incredible stuff
[16:44] right this is foundational personal AI
[16:47] assistant technology I'm going to be
[16:49] using this moving forward for all my
[16:51] personal AI assistant Tech there's also
[16:53] a kind of opposite side Library real
[16:56] time text to speech as the author
[16:58] mentions the counterpart of this Library

### Minute 17

[17:00] feel free to check that out I have a
[17:02] little bit of that tooling rolled into
[17:04] this this code base but I'm not super
[17:06] strung out on it uh and this should be
[17:08] St because I prefer 11 labs for my voice
[17:12] uh technology but if you want to hop in
[17:14] check out this code base I recommend
[17:16] just to get started you use the base
[17:18] assistant and you switch it to local
[17:20] mode right so you can run this fully
[17:22] locally so that's the real time speech
[17:24] to text Library
[17:29] every piece of generative AI technology
[17:31] is some combination of code logic data
[17:35] information and variables that all at
[17:38] some point get inserted into one or more
[17:41] prompts this is where all the magic is
[17:43] happening here's the typer command
[17:45] prompt so let's just break this down top
[17:47] to bottom we have the purpose we have a
[17:49] set of instructions which detail exactly
[17:52] what the model should do and how it
[17:53] should do it and then we have our you
[17:56] know set of typ or commands so this is
[17:58] you know quite literally this file so we

### Minute 18

[18:00] insert 5K tokens into this variable we
[18:04] can optionally pass in context files and
[18:06] if we go to that main typers assistant
[18:08] file go to the top here you can see our
[18:12] key commands here right and if we also
[18:15] open up our adaa script you can see
[18:18] exactly how this is getting kicked off
[18:19] we're running UV python main typer
[18:22] assistant with the awaken command and
[18:25] we're passing in a couple variables the
[18:27] path to our typer file the path to our
[18:30] scratch pad and our execution mode okay
[18:33] so if we look at the variables to this
[18:35] we're effectively taking these variables
[18:37] loading them and then inside of our
[18:38] prompt replacing them right so here's
[18:41] our type of commands here's our context
[18:43] files here's our scratch Pad super
[18:45] important and then here's our of course
[18:48] natural language request so this will
[18:50] come in as we ask for things to be
[18:53] completed for us right so this is our
[18:55] typer assistant one massive problem I
[18:58] see in the general AI ecosystem is that

### Minute 19

[19:00] everyone's going way too wide they're
[19:02] trying to build systems that do
[19:03] everything you can see this most clearly
[19:05] in the AI coding ecosystem people who
[19:08] are building these all-encompassing AI
[19:10] coding uh editors that try to do
[19:13] everything I think that's a massive
[19:15] mistake when you're building a product
[19:16] this is the opposite of how great
[19:18] products are built if you want to build
[19:20] something great you start small you
[19:22] start focused you start Niche and then
[19:24] you learn how to do it well and then you
[19:27] expand once your users customers are
[19:29] actually interested then you expand and
[19:32] build up to more use cases right you
[19:33] know dialing in on this personal AI
[19:35] assistant I wanted something that I
[19:36] could reuse and something that could be
[19:38] useful today I'm not waiting for more
[19:41] stuff to happen for more things to be
[19:43] released there is more than enough
[19:45] incredible generative AI technology for
[19:47] us to work and build for years and years
[19:50] even if all progress stopped right now
[19:52] the typer AI agent underneath our
[19:54] personal AI assistant is what our
[19:56] assistant interacts with to get work
[19:58] done
[19:59] given a list of typer commands so if you

### Minute 20

[20:01] have you know a set of typer commands
[20:04] like this right just like we had you can
[20:06] use this right away right as long as you
[20:09] have a consistent command structure this
[20:11] is useful immediately and over and over
[20:14] for typer based commands and typer is
[20:16] one of my favorite python CLI command
[20:19] Builders lets you build out clis around
[20:21] specific use cases so you can see that
[20:23] in the prompt right we have all of our
[20:24] commands we have additional context
[20:26] files and then we have the scratch pad
[20:28] and of course the natural language
[20:30] request personal AI assistants are a
[20:33] untapped dimension of engineering it
[20:36] gives you access to another layer of
[20:38] engineering that can run in parallel to
[20:40] you it's definitely a different way to
[20:42] work and just like all new technology
[20:45] just like you know continuing that trend
[20:46] of learning new skills this new
[20:49] technology is going to take practice to
[20:51] understand how to use personal AI
[20:53] assistant the right way it's going to
[20:54] take time to adjust to you know typing
[20:57] getting work done and speaking out loud
[20:59] to your assistant which can take work

### Minute 21

[21:02] offload it put it on to compute and work
[21:05] with you alongside you right we want to
[21:07] take incremental steps toward compute
[21:09] that's always on always solving problems
[21:11] for us always getting work done on your
[21:15] behalf when we look toward the future of
[21:16] personal AI assistants to me it's easy
[21:18] to see that once you start using it they
[21:20] can make you incredibly capable the next
[21:22] steps of this are very obvious they're
[21:25] kind of already getting rolled out into
[21:27] you know for instance chat GPT Claude
[21:29] you can give your assistant Vision let
[21:31] them see your screen right right this
[21:33] effectively expands the uh scratch pad
[21:36] to a kind of additional live feed you
[21:39] can let your assistant write code for
[21:41] you right imagine if one of our template
[21:44] commands here is you know execute code
[21:48] or write code or delete code or modify
[21:50] this is a big big Trend that we are
[21:53] steps away from if you've taken
[21:56] principal AI coding we do nearly all the
[21:58] preparation work both mentally and you

### Minute 22

[22:01] know digitally with our AI tooling that
[22:03] enables us to break into personal AI
[22:06] assistant based AI coding more on that
[22:09] in future videos an obvious Improvement
[22:11] here is to wire up different AI agents
[22:14] different purposes tweak the underlying
[22:16] models and prompts that your personal AI
[22:19] assistant can see and use and get work
[22:21] done with we can really play around with
[22:23] the ears brain and voice so those are a
[22:27] couple next steps for this feel free to
[22:29] Fork this code base get your personal AI
[22:31] assistant up and running at least kind
[22:33] of understand where things are going I
[22:35] think that personal AI assistant are a
[22:36] you know kind of next gen pattern that
[22:39] uh you know we can get into here early
[22:41] on the channel I'll be using this
[22:43] literally today after I you know
[22:45] finished filming this video to scale up
[22:47] my engineering even further I'm going to
[22:49] make this more reusable I'm going to
[22:51] make it easier to use so that I can you
[22:53] know write in the CLI Ada awake and then
[22:57] pass in the configur ation variables

### Minute 23

[23:00] inside of whatever code base I'm working
[23:01] on right so I can run this anywhere
[23:04] everywhere and we use this typer agent
[23:06] built inside of the personal AI system
[23:08] if you found these ideas and the easy
[23:11] access to this technology valuable hit
[23:13] the like hit the sub drop a comment and
[23:15] I'll see you in the next one stay
[23:17] focused and keep building