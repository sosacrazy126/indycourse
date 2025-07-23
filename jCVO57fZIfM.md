# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=jCVO57fZIfM
- **Duration:** 36:43
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 6945
- **Transcript Generated:** 2025-03-30 23:48:34

## Transcript


### Minute 0

[00:00] what's up Engineers Indie Dev Dan here
[00:02] we have an actionpack video today GPT
[00:07] 4.5 was
[00:10] released and uh moving on from that no
[00:14] gb2 4.5 is an amazing model
[00:16] unfortunately it's insanely expensive to
[00:19] use through the API it's only really
[00:21] usable for chat GPT Pro members but of
[00:24] course we need to focus in on the most
[00:27] important release potentially of the
[00:30] entire year Claude 3.7 Sonet and Claude
[00:35] code not only did anthropic release the
[00:38] absolute best base model they released a
[00:43] Hybrid Base reasoning model with
[00:46] thinking capabilities embedded inside of
[00:50] the model they've effectively released
[00:52] two models in one and not only not only
[00:56] did they release a twoin one model they
[00:58] also released Claude code you've likely

### Minute 1

[01:02] been using this if you're a fan of the
[01:04] Indy de Dan Channel you know how
[01:06] important air coding assistants are you
[01:08] know how important agents are this is an
[01:11] absolute crash out release okay I'm I'm
[01:15] telling you guys when I saw this when I
[01:17] read through this I started to lose my
[01:19] mind in this video we're going to
[01:21] Showcase several examples of how
[01:23] powerful this can be and of course we're
[01:25] going to use cloud code now we're going
[01:27] to break this down because uh this
[01:29] release changes things the most
[01:32] important image here it's this one
[01:35] agentic tool use the accuracy to be able
[01:39] to call the right tool at the right time
[01:42] is very very very important for the
[01:44] agentic future that we're moving into
[01:46] for building out effective powerful
[01:49] agents as we've been discussing on the
[01:51] channel over the previous few videos one
[01:53] more thing I want to point out before we
[01:54] jump in I am kind of mind blown that
[01:56] they called this
[01:58] 3.7 the first thing I thought when I saw

### Minute 2

[02:00] Cloud 3.7 3.7 Sonet is holy crap how far
[02:07] ahead are they inside the lab they they
[02:09] bumped soned up only two points and they
[02:12] gave it reasoning capabilities and it's
[02:15] the state-of-the-art based model now and
[02:18] they kept the price the same this is
[02:20] absolutely incredible uh let's dive into
[02:22] it what are we talking about today uh
[02:24] what's the idea for today's video how
[02:25] can we you know make sense of this and
[02:27] get value and all these incredible tools
[02:30] don't matter at all if we can't
[02:32] understand them build them and use them
[02:34] in our tooling and our developer
[02:35] workflows and then deploy them against
[02:38] real problems to actually create value
[02:42] okay let's be super clear and really
[02:44] honest about you know a lot of the tech
[02:46] ecosystem there are shells among shells
[02:49] of content creators and digital media
[02:52] idea pushers that don't actually use
[02:54] this technology and build with it I hope
[02:56] you can tell we actually build here on
[02:58] the channel if you've seen more than two

### Minute 3

[03:00] of my videos you know that that's the
[03:01] case I always try to take everything
[03:03] we're getting of this incredible
[03:05] generative AI technology and I always
[03:07] aim to create useful packages of
[03:09] information and ideas and patterns and
[03:11] principles and I try to you know hand
[03:13] them to you as much as I can every week
[03:15] here every single Monday so this week
[03:18] you know I have something that I think
[03:19] will be really helpful I have the clog
[03:21] 3.7 Sonet starter pack so inside of the
[03:24] starter pack you basically have
[03:26] everything you need to understand every
[03:28] one of the key capabilities of this
[03:30] model so that's what we're going to work
[03:31] through today this is going to be linked
[03:33] in the description for you this is my
[03:35] current model ranking and I'm super
[03:37] curious to see what you think about this
[03:38] leave a comment down below what do you
[03:40] think the current model ranking is in
[03:42] terms of raw power and intelligence uh
[03:45] despite any costs I completely forgot to
[03:47] add 01 in here that's going to be pretty
[03:48] high ranking too let's dive in let's
[03:50] break down the new 3.7 Sonet Hybrid Base
[03:55] plus reasoning model and let's talk
[03:57] about clog code

### Minute 4

[04:02] so let's go ahead and open up the Claude
[04:05] 3.7 Sonet starter pack we got to talk
[04:07] about the model stats 200k in 8k out as
[04:11] you'll see in this video you can extend
[04:13] the output token to 128k this is pretty
[04:17] crazy and then of course even crazier we
[04:20] have 64k thinking tokens that we can
[04:24] allocate we're effectively turning on
[04:26] and off our raising model capability
[04:28] with 3.7 on it at at will okay so we're
[04:31] doing this whenever we want we have one
[04:32] of the most up-to-date models by far you
[04:35] know November 2024 fantastic pricing um
[04:38] effectively no changes and they've
[04:39] boosted the capabilities I think they
[04:41] kind of learned a hard lesson from um
[04:44] releasing ha coup U at that frankly
[04:47] really terrible price we're going to
[04:48] dive into my uh extended thinking
[04:50] intelligence guide here's kind of how
[04:52] I'm framing where to set your thinking
[04:54] budget when you're using the uh
[04:56] intelligence model basically there's
[04:58] almost no reason to use any one of these

### Minute 5

[05:01] high settings unless you're solving
[05:03] incredibly difficult challenging
[05:05] problems okay um but we're going to get
[05:07] into that in a second let's just go
[05:08] ahead and fire up some examples all
[05:10] right so we're going to start from the
[05:12] most simplest we're just going to recap
[05:13] the simple examples and then we'll move
[05:15] into some of the uh High hitting
[05:17] examples and you know what actually
[05:19] scratch that um I'm too amped on this
[05:21] stuff we're just going to hop right into
[05:22] prompt with extended thinking I'm going
[05:24] to copy this I'm going to open up this
[05:25] file and at the top of every one of
[05:27] these files here you're going to see
[05:29] Clean and Clear instructions on how
[05:31] exactly to use every single one of these
[05:33] scripts these are powerful single file
[05:36] UV scripts we've talked about this in
[05:37] previous videos this is a fantastic way
[05:40] to isolate code it's a great way to run
[05:43] proof of Concepts and it's a great way
[05:45] to run as we talked about in our
[05:46] previous video single file agents moving
[05:48] on let's go ahead and copy this and
[05:51] let's just paste this in and fire it off
[05:53] so you can see here right away with the
[05:55] parameters here we're setting both a
[05:56] thinking budget and a Max tokens now so
[05:59] let's Ry this off and let's check out

### Minute 6

[06:00] the output so I've got this all
[06:01] formatted here for you so we have the
[06:03] request to Claud explain Quantum
[06:06] Computing to me all right and then we
[06:08] have some a thinking budget right so
[06:10] we're setting the minimum thinking
[06:12] budget 1,24 tokens so this is the raw
[06:15] API response coming back from Claude and
[06:17] you can see here we have a different
[06:19] type of structure than we're used to
[06:20] right we have not just the response
[06:23] block but we also have a thinking block
[06:26] all right so there's the signature of
[06:28] the thinking block which is just a hash
[06:30] and then we have the actual thinking
[06:32] tokens right so now this is visible to
[06:35] us so you can see it you know just
[06:37] working through the examples it's kind
[06:38] of setting up its response and then
[06:41] finally it's responding and if we scroll
[06:43] down here you can see here right that
[06:45] classic reasoning setup we have thinking
[06:47] tokens first and then we have the actual
[06:49] response afterward at the bottom of
[06:52] every one of these scripts I've added
[06:54] the token summary for you so that you
[06:55] can just kind of quickly see what the
[06:57] cost looks like right so we have inut
[06:59] tokens output tokens and now we have

### Minute 7

[07:02] thinking tokens that we can push up and
[07:04] down based on our use case so if we look
[07:06] at the script for a moment here you can
[07:09] see we have our parameters that we can
[07:11] play with an important thing to note the
[07:12] minimum thinking budget is 1,24 tokens
[07:16] so if you need the reasoning model this
[07:18] is the minimum value you should set
[07:19] classic Model set up here nothing
[07:21] special happening but you can see this
[07:23] is the new uh input structure for
[07:26] enabling thinking mode you specify this
[07:29] thinking parameter and then you say
[07:31] enabled and then you specify what your
[07:33] budget is right so this is the budget
[07:35] tokens so very cool and then nothing
[07:38] special happening down here we're just
[07:39] outputting the result and formatting
[07:41] really powerful really simple right at
[07:42] kind of a great simple API let's go
[07:45] ahead and look at the prompt extended
[07:47] thinking with
[07:51] stream so let's go ahead and push into
[07:54] the actual value that reasoning models
[07:57] give us they enable you to solve hard
[07:59] problems where the model always benefits

### Minute 8

[08:04] from having time to think just like you
[08:06] or I solving a hard problem thinking
[08:08] through a complex scenario I really love
[08:10] that simple example right if someone
[08:12] asks you a question uh that's
[08:13] challenging or difficult you don't just
[08:15] blurred out the first thing that you
[08:16] think of right um some of us do so when
[08:19] you're confronted with a hard problem
[08:20] you sit and you think right that's what
[08:22] these thinking budget tokens give us
[08:24] here's a whole list of actual reasoning
[08:27] problems that you can work through here
[08:29] that you can you know look at the
[08:31] answers are right above it so let's go
[08:33] ahead and just copy this one and let's
[08:35] let this rip we have 2,000 token
[08:37] thinking budget this is a simple math
[08:38] problem and this is a cool streaming
[08:41] example okay so this is a prompt with
[08:43] extended thinking with streaming let me
[08:46] go ahead and run that again so I'm going
[08:47] to paste this again and then check this
[08:48] out so we have the prompt tokens and
[08:50] then you can see the ANS are getting
[08:51] streamed in here right so we can see the
[08:54] live thinking process of our model and
[08:56] now here's the response bam and there's
[08:58] the output let's go ahead and check
[08:59] check it against the actual answer

### Minute 9

[09:03] 48924 that's the exact correct answer
[09:06] right so this is really cool right we
[09:07] have both the final answer but we can
[09:10] also see how our model got there and you
[09:13] can see this one actually took up some
[09:16] thinking tokens this was actually a math
[09:18] problem that required some real thought
[09:20] from the model so you can see here the
[09:22] output tokens was just 60 but it took
[09:24] 232 tokens to actually think through the
[09:28] answer and give you a solid response so
[09:30] to be 100% clear this is what you know
[09:33] these powerful reasing models are all
[09:35] about and now you have full control over
[09:39] the scale of intelligence of the model
[09:41] with the thinking budget tokens let's
[09:44] just go ahead and run another one this
[09:45] is a simple you know uh logical puzzle a
[09:49] says that b is lying B says that c is
[09:51] lying C says that A and B are both line
[09:54] who is telling the truth right so we can
[09:56] give Claude 3.7 some time to think here

### Minute 10

[10:00] and we can see that thinking getting
[10:01] streamed in you know really working
[10:03] through this problem with 2,000 tokens
[10:06] and now we have the answer so now it's
[10:07] formatting the actual output for us bam
[10:10] therefore B is the only one telling the
[10:12] truth and you know I've worked through
[10:13] this problem um B is telling the truth
[10:16] so this is the correct answer really
[10:18] powerful really capable and you can see
[10:19] here again I I I just love the
[10:22] visibility here and I love the fact that
[10:24] we can peer into the model and you know
[10:26] this is something that anthropic
[10:27] mentioned is going to be really
[10:28] important for model safety moving
[10:30] forward and I think it's just a great
[10:31] approach for that right when you can see
[10:33] the model thinking it's a lot easier to
[10:36] understand how it's deriving the actual
[10:37] answer for you right so this is awesome
[10:40] uh I think you can kind of get a good
[10:42] idea of the primary capabilities of the
[10:45] extended thinking let's go ahead and
[10:47] continue working through some examples
[10:48] but let's fire up plug
[10:53] first if we clear the terminal and just
[10:56] type CLA you can see here I have two mCP
[10:58] servers connected we'll talk about these

### Minute 11

[11:00] in a moment but let's just at a high
[11:02] level really discuss what this is okay
[11:06] what is CLA code really um anthropic
[11:09] explicitly mentions this a couple times
[11:12] if we just search agent you can see this
[11:14] keyword coming up um a couple times okay
[11:18] this is a very very important keyword
[11:20] and paradigm shift that's happening
[11:22] right now we're moving up the
[11:24] abstraction chain of generative AI as
[11:27] we've talked about in many previous V
[11:28] videos over the course of the past 2
[11:30] years you start with the prompt then you
[11:32] move to the prompt chain prompt chains
[11:34] are also known as these agentic
[11:36] workflows or graphs but then the next
[11:39] step is give the agent the tool it needs
[11:42] give it a powerful model tell it how to
[11:44] solve your problem and then let it run
[11:46] off and actually solve the problem for
[11:48] you to be super super clear what is
[11:50] cloud code Cloud code is an AI agent
[11:54] this is pure genius from anthropic a
[11:56] research preview developer tool where we
[11:58] pay for their model send them our

### Minute 12

[12:01] prompts so that they can improve uh the
[12:04] tool and their model I have upped my
[12:07] token usage maybe I'll throw a photo on
[12:09] the screen 100 fold using the new uh CLA
[12:13] 3.7 model in agents and in the new Cloud
[12:17] code what what can we do with this tool
[12:19] I just want to run a couple commands
[12:20] that showcase uh what this thing can
[12:22] really do you know we had some examples
[12:24] here right some puzzle examples Cloud
[12:26] code obviously it can write code you
[12:28] you're going to see 100 videos on cloud
[12:30] code writing code we'll dive into that a
[12:32] little bit more later I want to stress
[12:33] how important it is that this is an
[12:35] agent so we can do agentic things right
[12:38] it has several tools available list
[12:40] files
[12:42] respect get ignore now cloud is thinking
[12:46] and it's going to use one of several
[12:48] tools available to it it's not using
[12:50] traditional LS it's using git LS files
[12:54] okay so I'm going to hit yes this model
[12:56] called The Bash tool let's run something
[12:59] else update and I'm going to uh use a

### Minute 13

[13:01] hotkey I I strongly strongly recommend
[13:04] that you set up this hotkey for me it's
[13:06] command shift R now I have the relative
[13:08] path to this file so I'm going to paste
[13:10] this in and I'm going to say update this
[13:13] file add a usage example all right so
[13:18] CLA code kicking off it's running a read
[13:21] tool there was The Bash tool now we're
[13:23] running the read tool it's reading this
[13:25] entire file right I think that's the
[13:27] entire file yep 253 lines it's thinking
[13:29] it's working through this it's
[13:31] understanding what it needs to do and
[13:32] then in a moment here it's going to call
[13:35] the update tool okay update tool
[13:39] requires the file path and it also is
[13:42] going to have you know whatever it's
[13:44] it's actually going to update with right
[13:46] so you can see here here's another
[13:48] example it's a little too heavy for me
[13:50] so I'm going to say uh just going to tap
[13:51] Escape just add the UV run what is the
[13:56] dot dot dot to the usage examples
[13:59] nothing else as incredible as this tool

### Minute 14

[14:01] is it's still going to make mistakes
[14:03] right so there we go so I had to be more
[14:05] specific with my prompt there and do you
[14:07] want me to make this edit yes so this is
[14:09] really cool right you can go into YOLO
[14:11] mode or you can run one by one all right
[14:14] so I'm going to hit yes and then you can
[14:16] see there uh it ran update file with
[14:19] that change I just want to really
[14:21] emphasize this point we have update we
[14:23] have read we have bash this is an agent
[14:27] this is an AI agent it has a suite of
[14:30] tools a really powerful prompt right a
[14:33] powerful comprehensive prompt as you
[14:35] likely know you can connect to model
[14:38] context provider
[14:42] server if we just go ahead and clear and
[14:46] rerun you can see there I have these two
[14:48] servers connected let's hop into our
[14:51] server fetch example so this file
[14:53] showcases how you can add an mCP server
[14:57] directly to CLA code I I've already run
[14:59] this so basically you run Claude mCP add

### Minute 15

[15:02] Fetch and then you specify the clii
[15:04] arguments that you would need to run
[15:05] this we're using UV so that we don't
[15:06] have to do any setup and then you can
[15:08] run Claud mCP list if you open up a new
[15:10] terminal here and run this you can see I
[15:12] have those two servers set up and you
[15:15] can see the exact commands right so
[15:16] we're going to run my local mCP server
[15:19] in a moment here let's just go ahead and
[15:20] run this you know simple fetch example
[15:22] copy one of these examples and I'm being
[15:24] super lowlevel here with this prompt uh
[15:27] I can you know be a lot looser with it
[15:29] you can see there it's calling the fetch
[15:31] tool and there's the response fantastic
[15:35] let's go ahead and pull from the
[15:36] principal a coding page and list the
[15:38] names of the lessons and descriptions of
[15:41] every single lesson so let's copy this
[15:43] paste this and let's watch Cloud code
[15:46] get to work so again it's calling that
[15:48] fetch tool the tool has pagination built
[15:51] in it's going to you know get the next
[15:53] end pages so that we don't get too much
[15:56] back in one shot but you can see this
[15:58] right here right um these are all the

### Minute 16

[16:00] names hello AI coding world the your
[16:02] idks spec base a coding let the code
[16:04] write itself so on and so forth it's
[16:05] doing a great job here it used that tool
[16:08] and it processed everything exactly the
[16:10] way we needed it to uh very very quickly
[16:12] and again I I'm going to sound like a
[16:14] broken record but it just called a tool
[16:16] these are tools that the agent has
[16:18] access to and can properly call this is
[16:21] why in the beginning I mentioned that
[16:24] this is the most important Benchmark
[16:27] chart here okay it's it's the agentic
[16:30] tool use I don't think it's truly
[16:32] understood currently how important this
[16:34] Benchmark is you need to be able to call
[16:38] the right tool when you need it for
[16:40] powerful agentic tools applications and
[16:43] to build powerful agents you need
[16:46] precise tool calling this is great uh we
[16:49] can do uh even more with this right so
[16:53] we can do the same thing is an agent so
[16:55] just you can just ask itself back to
[16:57] back to back so we're going to do the
[16:58] exact same thing and then we're saying

### Minute 17

[17:00] then write these to a markdown file all
[17:02] right so just a couple more examples
[17:04] here I just want to you know really nail
[17:05] this point home searching through the
[17:07] page thanks to this tool it's making
[17:09] multiple tool calls to fetch and then at
[17:12] the end it's going to there we go it's
[17:14] going to run the uh right tool okay
[17:17] right tool right you can see file path
[17:20] uh let's go ahead and say uh yes
[17:22] normally I run this in Yolo mode and it
[17:24] just kind of you know does all the work
[17:25] for me we can type GS this is get status
[17:28] and you can see that new file created
[17:29] there let's open that up here's all the
[17:31] lesson names and the description okay so
[17:34] all I want to do here is dial in the
[17:36] point the idea that this is an AI agent
[17:38] with a slew of tools that you can call
[17:41] in any order as long as you're prompt
[17:44] communicates that to the agent and and
[17:47] and you know if you're using this tool
[17:48] you understand that you're working
[17:49] through that but this is just such an
[17:51] important Point why because claw code is
[17:53] just a single agent all right it's it's
[17:56] one agent they're going to be many many
[17:59] many more agents and you as an engineer

### Minute 18

[18:03] um Can Build and harness the
[18:05] capabilities of these agents the the
[18:08] really key important part is that you
[18:10] understand that these agents are a
[18:12] series of tools powered by a great
[18:14] prompt fueled by a great language model
[18:18] and this is part of why this release is
[18:21] so great Claude 3.7 is exceptional at
[18:24] calling the right tool when you need it
[18:27] super impressed with the coding
[18:29] capabilities of claw code we'll dive a
[18:32] lot more into actually using this tool
[18:34] you know there's a lot of chatter right
[18:36] now you know does this replace cursor
[18:37] AER Devon in their release they
[18:40] explicitly mention you know cursor
[18:42] mentioned Claude uh cognition right so
[18:45] Devon far better than any other model at
[18:48] planning code changes and handling full
[18:50] stack updates right basically what
[18:52] they're saying here what everyone is
[18:53] saying is that this model Powers my
[18:57] agents very well all right and and then
[18:59] of course you know uh it's great at

### Minute 19

[19:01] coding too right it's kind of expected
[19:03] this is the you know Claude 3.5 son it
[19:06] was the best-in-class base model for
[19:09] coding 3.7 takes it to the next level
[19:12] and again I'm I'm I'm super super mind
[19:14] blown that they only gave us two points
[19:17] here right they only incremented the
[19:19] minor version here by 2 points
[19:22] 3.7 what else do they have in the bag so
[19:25] let's go ahead and run my local mCP
[19:27] server all this is going to do is just
[19:28] call a weather endpoint but this really
[19:30] showcases how uh quickly you can set up
[19:33] a mCP server when you have the right
[19:35] tooling so basically you just run this
[19:38] and then you fire up cloud and of course
[19:40] make sure you have UV installed let's go
[19:43] ahead and open up CLA and you can see
[19:45] here we have this local weather mCP now
[19:47] we can reference and just call our
[19:49] weather tools we can just copy this one
[19:51] what is the weather in Germany right now
[19:53] just go and fire that off and you can
[19:55] see there my tool is getting called
[19:57] right my uh mCP server get forecast

### Minute 20

[20:00] passing in the parameter Germany all
[20:02] right so that's getting called 37 partly
[20:05] cloudy wow high humidity there right all
[20:07] right so great call it again and again
[20:09] and again right it's an agent just push
[20:11] it push the compute right so now it's
[20:14] going to make three tool calls Bam Bam
[20:17] Bam Germany Chicago San Fran very nice
[20:19] all right push it even further get the
[20:21] weather in all of these places output it
[20:24] to a markdown file right so copy paste
[20:27] same deal push the capabilities push the
[20:28] agent see what it can really really do
[20:30] right I can almost guarantee you you're
[20:32] not pushing this agent far enough you're
[20:35] not pushing agents far enough especially
[20:38] when it's powered by this incredible
[20:40] clae 3.7 Sonet look at this so you know
[20:43] pulled the weather it's calling the
[20:45] create tool right and of course we're
[20:47] going to hit yes now it's Sav GS get
[20:49] status we now have that new weather file
[20:51] open that up format it nice breakdown of
[20:54] the weather right single prompt firing
[20:57] off what was that six tool
[20:59] and you know that's the kind of key idea

### Minute 21

[21:01] here I know I'm being repetitive this
[21:03] hasn't been made clear enough the actual
[21:05] Innovation that's happening here CLA
[21:07] code is incredible because it is putting
[21:11] together the model that can call the
[21:15] series of tools to get the job you want
[21:17] done completed right that's that's the
[21:20] real Innovation here it's the model it's
[21:22] the framework of mCP and it's a great
[21:25] Showcase of those things coming out of
[21:27] claw code right and of course you know
[21:29] some of the obvious commands here we can
[21:30] hit slash cost looks like it's modeled
[21:33] very closely after ader and you know
[21:35] other great terminal based tools let's
[21:38] go ahead and push it even further here's
[21:40] a fun one right warmest to coolest list
[21:43] of temperatures in the capital of all
[21:45] these countries and then output to
[21:47] warmest coldest Capitals in a markdown
[21:49] table right so all right so you can see
[21:51] here Washington DC unknown unknown
[21:53] unknown and now it's trying again now
[21:55] it's doing something really really cool
[21:57] it's firing off a Tas TK I don't know if
[21:59] there's a lot of documentation on the

### Minute 22

[22:00] task tool let's go ah and see yeah so
[22:02] there's not really any documentation on
[22:04] the on the task tool but the task tool
[22:05] in itself is really really interesting
[22:07] you can see here it's fired off you know
[22:09] it missed Miss missed and then it
[22:12] created this task so this agent is kind
[22:15] of passing off work to a sub agent very
[22:19] very important idea there for agent
[22:20] orchestration and context management
[22:23] then we got a bunch of additional
[22:24] weather calls and then we got the create
[22:27] and now we can fire this off you can see
[22:28] that that is coming in sorted and once
[22:31] again we can just click open this file
[22:34] format and you can see there we have
[22:36] capital country temperature top to
[22:38] bottom the agent is doing a series a
[22:43] chain a you know a job set of work for
[22:48] us and we are typing in natural language
[22:50] we're making sure that our prompt is
[22:52] communicating what we want and we're
[22:53] moving more toward prompting something
[22:56] like this is a lot different than
[22:57] prompting a crap of code so you don't
[22:59] really need the mid lowl prompt details

### Minute 23

[23:03] that we discuss in principal ad coding
[23:06] but you can see here just with the right
[23:08] details with the right amount of
[23:10] information we have you know 10 tool
[23:12] calls happening right and it's all about
[23:16] that information density in your prompt
[23:18] are you communicating the right ideas to
[23:20] your agent to get the job done so
[23:23] incredible stuff there uh that's the
[23:25] local mCP server again all this stuff is
[23:27] going to be linked in the description
[23:29] for you to check out uh really dive in
[23:30] and understand how this is set up and
[23:33] how you can build your own mCP servers
[23:35] how you can reuse existing mCP servers
[23:37] there are quite a few mCP servers that
[23:41] you can you know get and use just right
[23:43] out of the box right all the ones you
[23:45] would expect SQL light right we have uh
[23:47] post grass and we have tons of third
[23:49] party uh tools so you know it really is
[23:53] looking like anthropic with CLA code
[23:57] they are Paving the away in this next

### Minute 24

[24:00] age in this next kind of phase of
[24:02] generative AI where what you really want
[24:05] is to be plugged up to all the right
[24:08] agent tools right and then you want a
[24:10] powerful model that can guide your agent
[24:14] so that it's always calling the right
[24:15] series The Right steps the right flows
[24:18] of tools with the right parameters
[24:20] really really big idea here you know
[24:21] once again on the channel we're right on
[24:23] track agents agents agents check out the
[24:27] previous few videos where we talk about
[24:28] about
[24:31] agents prompt with extended thinking and
[24:35] Tool use just going to go ahead and copy
[24:37] this open up this file scroll to the top
[24:39] as I mentioned there's going to be
[24:40] complete examples in every one of these
[24:42] scripts you can just copy and fire off
[24:44] ourselves I'm just going to paste this
[24:45] in and you can see here we have a couple
[24:48] of tools right so now we have two tools
[24:51] and what's going to happen here is that
[24:53] claw 3.7 is going to run the right tool
[24:55] based on our prompt right so you can see
[24:58] here prompt what's the weather in
[24:59] Minneapolis what should I wear and then

### Minute 25

[25:02] we're giving it a little bit of thinking
[25:04] budget right the minimum thinking budget
[25:06] a little bit of thinking helps the model
[25:07] it really doesn't need to think here
[25:09] just as an example you can see exactly
[25:11] what's happening here all right and so
[25:12] we're thinking through there's the
[25:14] output and it's calling those tools
[25:17] right tool use request location
[25:19] Minneapolis great there's a response and
[25:21] then we have the uh another tool use
[25:23] request get clothing recommendation and
[25:26] this in itself is just another prompt
[25:28] that's running and it is returning this
[25:31] right I recommend wearing a you know
[25:33] medium weight jacket blah blah blah so
[25:35] just a simple example that you can work
[25:37] through to understand how you can call
[25:39] tools with claw let's go ahead and
[25:41] continue pushing here let's look at the
[25:44] biggest you know most heavy-hitting
[25:47] example we can prompt with extended
[25:49] output and extended thinking and
[25:51] streaming let's go ahead and just uh
[25:53] look at what's happening here another
[25:55] great part about claw 3.7 Sonet is that
[25:57] it is very precise and it truly follows

### Minute 26

[26:01] your instructions so when we say
[26:02] something like this generate a 10,000w
[26:06] comprehensive analysis on Renewable
[26:07] Energy Technologies we set a high Max
[26:10] tokens and then we set thinking budget
[26:11] okay and then I'm enabling extended
[26:14] output right uh 13k tokens out this is
[26:17] going to go um above the
[26:20] 8K output that uh Claude has here right
[26:24] so we need to boost this up to a
[26:26] potential 100 28k out uh so we can copy
[26:30] this and py this off this is going to be
[26:32] really cool so here it is here's our
[26:34] live you know stream right our live
[26:37] stream of the thinking process you can
[26:39] see Claude thinking and now it has the
[26:41] answer and now it's just going to run
[26:44] through these tokens all right so what
[26:46] did we ask for here we said 10,000 words
[26:50] so you can see there you know 500 this
[26:53] is going to just keep ticking up it's
[26:55] scrolling out of view here uh so we're
[26:58] we're just going to wait for the the uh
[26:59] response words to come in here but this

### Minute 27

[27:02] is pretty incredible right we're getting
[27:04] um insane model instruction following
[27:07] again we have other examples here be
[27:09] careful when you fire these off this
[27:10] will you know hit the API and likely you
[27:13] know consume the tokens it takes to
[27:15] respond with the prompt right the
[27:18] extended output token flag really
[27:21] enables you to to push the output of the
[27:22] model far beyond you know any model
[27:25] we've really seen before so you can see
[27:27] here it's still pushing right 3K tokens
[27:30] you can see it's about 10% of the uh
[27:33] total available token usage that's great
[27:36] you can see it only used you know 300
[27:38] tokens to think far below the thinking
[27:41] budget we gave it of what do we give it
[27:43] here uh 8,000 yeah just this is not a
[27:45] reasoning problem to solve right so we
[27:47] could have easily dropped this down to
[27:49] 1K while this is running you know let me
[27:51] give you my quick guide here on
[27:53] intelligence right how much intelligence
[27:54] do you really need to solve any problem
[27:56] a big takeaway here is that
[27:58] we now have fine grain control over the

### Minute 28

[28:01] reasoning capabilities of this powerful
[28:03] model so this is the way I like to slice
[28:05] it up basically we have extra small
[28:07] intelligence all the way up to 4 XL you
[28:10] basically will never need this you you
[28:12] basically will never need to push the
[28:14] model this far this hard uh it is a lot
[28:16] more likely that you'll push into these
[28:18] ranges you know given that you're
[28:19] solving an interesting enough problem
[28:21] where the model actually needs to think
[28:23] as anthropic mentioned I found this to
[28:25] be really useful basically you just
[28:26] start with the bare minimum and you know
[28:28] track your token usage as we are here if
[28:31] you never hit the 1K Mark you never need
[28:33] to go to 2K all right so this is really
[28:35] cool so we just finished and you can see
[28:37] here um our output tokens chewed up you
[28:40] know 6K right so we really really pushed
[28:43] it we really got that uh wow look at
[28:46] look at that up you can really see that
[28:47] this model pushed uh really hard here my
[28:51] word calculation is likely off we're
[28:53] likely not counting it likely got a lot
[28:55] closer here than than we think when
[28:57] you're really pushing the out tokens
[28:58] this is when you're going to boost up uh
[28:59] the cost so this is really powerful

### Minute 29

[29:01] right so this is an example of using
[29:03] both the uh streaming with the extended
[29:07] 128k token output and we can just goe
[29:10] and search this so you can see exactly
[29:11] what that looks
[29:13] like right so if we hop down here you
[29:15] can see we're enabling that beta flag to
[29:17] enable these longer outputs this is
[29:19] going to be in the description for you
[29:21] to hop in and play with so you can
[29:22] really understand the capabilities you
[29:24] can also just you know give this to a
[29:26] model give this to your a coding
[29:27] assistant and have generate whatever uh
[29:29] you're looking for so last thing I want
[29:31] to show off here is an
[29:36] agent you can be building your own
[29:38] agents to solve your domain specific
[29:40] problem right now and I'm kind of giving
[29:42] you the a quick start here with the
[29:44] single file agent showcasing how exactly
[29:47] you can do this so before the cloud code
[29:49] release we built a um bash and editor
[29:52] agent on top of claud's bash and editor
[29:54] tools and what we can do is this so
[29:56] we're going to copy this and and run
[29:58] this agent here so agent Loop 1 out of

### Minute 30

[30:01] 10 it has 10 compute uses I asked it to
[30:05] do this right the user asked me to
[30:07] create a file called hello.txt with the
[30:10] content hello world inside it I can use
[30:12] the create file tool to accomplish this
[30:14] task it sees the parameters of that tool
[30:17] right so you can see the tool call right
[30:18] here reasoning path and file text you
[30:21] can see the thinking budget right the
[30:23] thinking tokens um walking through what
[30:26] it needs to do to call the tool you can
[30:28] see there's the tool call and then
[30:30] there's the file created response right
[30:32] so this is what that response looks like
[30:34] you can see we have the response raw
[30:36] text and then we have the actual tool
[30:38] use that's all the agent needed to do
[30:40] here right so it's now calling the
[30:42] complete task tool letting me know that
[30:45] it is done just like Claude code here we
[30:48] have an agent that has a series of tools
[30:50] and if we just look at tools we can see
[30:54] here that we have you know a nice slew
[30:56] of tools here this agent has a view file
[30:59] tool it has a create file tool it has

### Minute 31

[31:02] string replace insert line so on and so
[31:05] forth here we have our own kind of you
[31:06] know mini version of cloud code and the
[31:09] idea here again is the is the same you
[31:12] can build powerful agents that can help
[31:14] you solve your domain specific problem
[31:17] by giving it the right tools that you
[31:19] would need to solve the problem and by
[31:22] fueling it with a powerful model like
[31:24] clog 3.7 sonin if we scroll to the top
[31:27] and we run this prompt here you can see
[31:29] duplicate whatever text is in hello.txt
[31:32] 10 times on new lines then create a
[31:35] markdown file Json file Ando file with
[31:38] the same content in the format for that
[31:41] file type and you can see I'm upping the
[31:44] compute budget and I'm also giving it 2K
[31:46] thinking tokens okay so I'll copy this
[31:49] clear and fire this off we do have that
[31:52] you know hello world text right here so
[31:53] we can open that up you can see that and
[31:55] now it's walking through the process
[31:56] right so it's calling view5 it's calling
[31:58] string replace it's calling create file

### Minute 32

[32:01] right it's creating the markdown file
[32:02] now it's creating that Json file you can
[32:04] see it's calling the create file tool
[32:06] over and over and now it's done okay so
[32:10] so you know this is really cool right we
[32:11] have our own bash file agent operating
[32:15] for us right completing arbitrary tasks
[32:18] because we've given it the right set of
[32:20] tools the right prompt and a powerful
[32:22] enough model clog 3.7 Sonet to
[32:25] accomplish the job and call the right
[32:27] tool
[32:28] this is why tool calling is so important
[32:30] this is why Claude 3.7 Sonet is an
[32:34] absolute crash out critical release okay
[32:38] it just gives you everything you need to
[32:42] not only you know create great prompts
[32:44] great prompt chains but also to take the
[32:47] next step in the composition of
[32:50] generative AI to the next step to agents
[32:53] okay when you think of agents this is
[32:57] what you should be really thinking about
[32:58] it's this this this composition of tools

### Minute 33

[33:03] and the right prompt and a good enough
[33:05] model to understand what you want done
[33:07] and you know this this is this is the
[33:09] agent right this is the agent okay so um
[33:13] I know I'm I'm repeating myself over and
[33:15] over it's just you really have to uh
[33:17] kind of nail The Point again and again
[33:19] to really understand how important this
[33:20] is and you can see at the end here our
[33:22] powerful model um you know our hybrid
[33:25] Reasoner base model is calling complete
[33:28] task because it knows that it's done
[33:30] right it it fully is aware that it's
[33:32] completed the prompt we asked it to
[33:34] complete okay and you can see it did it
[33:36] how much compute did that take so it
[33:37] took six compute Loops all right so
[33:40] that's great if we run uh GS or get
[33:43] status you can see here look at all
[33:46] these files it created right uh look at
[33:47] how much work it can do obviously I know
[33:50] simple examples but you can see the
[33:53] power of the tool calling capabilities
[33:55] of the agent with the model right so we
[33:57] can go open this up hello. Json look at
[33:59] that uh hello. markdown check that out

### Minute 34

[34:02] hello. yaml perfect yaml format and uh
[34:05] you know we have our other files here
[34:07] generated by our other agents generated
[34:08] by CLA code um I hope you can kind of
[34:11] see where things are going I hope you
[34:13] can see why this is so important this is
[34:15] just a such an important release lots of
[34:18] details here documentation all here for
[34:21] you uh check it out get yourself ramped
[34:23] up super quickly with this code base and
[34:26] understand the capabilities of this
[34:27] model this is a very very powerful model
[34:30] and um you know again let me know what
[34:31] you think about my ranking when we zoom
[34:34] out and take a look at the bigger
[34:35] picture you know it can be really easy
[34:37] to fixate on a single day or a single
[34:40] release but every once in a while
[34:42] there's a release that that really moves
[34:44] things forward and anthropic is really
[34:46] becoming that brand name of uh when
[34:49] anthropic moves when they think when
[34:51] they say something it's very very
[34:53] important to pay attention because it's
[34:55] it's what they're saying on the blog but
[34:57] it's exactly what they're saying and
[34:59] what they're showing that really matters

### Minute 35

[35:01] lot of really fantastic stuff here when
[35:03] we when we zoom out a little bit when we
[35:05] look at the larger Trend what does the
[35:07] release of claw 3.7 Sonet mean for us
[35:09] engineers and what does Claud code mean
[35:12] it means exactly as I've been saying as
[35:14] I've been predicting and and
[35:15] communicating capable agents are here
[35:18] they're getting rolled out and the
[35:20] people the engineers the builders that
[35:22] have them are taking that next step
[35:24] they're getting that next level of
[35:26] asymmetric Returns on their time by
[35:29] using agents when you combine it with a
[35:31] powerful Next Generation hybrid model
[35:34] right base plus reasoning rolled into
[35:36] one what we can do and the systems that
[35:39] can be built it's not clear what we can
[35:42] do with these tools now it's not clear
[35:44] what one single agent can do the only
[35:47] thing that's clear is that agents are
[35:50] here and you can now take your compute
[35:52] to a new level there's now a framework
[35:55] and a you know set of infrastructure you
[35:58] can use inside of your tools embedded

### Minute 36

[36:02] inside of the agent architecture to take
[36:05] your compute usage to the next level and
[36:07] as I've been saying on the channel there
[36:09] is a causal relationship between your
[36:12] compute usage and the amount of value
[36:15] you can create as an engineer and as a
[36:18] builder now here's the question that you
[36:20] can keep asking yourself to propel
[36:22] yourself forward do you have the right
[36:25] agent connected to the right tool
[36:28] to solve the problems you're facing if
[36:31] you made it to the end and you found my
[36:32] take valuable if you found the
[36:34] information valuable hit the like leave
[36:36] a comment subscribe stay focused and
[36:39] keep building