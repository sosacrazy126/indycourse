# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=vN0t-kcPOXo
- **Duration:** 17:04
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 2817
- **Transcript Generated:** 2025-03-30 23:49:11

## Transcript


### Minute 0

[00:05] a go ahead and open up open ai's
[00:07] realtime API blog
[00:12] announcement I've opened the browser to
[00:14] open ai's realtime API blog announcement
[00:17] for you thanks a if you need any more
[00:19] help just let me know it's time to start
[00:22] rethinking how we interact with our
[00:24] computers now that open AI has released
[00:27] the realtime API you and I can build
[00:30] seamless Next Generation AI experiences
[00:34] as always the greatest technology and
[00:36] opportunities come to you and I first
[00:39] the engineer are you ready for speech to
[00:41] speech AI assistance powered by Advanced
[00:44] reasoning models like 01 this is what
[00:48] we've been waiting for let's play with
[00:50] [Music]
[00:52] it so no one is really using these tools
[00:56] to their full capabilities yet myself
[00:58] included let's show off early versions

### Minute 1

[01:00] of how we can truly utilize personal AI
[01:07] assistance hey
[01:09] a hey Dan how can I assist you
[01:12] today yeah can you go ahead and open up
[01:15] chat GPT open up Claude open up Gemini
[01:18] then can you give me the current time
[01:20] then can you generate a random number
[01:22] for me and then after that go ahead and
[01:24] open up Simon W's blog and then let's go
[01:27] ahead and open up Hacker News as well
[01:43] I've opened chat GPT Claude and Gemini
[01:47] for you the current time today is 1210
[01:50] a.m. on October 5th
[01:52] 2024 I also generated a random number
[01:55] for you 23 Simon W's blog and Hacker
[01:58] News have been opened as well uh okay so

### Minute 2

[02:02] this is getting crazy right open AI
[02:04] employees are going to salivate when
[02:06] they watch this video it's a beautiful
[02:08] orchestration of all of their great work
[02:11] so we have the real-time API calling a
[02:15] chain of tools with 100% accuracy which
[02:19] contain individualized AI agents and
[02:22] let's simplify AI agents that's any
[02:24] combination of code and additional
[02:26] prompts with a single purpose built to
[02:29] solve a single problem these AI agents
[02:31] can then run their own structured output
[02:34] calls that feed back into our top level
[02:37] digital assistant I'm not going to lie I
[02:39] am high as a kite envisioning the
[02:41] capabilities and the future we can
[02:43] unlock with this tooling the distance
[02:46] between your thoughts and your actions
[02:48] on your device are fading fast with this
[02:51] combination of Technology let's push
[02:53] this further with some more interesting
[02:55] agentic functionality with prompt chains
[02:57] and 01 reasoning models powering a file

### Minute 3

[03:00] manipulation
[03:01] [Music]
[03:04] agent so this is all running locally via
[03:08] a async python
[03:13] application hey Ada can you go ahead and
[03:15] generate a CSV file for us go ahead and
[03:18] call it uh user analytics and just add
[03:21] 10 Mack rows
[03:30] I've created the CSV file user
[03:32] analytics. CSV with 10 rows of mock data
[03:36] great job this looks awesome so can you
[03:37] go ahead and delete Row 5 6 and 7even
[03:41] and then can you add a new column let's
[03:43] call it uh membership and set it all to
[03:53] premium I've updated the file user
[03:56] analytics. CSV rows 5 six and 7 have
[03:59] been deleted and a new column called

### Minute 4

[04:02] membership has been added with all
[04:04] values set to premium is there anything
[04:06] else I can assist you with let's make
[04:08] another change here can you go ahead and
[04:09] add 70 additional rows to the user
[04:12] analytics file go ahead and use a
[04:14] reasoning model for
[04:25] this the file user analytics. CSV has
[04:29] been up updated with 70 additional rows
[04:31] of mock data using the reasoning model
[04:34] okay so pretty incredible stuff there
[04:36] right just by talking to my computer I
[04:38] am generating and modifying this user
[04:41] analytics. CSV file this is getting kind
[04:44] of out of hand right this is incredible
[04:46] this is the dream of multi-agent
[04:48] applications we've been building toward
[04:50] on the channel for over a year now since
[04:52] the very first one prompt is not enough
[04:54] video I want to share a couple
[04:55] interesting insights and useful
[04:57] engineering patterns around building
[04:59] personal AI assistant but first we have

### Minute 5

[05:01] to highlight what's happening here so in
[05:03] a very sloppy 1,000 lines of code we
[05:07] have a real- time speech to speech
[05:10] assistant that can connect to and
[05:12] accurately call other agents that's huge
[05:15] these other agents are called through
[05:17] tools and these agents can then
[05:20] themselves run their own prompts they
[05:22] can use Advanced reasoning models like
[05:24] 01 and ultimately there's really no
[05:26] limit on what you can do inside of a
[05:28] function call right this guy's the limit
[05:30] now the real trick is do you know what
[05:33] you want to build and do you know what
[05:35] you need to do to wire together your
[05:37] architecture with your personal AI
[05:39] assistant at the top at the center which
[05:42] then commands your army of AI agents
[05:45] that's what's next for us here on the
[05:47] channel we're taking Ada to the limits
[05:49] and then we're going to break those
[05:50] limits that's been a big milestone and a
[05:52] big Keystone for us living software that
[05:55] works for us while we sleep let's go if
[05:58] you're starting to build out your own
[05:59] personal AI assistant I'm super curious

### Minute 6

[06:01] what are some patterns you're setting up
[06:03] and what are the first use cases you
[06:05] want your personal AI assistant to solve
[06:08] on your behalf so we have a couple tools
[06:10] that really lead a lot of our
[06:12] functionality here right you saw the get
[06:14] time method you saw the random number
[06:16] you saw open browser and then we have
[06:19] some kind of essential file manipulation
[06:22] calls right there's create file update
[06:24] file and delete file let's go ahead and
[06:26] showcase these a little bit more and
[06:27] really show off what these three simple
[06:30] but essential methods can do with a
[06:33] personal AI
[06:36] assistant hey aah can you go ahead and
[06:38] delete the learning rust file are you
[06:40] sure you want to delete the learning
[06:42] rest MD file if so please confirm with
[06:46] Force delete yeah go ahead and force
[06:47] delete that file we won't be needing
[06:49] that fantastic can you go ahead and
[06:51] create a new file and just explain the
[06:53] basics of list comprehension and list
[06:56] manipulation and you know what actually
[06:58] go ahead and just talk about all the

### Minute 7

[07:01] different types of Loops that you can
[07:02] use in Python instead of a markdown file
[07:05] just go ahead and create a fullon python
[07:07] file with examples and make sure you
[07:09] comment and document it all really
[07:16] well I've created the file python loops
[07:19] and comprehensions dopy with
[07:21] explanations and examples on list
[07:23] comprehensions and various types of
[07:25] Loops in Python if you need further
[07:27] assistance or more information just just
[07:29] let me know fantastic thank you aah can
[07:31] you go ahead and update our python loops
[07:33] and comprehension file and uh just go
[07:35] ahead and move everything into a
[07:37] function and then uh place a main block
[07:40] at the bottom where we can comment in
[07:42] and out each example and kind of work
[07:44] through them at our
[07:51] Leisure the python loops and
[07:53] comprehensions Pi file has been updated
[07:56] everything is now organized into
[07:58] functions with a main block at the

### Minute 8

[08:00] bottom for easy testing and exploration
[08:03] you can now comment in and out each
[08:05] example as needed wonderful thanks so
[08:07] much AA um there's a triple quote at the
[08:09] bottom of the file go ahead and remove
[08:10] that the triple quote at the bottom of
[08:13] the Python loops and comprehensions dopy
[08:15] file has been removed if there's
[08:17] anything else you need feel free to let
[08:19] me know nice job AA can you go ahead and
[08:21] create two more versions of our python
[08:24] loops and comprehensions file basically
[08:26] we want another version in typescript
[08:28] and let's go ahead and create another
[08:29] version of the same thing in C so create
[08:33] both those files with the you know
[08:34] appropriate file names and file
[08:36] extensions and just explain all the
[08:38] variance of Loops in both typescript and
[08:50] C the files loops and comprehensions
[08:53] dots for typescript and loops and
[08:56] comprehensions CS for Sharp have been
[08:58] created they both include explanations

### Minute 9

[09:01] and code examples of various loops and
[09:04] comprehension methods in their
[09:05] respective languages great job thank you
[09:07] can you go ahead and delete all of our
[09:09] Loop files go ahead and force delete
[09:15] them both loops and comprehensions TTS
[09:19] and loops and comprehensions docs files
[09:22] have been successfully deleted nice job
[09:24] beta go ahead and get rid of the Python
[09:26] loops and comprehensions as well the
[09:28] python loops and comprehensions file has
[09:31] been deleted if there's anything else
[09:32] you need help with so these are really
[09:34] interesting tools I wanted to share with
[09:36] you just to give you an idea of what's
[09:38] coming next in the age of gender of AI
[09:40] now that we have these real-time speech
[09:42] to speech capabilities it's all about
[09:45] utilizing their capabilities these are
[09:47] some really important functions to keep
[09:49] your eyes on and to build out into your
[09:50] personal AI assistant because a lot of
[09:52] engineering is all about file
[09:53] manipulation file updates file creates
[09:56] file deletes and manipulation so just to
[09:59] give this idea to you a couple

### Minute 10

[10:01] additional things I want to show you
[10:02] here in the beginning I asked Ada to
[10:04] open up a bunch of browser URLs every
[10:07] assistant is going to need some
[10:09] personalization some specific
[10:11] information that's specific to you and
[10:14] the things that you're interested in so
[10:15] you can see here we have the browser
[10:16] URLs that's what got loaded into the
[10:19] open browser AI agent and then of course
[10:22] we have some auxiliary information down
[10:23] here browser asistant name and human
[10:26] name you can see this personalization
[10:28] getting expanded very quickly and an
[10:30] interesting agentic pattern we're going
[10:32] to be digging into on the channel is
[10:34] having an agent automatically update our
[10:37] personalization file personalization
[10:39] settings is going to be really important
[10:41] and I also wanted to share this runtime
[10:43] table so I think it's super important to
[10:45] have proof of the speed of these agents
[10:48] and I got to say I'm really really
[10:49] impressed here the real-time speech to
[10:51] speech API from when I finished speaking
[10:54] to getting a response is on average
[10:57] about a second when we're running tools
[10:58] obviously this time gets blown up quite

### Minute 11

[11:01] a bit but I think that's to be expected
[11:03] there are other ideas like moving tool
[11:05] calls to an async thread to let those
[11:07] run in the background definitely an
[11:09] improvement that can be made here but
[11:10] you can see here real-time API responses
[11:12] are really really really great um sub 1
[11:15] second for the entire flow this is
[11:17] really incredible it seems like under
[11:19] the hood what their model is doing is
[11:22] starting to generate the response as
[11:24] we're speaking since tokens run in
[11:27] sequence they can automatically start
[11:28] generating the response and then stream
[11:31] that back to us in real time right so
[11:33] this is really really cool really
[11:34] incredible stuff this technology is
[11:36] truly groundbreaking and then you can
[11:38] see some of my other calls here right so
[11:40] delete file took under a second create
[11:42] took about a second update file took 3
[11:44] seconds right so updates more involved
[11:47] because we're not just setting up the
[11:48] initial right we're having the llm
[11:50] updated and of course you can see here
[11:52] when I ran the reasing model that took
[11:54] about 18 seconds right so just wanted to
[11:56] give you some data here give you some
[11:57] insights into the actual run time of the

### Minute 12

[12:00] real-time API I am in love with these
[12:03] numbers you know in our previous
[12:05] personal AI assistant videos it was
[12:07] taking about in the best case 5 Seconds
[12:10] to run the speech to text llm and text
[12:13] to speech workflow that you need to
[12:16] complete an AI assistant open AI is
[12:18] doing all those steps in less than a
[12:20] second here for simple conversational
[12:22] workflows right so this is truly
[12:24] incredible technology of course it comes
[12:26] with several tradeoffs and anyone
[12:29] telling you different is wrong or
[12:30] they're trying to sell you something the
[12:32] real-time API alone is incredibly
[12:35] expensive you know talk about huge costs
[12:36] I'm not surprised but the cost must come
[12:39] down for this to be viable at scale if
[12:41] we check out the pricing here you can
[12:42] see so this is 6 minutes of audio in and
[12:45] 24 cents out um this is heavy pricing
[12:48] when I was testing this out uh the costs
[12:50] for me were around I think it was $10 to
[12:52] $15 for I don't know it was like an hour
[12:55] testing back and forth right so the
[12:57] costs are there that's a trade-off and
[12:59] of course I think the second largest

### Minute 13

[13:00] trade-off here is vendor lock in if you
[13:03] work through this code base you'll see
[13:04] that everything I've built here is on
[13:06] the open AI stack all the llms the
[13:09] reasoning model the speech to speech the
[13:12] real-time API open AI wants to be the
[13:15] king of agentic they want to be the king
[13:18] of AI agents llms and the entire
[13:21] ecosystem right even the B to C side of
[13:23] it these are risks that we kind of just
[13:26] have to take in order to get and utilize
[13:29] the top generation the state-of-the-art
[13:32] application models and apis right the
[13:35] real-time API there's nothing as close
[13:38] to this they've embedded the speech to
[13:40] text the llm and the text to speech all
[13:44] in one workflow we're getting subc
[13:46] responses and we can call tools that's
[13:49] all we've needed to push through to the
[13:51] next generation of agentic Technology
[13:55] right now these are risks we have to
[13:56] take to stay on the edge of what's
[13:58] possible so we can learn and master the

### Minute 14

[14:00] next generation of software before it
[14:02] hits the masses so I hope it's super
[14:04] clear What's Happening Here the distance
[14:07] between you and your device is slowly
[14:10] fading away can you feel it I can feel
[14:12] it we can think then just speak and it
[14:15] knows what we're looking for it's scary
[14:17] it's exciting it's real it's here this
[14:20] beautiful um hacked together prototype
[14:23] code base uh contains about a th lines
[14:25] it's it's here it's ready for you if
[14:26] you're interested um I hadn't seen a ton
[14:29] of python based on device implementation
[14:31] so I wanted to throw one together to
[14:33] test and validate this agent and to set
[14:36] up a new version of ADA that I can grow
[14:38] and expand on it's a simple proof of
[14:40] concept of what's coming I think for us
[14:43] Engineers this is a Next Level tool that
[14:46] is really important to spend time on and
[14:48] pay attention to and build into your
[14:50] development workflow there's really no
[14:53] limit to what we can do here it's all
[14:55] about what we can imagine and it's about
[14:58] staying out of open ai's way don't go

### Minute 15

[15:01] out and build a product don't go out and
[15:03] try to sell something that is going to
[15:05] get bulldozed by the next open AI
[15:07] release steer clear just imagine the
[15:10] tech is going to improve the models will
[15:12] improve and then think about what you
[15:14] can build alongside these next
[15:17] Generation generative AI tools and API
[15:20] tooling I think a huge theme we're
[15:22] seeing here very clearly is that voice
[15:25] is a key piece of the next generation of
[15:29] user experiences a question we're going
[15:31] to be looking to answer on the channel
[15:33] is how can we utilize personal AI
[15:35] assistance in combination with
[15:37] Incredible prompts and reasoning models
[15:40] to get more work done in parallel faster
[15:44] than ever if that interest you drop a
[15:46] like drop a sub and join the journey
[15:48] really excitingly we are about to hit
[15:50] and cross the 20K Subs Mark it's been an
[15:54] incredible journey so far we've
[15:56] transformed so many times and we've
[15:58] learned leared so much over the course

### Minute 16

[16:00] of the Channel all the way from one
[16:02] prompt is not enough to learning AER to
[16:05] exploring cursor to understanding prompt
[16:07] chains agent orchestration building out
[16:10] multi-agent systems it's all coming
[16:13] together with the release of the
[16:14] real-time API and it's building up to
[16:16] something incredible we're getting
[16:18] closer to building living software that
[16:20] works for us while we sleep with every
[16:23] single video I want to say a huge thanks
[16:25] to every Builder and engineer that's a
[16:27] part of this journey I I appreciate all
[16:29] the positive comments and all the
[16:31] feedback and I just want to remind you
[16:33] you are in control of this technology
[16:35] you can take this and together we can
[16:38] imagine a future with these tools I want
[16:41] this channel to be a place where you can
[16:43] come to understand the capabilities of
[16:46] this technology so that you can build a
[16:48] better future for yourself for your
[16:51] family for your work and for your
[16:53] passions we're not going to stop until
[16:55] we have living software working for us
[16:58] while we sleep keep building stay

### Minute 17

[17:00] focused I'll see you in the next one