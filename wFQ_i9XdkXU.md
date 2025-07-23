# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=wFQ_i9XdkXU
- **Duration:** 23:49
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 4522
- **Transcript Generated:** 2025-03-30 23:48:31

## Transcript


### Minute 0

[00:00] what's up Engineers Indy Dev Dan here in
[00:02] this video I have six CLA code Pro tips
[00:06] that will help you achieve asymmetric
[00:08] Engineering in the generative AI age but
[00:12] the big theme behind the face value of
[00:15] this video is that tools like CLA code
[00:19] mCP and AI coding assistance and agents
[00:22] enable you to build systems that build
[00:26] systems for you this is the advantage
[00:29] you and I have as Engineers Vibe coding
[00:33] is the lowest hanging fruit system
[00:35] building enables you to reuse the value
[00:38] you create over and over and over so
[00:42] with this lens let me share my top six
[00:45] claw code tips for a gentic coding you
[00:48] can use to accelerate your Engineering
[00:51] in the Gen AI
[00:53] [Applause]
[00:56] age the CLA code team is shipping in the

### Minute 1

[01:00] shadows let's cover some of their new
[01:03] releases and a few techniques you can
[01:06] use to ship faster than ever let's start
[01:09] with one of my new favorite techniques
[01:11] context priming let's open up cursor and
[01:15] let's fire off CLA you can see I have
[01:18] five mCP servers we're going to cover a
[01:20] few of those in this video but first
[01:23] what is context priming how can it help
[01:26] you use cloud code in a more efficient
[01:28] effective way when you first startup CLA
[01:31] it's effectively an empty agent it
[01:33] doesn't see what you see it can't see
[01:36] your code base it doesn't know what you
[01:38] know it's basically a blank page it's a
[01:41] blank agent we need to let it know what
[01:44] you're working on I've started adding
[01:46] this inside of all of my readmes if we
[01:48] open up the readme and search for
[01:50] context priming you can see I have this
[01:52] simple prompt let's copy this and paste
[01:55] it in the Claude And Fire it off this is
[01:57] going to let Claude read the essential

### Minute 2

[02:00] files of the code base and then run get
[02:02] LS files to understand the code base you
[02:06] can see here the cloud code Engineers
[02:07] have implemented a couple new awesome
[02:09] features we're doing parallel reads with
[02:11] this cool sub agent call tool all these
[02:14] items are now getting added to Cloud
[02:16] codes context window at application
[02:19] startup you can see here it's giving us
[02:21] a nice summary but most importantly it
[02:25] now has this information inside of its
[02:28] context window if we type SL cost you
[02:30] can see there of course this is not a
[02:33] cheap tool right you're going to have to
[02:35] pay to play with Cloud code but you can
[02:37] see here you know we've done some
[02:39] operations already we have 40 cents
[02:41] worth of work that is now context AKA
[02:45] active memory for CLA code this lets you
[02:48] set up your AI coding assistant to win
[02:51] right away by downloading the Essential
[02:54] Elements of your code base I highly
[02:56] recommend you add something like this to
[02:58] your read me so that you can get started

### Minute 3

[03:00] quickly when you have to reset your
[03:02] Cloud code instances when you're nearing
[03:04] that 200k context token window limit as
[03:08] you'll see here in a moment when we run
[03:10] an AI coding prompt this small tweak
[03:13] speeds up your work quite a bit if we
[03:14] run get LS files you know we can now see
[03:18] a general structure of the code base I
[03:20] also like to run tree sometimes and pass
[03:23] that into claw and so as you can see
[03:25] here we are operating in the single file
[03:28] agents code base this is something we've
[03:29] worked on on the Channel all the work
[03:32] we're doing here is going to be
[03:33] available to you link in the description
[03:35] we're using UV to build out these
[03:38] powerful single file agents again we're
[03:40] going to look at these in just a moment
[03:43] here that's tip number one let's move on
[03:44] to tip number two context is King this
[03:48] is not new if you've been working in the
[03:51] AI coding space and if you've been
[03:53] working with language models you always
[03:55] want to be feeding claw code and your AI
[03:57] coding tools the context it needs to get

### Minute 4

[04:00] the job done if we type slash mCP here
[04:04] you can see I have five mCP servers in
[04:07] this current project the winning
[04:09] engineers in the Gen AI age will always
[04:12] be thinking from the perspective of
[04:14] their AI agents what can they see if
[04:17] someone were to prompt me with this
[04:19] context and this tool would I be able to
[04:22] accomplish the task having the right
[04:23] tools and the right mCP servers gives
[04:27] your Cloud code instances what it needs
[04:30] to succeed I think of mCP servers and
[04:32] tools in two classes we have collectors
[04:36] and we have executors first you collect
[04:40] contacts with your collectors and then
[04:43] you execute crud operations right you
[04:45] update files you update databases you
[04:48] operate on information you have
[04:50] collectors and you have executors right
[04:53] now I have two primary tools for
[04:56] collection I use the out of the box
[04:59] fetch tool right from the anthropic

### Minute 5

[05:02] servers and I also use fir craw mCP fir
[05:06] crawl is a simple tool I'm not sponsored
[05:08] by them or anything but they are my
[05:10] recommendation if you want to scrape and
[05:12] crawl single websites if you want to
[05:14] extract key information and also if you
[05:16] want to Traverse multiple Pages they
[05:19] also help you get around some of the SSR
[05:21] and server rendering issues and blocking
[05:24] that tools like fetch are limited by
[05:26] let's go ahead and take a look at the
[05:27] new file editor agent us using Sonet 3.7
[05:32] this is really cool this is a new simple
[05:34] file editing agent that can edit files
[05:36] using the brand new text editor for 3.7
[05:40] Sonet specifically this is a brand new
[05:42] text editor tool that enables you to
[05:44] build agents that can edit files
[05:47] precisely this is a massively important
[05:50] tool for agents this is a great example
[05:53] of an Executor tool and so we have this
[05:55] brand new tool inside of this agent we
[05:57] can do something like this I can just
[05:58] copy this we're using UV single file

### Minute 6

[06:00] scripts I'll open up a new terminal
[06:02] instance here and I'll just say
[06:05] summarize into a new readme summary. MD
[06:10] okay so this is a simple file editing
[06:14] agent it can read and write and let's go
[06:17] ahead and full screen this you can see
[06:19] we're calling the view tool here it read
[06:21] the read me it has those 20 lines and
[06:24] now it's written that file so with three
[06:26] agent loops and really just two it's r a
[06:29] file and it's created a file and then
[06:31] it's reported the results you can see
[06:33] the token output here so now we should
[06:35] be able to open up this new read me
[06:37] summary and you can see here we have
[06:39] that exactly here we have a nice concise
[06:41] summary of what's been done this is all
[06:43] built on top of anthropics brand new uh
[06:47] text editing tool built specifically for
[06:50] 3.7 Sonet anthropic realizes how
[06:53] important file editing is for building
[06:56] out you guessed it effective agents so
[06:59] there's a new additional feature that I

### Minute 7

[07:01] want to add to this agent and thropic
[07:03] has also shipped this brand new token
[07:05] efficient tool use beta flag so let's go
[07:09] ahead and pull this content and add this
[07:11] to our existing agent so instead of you
[07:13] know shipping this previous command
[07:16] let's go ahead and copy this out we want
[07:17] to be able to copy this efficiency okay
[07:21] and then this will run with the beta
[07:23] flag so this is a single page so it's
[07:25] really simple normally you could just
[07:26] copy this but I want to show off how
[07:28] important it is to have these tools
[07:30] embedded in clog code let's say we
[07:32] needed a couple pages of documentation
[07:34] right what I'll do here is I'll just
[07:35] copy this open up a new file paste that
[07:38] there and then copy this URL as well
[07:41] paste that there and then I'll write a
[07:43] prompt right in this file fetch combine
[07:47] and then do this right so I'm going to
[07:49] copy this and we have our fetch tool
[07:51] inside of CLA code mCP so now we can
[07:54] just paste and let this fire off so this
[07:56] is going to run fetch on both these and
[07:58] it's going to create a new mark on
[07:59] document we've talked about this in

### Minute 8

[08:01] previous videos but I want to highlight
[08:02] this one more time it's super super
[08:04] important to think of your tools as
[08:07] collectors and executors and so you can
[08:09] see here we have Cloud code's new
[08:12] parallel run subtask just ran both of
[08:15] those at the same time it's now looping
[08:17] through the actual content and it's
[08:19] going to create a new file so let's go
[08:21] ahead and look at our AI docs you can
[08:23] see we have several docs in here already
[08:25] and this is going to create a new
[08:27] markdown document for us with this
[08:29] content uh collected
[08:32] automatically fantastic we're going to
[08:34] go into YOLO mode we want CLA code
[08:36] operating in its full agentic form we'll
[08:39] hit yes and you can see this new
[08:41] document added here it has both the tool
[08:45] use docks and the efficient tool use
[08:48] combined so this is great right now that
[08:50] we have collected the context for this
[08:53] we can go ahead and write a follow-up AI
[08:55] coding prompt to update our existing
[08:58] single file a agent file editor with the

### Minute 9

[09:00] new Sonic 3.7 file editing tool and we
[09:04] can have it update to actually use Let
[09:06] Me Go a and collaps everything so you
[09:08] can see what we have here you can see
[09:09] all the file editing tools and we can go
[09:11] ahead and update this to uh use the new
[09:13] flag right so let's go ahead and do that
[09:15] I'm going to use my uh file reference
[09:18] hotkey for me it's command shift R I
[09:20] highly recommend you set this I'm going
[09:22] to paste that in and then I'll say
[09:24] update via a D- efficiency flag so we're
[09:29] going to kick that off you know to be
[09:31] super clear we don't need to reread this
[09:33] file because it is in fact already in
[09:36] the context window right Claud just
[09:38] wrote that so it has it in its context
[09:40] window you always want to be thinking
[09:41] from your agent's perspective you can
[09:43] see it's running the read tool here
[09:45] right to and create a flask API with
[09:47] three end points with the efficiency
[09:49] token flag there we're also passing in
[09:52] the thinking tokens and Max compute
[09:54] loops and there we go so there's the
[09:56] code coming in D- efficiency flag that's
[09:59] looks great let's go ahead and full

### Minute 10

[10:00] screen this so we can watch and looks
[10:02] like we got a little error here
[10:03] premature close just going to say
[10:04] continue the anthropic apis over the
[10:06] past couple weeks have been absolutely
[10:08] hammered and you know it's very likely
[10:10] to the mass adoption of Claude 3.7 Sonet
[10:14] on top of CLA code I've had many many
[10:17] many API rate limits um in the past so
[10:21] okay so this looks great so it looks
[10:22] like that change got in you can see um
[10:25] Cloud code summarizing everything that
[10:27] got changed that looks awesome you can
[10:29] see the that brand new message args beta
[10:32] flag so let me give you tip three and
[10:35] four together we're going to have claw
[10:37] code uh review and actually execute this
[10:40] code we've already covered that in
[10:41] previous videos right we're closing the
[10:43] loop we're letting our AI coding tools
[10:45] you know get the feedback it needs by
[10:47] actually just executing the command but
[10:49] there's a couple key commands right
[10:51] inside of claw that you should be aware
[10:53] of if we type slash relase you can see
[10:56] that there are release notes now that's
[10:58] tip three it might seem simple but the

### Minute 11

[11:01] cloud code Engineers are really shipping
[11:02] in the shadows here and you want to be
[11:04] keeping track of everything you're
[11:05] releasing if we hit enter here um I want
[11:07] to point out something really really
[11:09] cool that was just released you can say
[11:12] ask Claud to make a plan with thinking
[11:14] mode so obviously they're tapping into
[11:17] Cloud's Hybrid Base reasoning model
[11:20] capabilities if you say think think
[11:22] harder or Ultra think you will tap into
[11:26] these so that's tip number four let's go
[11:28] ahead and use that tip we just set up
[11:30] this brand new efficiency Flag by
[11:32] pulling in this context using an mCP
[11:35] server here it is here and I'm going to
[11:37] update this prompt just a little bit
[11:39] create a flask API with three endpoints
[11:41] inside of agent workspace yeah sure that
[11:44] looks good and so now we have this here
[11:47] it's going to run in efficiency mode and
[11:49] we're also going to have thinking tokens
[11:50] what I want to do here is create two
[11:52] versions right I want this to run uh
[11:55] without efficiency and with efficiency
[11:57] so that we can actually see the
[11:58] difference I'm not going to run this

### Minute 12

[12:00] right there's no reason for me to do
[12:01] this I'm going to hand this work off to
[12:03] Cloud code I'm going to hand this work
[12:05] off to my AI coding tools so I'm going
[12:07] to copy this and then we're going to
[12:09] also combine this with a think mode and
[12:12] so here's what I'll do I'll move over to
[12:14] our temporary file I'll paste this
[12:16] command in test out the token efficient
[12:19] exactly the following command without--
[12:22] efficiency and then we'll say with and
[12:25] there we go we're getting some great
[12:26] Auto completions from cursor Tab and
[12:28] then what I want to say say here is
[12:30] record think hard in the review process
[12:34] okay I'm going to paste this into Cloud
[12:35] code and then I'm going to fire this off
[12:38] okay so now it's going to actually run
[12:40] the agent itself it's going to you know
[12:42] keep track of the results and then it's
[12:45] going to run both in efficiency mode and
[12:48] without efficiency mode okay so you can
[12:51] see the output of our agent there we had
[12:53] an issue with our thinking tokens looks
[12:56] like we're passing in way too many
[12:57] thinking tokens let's go ahead and drop
[12:58] that down so so I'm going to drop this

### Minute 13

[13:00] down let's run this at the minimum for
[13:02] thingy tokens which is 1,024 so I'll
[13:04] copy and then paste this back in and run
[13:08] so we're going to kick off the First
[13:09] Command here running without the
[13:10] efficiency beta flag there we go so we
[13:13] can see you know there's the total token
[13:15] usage there and now we're going to run
[13:18] with the efficiency flag so you can see
[13:20] we use a total of you know 5,700 tokens
[13:23] we just go ahead and copy that out and
[13:25] we'll just throw this in a file here and
[13:28] then we'll go ahead and run with
[13:30] efficiency looks like we're getting a
[13:31] little error here we're going to go
[13:32] ahead and let Claude do its thing okay
[13:35] so you can see here Sonic picking up on
[13:38] an error that it made it actually um is
[13:40] using this older syntax where you import
[13:43] anthropic beta um this is good this is
[13:45] why we have the documentation there it
[13:46] can automatically make Corrections when
[13:48] it needs to so there it is it just made
[13:51] that change and you can see there yep
[13:54] nice so we're going to continue down the
[13:55] line all we want to do is check to see
[13:58] um if we have that use efficiency token

### Minute 14

[14:01] there there we go we can get rid of that
[14:03] code that looks great and then uh we're
[14:05] just going to remove I always like to be
[14:08] really careful when I look at the you
[14:10] know any type of RM um but that looks
[14:12] good we want to remove that one file
[14:14] that's fine and now we should be in a
[14:16] good place to rerun yeah let's go ahead
[14:18] and take a look at this okay so we want
[14:20] to run without efficiency flag that's
[14:22] fine it wants to redo the process there
[14:25] we go so let's go ahead and copy this
[14:27] value here
[14:30] right we have uh 6,000 tokens let's go
[14:32] ahead and update our token value so we
[14:35] have 6,000 tokens here then it wants to
[14:37] reset and basically run it again right
[14:39] with the efficiency flag so let's go
[14:41] ahead and hit yes and let's see how the
[14:43] efficiency token flag can save us some
[14:46] tokens for our
[14:51] agents so let's take a look um you can
[14:54] see here Cloud code is giving us a nice
[14:56] analysis looks like without token of
[14:59] efficiency we got 6K tokens and width we

### Minute 15

[15:01] got uh 5.7 so not a major you know
[15:06] saving um but not too bad either right
[15:08] looks like we got 5.7 uh% reduction and
[15:11] it looks like the big savings which is
[15:13] honestly where you want to have the
[15:15] savings is in the output tokens right
[15:17] because the output tokens are priced at
[15:18] I think $15 per million right so this is
[15:21] really good actually um we want to be
[15:22] saving on the output token so so this is
[15:24] an example of how several tips several
[15:26] techniques can come together right
[15:28] context is King
[15:29] you want to be paying attention to what
[15:31] your AI coding assistant can see what's
[15:34] actively inside its context window and
[15:36] then we also looked at the slash relase
[15:39] so SL relase notes tells you what are
[15:41] the cloud code Engineers cooking up
[15:43] right this is super super important we
[15:44] also then tapped into claud's thinking
[15:47] tokens right Claude 3.7 reasoning
[15:49] capabilities so this is super super
[15:50] powerful so we've now updated our agent
[15:52] if I search for you know Das Dash
[15:54] efficiency we can see we have that brand
[15:56] new efficiency flag that enables you can
[15:59] see here if use token efficiency we then

### Minute 16

[16:03] add this new cool beta flag right so
[16:06] that looks great it did save us you know
[16:08] some five 6% of tokens that will
[16:11] definitely add up over time all right so
[16:13] tip number five if I type slash and hit
[16:16] down a couple times you're going to see
[16:17] something pretty cool if I scroll to the
[16:19] bottom you'll see I have a couple of
[16:22] prompts right so a couple of my mCP
[16:24] servers have built-in prompts that I can
[16:27] just run okay so you can see fetch um
[16:30] has you know the the obvious one that
[16:32] you would think if I hit enter here it's
[16:33] going to set up Cloud code to uh have
[16:36] that Ur that I can pass in right so the
[16:38] key thing I want to show off here is not
[16:40] the fetch tool again it's the fact that
[16:42] you can use these slash commands to
[16:44] quickly activate one of the prompts if
[16:46] we look at the model context protocol
[16:48] servers if we go into fetch again we can
[16:51] see that there's this prompt right and
[16:53] this is really cool I think this is a
[16:55] pretty underused element of mCP servers
[16:58] you can create predefined prompts where

### Minute 17

[17:00] you have your mCP host pass in specific
[17:04] variables right so a simple example here
[17:06] is just fetch right so we type SL Fetch
[17:08] and this is a prompt that we now have
[17:10] access to right if we also look at
[17:12] there's another one here for SQL light
[17:14] let's hop into something a little bit
[17:16] newer you can see there's a prompt here
[17:18] that provides a uh demonstration of how
[17:21] to use SQL light with mCP right so if we
[17:24] clear this out and I type mCP you can
[17:26] see that we do have our you know light
[17:29] mCP and then I can type SL SQL and you
[17:32] can see here that exact Command right so
[17:36] this is a prompt that we can fill in
[17:38] with variables you can see the argument
[17:40] there is topic so if I hit uh enter here
[17:42] whatever sales now it's going to send
[17:45] back to the SQL light mCP server that we
[17:47] have installed and it's going to start
[17:49] setting up some data right so if we
[17:51] scroll up here it's going to kind of
[17:53] walk through this scenario walk through
[17:55] this setup the whole point here is that
[17:57] mCP servers allow you to tap and into
[17:59] these different prompts and so that can

### Minute 18

[18:01] be pretty powerful so one more tip I
[18:03] want to give you here is the fact that
[18:05] you can add Claude mCP servers very
[18:08] quickly with Json format so here's where
[18:11] I like to do this let's go ahead and
[18:12] close this CLA instance you can see we
[18:14] spent $3 there and let me go ahead and
[18:15] run you know Claude mCP list just as an
[18:18] example let me go ahead and get rid of
[18:21] fetch so we can say CLA mCP remove fetch
[18:26] okay so this will remove that and if we
[18:28] clear run mCP list we'll see that we no
[18:31] longer have the fetch command there
[18:33] right if we hop back into Claud I have
[18:35] an alias for Claud just clld saving a
[18:37] couple keystrokes uh do/ mCP you can see
[18:40] our connected mCP servers then if we hop
[18:42] back into the release notes you'll see
[18:44] that we can add mCP servers as Json
[18:48] string so this is a simple but very
[18:49] useful way to get up and running with
[18:52] mCP servers inside of cloud code so if I
[18:55] just copy this open up a new file paste
[18:57] this in and you know let's get fetch

### Minute 19

[19:00] reinstalled so the name for this is
[19:01] going to be fetch mCP and then all we
[19:04] need now is Json how do we set the Json
[19:07] for this if we open up fetch server
[19:09] again let's just go back here scroll
[19:11] down to the uvx we have this command
[19:14] here right so we can go ahead just copy
[19:16] this and then we can paste this and then
[19:18] we need to just clean this up a little
[19:19] bit so all we need is the content inside
[19:23] of the actual object okay so we don't
[19:25] need mCP servers this is for your claw
[19:27] desktop and we also don't need this kind
[19:30] of starting key value so we can get rid
[19:32] of that get rid of the trailing brace
[19:35] and then we can just use this right so
[19:36] this is valid Json we can then take this
[19:39] and paste it here what I like to do here
[19:41] is run something like this we your
[19:43] dollar sign PB paste and then this will
[19:46] take whatever is on our clipboard and
[19:48] just use that right so we can close
[19:50] Cloud code here and then paste this
[19:52] value and then copy whatever Json we
[19:55] want to use and then hit enter here and
[19:57] this is going to add that brand new
[19:59] fetch mCP server just as we defined okay

### Minute 20

[20:03] so now if I type you know CLA mCP
[20:05] list you're going to see that right here
[20:08] right Fetch dmcp and then we can run
[20:11] Claud and you can see here we found 5
[20:14] mCP servers if I go ahead and type SL
[20:17] mCP you're going to see that new fetch
[20:19] mCP server up and running you can
[20:21] quickly add mCP servers into CLA code
[20:24] using Json format and they also added
[20:26] this you know Claud mCP ad um
[20:29] step-by-step wizard uh that you can also
[20:31] use so if we clear and run this you can
[20:33] see that they have a you know setup
[20:35] command there that you can you know use
[20:37] to step by-step walk through adding a
[20:39] new mCP server so obviously I like the
[20:42] Json approach it's a little bit faster
[20:44] if you know what you're doing but you
[20:45] know equally as good you can just come
[20:47] in here and you know name them whatever
[20:49] you want you can set up the project
[20:50] scope these are all you know command
[20:52] line flags and then you know path to
[20:54] server so on and so forth right so this
[20:56] is a nice way to walk through the
[20:57] process I think the the CLA code team is
[20:59] really executing here they're creating a

### Minute 21

[21:01] lot of value inside of this tool you
[21:03] know again it's super important to note
[21:05] as mentioned in our previous video Cloud
[21:07] code is saying massive Mass adoption
[21:10] this tool is really Paving the way for
[21:12] the next phase of engineering right we
[21:15] started with you know doing everything
[21:17] by hand typing code manually we moved to
[21:20] co-pilots we then started iteratively
[21:22] writing prompts and you know using AI
[21:25] coding tools the next big phase is
[21:28] agentic coding and at the Forefront
[21:31] really you know the poster child for
[21:33] this is claw code specifically with 3.7
[21:36] son it it's a breakthrough tool that's
[21:39] allowing new capabilities for agented
[21:40] coding when you combine it with mCP you
[21:43] can now equip your AI coding assistant
[21:45] your a gent to coding Tool uh with all
[21:48] of the capabilities it needs to run not
[21:51] just programming tasks but to run tools
[21:54] that allow you to collect and execute
[21:57] across various domains S as Engineers

### Minute 22

[22:00] it's Ultra important to take advantage
[22:02] of these tools and focus on Building
[22:04] Systems that build systems for us where
[22:07] we're going on the channel and a place I
[22:09] highly recommend you spend some time
[22:10] investing is look at what agents you can
[22:14] build to multiply your productivity to
[22:17] help you scale up what you can do agents
[22:20] allow you to scale your impact even
[22:22] further remember that cloud code itself
[22:26] is just an agent right it's an agent
[22:28] agent for engineering it's an agent for
[22:30] the terminal it's the agent for
[22:32] engineering a big focus on the channel
[22:35] is going to be building out agents for
[22:36] various use cases and understanding
[22:39] agent design and agent architecture at a
[22:43] fundamental level if that interests you
[22:45] join the journey make sure you're
[22:46] subscribed this is how we scale our
[22:48] impact and consume more compute to work
[22:52] on our behalf we're barely scratching
[22:54] the surface of what we can do with
[22:57] agents this is are unique Advantage do

### Minute 23

[23:00] not underestimate this it's time to
[23:03] start Gathering your Suite of tools of
[23:05] both collection and execution tools so
[23:08] that you can continue to scale up what
[23:10] you can do with Incredible AI coding
[23:12] tools like CLA code these are just five
[23:16] of you know several mCP servers that I'm
[23:18] looking at and playing with comment down
[23:20] below let me know what mCP servers are
[23:22] your favorites a lot of this will depend
[23:24] on the tools and the tooling that you
[23:26] use to engineer you might be using
[23:28] postgress you might be in Docker a lot
[23:30] so you'll be using the docker tools
[23:32] comment down below let me know what
[23:33] you're using let me know what your
[23:34] favorite tools are if you made it this
[23:36] far into the video Drop the like
[23:38] subscribe join the journey the key here
[23:40] is to focus on Building Systems that
[23:42] help you build systems stay focused and
[23:46] keep building