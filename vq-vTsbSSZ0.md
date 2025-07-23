# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=vq-vTsbSSZ0
- **Duration:** 35:12
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 7243
- **Transcript Generated:** 2025-03-30 23:48:36

## Transcript


### Minute 0

[00:00] what's up Engineers Indy Dev Dan here in
[00:02] this video I want to show you the one
[00:05] most important AI coding pattern you can
[00:07] use to maximize the impact you can have
[00:11] with powerful reasoning models and Next
[00:13] Generation language models like GPT 4.5
[00:17] and whatever new model anthropic is
[00:19] cooking up this is a threepiece combo
[00:21] video we're going to be using everyone's
[00:23] favorite AI code editor cursor this is
[00:26] the name brand in AI coding right now
[00:29] we're also going to be using using a new
[00:30] tool built on top of Aer AER is the best
[00:33] open- source AI coding tool we're going
[00:35] to be using AER inside of a brand new
[00:38] lightweight exclusive AI coding tool I'm
[00:40] excited to share more about this in the
[00:43] video this is an experimental tool for
[00:45] surgical AI code changes and finally you
[00:49] saw it in the title we'll use the tool
[00:51] many Engineers fear the editor of the
[00:54] future the engineering career killer
[00:56] Devon I've been waiting to pull the
[00:58] trigger on this one and after after the

### Minute 1

[01:00] 03 Mini model was released I knew that
[01:02] Devon would be in a good place to try
[01:04] and I think I was right about that
[01:06] you'll see what you can do with Devon in
[01:08] this video without spending the massive
[01:10] $500 a month that it takes to get this
[01:12] thing online so it's been a while since
[01:15] we've done some handson AI coding on the
[01:17] channel I have to warn you guys things
[01:19] have changed a lot this video is going
[01:20] to be both weird and awesome what is the
[01:23] one pattern you can use with any AI
[01:25] coding tool and any powerful model to
[01:29] scale your your air coding to new
[01:31] heights let's get right into
[01:35] it so what is the pattern what is the
[01:37] technique it's planning planning is the
[01:40] single most powerful pattern you can use
[01:42] right now to scale your engineering to
[01:45] new heights let me show you how and why
[01:48] instead of cranking out AI coding
[01:50] prompts we're just going to open up
[01:51] cursor and we're just going to start a
[01:54] brand new plain text file this is the
[01:57] beginning of everything we want to build
[01:59] no agent mode no tab tab tab just a

### Minute 2

[02:02] blank file so what are we building what
[02:04] are we planning what are we thinking
[02:06] about last week we put together single
[02:07] file agents you can see I'm in that code
[02:09] base right now every one of these files
[02:11] hold some unique capability in an
[02:13] agentic Loop and we can kick one of
[02:15] those off right now with this command
[02:17] I'm going to paste the S and this is
[02:18] going to run a query against an SQL
[02:21] light database in an agent Loop so we're
[02:24] looking for all active users between the
[02:26] score created in 2024 this agent Loop
[02:29] had 10 total compute Loops it only took
[02:31] four to accomplish the task and you can
[02:33] see here here's our exact result coming
[02:35] out of our SQL light database and it
[02:37] automatically understood and interpreted
[02:39] our query properly it fixed all the
[02:41] column names you can see is active
[02:43] equals 1 score between and uh year 2024
[02:47] right and it also corrected the table
[02:49] for it so this is the power of a compact
[02:51] single file agent I'll go ahead and Link
[02:53] this video in the description if you
[02:55] want to learn more about single file
[02:56] agents in this video we have three tools
[02:58] so let's go ahead and build build three

### Minute 3

[03:00] new useful agents first we're going to
[03:02] build a CSV agent this is going to run
[03:05] data analytics queries on top of large
[03:08] th000 10,000 line plus CSV files we're
[03:11] going to hand off this work to Devon and
[03:13] then we're going to build a precise web
[03:15] scraper that pulls content and then
[03:17] reformats it into the right form and
[03:20] then lastly we're going to rebuild
[03:21] anthropics bash and file editing tools
[03:24] into an all-in-one agent we're going to
[03:26] have pack patterns build this up for us
[03:28] so you have a blank file open and your
[03:30] boss just walked by and sees you staring
[03:33] at a blank screen he starts to wonder
[03:36] why he hired you so you're about to show
[03:38] them why I have code Snippets for all of
[03:41] my you know specs and all my plans but
[03:43] let's just go ahead and write this from
[03:44] scratch okay polar CSV agent High
[03:48] Lev overview tasks AKA prompts I don't
[03:52] want to waste your time so I'm going to
[03:54] skip through some of this typing and
[03:55] we're going to walk through the key
[03:56] ideas as we go create a polar

### Minute 4

[04:00] open Ai and state API UV run SFA po V2
[04:07] instead of this we want prompt so this
[04:08] is going to be our user prompt so this
[04:11] is going to be our feedback loop and we
[04:12] can go ahead and just be specific get
[04:14] the relative file path and paste that in
[04:16] and let's say something like what's the
[04:18] average age of users and then at the end
[04:21] here we're going to have- C compute
[04:23] count so how many compute Loops do we
[04:25] want our agent to have yeah CSV pathi
[04:27] since we're passing this work off to
[04:30] Devon Devon can also read links so what
[04:32] I'll do here is just paste in some links
[04:35] that could be useful so I'll say docs
[04:37] and we'll past in both the polers and
[04:39] the UV inline scripts so for our single
[04:42] file agents we are using the inline UV
[04:46] dependencies this allows our python
[04:47] script to run with dependencies as a
[04:49] single file we're going to use that same
[04:51] pattern here implementation details all
[04:54] right so we have a bunch of
[04:55] implementation details here and what I
[04:57] really like to do with the details is
[04:58] just kind of of Consciousness walk

### Minute 5

[05:01] through everything that I want the agent
[05:03] to do so just to highlight a couple
[05:04] things here we want to reuse our current
[05:07] existing agent structure we want to
[05:08] specify some of the libraries we're
[05:10] using right so open AI M Rich I'm saying
[05:12] use the O3 model you can see all the
[05:14] tools that we want to agent to have
[05:16] access to list columns sample CSV so on
[05:18] and so forth so the task here AKA
[05:20] prompts is a series of steps that you
[05:23] would take or that you would hand off to
[05:25] a you know junior or mid-level engineer
[05:27] to actually get the job done and we're
[05:28] going to see how important this is you
[05:30] know for tools like Devon for any tool
[05:33] like cursor having these predefined
[05:35] steps inside of the workflow is going to
[05:37] be really really important so I'll go
[05:38] ahead right now and I'll walk through
[05:39] all the individual tasks that I want to
[05:41] actually build out this new single file
[05:43] agent fantastic so what we have here is
[05:46] effectively a list of prompts and you
[05:49] know you may be thinking if you've been
[05:51] with the channel for a while you might
[05:52] be thinking hey we've talked about these
[05:54] before these spec prompts these plans
[05:56] and if you've taken principal AI coding
[05:58] you know that this is a kind of really
[05:59] really key pivotal idea inside of the

### Minute 6

[06:01] course yes and yes this is where all
[06:04] engineering will go over time we need to
[06:06] be focusing on packaging our work so
[06:08] that we can do the following instead of
[06:11] actually writing any code instead of you
[06:12] know going into detail I'm just thinking
[06:14] through everything here top to bottom
[06:16] you know we have almost 1,000 tokens
[06:17] here 500 Words detailed in this really
[06:20] clean concise plan and I'm going to do
[06:22] something really amazing now with this
[06:23] I'm just going to copy all this I'm
[06:27] going to open up Devon so how does this
[06:28] work with Devon basically you just write
[06:30] a prompt and Devon has access to your
[06:33] code base and then it operates on your
[06:35] code base on your behalf and then at the
[06:36] end it will create a PR this is going to
[06:38] be really fun so I'm going to paste this
[06:40] write a couple lines here at the top
[06:42] workflow Branch from and I'm just going
[06:45] to pull my current Branch name I think
[06:46] I'm operating on experimentals
[06:50] Implement verify PR back to
[06:53] experimentals branch
[06:59] kick this off so now we're kicking off a

### Minute 7

[07:02] Devon AI assistant to do this work for
[07:04] us okay here's kind of what the user
[07:06] interface looks like right you can see
[07:08] all the engineering tools here on the
[07:11] right and on the left you have a chat
[07:13] conversation with Devon and basically
[07:16] it's just going to say you know I
[07:17] understand you want me to do blah blah
[07:18] blah and then it's going to walk through
[07:20] its process live and go kind of Step by
[07:23] Step through everything I'm very
[07:25] impressed with this tool as you'll see
[07:27] it really emphasizes the importance of
[07:29] of creating powerful plans and you know
[07:32] really detailing the work that you want
[07:34] done we talk about maxing out your
[07:36] compute and leveraging compute a lot on
[07:39] the channel this tool is a you know very
[07:41] powerful manifestation of that for the
[07:43] AI coding workflow for engineer you can
[07:45] see here it's created an entire plan
[07:48] that it's going to work through right it
[07:49] has its own agentic planning Loop it has
[07:52] access to the terminal you can see it
[07:53] has my box here with another code base
[07:56] and it is starting to get some work done
[07:57] here so this is really cool we're going
[07:59] to to let our AI coding tool do its job

### Minute 8

[08:02] and we're going to continue working on
[08:04] our own okay so we're going to close
[08:06] this and let's go ahead and continue
[08:08] with our second agent and this is going
[08:10] to be work that we're going to hand off
[08:12] to cursor agent mode a really cool part
[08:15] about these new long running plan based
[08:17] AI coding Tool jobs you get into this
[08:20] kind of three-step process where you
[08:21] have a plan step you have a wait step
[08:25] and then you have a review step and so
[08:27] you can do something really cool during
[08:28] this flow I've got into a nice kind of
[08:30] flow here where I am planning awaiting
[08:34] and then reviewing one kind of stream of
[08:37] work and then during the await step
[08:39] right during the weight step I kick off
[08:41] another plan weight review and another
[08:43] AI coding tool and then you can kind of
[08:45] you know basically just continue doing
[08:47] that and eventually you come back to
[08:48] some review step looks like you know uh
[08:50] Devon is not ready for review yet it's
[08:52] still getting work done we're going to
[08:53] go ahead and give it its space so let's
[08:55] go ahead and open up the terminal here
[08:57] and instead of using a a kind of blank

### Minute 9

[09:00] file let's go ahead and use pack
[09:02] patterns so we're just going to use pack
[09:04] patterns to create the template so I'm
[09:06] just going to type pack spec new and
[09:08] then inside the specs directory precise
[09:11] scraper agent and this is going to be
[09:14] the markdown so this is going to create
[09:16] a brand new plan for us here we can see
[09:18] here we have this precise scrape agent
[09:21] and so this is a markdown template that
[09:23] we can work with so this is one of
[09:24] several patterns inside of this tool
[09:26] that we'll talk about more in a moment
[09:28] the great part about this tool is that
[09:29] you don't have to actually run the
[09:31] generated document the generated plan
[09:33] with the tool you can use it with any AI
[09:35] coding tool you want so you can see here
[09:36] we have this brand new plan and let's go
[09:38] ahead and I'll work through this again
[09:41] I'm going to skip through some of this
[09:42] so you don't have to sit through the
[09:43] entire plan but it is important to kind
[09:45] of highlight some of the key elements of
[09:47] this right and so I'm going to just
[09:49] delete mid-level objectives you don't
[09:50] really need that here and then I'm going
[09:52] to fill out some of the implementation
[09:53] notes so scraper agent.
[09:57] scrapes based on users it's going to

### Minute 10

[10:00] look something like that and so you can
[10:01] see here we're starting to fill out the
[10:02] details I like this idea of starting
[10:04] kind of at the end right starting at the
[10:06] end vision of what you want to see what
[10:08] you would run UV run scraper agent pass
[10:10] a URL pass the output file optionally
[10:13] then we pass in the prompt right and we
[10:14] also have the compute there that we can
[10:16] specify we are at a point where it's
[10:18] important to have some code so I'm going
[10:20] to actually open up the fir crawl
[10:23] documentation here I have it right here
[10:25] you know never be afraid to just throw
[10:28] additional information at at your agents
[10:30] at your plans this is the fir crawl UI
[10:32] I'm going to hit get code and I'm just
[10:34] going to copy kind of the main workflow
[10:36] here for python okay so I'm just going
[10:38] to take that and make sure this is
[10:41] Python block and then I'm just going to
[10:42] paste that in all right so that looks
[10:44] good and if we just scroll through this
[10:47] this looks pretty good we can get rid of
[10:48] some of this noise going to continue
[10:50] with the implementation notes here all
[10:52] right so fantastic so we just have a
[10:53] bunch of details mostly just code and a
[10:56] couple notes on the user prompt details
[10:59] so we going to collapse this and we have

### Minute 11

[11:01] this context block since we're operating
[11:04] in uh cursor it's pretty good at picking
[11:06] up on context and reading files is
[11:08] running an agent mode and they can pull
[11:09] that in so we don't really need this I'm
[11:11] just going to go ahead and delete this
[11:12] last but not least you know this is a
[11:14] really important part of every one of
[11:15] your plans it doesn't matter if you're
[11:16] running a yaml plan a plain text file
[11:19] plan markdown plan I highly highly
[11:21] recommend that you have steps tasks
[11:24] right these are effectively prompts that
[11:26] you can run so we're going to walk
[11:27] through these tasks right now and just
[11:29] kind of continue to build off of the
[11:32] implementation notes and the highle
[11:34] objective so that we can pass it off to
[11:36] composer and let composer do the heavy
[11:38] lifting for us so here we have a suite
[11:42] of tasks and without even looking at the
[11:44] details which are effectively themselves
[11:46] prompts remember these are lists of
[11:49] prompts um you can kind of see what this
[11:50] is going to do right build out the
[11:52] scrape tool build out the read local
[11:53] file and update local file tools double
[11:56] check verify the implementation and this
[11:58] is something really cool that you can do
[11:59] and I highly recommend that you do this

### Minute 12

[12:01] more and more with these new class of
[12:03] agent based AI coding tools you can ask
[12:06] them to verify their work right so we
[12:08] can take something like this and at the
[12:10] end you can just say you know in
[12:12] addition to like a double check step we
[12:14] just kind of recap everything that you
[12:15] want you can say now run this command to
[12:18] make sure that everything you're doing
[12:20] is up to par right you're literally
[12:21] saying great go ahead and run so you can
[12:23] see here at the end here we're going to
[12:25] query the principal a coding landing
[12:27] page and ask what the names and
[12:29] description of each lesson output in a
[12:31] markdown table so this is how we'll know
[12:33] that our agent did the work so let's go
[12:36] ahead and fire this off and then we'll
[12:37] step back from this plan wait review
[12:41] Loop and while we're waiting we're going
[12:42] to go back to the review step of our uh
[12:46] Devon assistant here which should be oh
[12:50] wow Devon's still working here okay so
[12:52] not quite complete yet we're going to go
[12:53] ahead and let Devon keep cooking um so
[12:56] not exactly sure what's going on here
[12:58] but we're going to let it continue to
[12:59] kind of run there so let's go ahead and

### Minute 13

[13:01] run this plan inside of cursor composer
[13:05] with agent mode on so agent Mode's
[13:07] really important because we need to
[13:09] operate on tools we need it to read
[13:10] context we need to uh run terminal
[13:12] commands edit files so on and so forth
[13:14] right so we're giving cursor the control
[13:16] that needs to implement this
[13:20] feature
[13:22] Implement precise agent scraper great
[13:25] verify your work once it's complete with
[13:29] with this command and so that's going to
[13:32] let cursor self validate right so I'm
[13:35] going to go ahead and hit submit here
[13:36] and let's watch cursor in agent mode
[13:39] build out this new agent this is really
[13:41] cool running several tools here in it's
[13:43] agent loop it's listing the directory
[13:44] it's reading file so it's referencing
[13:46] this file that we said to you know
[13:48] reference throughout our plan and so now
[13:50] it's working on actually generating this
[13:52] code so now it's generating our uh
[13:54] scraper agent great so you can see there
[13:56] it got the single file UV depend
[13:59] Tendencies at the top we got our fir

### Minute 14

[14:01] crawl import and if we open up the file
[14:04] here you can see it making progress
[14:07] right it's implementing it looks like
[14:09] step by step clearly it's not done yet
[14:10] only 200 lines there we go we got a nice
[14:13] patch coming in there bunch of work
[14:14] coming in look at this we have 2.5k
[14:16] tokens and let's just go ahead and see
[14:19] how everything's going that's good so
[14:21] it's checking to make sure that I have
[14:23] the fir craw API key you can see it read
[14:25] that um and I need to make sure that it
[14:27] doesn't leak my API key anywhere here
[14:29] okay looks like we're good you can see
[14:31] here it actually ran my execution Loop
[14:34] and it saw that there was an error right
[14:36] so so this is really really powerful it
[14:38] has all the context of my plan all the
[14:40] code that it generated and it has the
[14:42] execution Command right it's able to
[14:44] close the loop and actually run things
[14:46] end to end and then if there's something
[14:48] you know that's gone wrong it'll fix it
[14:50] itself right this is a key idea from
[14:52] Principal a coding that we've discussed
[14:54] and we can see it coming through in a
[14:56] lot of the modern you know agent-based
[14:58] modes right the loop is being closed

### Minute 15

[15:01] here in a lot of these tools you can see
[15:02] here cursor just walking through several
[15:05] things here now it's just continuing to
[15:07] smash that output command and make sure
[15:10] that things are looking good and so as
[15:12] we'll see in a moment this is a pattern
[15:14] that I built directly into pack patterns
[15:18] this is a lightweight AI coding tool for
[15:20] large scale Max compute low error
[15:23] Engineering in the generative AI age I'm
[15:24] trying to pack a lot of value in this
[15:26] video here um so I don't want to you
[15:28] know over stuff it but this is going to
[15:29] be a new tool available for principal a
[15:32] coding members that have completed
[15:34] principal a coding I wanted to create
[15:36] something that has the patterns that
[15:37] we've discussed embedded inside of a
[15:39] lightweight tool that's what this is
[15:41] again more on that in a second when we
[15:42] write the plan that will execute inside
[15:45] of pack patterns but um if we hop back
[15:47] to Devon here we can see that it uh
[15:50] created a PR for this agent let's go
[15:53] ahead and view this PR and this is
[15:54] really cool right now right we have two
[15:57] agents running two agents getting work

### Minute 16

[16:00] done for us our uh cursor agent here is
[16:04] running and has exceeded our Max Loops
[16:07] I'm going to go ahead and stop it here
[16:08] it looks like it's gotten the kind of
[16:10] main flow down I'm going to accept the
[16:12] changes here so we can review this code
[16:14] in a second let's go ahead and check the
[16:15] response from Devon to see how we're
[16:17] doing here this is really cool so when
[16:18] you're operating in Devon it acts like
[16:21] an engineer so you can see here it wrote
[16:23] a bunch of code changes here it ended up
[16:25] with 600 line changes from our 100 line
[16:29] plan um that's the multiplier you want
[16:31] to see and if we hop into the file
[16:33] changes it will perfectly only have this
[16:36] one file right we just said create a new
[16:37] single file agent that's what it's done
[16:39] here we can quick scroll through the
[16:41] changes and see all of our open AI
[16:44] pantic structures we can see our tools
[16:47] here here's our prompt this looks
[16:48] fantastic it's really listening to what
[16:50] I wanted and it's listening to the exact
[16:52] prompt that we gave it you can see are
[16:54] two Dynamic variables inside of our
[16:55] prompt there's our tools and the tool
[16:58] here that really matters is if we look

### Minute 17

[17:01] for our Ron poers code let's look at
[17:04] this so where's our polers code poers
[17:07] python code and if we just search this
[17:09] it is actually just going to split the
[17:11] lines on a temporary file and just run
[17:14] the polar code after pulling in the data
[17:17] frame here okay very interesting so uh
[17:19] this looks good and you can see here we
[17:21] have our main loop with all of our
[17:23] arguments pretty impressive stuff right
[17:24] there's our open AI 03 mini call a lot
[17:27] of work is happening here a gentically
[17:29] big shout out to Devon and all the work
[17:31] done here just to make it super clear
[17:33] there's likely going to be some issues
[17:34] inside of these kind of harder to run
[17:36] you know methods I'm literally having
[17:38] the agent generate polar's python code
[17:40] and then run it inside of a temp file as
[17:43] a single tool call so I'm going to be
[17:45] super impressed if this runs all the way
[17:46] through if nothing else this code is
[17:48] what 80 90 maybe 95% there and then we
[17:51] can push it all the way home or if we
[17:53] want to we can come in here and
[17:55] explicitly just add additional feedback
[17:57] for Devon but but this looks good I'm
[17:59] not going to do anything else here you

### Minute 18

[18:01] can see that it did self verify talking
[18:04] about this pattern a lot right Clos Loop
[18:05] systems self verifiability inside of
[18:08] your AI coding tools Devon can do this
[18:10] right both Devon and you saw here in
[18:12] cursor cursor can also do this all right
[18:14] so we have self verifiability inside the
[18:16] tool it ran this and it successfully
[18:19] calculated the average age here 37.87
[18:21] years as a way to quickly validate that
[18:24] those changes might be good we can just
[18:25] go into Data we can look at the
[18:27] analytics file we a prompt at this
[18:30] what's the average age you know just
[18:32] running an inline selection prompt here
[18:34] from Sonet uh it looks like it's 37.8 so
[18:37] this looks right let's go ahead and
[18:39] close this and I'm just going to go
[18:40] ahead and merge in this change from
[18:42] Devon so I'm going to uncomment that go
[18:44] ahead and let that merge so this is
[18:46] great we have that new agent while we're
[18:48] working on this agent right so I really
[18:51] love that idea right you have this stack
[18:53] of plan weight review and again during
[18:56] the weight step you can start another
[18:58] plan weight review and then during that

### Minute 19

[19:00] weight step you can review or start
[19:02] another plan weight review right so this
[19:04] is a new workflow I'm playing with I'm
[19:06] getting a lot more done with a two to
[19:08] three AI cing assistants that have some
[19:10] type of agentic workflow that have some
[19:12] long running plan based flow inside of
[19:15] it before we merge in let's go ahead and
[19:17] finish up our scraper AI agent that
[19:19] we're building with composer agent and
[19:21] cursor here so I want to let the agent
[19:23] continue to make progress here so what
[19:25] I'll do here is I'll just copy this I'll
[19:27] go to the terminal and I'll just want to
[19:29] test this out so I want to see content's
[19:30] been scraped next I'll read okay I've
[19:33] retrieved I've extracted names have been
[19:37] okay so something is not going right
[19:40] here let's just copy the issue here and
[19:44] hand it back to composer so what's the
[19:48] issue here from our SFA scraper and I'll
[19:52] just past in the error here and let's
[19:54] see what it comes up with so let me take
[19:56] a look at this prompt here we have the
[19:58] URL user prompt this all looks good it

### Minute 20

[20:01] looks like we are
[20:03] scraping and what's getting run here
[20:05] actually okay so it looks like it has to
[20:07] update the prompt for something so this
[20:09] is not operating exactly as we wanted to
[20:11] that's okay I don't want to overstress
[20:13] on the implementation here we're going
[20:15] to give it another shot and then we'll
[20:17] move on from cursor agent mode here if
[20:20] we're not seeing the exact results we
[20:21] want to see so let's go ahead and let it
[20:23] spin a little bit further here it made
[20:25] some changes now it's going to run again
[20:27] and let's see if it can properly call
[20:30] these tools I am seeing that we're
[20:32] missing some of the inside uh tool calls
[20:35] these just aren't showing up in the log
[20:37] so it looks like it's actually not um
[20:39] you know completely calling the right
[20:42] tools um actually that might be the
[20:44] issue so I want that log here right so I
[20:46] want to console print here and I want it
[20:49] to look like this there we go now let's
[20:52] run this again run again there we go so
[20:56] this is the issue you can see here this
[20:58] is why logging is very important you
[20:59] want to create visibility for your agent

### Minute 21

[21:01] think from your agent's perspective uh
[21:03] the problem here is that the tool call
[21:05] names were actually wrong this if
[21:07] statement did not match properly so it
[21:09] did not even call the right tool all
[21:11] right so we're going to stop the process
[21:13] here um this workflow has you know kind
[21:16] of gone Ary I'm sure it's a couple steps
[21:19] away if we go ahead and zoom out wow
[21:21] okay so this is definitely a problem
[21:22] right we're running TBT 3.5 there's
[21:25] clearly something going on here right it
[21:27] looks like our tools are actually not
[21:28] bad it definitely went off the rails
[21:30] this is a good example of me giving the
[21:32] agent a little bit too much agency as
[21:35] soon as it added that kind of workflow
[21:37] step here it broke that typical agentic
[21:40] Loop so you know my fault for not using
[21:42] the tool right but also frustrating that
[21:44] even with this really kind of clear
[21:46] concise plan the agent wasn't able to
[21:49] properly get to the right space that's
[21:51] fine this is something that I'm going to
[21:53] you know fix up tune and I'll make sure
[21:54] this actually lands in the code base
[21:56] let's go ahead and pull in our changes
[21:59] from Devon so I'll just run uh get pool

### Minute 22

[22:03] okay and so we have our brand new polar
[22:06] agent here from Devon let's go ahead
[22:08] let's give this a whirl and if we open
[22:10] up that plan and just copy out that
[22:13] validation you know verification command
[22:15] and let's just run
[22:16] [Music]
[22:19] this and I'm just going to kick this off
[22:22] all right so nice there's our clean
[22:23] agent Loop just like we asked for in
[22:26] that same structure as our previous
[22:29] uh V2 agents and wow look at that so we
[22:31] have list
[22:32] columns nice there's our sample CSV ARS
[22:36] wonderful so you can see there our agent
[22:39] is getting a sample and wow and there's
[22:43] the code right so it generated code it
[22:45] ran the code and then it just ran oh we
[22:48] got a little issue here okay okay so not
[22:50] too bad right for a task as complex as
[22:54] this um Devon actually made this run
[22:57] first go this is really really cool and
[22:59] if I just search I wonder if I just

### Minute 23

[23:01] search for age I should not see this in
[23:03] the code at all right CU that means that
[23:05] it generated it itself okay so this is
[23:08] good I don't see this at all outside of
[23:09] this comment and if we just search for
[23:11] you can see our sample code there sample
[23:14] CSV method list that looks great and if
[23:17] we go to run test polers yeah you can
[23:20] see here we're passing in polar python
[23:23] code and then that's getting executed so
[23:25] this is pretty fantastic so it looks
[23:26] like we got a little error here and this
[23:29] should have fed back into our agentic
[23:31] Loop that's fine you know this is
[23:33] something that we can run with a
[23:34] follow-up prompt I'm going to hold off
[23:35] on that you likely already understand
[23:37] the iterative process but this is really
[23:40] cool right we handed off this entire
[23:42] process to Devon by writing this plan
[23:44] here polar CSV agent right so we have
[23:46] this nice four-step plan fourth step is
[23:49] verify uh we gave it all the details it
[23:51] needed implementation details docs and
[23:54] state and you know even though our
[23:56] cursor agent didn't get the job done for
[23:58] us it did a pretty good job of getting

### Minute 24

[24:00] us you know to that first draft here in
[24:03] our scraper agent right there is
[24:05] definitely still uh work to be done in
[24:08] the agent space you're seeing a lot of
[24:10] AI coding tools push toward
[24:13] that pack spec new and we're going to
[24:17] write specs bash file
[24:20] anthropic agent and for the pattern I'm
[24:24] going to use list director this is an
[24:27] experimental pattern but it is very
[24:29] powerful so let me show you exactly what
[24:31] this looks like here is a spec prompt so
[24:34] you know starting from the top here
[24:35] we're running the director pattern pack
[24:37] patterns comes with a suite of patterns
[24:40] that you can run we're running in
[24:42] architect mode remember this is built
[24:43] directly on top of Aer so all the you
[24:46] know niceties and model names and
[24:48] conventions it's all built right on top
[24:50] of Aer and so we have a main model we
[24:51] have an editor model and then we have
[24:53] something cool here we have an evaluator
[24:55] model we then have our editable context
[24:58] and our read only context and then just

### Minute 25

[25:00] like you saw in our previous plans we
[25:01] have our highle objective also
[25:03] implementation details and then last but
[25:05] not least we have our tasks so there's
[25:08] something really important about these
[25:10] tasks that you'll notice here not only
[25:11] do we have a title and a prompt we also
[25:14] have evaluator count and evaluator
[25:17] command this is basically saying when we
[25:20] finish this AI coding prompt when our
[25:21] assistant finishes writing this code for
[25:23] us run this command take the output and
[25:26] feed it right back in to the assistant
[25:29] and if it fails do it end times so this
[25:31] allows us to you know close the loop on
[25:35] the system and this is something that's
[25:36] really important that we talk about in
[25:38] principal AI coding this is my take on
[25:41] how to transition from the old ways of
[25:42] engineering to the new ways of
[25:44] engineering with a coding assistants
[25:46] this is a topic we dig into a lot in
[25:49] lesson s let the code right itself like
[25:51] I mentioned throughout this video you're
[25:52] seeing this new pattern emerging inside
[25:54] of these powerful AI coding assistants
[25:57] with agent mode and agent mode is just
[25:59] the first version of this right we saw

### Minute 26

[26:01] here in Devon that it was able to you
[26:04] know run this uh
[26:06] verify um you know we said verify you
[26:08] can see verification verified verified
[26:11] right this is a pattern that powerful AI
[26:14] coding tools agentic tools must build in
[26:17] we're going to see this in every single
[26:19] powerful a coding tool that stays
[26:20] relevant you need to close the loop to
[26:22] close the loop you need to you know
[26:23] concretely have a verification command
[26:26] and inside of pack patterns that's known
[26:28] here as the evaluator command so you're
[26:30] going to run that and that enables you
[26:32] to take the output from whatever prompt
[26:34] you just ran right the current state of
[26:36] your application say you're running you
[26:37] know Pi test is the most obvious one you
[26:39] know you can take that command you can
[26:40] take the output feed it back into a
[26:42] model and then take that model and have
[26:44] the model talk to your AI coding
[26:45] assistant all right and so that's what
[26:48] the evaluator model is again we talk
[26:50] about this a lot and you know among
[26:52] other kind of really key AI coding
[26:55] principles and patterns that are you
[26:57] know slowly going to become mainstream
[26:59] talk about all this in principal a

### Minute 27

[27:00] coding feel free to check this out link
[27:02] is going to be in the description it's
[27:04] going to be available to all principal
[27:05] AI coding members that have completed
[27:07] the course consider this just a bonus
[27:09] you know this tool is a simple way for
[27:10] me to provide more value to principal a
[27:14] coding members to access this tool you
[27:15] can go to the dashboard and then once
[27:18] you have completed every lesson you
[27:20] unlock exclusive member only assets the
[27:22] new asset here that we're going to have
[27:24] available is the pack patterns CLI AI
[27:27] coding Library so again this is a thin
[27:30] experimental lightweight tool built on
[27:32] top of Aer and it consists of several
[27:35] different patterns I've you know put a
[27:37] lot of work into the documentation here
[27:38] so feel free to jump in here check it
[27:40] out uh get installed you know set up
[27:42] your API key it's going to be really
[27:43] really simple to get started the key
[27:46] idea here is that um plans are the
[27:48] future of engineering plans are how you
[27:51] package and set up large scale changes
[27:54] and then you hand it off to Great air
[27:56] coding tools like like Devon like cursor

### Minute 28

[28:00] and like pack patterns uh that I'm going
[28:02] to show you here right now so I'm going
[28:04] to Blink through creating this prompt
[28:06] all right so I've filled out this spec
[28:09] prompt with pack pattern spec files you
[28:11] specify both the editable context and
[28:13] the readon context just as if you were
[28:15] in an AER instance same deal here right
[28:17] we have all of our implementation
[28:18] details you can see here I have the
[28:20] example API call here with our bash
[28:22] editor agent from anthropic to kick off
[28:25] these spec prompts we can run pack spec
[28:29] run and then just pass the path and uh
[28:32] that's it so now our AI coding assistant
[28:34] is going to uh take all of these details
[28:37] format it for us in the right way and
[28:38] then run our prompts top to bottom we
[28:40] covered a lot of ground here in this
[28:41] video from Devon to cursor to pack
[28:44] patterns what I want to showcase here
[28:46] really is you know a concrete
[28:48] methodology a concrete pattern for
[28:50] scaling up your compute usage as these
[28:52] AI coding tools and really just as
[28:54] generative AI tools gain the ability to
[28:57] run these long running a gentic Loops
[28:59] we're going to be able to do more and

### Minute 29

[29:01] more so how can we do more instead of
[29:04] just running a single prompt instead of
[29:05] going into uh chat mode or opening up a
[29:09] single AER instance we can always just
[29:11] go you know AER Sonet sfas right we can
[29:14] always hop in here and you know ask what
[29:16] is this and you know write a coding
[29:19] prompts right um but we can do a lot
[29:21] better you saw here with Devon with a
[29:24] great plan it was able to end to end you
[29:27] know with many tool calls with prompting
[29:29] with whatever systems they have going on
[29:31] here systems like this are going to
[29:32] continue to emerge and in order for us
[29:35] to take advantage of them in order for
[29:36] us to really hand off more and more of
[29:39] our work in order for us to scale up the
[29:41] amount of work we can accomplish it's
[29:43] going to be really important that we
[29:44] create the right packages for these
[29:46] tools the kind of key package is very
[29:49] clearly uh plans right it's very clearly
[29:53] just plans where you can detail out
[29:55] exactly what you're looking for at
[29:56] implementation details and then most
[29:58] importantly a list of prompts all pack

### Minute 30

[30:01] patterns is by the way for anyone that
[30:03] wants to implement this on their own you
[30:05] basically just create a loop over your
[30:07] AI coding assistant and some prompts
[30:09] right that's the kind of you know
[30:11] fundamental version of what pack
[30:12] patterns is doing obviously I've added a
[30:14] lot of bells and whistles and the list
[30:17] director pattern here is one example of
[30:19] that and you know literally it's right
[30:21] out of the principal AI coding course if
[30:23] you've taken the course you'll know
[30:25] exactly what's going on uh with this
[30:27] tool you know you'll be able to really
[30:29] fly through all the documentation here
[30:32] it's going to make a ton of sense to you
[30:33] right you have a pattern you want to
[30:35] create a new spec file and it all starts
[30:37] with a simple list pattern right so
[30:38] literally just a list of prompts and
[30:40] then from there we can add more
[30:43] interesting patterns like the director
[30:45] pattern to scale or compute and to hand
[30:47] off more of the work to our AI coding
[30:49] assistant right and you're seeing that
[30:50] here with the director Loop probably
[30:52] going to get there in a second here yeah
[30:53] so we're on the last prompt here and so
[30:56] after this prompt kicks off we're going
[30:58] to be add a review and validate step in

### Minute 31

[31:00] which case after this a coding prompt
[31:03] runs we're then going to have pack
[31:05] patterns executed and take any feedback
[31:08] any errors and feed it right back into
[31:10] our AI coding assistant all right um You
[31:12] can see here yep so now we're on step
[31:13] three review and validate if we scroll
[31:15] up here you can see all the previous
[31:16] work right we had linting issues that
[31:18] were fixed and here is you know all of
[31:20] our tools this is all getting built out
[31:21] this looks really really great right so
[31:23] look at this massive you know large
[31:24] scale change and if we scroll to the
[31:27] bottom here we should get into our
[31:30] director Loop so yep so here we are so
[31:32] this is really cool so now we're getting
[31:33] our agent to you know execute the code
[31:36] and then provide feedback there it is
[31:38] wow fantastic um so this is crazy I'm
[31:41] actually shocked to see if this actually
[31:43] uh oneshotted this entire process
[31:47] um let's let's see uh that's crazy
[31:50] success true okay so let's just try it
[31:52] so I'm going to take this command and
[31:55] you know it's running a simple prompt
[31:56] right this is our anthrop bash editor
[31:59] agent and I'm not even going to open the

### Minute 32

[32:01] agent um and all we're doing here is
[32:03] list all python files all right so our
[32:06] new tool has bash access and it can also
[32:09] edit files for us so I'm just going to
[32:10] say list all python files let's see how
[32:12] it does
[32:13] here okay so let's see okay so the agent
[32:17] Loop definitely completed successfully
[32:19] and where's that LS if we just search LS
[32:21] we should see that here yeah LS star
[32:23] python okay fantastic so it looks like
[32:25] we're not getting the actual output here
[32:27] let's go ahead and open up this agent
[32:29] and this should be relatively simple to
[32:31] fix we actually might be able to have
[32:33] csor just quickly come in here for us
[32:35] and get the result for us so exactly
[32:38] yeah so that's that and then let's go
[32:40] ahead and just rerun this now we should
[32:42] get our results uh printed out for us
[32:44] yeah look at that tool results fantastic
[32:46] so incredible uh just to highlight it
[32:48] again you know this is the power of a
[32:50] great plan okay I just one shoted that
[32:53] work it looks like we have you know
[32:55] 1,000 tokens 99 lines here you know it
[32:58] does take some upfront work some upfront

### Minute 33

[33:00] investment to think through all the work
[33:01] you went done as you can see here but
[33:03] once you do that and once you pair it
[33:04] with powerful models you can see here we
[33:06] have a model stack of three models that
[33:09] ran 280 seconds here and you can see
[33:12] here we have an evaluation Loop that's
[33:14] confirming right it ran this code for us
[33:17] and it confirmed that things are working
[33:20] all right so this is really cool um I'm
[33:22] going to clean up these agents you can
[33:23] check these out in this code base and
[33:25] you know something really cool here
[33:26] you'll be able to see the uh PR that
[33:30] Devon made that's going to be merged in
[33:31] here merg into the code base you can see
[33:33] its commits here um so really cool stuff
[33:36] unfortunately we didn't get agent mode
[33:37] to properly you know work through those
[33:39] changes for us that's fine we gave it a
[33:41] little bit too much agency and you know
[33:44] I don't think that um cursor's composer
[33:46] can handle these large plans yet uh
[33:48] we'll see how that you know develops in
[33:50] the future I think really cursor is more
[33:51] for iterative step by step I really want
[33:53] to highlight you know the tools that let
[33:55] you create plans that you can then hand
[33:58] off tons of work you know entire

### Minute 34

[34:00] features those are the tools you're
[34:02] going to want to look for all right so
[34:04] you know once again just a pitch it
[34:06] principal a coding pack patterns is
[34:08] available now for all principal a coding
[34:11] members that have completed uh the
[34:13] entire course this is just an extra
[34:15] bonus for members and it's more
[34:17] incentive for anyone that's interested
[34:19] in principal a coding to you know go
[34:21] ahead sign up give it a shot you know
[34:23] once again there's a uh full refund
[34:25] guarantee if you bail before the fourth
[34:28] lesson this is my take on how to stay
[34:31] relevant in the age of AI with AI coding
[34:34] as you saw in this video there's a lot
[34:36] of interesting new powerful AI coding
[34:39] techniques and fullon agentic workflows
[34:41] you know agents that are going to be
[34:43] tackling this problem and you know if
[34:46] you're not on this boat if you don't
[34:48] understand what you can do 2025 is it
[34:50] I'm going to be the first guy to just
[34:51] say it to your face if you're not using
[34:53] AI coding Tools in 2025 you won't make
[34:56] it to 2026 you will not be on an upward
[34:58] trajectory anymore you need AI coding

### Minute 35

[35:00] tools to scale your impact if you like
[35:02] this video you know what to do like
[35:05] comment subscribe thanks so much for
[35:07] watching stay focused and keep building