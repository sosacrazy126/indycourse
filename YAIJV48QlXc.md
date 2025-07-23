# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=YAIJV48QlXc
- **Duration:** 32:26
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 6147
- **Transcript Generated:** 2025-03-30 23:48:38

## Transcript


### Minute 0

[00:00] what's up Engineers Andy Dev Dan here
[00:02] something I think about a lot is how can
[00:05] we maximize our compute usage with
[00:07] powerful AI agents while steering clear
[00:10] of the road map of companies like open
[00:13] AI when open AI releases an agent
[00:18] 1,256 startups are immediately destroyed
[00:22] eviscerated for example if you were
[00:24] building a research agent open AI deep
[00:27] research just ate your breakfast lunch
[00:30] and dinner imagine all your time
[00:32] engineering resources and time
[00:34] investment vanished instantly cooked
[00:37] from startups to individual Engineers it
[00:40] doesn't matter how great your work is or
[00:42] how far you've scaled your AI coding or
[00:45] what technical Innovation you found if
[00:47] you invest in the wrong agent in the
[00:50] wrong tool in the wrong product you're
[00:52] at risk of Getting bulldozed By open Ai
[00:55] and other gen tech companies so how can
[00:58] we stay ahead and build powerful

### Minute 1

[01:01] effective agents while staying out of
[01:04] the way of the generative AI road map I
[01:06] spent a lot of time in this space and I
[01:09] want to share a pattern with you for
[01:12] building powerful lean compute gobbling
[01:15] AI agents that can help you move fast
[01:18] iterate and scale your compute usage
[01:20] while staying out of the way then near
[01:23] the end of this video we're going to
[01:24] discuss why we care about agents so much
[01:27] and I'll explain why I and other engine
[01:29] engers are so obsessed with agents
[01:33] agents are everything and I'll explain
[01:35] why in this video by using astrals
[01:38] all-in-one python tool UV and by
[01:42] combining it with powerful AI coding
[01:44] techniques we can build and deploy
[01:47] single file
[01:49] [Applause]
[01:52] agents so what do a single file agent
[01:55] and how does it help us move fast scale
[01:57] our compute and avoid getting disrupted

### Minute 2

[02:00] by big tech companies I have this simple
[02:02] project here in cursor and right away
[02:05] you'll notice something weird we only
[02:08] have two files we have a file database
[02:11] and a python file so before we dive into
[02:14] the agent architecture let's just run
[02:16] our agent with UV and let me show you
[02:19] how powerful this single file is UV run
[02:23] SFA single file agent DD analytics.
[02:26] database will pass in that database
[02:28] file- P for prompt list all tables and
[02:32] their columns - c Let's us set the
[02:35] compute that our agent can use we'll set
[02:37] this to 10 let's kick off our duck DB AI
[02:40] agent you see here it's kicking off the
[02:42] first compute Loop and it only needed
[02:45] one shot to complete this you can see we
[02:47] have a single function argument call you
[02:49] can see we're using the rich python
[02:51] library to format the output here this
[02:54] agent in particular is powered by open
[02:56] AI 03 mini so what just happened there

### Minute 3

[03:00] how was I able to pack in so much
[03:02] intelligence and capability into a
[03:04] single python file we're going to dive
[03:06] into that in just a second but I want to
[03:08] show you the full agentic loop that our
[03:10] agent can go through so let's run this
[03:12] again but let's ask our duck DB AI agent
[03:15] to do something more complex for us I'm
[03:16] going to say users score greater than 80
[03:19] and Status active Okay so you can see
[03:22] here this is the wrong table name um it
[03:25] has to figure out where these columns
[03:26] are coming from and what the exact name
[03:28] of these columns are okay so so there's
[03:30] a lot that I'm kind of leaving up to our
[03:31] agent to figure out and it's going to
[03:33] run that exact same pattern right so we
[03:35] now have an agent Loop only this time
[03:37] it's going to take a more iterative
[03:39] approach so you can see there it's
[03:41] listing tables it found the user table
[03:43] it then is running this describe table
[03:45] arguments tool call so that I can
[03:48] understand what this table looks like
[03:49] there's the output for that and then at
[03:51] the end here it's running Run final SQL
[03:54] query this is the final tool call the
[03:56] final function call and we can see the
[03:58] exact query it's running and the exact

### Minute 4

[04:00] outputs we have an AI agent that is
[04:02] adept at operating duck DB local
[04:05] databases so this is super powerful as a
[04:08] series of tools at its disposal it can
[04:10] use to solve the problem of information
[04:13] Discovery to understand the structure of
[04:15] the database and then it has full
[04:17] autonomy right up to 10 compute Loops to
[04:20] solve the problem and return the results
[04:23] to us we're using multiple libraries
[04:25] inside of a single file so how is this
[04:27] possible we have to give credit to
[04:30] astrals UV you can think of this as bun
[04:33] for python it's the all-in-one python
[04:36] ecosystem manager it basically replaces
[04:39] every other python tool and most
[04:41] importantly for us for these powerful
[04:43] single file agents it gives us this
[04:46] ability run scripts with support for
[04:49] inline dependency metadata let's dive
[04:52] into this feature right now so we can
[04:54] see how we're building out these
[04:56] powerful single file agents

### Minute 5

[05:02] so if we open up our duct DB open aai
[05:05] Agent here you can see right at the top
[05:07] of this file something fascinating right
[05:10] we have dependencies you know you saw
[05:13] with this single command here right we
[05:15] had UV run this creates a Sandbox
[05:19] environment this allows us to run the
[05:21] script as a standalone file with these
[05:24] dependencies included so we have open AI
[05:26] rich and pantic so this is the first key
[05:29] aspect of the single file agent
[05:31] structure we need to be able to load and
[05:33] use dependencies from any python Library
[05:36] most importantly we need a model
[05:38] provider right so now we have this we
[05:40] have access to this and our single file
[05:42] agent now what does the agentic
[05:44] structure look like for this agent you
[05:46] can see we're using pantic to create our
[05:48] argument structure so for instance for
[05:51] our list table args we have the model
[05:54] pass in reasoning this is a powerful
[05:56] pattern to help you understand what your
[05:58] language model was thinking at every

### Minute 6

[06:00] single step if we open up every one of
[06:01] these tool argument structures I'm
[06:04] always requesting reasoning you can see
[06:06] it there you can see it there so on and
[06:09] so forth right so that's a super
[06:10] important pattern you can use when
[06:12] building your agents always pass in
[06:14] reasoning and then always log the
[06:16] reasoning so you can see we have tools
[06:18] we have the agent prompt but the most
[06:19] important thing is the agentic loop down
[06:22] here so let's go ahead and break this
[06:23] down and then let's go ahead and look at
[06:24] how we can distribute this pattern with
[06:27] AI coding to scale it up to an entirely
[06:30] new AI agent so at the start here we're
[06:33] pulling in all of our arguments we have
[06:34] our- D for database - P for prompt - c
[06:37] for compute we have our open AI key
[06:40] check here we're then making our
[06:42] database path Global so that every
[06:44] single function can access it we're
[06:46] building our prompt and then we're
[06:47] running the main agentic Loop so this is
[06:50] where all the magic happens this is
[06:51] where we give our AI agent full control
[06:53] to run tools run functions gather
[06:56] feedback build up its context and solve
[06:59] the problem problem we once solved let's

### Minute 7

[07:01] open this up so we're doing our compute
[07:02] Loop check here and then as you can
[07:04] imagine we're running our intelligence
[07:06] so we're using 03 mini you can see here
[07:09] we're requiring a tool call with every
[07:11] Loop we want our llm to execute a tool
[07:15] we're then looking for Tool calls once
[07:17] we find a tool which we should always
[07:19] have we are running our process of
[07:22] determining which tool to select you can
[07:24] build any type of structure any type of
[07:26] map you want to handle this I'm just
[07:27] doing this with the simplest pattern
[07:29] possible here we just have a bunch of if
[07:30] statements that parse the arguments and
[07:33] then call the function we then take the
[07:35] result and we pass it back in to the
[07:37] language model right we pass it back
[07:39] into to our context window very
[07:41] importantly here we also have an
[07:43] exception so if something goes wrong
[07:45] inside of the tool we're also passing
[07:47] this back to the model right we want our
[07:49] agent to just solve the problem right we
[07:51] want to design a great prompt we want to
[07:53] design great tools and then just hand
[07:54] off the problem to our agent we go off
[07:57] we go on about day we go you know solve
[07:59] other specific problems and then in

### Minute 8

[08:00] parallel it's solving this problem that
[08:03] we gave it really well thanks to our
[08:05] clean agent design so this is one agent
[08:08] pattern that I'm working with but I want
[08:10] to point out something that's really
[08:12] powerful here you saw the list tables
[08:14] described sample but we also have this
[08:16] run test SQL query and Run final SQL
[08:20] query from the tech ecosphere you may
[08:22] have picked up on this idea of
[08:24] verifiable domains and closed loop
[08:28] systems this is something that we talk
[08:29] about about in principled AI coding
[08:31] specifically for the AI coding domain
[08:33] but it really applies to all agentic
[08:35] technology we can do something
[08:37] interesting here with this run test SQL
[08:39] query let's go ahead and open up the
[08:41] arguments and you can see here it looks
[08:44] the exact same as our Run final SQL
[08:47] query and we can go ahead and fire off
[08:48] our agent again and just take a look to
[08:50] see if it's actually going to kick off
[08:52] this call sometimes it completely skips
[08:55] the run test SQL query because it just
[08:57] doesn't need it it doesn't need the test
[08:59] but we can you can do something like

### Minute 9

[09:00] this create a new table high score users
[09:04] from the user table and select all users
[09:08] with score greater than 80 that are
[09:11] active and 2025 let's pass it off to our
[09:14] duck DB AI agent and just see how it
[09:16] does with this I'm also going to kick up
[09:18] the compute Loops just in case it needs
[09:19] a little bit more energy let's kick that
[09:21] off and let's see how it does here so
[09:24] you can see it's first validating the
[09:26] structure right it needs to find the
[09:27] tables so it's running list tables it's
[09:29] seeing the schema structure of that
[09:31] table it's now running this test SQL
[09:34] command so it's verifying that what
[09:36] we're going to ask for will work instead
[09:39] of you know looking for human in the
[09:40] loop feedback or instead of running the
[09:43] final query what it's doing here is
[09:44] running this test SQL query this is a
[09:47] really important pattern for building
[09:49] out great agents you don't have to wait
[09:51] to close the loop to let your agent
[09:53] fully validate the process right so I
[09:56] have this run test SQL it's running this
[09:58] internally
[09:59] adding more information to its context

### Minute 10

[10:01] window you know gathering information
[10:03] about how to solve the problem of you
[10:05] know creating this query creating this
[10:07] new table and then finally after it's
[10:10] validated it it's then running this
[10:11] final query here right so after
[10:13] validation it's now saying you know we
[10:15] can take this query it's safe it works
[10:17] it looks good let's go ahead and run
[10:19] this final query and create this new
[10:22] table so now of course if we hit up and
[10:24] we hit up again let's get a smaller
[10:26] command to work with and we just say you
[10:28] know list all tables and one sample Row
[10:32] for each table and we fire that off we
[10:34] should now get this brand new high score
[10:37] so there's the high score users and the
[10:39] users table so this is fantastic right
[10:41] there's the sample our AI agent is
[10:44] understanding these table structures
[10:45] it's understanding what we want and what
[10:47] we want to do and then it's giving us
[10:49] you know these concrete outputs and you
[10:51] can see here how important it is to have
[10:53] the reasoning inside your agents right
[10:55] it is explaining the results we're
[10:58] getting back here in a really concise

### Minute 11

[11:00] way and this is really cool you can see
[11:02] in the reasoning it's saying the sample
[11:04] Row from user and high scores is exactly
[11:06] the same so it's just going to return
[11:09] the top result okay so this is really
[11:11] powerful I hope you can see that you
[11:13] know single file agents are powerful but
[11:15] having a great AI agent structure with
[11:17] the right tools and the right order is
[11:20] equally as powerful right it doesn't
[11:22] matter if you can build an agent it
[11:24] matters if you can build an effective
[11:26] agent shout out to anthropic for writing
[11:28] you know this great post post on
[11:29] building effective agents this document
[11:31] contains a lot of really key information
[11:33] I brought it up several times on the
[11:34] channel I think it encapsulates a lot of
[11:36] the key ideas and serves as a great
[11:38] starting point for building out agents
[11:40] right they kind of end their story here
[11:43] with agents with this simple Loop right
[11:45] which is effectively all in Asian is you
[11:46] have an llm call environment to an llm
[11:49] call and then they stop kind of whenever
[11:50] they need to but all the magic happens
[11:54] in this Loop right happens in this
[11:56] agentic Loop and this is where you know
[11:58] many struct structures can take place

### Minute 12

[12:00] this is where many fortunes will be made
[12:02] and lost uh you know due to just going
[12:05] after the wrong thing going after the
[12:06] wrong idea and you know again this is
[12:08] why I want to bring this up the single
[12:09] fall agents enable us to build lean
[12:12] compute machines you don't want to
[12:14] overinvestment
[12:29] of top goto use cases for agents I think
[12:32] that's important but uh this is why I
[12:34] bring up this pattern of building
[12:36] lightweight lean single file agents so
[12:39] that you don't
[12:43] overinvestment so this is an important
[12:46] pattern I think pre verification is just
[12:48] as important as post verification or
[12:51] closed loop verification um like I
[12:53] mentioned this is something we talk
[12:54] about in principal a coding more on that
[12:56] later in the video having a test command
[12:59] run and then a final command run

### Minute 13

[13:01] whatever your domain specific problem is
[13:04] if your domain is verifiable I highly
[13:06] recommend you check out this pattern of
[13:09] giving your agent tools to solve the
[13:12] problem but also tools to prever verify
[13:15] that the answer that they're going to
[13:16] give you is the correct answer all right
[13:18] and so that's what we're doing here with
[13:20] our duck DB single file agent so so
[13:23] what's the next step with this right we
[13:24] have these powerful single pile agents
[13:26] with a great agentic structure that can
[13:28] solve problems for us we're going to
[13:30] need many different types of AI agents
[13:33] not just this one right we're going to
[13:34] need for instance an SQL light agent how
[13:37] can we take this agent and the agent
[13:39] structure and basically duplicate it you
[13:41] know make a couple tweaks to it so we
[13:42] can scale and reuse our single file
[13:45] agent pattern right with this powerful
[13:47] tooling thanks to astral UV we now churn
[13:50] out these powerful condensed air agents
[13:53] so you know how can we do that we all
[13:55] already know the answer to this
[13:57] especially if you've been with the
[13:58] channel or if your eyes are open in the

### Minute 14

[14:01] tech ecosystem at all right now we can
[14:03] do this with AI
[14:05] [Applause]
[14:08] coding so now that we have this agent
[14:11] working in a single file with a great
[14:14] agent pattern and all dependencies
[14:16] encapsulated we can iterate at light
[14:18] speed with powerful AI coding techniques
[14:21] many of which we've discussed in
[14:23] principled AI coding we're overdue for
[14:26] AI coding on the channel so let's go
[14:28] ahead and write up a concise AI coding
[14:31] spec prompt to create a new SQL light
[14:33] single file agent and then I'll pitch
[14:36] principled AI coding for those who
[14:37] aren't aware of what it is and how it
[14:40] can accelerate your engineering I also
[14:42] have some updates coming for existing
[14:44] members we're going to have some nice
[14:46] lightweight tooling to help us utilize
[14:48] all the principles we learned inside the
[14:50] course so more than that in a second
[14:52] let's first build out our SQL light AI
[14:55] agent so this is going to be relatively
[14:57] simple since duck DB and SQ SQL light
[14:59] are very very similar what we'll do here

### Minute 15

[15:01] is open the terminal we'll type CP SFA
[15:04] we'll basically just copy this create an
[15:06] SQL light version light great I'm also
[15:08] going to touch AI code. sh and this is
[15:12] where we're going to build out our
[15:13] context model and prompt so that we can
[15:16] quickly reuse our single file agent
[15:18] pattern in a reusable scalable way I use
[15:21] AER as my primary AI coding Workhorse
[15:24] you can deploy this pattern with any AI
[15:27] coding tool you want of course you
[15:29] cursor wind Surfer Klein whatever your
[15:31] deal is go ahead and hop into that I
[15:32] like to use AER and cursor side by side
[15:34] and let me show you a new pattern and
[15:36] let me also just kind of you know share
[15:38] some of the advantages you get when you
[15:40] use a a coding tool like ader so I'm
[15:43] just going to paste this in here since
[15:44] I've done this a million times let's
[15:46] start with just this blob here okay so
[15:48] we're passing in our prompt as the first
[15:50] argument we're kicking off AER I want to
[15:52] run the 03 Mini model in architect mode
[15:55] with the high reasoning effort this is
[15:57] some of the best computer you can get
[15:59] right now I want claw 3.5 Sonet to make

### Minute 16

[16:02] the edits that 03 mini suggests and then
[16:05] we have a couple of configurations here
[16:06] just to speed things up and then in my
[16:08] context you can see I'm passing in I
[16:10] want every single python file available
[16:12] as the context okay and then finally the
[16:14] message is just going to be the prompt
[16:16] so whatever we pass in here we can you
[16:18] know run this now we can say sh Ai and
[16:22] then just pass in whatever prompt and
[16:24] then we can start getting AI coding
[16:25] changes in on this right let me show you
[16:27] a little hint of what I have coming for
[16:29] principled a coding members there's a
[16:31] big theme right now about scaling
[16:33] compute usage and just throwing more
[16:36] compute at the problem and then your
[16:38] problem will be solved you know
[16:39] basically just by turning up the knob we
[16:42] can see that this is true even for AI
[16:44] coding this is going to look really
[16:45] stupid but you're going to understand
[16:47] how powerful this is as we work through
[16:48] this I'm later going to copy this
[16:51] command I'm going to paste it here so
[16:54] let me turn off cursor tab so we can
[16:55] write this by ourselves here I'm going
[16:57] to say double check all changes

### Minute 17

[17:00] requested to make sure they've been
[17:02] implemented and that's it and so what we
[17:05] end up with here is a prompt chain of
[17:07] length four right we have an architect
[17:10] drafting the changes and then an editor
[17:12] writing the changes and then again we
[17:14] have an architect double-checking all
[17:16] the changes that just happened in a
[17:18] brand new instance and then we have an
[17:20] Editor to write those changes right to
[17:22] write anything that was you know
[17:23] potentially missed fantastic so now
[17:25] we're going to actually write the prompt
[17:26] this is going to be really simple I'm
[17:28] going to get the path to this I'm just
[17:29] going to say update and then I'll say
[17:31] refactor to Target SQL light
[17:35] databases keep all functions the same
[17:38] but Target SQL light databases with SQL
[17:42] light 3 so I'm being specific about what
[17:43] library I want use here update tools and
[17:46] prompt to reference SQL
[17:49] light okay because if we open up this
[17:52] file you can see here if we just search
[17:54] duct DB we have you know many references
[17:56] you can see on the side here we have
[17:58] many references to duct B so that's it

### Minute 18

[18:00] that's the prompt I'm going to copy this
[18:03] and I have this kind of reusable AI
[18:05] coding configuration right you can think
[18:07] of this as a kind of just generic a
[18:09] coding um script that we can call that
[18:12] runs a compute enhanced AI coding chain
[18:16] of assistants right we have two AER
[18:17] assistants in architect mode we're just
[18:19] going to copy this we do dollar sign PB
[18:21] paste that's it so this is going to
[18:22] update it's going to kick off two AI
[18:24] coding assistants running back to back
[18:26] this is our first shot and this is our
[18:28] our reflection step right all right so
[18:31] there we go we're getting our changes
[18:33] we're updating our tool calls to
[18:35] reference SQ light instead of duct DB
[18:38] and then at some point here we're going
[18:40] to see our prompt get updated so you can
[18:42] see there all those tools that looks
[18:43] great we on Final SQL query now we're
[18:46] referencing SQL light instead of duct DB
[18:48] you can see we had an update in the
[18:49] prompt and now we're running the
[18:51] reflection right so remember the
[18:53] reflection is literally just this double
[18:55] check all changes requested and then
[18:57] we're pasting The Prompt in again so
[18:59] let's see what happens now we've already

### Minute 19

[19:00] taken one shot at architect and editor
[19:03] with AER and now we're running again so
[19:05] you can see here look at how many things
[19:07] were missed right we have the architect
[19:09] saying hey you missed this here hey you
[19:11] missed this here and then the editor is
[19:13] coming in and actually Chang those
[19:15] things right so we can now search SQL
[19:17] light and so we should see a bunch of
[19:19] references to SQL light now with that
[19:21] new syntax you know as a test we can
[19:23] also come in here and search duck DB
[19:25] right so this is really good we don't
[19:26] see any references to duck DB anymore
[19:28] more fantastic um and now we should be
[19:31] able to run our SQL light agent just as
[19:34] we did our duct DB open AI agent so in
[19:37] order to do that we need to pull in an
[19:38] SQL light version of this I'll paste
[19:41] this in and you can see my SQL light
[19:43] extension uh showing this table here
[19:46] right so this is our user's table let's
[19:47] go and close this so we now have this
[19:49] ready for our new SQL light agent let's
[19:51] go ahead and save this and now let's
[19:53] just run our SQL light agent SFA single
[19:56] pile agent and we're going to run our
[19:58] SQL light version - D analytics SQL

### Minute 20

[20:01] light database - P list five rows from
[20:05] user table and for our compute we'll
[20:07] just say five right should be pretty
[20:09] simple so far so good right our code
[20:10] compile so that looks great we have our
[20:12] first tool call that looks awesome there
[20:14] it is so SQL light uh running just like
[20:17] our duck DB did we're getting a you know
[20:19] slightly different output format because
[20:21] of course we're using SQL light we were
[20:22] able to reuse our existing single file
[20:25] agent architecture we made an update to
[20:27] it with a clean prompt chain of length
[20:29] four where every prompt was us kicking
[20:32] off AER we have an architect and then an
[20:34] editor and then we just basically
[20:35] doubled it right our reflection actually
[20:37] saved us you know a little bit of energy
[20:39] this idea of scaling up your compute
[20:42] really does translate to almost anywhere
[20:44] you're using language models anywhere
[20:47] you're running a prompt right even if
[20:49] it's embedded inside of a tool like AER
[20:51] right you have to remember all these
[20:52] tools right cursor AER chat GPT Claude
[20:56] right every one of these tools at the
[20:58] end is is running the new fundamental

### Minute 21

[21:00] unit of knowledge work it's all about
[21:02] the prompt and agents is how we scale
[21:05] The Prompt up this is how we scale up
[21:08] our impact at the beginning I said we
[21:09] would talk about you know why is
[21:11] everyone so obsessed with agents this is
[21:13] why it's because agents lets us scale up
[21:17] our compute usage and then the age of
[21:19] generative AI when you scale your
[21:21] compute you scale your impact this is a
[21:24] big theme on The Andy Deb Dan Channel
[21:27] right now in q1 2025
[21:29] the most important thing we can do is
[21:30] figure out how to scale our compute
[21:33] agents are the name of the game you just
[21:35] saw what we did here with a duck DB you
[21:38] know domain specific Focus agent with
[21:40] only five tools right it gathers context
[21:44] it understands the structure it then
[21:46] internally validates for hard problems
[21:49] and then it gives us the final result
[21:51] right when we take astral's UV and the
[21:54] ability to package dependencies in these
[21:57] isolated s single file agents right
[21:59] these single file scripts this really

### Minute 22

[22:01] lets us move fast scale our compute and
[22:04] get work done and solve problems fast
[22:07] without overinvestigation
[22:28] gather contexts to solve that specific
[22:31] problem you're trying to solve all right
[22:33] this is the key um this codebase is
[22:35] going to be linked in the description
[22:37] for you drop the like drop the sub and
[22:40] you know drop a comment let me know how
[22:42] deep into agents you are right now are
[22:44] you on the surface are you you know
[22:45] trying to understand agent structures
[22:48] are you using any agents right now and
[22:50] you know let me know what you think
[22:51] about this idea to build out these
[22:54] single file agents that you can quickly
[22:56] reuse and redeploy with help of you know
[22:59] whatever your favorite AI coding tooling

### Minute 23

[23:01] is at a high level the longer your
[23:03] prompt chain the more compute you're
[23:05] using right and when we think about it
[23:08] what's happening in this agent Loop that
[23:10] we're running here in both our sqlite
[23:12] and our open AI version you know what's
[23:13] happening here we can kick this off
[23:14] again let's go ahead and ask another
[23:16] question here let's list five users GT
[23:19] greater than status archived or pending
[23:23] all right let's kick that off and
[23:29] fantastic so we can see that we we have
[23:31] status archived or pending age is always
[23:33] over 30 right and this is running in
[23:36] this agentic loop it's solving this
[23:38] problem automatically it has the tools
[23:39] it needs to do the job and you know
[23:41] something I want to mention here you can
[23:43] think about an agent as a elongated
[23:46] prompt chain right it's a series of
[23:48] prompt calls over and over and over
[23:50] again targeting a specific domain
[23:52] problem and it's all about figuring out
[23:54] how to best solve that problem with the
[23:56] compute that you give it and so if an
[23:57] error URS Cur here we would probably
[23:59] need to give you know more compute more

### Minute 24

[24:02] uh you know Loops we're running 03 mini
[24:04] is a powerful reasoning model so you
[24:06] know as it's thinking through what tools
[24:07] to call and solving these problems it's
[24:09] doing an extraordinary job an
[24:11] interesting way to think about the AI
[24:12] agent is that the more compute you're
[24:14] giving it basically what we're doing is
[24:15] we're extending the prompt chain right
[24:17] we're elongating the number of compute
[24:20] runs that it has so if we wanted to
[24:22] solve a really hard problem for instance
[24:25] you know open ai's deep research tool
[24:27] this thing runs for for 5 to 30 minutes
[24:30] right so you can imagine you know its
[24:32] compute Loop is you know blasted up to
[24:34] like 100 across various tools various
[24:37] functions you know various capabilities
[24:40] that's a really powerful idea we're
[24:41] going to be looking into more on the
[24:43] channel like I mentioned I'm going to
[24:44] have these single file agents in a
[24:46] codebase for you to check out tweak and
[24:48] make your own I'll add a couple
[24:50] additional versions here that I was
[24:51] playing with so that you can you know
[24:53] check them out and build out your own I
[24:54] have a version where I have the meta
[24:56] prompt we've talked about on the channel
[24:58] in inside of a single file agent you can
[24:59] just quickly query your uh meta

### Minute 25

[25:02] prompting agent to generate a new prompt
[25:03] for you things are moving fast agents
[25:05] are here one of the most important
[25:07] agents and one of the most important
[25:09] things you can do right now is learn how
[25:12] to write code with AI and not just learn
[25:15] but really scale your capabilities with
[25:18] writing code with AI many of you on the
[25:20] channel you've already dove in to
[25:22] principled a coding let me just pitch
[25:24] this for those who haven't taken it yet
[25:26] this is really important and I want to
[25:27] make sure I'm sharing this tool so that
[25:29] everyone is understanding the State
[25:32] Engineering is in and how they can
[25:34] progress keep up and thrive in the new
[25:36] world of generative AI so principal AI
[25:39] coding is my take on how to transition
[25:42] from the old ways of engineering to the
[25:44] new way we now have over a thousand
[25:47] Engineers that have taken principal a
[25:49] coding that have a New Perspective and
[25:52] actionable patterns and principles they
[25:54] can use for their Engineering in today's
[25:57] landscap ape of generative Ai and more
[25:59] importantly for the next wave of

### Minute 26

[26:02] generative AI based engineering so you
[26:05] know I don't know if you've noticed um
[26:06] if your eyes are open you've probably
[26:08] noticed this but software engineering
[26:09] has changed and it's time to change with
[26:12] it a coding is the largest productivity
[26:13] multiplyer for engineers to ever exist
[26:16] this is something that you can't miss
[26:18] out on okay if you miss out on this
[26:21] you'll be left behind I think 2025 is
[26:23] the last year where you can write code
[26:25] without Ai and really be used useful
[26:29] right really be employable really be uh
[26:32] able to contribute in a meaningful way
[26:34] go on Twitter for 5 seconds go on Reddit
[26:37] and you know just type in a coding type
[26:38] in cursor type in AER um type in Klein
[26:41] like type in any one of these tools and
[26:43] you'll understand that there are
[26:45] Engineers um all the way from Noob
[26:48] beginners to senior expert principal
[26:51] bigname Engineers right that you you
[26:53] know likely look up to they understand
[26:55] this curve right they understand these
[26:57] two curves you're are either using the
[26:59] tool that helps you scale your impact or

### Minute 27

[27:02] you're not okay and you know just to say
[27:05] it really bluntly if you're not writing
[27:07] code with AI if you're still manually
[27:09] coding you are not using the best tool
[27:11] for the job anymore if you're writing
[27:13] code with AI you are absolutely on an
[27:15] upward curve okay principal a coding was
[27:18] built to help you make this transition
[27:20] in the shortest amount of time possible
[27:23] okay the only thing better than
[27:25] experience is experience earned faster
[27:28] we focus on principles not tools
[27:30] principles not models okay there's going
[27:33] to be an onslaught of Agents of tools of
[27:36] models you know this already right
[27:38] you're you're aware of this we need
[27:40] principles to endure change over time so
[27:43] you know this course helps you get there
[27:44] it helps you endure change with
[27:46] principles and one of the key principles
[27:48] we talk about in lesson three is context
[27:51] model prompt these are the big three the
[27:54] most important elements for getting work
[27:56] done in AI coding but really with all of
[27:58] generative AI there are eight lessons in

### Minute 28

[28:01] this course they take you from beginner
[28:02] to intermediate to advance we talk about
[28:05] big topics that are you know really
[28:07] becoming mainstream in the generative ai
[28:10] ai coding world we talk about the spec
[28:12] prompt right scaling up your work by
[28:15] writing larger prompts larger specs and
[28:18] we talk about you know a big topic
[28:19] that's come up recently is this idea of
[28:21] closing the loop right by creating these
[28:24] closed loop self verifiable systems your
[28:28] AI coding tools and your agentic systems
[28:31] can actually get the work done by
[28:33] themselves if you give them enough
[28:35] direction if you tell them where to go
[28:36] and how to resolve and give them
[28:37] feedback you close the loop okay this is
[28:40] a really important powerful pattern this
[28:42] is going to be big over 2025 and 2026
[28:45] people are already starting to talk
[28:46] about this more this is getting
[28:47] uncovered so you want to move on this
[28:48] stuff before it really really hits the
[28:50] masses okay so eight lessons here um you
[28:53] know lots of great reviews feel free to
[28:54] check out you know tons of the other
[28:56] videos and AI coding content I have on
[28:58] the channel um this is here for you and

### Minute 29

[29:00] just to mention it I have a no questions
[29:02] asked refund before Lesson Four this is
[29:05] basically risk-free at this point right
[29:07] so hop in if you don't like my style if
[29:09] you don't like the video if you don't
[29:10] understand what's happening if it's too
[29:11] complex or if it's not complex enough
[29:13] and you're too much of an omni chat
[29:15] engineer and you already know what I'm
[29:17] going to say in the next you know six
[29:18] videos or whatever that's fine you get a
[29:20] full refund for you start lesson 4 no
[29:23] questions asked we've had zero issues
[29:25] with this there's a lot of value here
[29:27] and you know I just want to pit it on
[29:28] the channel for all existing principled
[29:30] AI coding members I'm going to be
[29:32] rolling out some new tooling that helps
[29:34] us use the patterns we learned in
[29:37] principal AI coding in a cool
[29:38] lightweight way I'm building this on top
[29:40] of the powerful all-in-one tool UV so
[29:43] it's going to be super simple to set up
[29:45] use and deploy and we're of course going
[29:48] to continue using our you know
[29:50] top-of-the-line uh most customizable
[29:53] configurable powerful AI coding
[29:55] assistant AER so stay tuned for that and
[29:58] you know even if you don't use ader you

### Minute 30

[30:00] know even if you're not a fan of CLI
[30:02] based you know full control AI coding
[30:05] assistants that's fine um again we use
[30:08] AER as a tool here to showcase the
[30:11] principles this course is not about AER
[30:13] okay so just to quickly mention that and
[30:15] uh yeah that's principal AI coding uh
[30:18] hop in here before you know the next
[30:21] wave of coding comes which I'm going to
[30:23] be preparing everyone for again inside
[30:26] this course those lessons are in the
[30:28] works they're in the queue but that's
[30:29] going to be for later in this year just
[30:32] to say it out loud here right now ai
[30:34] coding is the wave the next wave that's
[30:36] upon us is agentic coding when you fully
[30:40] close the loop what you end up with is
[30:42] systems that can operate on their own so
[30:45] stay tuned stay locked in I hope you can
[30:48] understand why agents are so important
[30:50] in the age of AI you first start with
[30:52] the prompt you then move to prompt
[30:53] chains you have series of llm based
[30:56] calls that can do work on your behalf
[30:59] and then you move to AI agents right

### Minute 31

[31:00] this structure where you give them the
[31:03] tools they need to solve the problem and
[31:05] then you let them learn gather
[31:07] information execute get feedback agents
[31:09] is how we continue to scale our compute
[31:11] this is where we're going to be focused
[31:13] on the channel it's all about scaling
[31:15] compute usage maximizing what you can do
[31:18] it's all about AI coding so that you can
[31:20] write faster than ever so that you can
[31:22] build out these agents fast you know
[31:24] just to come full circle here that's why
[31:26] the single file
[31:28] agent pattern is so important because we
[31:30] meet at the intersection of three
[31:33] important Innovations we have astrals UV
[31:36] allowing us to bundle dependencies into
[31:38] a single file we have self- validating
[31:41] agent patterns where we can write great
[31:44] tools and great prompts to allow the
[31:46] agent to self verify before it Returns
[31:49] the response to us and then of course we
[31:52] have powerful AI coding techniques many
[31:55] of these we cover in principal AI coding
[31:57] this lets us reuse scale clone and

### Minute 32

[32:01] duplicate our single file AI agents into
[32:04] many different domains you can imagine
[32:06] we have an agent that builds agents okay
[32:10] so we have a lot of Big Ideas to cover
[32:12] on the channel if you're interested in
[32:13] this if you made it this far in the
[32:14] video you know what to do drop the like
[32:17] drop the sub leave a comment stay
[32:19] connected and whatever happens stay
[32:22] focused and keep building