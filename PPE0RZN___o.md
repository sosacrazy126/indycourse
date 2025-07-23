# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=PPE0RZN___o
- **Duration:** 37:26
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 7516
- **Transcript Generated:** 2025-03-30 23:48:41

## Transcript


### Minute 0

[00:00] what's up Engineers Indy Dev Dan here
[00:02] we've entered the age of Agents
[00:05] Microsoft is rolling out co-pilot agent
[00:08] mode open AI had back-to-back launches
[00:10] with operator right into deep research
[00:14] this is the most comprehensive deep
[00:16] research tool I've ever seen and used
[00:19] Gemini has a version of Deep research
[00:21] more notably they have their notebook AI
[00:24] agent meanwhile anthropic created
[00:27] computer use and kind of set off this
[00:30] entire stream of generative AI companies
[00:32] building agents on top of their own
[00:34] technology the computer use text editor
[00:37] and Bash tools are still some of the
[00:40] most slept on tools to date check this
[00:42] out here's a simple bun logging script I
[00:45] can open up the terminal I have a file
[00:47] editing agent built on top of anthropics
[00:50] file editing tool we can run this prompt
[00:52] and it'll make three distinct changes
[00:54] for us it's going to read this file
[00:56] update it it's going to add the
[00:57] directory pram just like we're asking
[00:59] and then it's going to add confirmation

### Minute 1

[01:00] flag you can see that just came in there
[01:02] then it's going to create two new
[01:03] versions a shell script version and a
[01:05] Powers shell version there it is if I
[01:08] run that greb command again you can see
[01:11] we now have those three individual files
[01:14] here's the updated bun version clear
[01:16] logs. sh here's the shell version clear
[01:19] logs. PS1 here's the Powershell version
[01:23] with a single command I was able to
[01:25] generate three changes thanks to my file
[01:28] AI agent so is not clear to you already
[01:31] AI agents are extremely powerful why is
[01:35] that it's because they turn your prompt
[01:37] context and model into actions at scale
[01:41] it's important that you and I the
[01:43] engineer know how and when to build and
[01:46] deploy AI agents across your developer
[01:49] tooling projects and work in this video
[01:52] I want to take you through the prompt
[01:54] The Prompt chain and the AI agent to
[01:56] help you understand which one you need
[01:59] to get the job done we'll lean on

### Minute 2

[02:01] anthropics incredible building effective
[02:04] agents post and I'll share my
[02:06] distillation of what matters and
[02:09] mistakes I've made when building AI
[02:11] agents so you can avoid making the same
[02:14] mistakes let me introduce you to my new
[02:17] video editing tool
[02:19] [Applause]
[02:21] a okay so before we dive into what
[02:24] exactly this tool does let's go ahead
[02:26] and go over to the elcut agent file and
[02:29] I'm going to kick off a benchmark that
[02:31] is going to run a series of problems for
[02:34] us using the prompt The Prompt chain and
[02:37] the AI agent version this Benchmark is
[02:39] going to tell us which one of these
[02:41] levels we need to actually solve this
[02:44] problem Bon run a cut agent and this
[02:47] Benchmark is going to run in the
[02:49] background in parallel to us and we'll
[02:51] Circle back to this to answer questions
[02:53] like are reasoning models always better
[02:55] than base models do gp4 AI agents beat
[02:59] 03 3 mini prompts does a 03 mini prompt

### Minute 3

[03:02] beat a 03 prompt chain how much more
[03:05] expensive is an AI agent versus a prompt
[03:08] chain and more importantly is it worth
[03:10] it so what's a cut how does it work and
[03:14] why did I build it aut is the fastest
[03:17] way to remove uh filler words repeats
[03:19] and nonsense out of your videos so you
[03:22] can go from scripts that you know have
[03:25] stuttering in them that have filler
[03:26] words and repeats and then it'll end up
[03:28] looking like this the scratchpad active
[03:30] memory pattern is going to be really
[03:32] important for rolling out useful
[03:34] personal AI assistance the key here is
[03:37] that it focuses on the transcript so
[03:39] let's walk through the process it all
[03:41] starts out with Word level transcript
[03:43] you can use a whisper transcription tool
[03:46] to generate this type of Json structure
[03:48] right we have all the text and then we
[03:50] have the individual words at specific
[03:52] start and end times this is the raw
[03:54] script what I like to call the base edit
[03:57] that we're going to have our AI agents
[03:58] edit for us so we scroll down here you

### Minute 4

[04:00] can see we have you know a couple
[04:02] sentences worth step two is create
[04:04] slices so it is too much work to pass
[04:06] off an entire transcription for you know
[04:09] a 30 40 50 minute long video to any
[04:12] language model if we open up a
[04:14] transcription here you can see we have
[04:17] 350,000 tokens in this single transcript
[04:20] and that includes all the text here and
[04:22] then Word level breakdowns just as you
[04:24] saw before and this is a real transcript
[04:27] from the deep seek personal AI assistant
[04:29] video there's just too many tokens even
[04:31] if you hand this off to Gemini it's not
[04:33] going to be able to solve this problem
[04:35] in any cohesive way at scale how can we
[04:37] handle this we can create slices so
[04:39] slice is a chunk of the transcript
[04:42] containing a few sentences each from the
[04:44] transcription above we could create two
[04:46] slices in these two slices there are a
[04:48] couple key things that need to be edited
[04:50] out next we're going to allocate our AI
[04:52] agents right so in our case this is
[04:54] going to be our prompt prompt chain or
[04:56] our full-on AI agent as we saw here
[04:58] right and we're going to walk through
[04:59] this in just a moment I'm really excited

### Minute 5

[05:01] to share with you how the prompt versus
[05:03] The Prompt Chain versus the AI agent
[05:05] performs for this use case the results
[05:08] are not exactly as you would expect this
[05:10] is the really cool part about creating
[05:11] slices and it's a great part about
[05:13] breaking your large problem into smaller
[05:16] more manageable chunks right if ever
[05:17] you're feeling overwhelmed with a
[05:19] specific problem it's probably just too
[05:21] big and you haven't broken it down into
[05:23] small enough chunks engineering 101
[05:25] slices give us this incredible ability
[05:27] to for each slice we'll create an at an
[05:30] AI agent and basically hand off this
[05:32] problem to compute at scale so you can
[05:34] imagine we'll have hundreds of slices
[05:36] getting edited all at the same time in
[05:38] parallel now step four is where all the
[05:41] magic happens slice one you have this
[05:43] before text and then you end up with
[05:44] this after text right so this is
[05:46] happening in parallel slice one and
[05:48] slice 2 and slice n are getting edited
[05:51] all at the same time with compute and
[05:54] then finally we can bind the edits into
[05:57] the sequence of timeline edits and every
[05:59] video editor has a different format I

### Minute 6

[06:01] use Final Cut Pro so I'm going to be
[06:02] converting these into FCP XML files
[06:05] we're not going to get into this too
[06:06] much but there's what the format looks
[06:09] like we're going to go from prompt to
[06:12] prompt chain to AI agent and we're going
[06:14] to see across these three levels of
[06:17] abstraction which one performs the best
[06:19] let's go ahead and run a prompt and
[06:21] really understand what this problem
[06:23] looks like B run upcut agent and then we
[06:25] can kick this off let's let this prompt
[06:28] run so this is just running a prompt you
[06:30] can see it got the problem wrong let's
[06:31] go ahead and figure out why so let's
[06:33] open up the logging and just look at
[06:36] this individual prompt so we can open
[06:38] this up I've been experimenting a lot
[06:39] lately with markdown based logging just
[06:42] for a more easier to read logging
[06:44] experience and let's go top to bottom
[06:46] here so here's the original text and
[06:48] here's the target text so every one of
[06:51] our benchmarking problems coming out of
[06:53] our benchmarking file it looks like this
[06:55] right here's the structure of it right
[06:56] so we have the problem ID we have that
[06:58] slice and remember the slice is a piece

### Minute 7

[07:01] of the transcript and then we have the
[07:02] correct text and the beginning text
[07:05] inside of the slice here's what a slice
[07:07] looks like most importantly we have the
[07:09] words and we have the text so let's look
[07:11] at what we're starting with and what
[07:12] we're ending up with so bunch of
[07:14] gibberish in the beginning uh these are
[07:16] all real transcripts from videos from
[07:18] previous videos by the way so yeah this
[07:20] is me just you know stuttering and
[07:21] saying uh over and over turns out
[07:23] talking about technology can be
[07:25] sometimes harder than the technology
[07:27] itself we then say the scratch Pad actor
[07:29] memor is going to be really important so
[07:30] basically what we want to do here is get
[07:31] rid of this intro right so that's the
[07:33] target text right it's everything
[07:35] remaining this is what we want our model
[07:37] to edit down to okay so you can see we
[07:40] wrote The Prompt we'll look at what
[07:41] exactly this prompt looks like in just a
[07:43] moment our llm created these deletions
[07:46] for us start time end time the duration
[07:49] explanation you can see the exact words
[07:51] that it removed so it's going to remove
[07:52] of and then act um the here's the
[07:56] original here's what we wanted to Target
[07:59] and then here's what the prediction was

### Minute 8

[08:01] right here's what our model output for
[08:03] us you can see it didn't quite get the
[08:05] edit right this is an example of where a
[08:07] prompt is not enough and I'll and I'll
[08:10] link just for fun I'll link the original
[08:12] one prompt is not enough video that
[08:14] really kick off the channel back then we
[08:16] were talking about the same concepts
[08:17] with much more primitive technology it's
[08:20] incredible to think about how far we've
[08:21] come since that video but you know one
[08:23] prompt is not enough when you're trying
[08:25] to do more and more at scale and you're
[08:27] trying to accomplish and hand off a ton
[08:29] of work to your AI tooling and here's
[08:32] the target text right so we can see here
[08:33] a simple prompt did not do the job let's
[08:36] look at what this prompt actually looks
[08:38] like so if we open up this prompt you
[08:40] can see here we have our classic clean
[08:42] XML is format we have our purpose we
[08:45] have our instructions and then we have
[08:47] our variables at the bottom this was a
[08:50] dynamic variable and our application
[08:52] replaced it so this you know looks like
[08:54] this in our code right so this is a you
[08:57] know variable that will be replaced

### Minute 9

[09:00] and what it ended up doing here was
[09:01] placing the iteration slice that we're
[09:03] operating on right and remember the
[09:05] slice is just a small piece of the
[09:08] entire transcript so that's what the
[09:10] iteration slice is you can see we have
[09:11] some instructions here classic prompting
[09:13] nothing new here that we haven't
[09:14] discussed on the channel before let's
[09:16] scale this up right this is the prompt
[09:18] and if we open up our llms file collapse
[09:21] everything we have the intelligence
[09:23] comment here and this is what that looks
[09:24] like in code okay so nothing too fancy
[09:27] but it is important that I share it here
[09:28] because it's tool is proprietary prompt
[09:31] up there we have our XML slice that
[09:33] we're replacing with the incoming slice
[09:35] and then we're doing some logging
[09:37] reasoning effort check and then we're
[09:38] just pulling out a bunch of auxiliary
[09:40] information from the response right
[09:42] that's the prompt if we look at
[09:44] anthropics building effective agents doc
[09:46] it all starts with The Prompt what we've
[09:50] done here is we've given our language
[09:52] model access to an output structure so
[09:54] that we can pass in a prompt our llm
[09:57] then makes a judgment call on the output

### Minute 10

[10:00] in the prompt version we don't have
[10:02] anything fancy here all we have is a
[10:03] structured outputs call that generates
[10:06] our deletions and so that's all our
[10:08] prompt is doing you can see here we have
[10:10] our response format that has our uncut
[10:13] uh deletion and we are using Zod
[10:15] response format for structured outputs
[10:18] let's go ahead and kick up our compute
[10:20] there's two levers we can pull here
[10:22] right away we can just do one of them
[10:24] for fun right we can quickly just take
[10:27] this right this is running GPD 40 we can
[10:29] go config we can go llm model we can go
[10:31] O3 mini and then we can just quickly you
[10:33] know kick this off again and now o03
[10:35] mini is going to take a hit at solving
[10:38] this problem let's take a look at the
[10:40] output that 03 mini gave us same deal we
[10:43] have the original text we have the
[10:44] target there's the prompt for O3 mini
[10:47] here's the deletion it created and so if
[10:49] you scroll down here you can see O3 mini
[10:51] got this problem right with just a
[10:54] prompt very cool to see this right so we
[10:56] have the original text and then we have
[10:58] the predicted final text coming out of

### Minute 11

[11:00] our language model and then we have the
[11:02] target text so that's us answering the
[11:04] problem successfully and incorrectly so
[11:06] I'll comment this out and let's go ahead
[11:07] and look at the prompt Chain by looking
[11:10] at the log you'll understand exactly how
[11:12] it works so let's kick this
[11:15] off what we're doing here with the
[11:17] prompt chain is we're taking that same
[11:19] problem and we're throwing more compute
[11:21] at the problem you can see here gbg 40
[11:24] got this problem correct with a prompt
[11:26] chain so let's go ahead and look at the
[11:28] log and then let's break down how the
[11:29] prompt chain worked let's go ahead and
[11:31] open up V2 this is the UT prompt chain
[11:34] and let's look at how a prompt chain
[11:36] outperforms the single prompt okay so
[11:38] once again we have that exact same
[11:40] problem right uh this scratch bad kind
[11:42] of blah blah blah so basically we have
[11:43] the starting text and then we have the
[11:45] ground truth right this is the end
[11:47] result we're looking to get to and then
[11:48] we have this new piece of information
[11:50] when you're using prompt chains and AI
[11:52] agents you'll always want to limit the
[11:54] amount of compute or Loops that your AI
[11:56] tooling can run you don't want it to run
[11:59] infinitely you might have a bug

### Minute 12

[12:01] something might go wrong and there is
[12:02] nearly always a sweet spot or a perfect
[12:05] range for the problem that you're trying
[12:07] to solve so you can see here for this
[12:09] prompt chain I'm allowing eight compute
[12:11] Loops eight iterations okay so we start
[12:14] with this one deletion here um this the
[12:17] scratch Pad kind of act um and then if
[12:20] we scroll down here you can see you know
[12:21] that made a pretty good edit then we can
[12:23] scroll down and then you can see it only
[12:25] took out um so it's taking another shot
[12:27] it sees that you know after this first
[12:30] ROM that I made I still need to edit
[12:32] more okay so now it's just taking out um
[12:34] third compute Loop right so it has you
[12:36] know five shots left and so now it's
[12:38] telling us that no deletions were
[12:41] generated so it's going to exit the loop
[12:43] so inside of this prompt which we'll
[12:44] look at in a moment there was a
[12:45] condition that says um if you're done
[12:47] return an empty list okay it created two
[12:51] deletions here's the first one with
[12:53] several words in the deletion and then
[12:55] we have in a follow-up Loop because it
[12:57] didn't create the perfect edit the first
[12:59] first time you can see here we have the

### Minute 13

[13:00] words um edited that out and then we
[13:03] have the final iteration slice so this
[13:05] is what our final slice looks like with
[13:07] the edits made from the deletions okay
[13:09] so there's that nice Json object there
[13:11] and then you can see here here's the
[13:12] original here's what our prompt chain
[13:14] output for us and here's the target text
[13:16] you can see we of course have the
[13:18] correct answer this is really important
[13:21] because for this simple use case of
[13:23] effectively determining which words to
[13:26] remove that don't make sense you can see
[13:28] here that having a little bit more
[13:30] compute you know quite literally it just
[13:31] needed one additional run right so we
[13:34] had one deletion then we had another
[13:36] deletion and then on our third compute
[13:38] Loop it said there's nothing left for me
[13:40] to do here I'm done by turning our
[13:42] prompt into a prompt chain quite
[13:44] literally just saying run it again it
[13:46] was able to generate an improved answer
[13:48] for us so you know that's the log and
[13:51] you can see here we have three prompts
[13:53] right so one prompt for our first run so
[13:56] we have this first prompt here and then
[13:57] we have our second prompt and then our
[13:59] third prompt and it was in our third

### Minute 14

[14:02] prompt where the prompt chain you know
[14:04] the language model returned no deletions
[14:06] so that means we're done okay let's go
[14:08] ahead and just take a look at the prompt
[14:10] for a moment here and you'll see a very
[14:12] similar structure except for the primary
[14:13] difference that we have an original
[14:16] slice and current deletions okay so in
[14:19] addition to the iteration slice which is
[14:22] the small piece of the transcript that
[14:24] we're working on currently we also have
[14:26] the current deletions so when our model
[14:28] is looping it needs to know what it's
[14:31] already edited and it needs to know the
[14:33] starting point okay so this is where it
[14:35] started this is the current deletions
[14:37] that it's made and then the iteration
[14:39] slice is the result of those deletions
[14:43] on the original slice so let me just
[14:45] show you the second prompt you can see
[14:46] here current deltion is empty and in
[14:48] this version our current deletions has
[14:51] some content right so in the second
[14:53] prompt we have made edits right and you
[14:55] can see here this corresponds to the
[14:58] edits we saw exactly in the log The

### Minute 15

[15:00] Prompt chain it allows us to keep track
[15:02] of the state the original slice the work
[15:05] that it's done and the work that it's
[15:07] doing that's iteration two and then of
[15:09] course we have the third iteration you
[15:11] can see here same deal except we have an
[15:13] additional current deletion right so we
[15:15] have two deletions in here we can go
[15:17] ahead and separate this just to make it
[15:18] a little bit more clearer right so you
[15:20] can see those two removed
[15:22] words right there okay so this is our
[15:25] prompt chain and we can go ahead and
[15:27] dial into this code for a moment here
[15:28] prompt
[15:29] chain we can see here we're just setting
[15:31] up logging we're pulling out our model
[15:33] we're pulling out the problem slice
[15:35] starting text and then we're actually
[15:37] running the code here in the end every
[15:39] one of these versions right every one of
[15:41] our prompt our prompt chain and our AI
[15:43] agent is just going to return deletions
[15:46] it's really important to set up your
[15:47] workflows so that they're always
[15:49] returning consistent types consistent
[15:51] formats this allows you to operate on
[15:53] them at scale and create versions of
[15:55] them so all we're doing here is
[15:57] outputting deletions and then some
[15:59] auxiliary information right in this case

### Minute 16

[16:01] we just have the cost so let's go into
[16:03] generate a cut deletions V2 this is our
[16:06] promp chain so V1 is just a prompt V2 is
[16:10] a prompt chain so let's take a look at
[16:12] what this looks like and you can imagine
[16:14] it is you know effectively going to be a
[16:16] loop and you can see here we're passing
[16:17] in Max compute and we're updating this
[16:19] to I think eight but you can see here
[16:21] what's happening right we basically have
[16:22] the same thing and we're just looping
[16:24] this time right we're keeping track of
[16:25] some more State there's our iteration
[16:26] slice there's our original slice and
[16:28] here's our you know list of deletions
[16:30] that we're keeping track of and then of
[16:32] course here's our Loop right so just as
[16:34] you saw before there's our instruction
[16:36] Rich prompt purpose and then our Dynamic
[16:39] variables that get updated inside of our
[16:41] application right if we collapse the
[16:43] prompt you can see we're always
[16:44] outputting our prompt file we have our
[16:46] actual execution Loop this is the prompt
[16:49] chain let's go ahead and run the most
[16:53] exciting version right let's run the AI
[16:56] agent
[16:59] let's kick this

### Minute 17

[17:00] off this agent has 16 compute Loops so
[17:04] I'm giving it 16 compute uses and
[17:08] unfortunately gbd 40 got the problem
[17:10] wrong so let's figure out why why did it
[17:12] edit this problem incorrectly okay let's
[17:15] look at V3 you can see here it made four
[17:18] prompts in total and if we hop into this
[17:20] file we can see a lot of the same things
[17:22] the big difference here is that our AI
[17:25] agent now has access to a series of
[17:28] tools it has name and args it's running
[17:31] make deletions here just cutting out
[17:33] this one word it's running another tool
[17:35] call here editing out a few additional
[17:37] words so on and so forth right you can
[17:39] see here it just continues to call make
[17:41] deletion we run over and over and over
[17:43] and over and then once we get to the
[17:44] bottom it now calls an explicit tool
[17:47] instead of returning an empty list it
[17:48] calls complete edit when it's done so if
[17:51] we scre all the way to the bottom we'll
[17:52] get that exact same structure so you can
[17:54] see the scratch packed active memory
[17:56] pattern is going to be really important
[17:57] for rolling out useful person AI
[17:59] assistance it just took out scratch Pad

### Minute 18

[18:01] didn't think scratch Pad was important
[18:02] so it edited that out okay so this is
[18:04] something that will just happen
[18:06] sometimes you know you can see here
[18:07] between the prompt chain and the AI
[18:09] assistant on this singal use case more
[18:11] compute isn't always better and this is
[18:13] a really important thing to call out
[18:14] okay so this is our AI agent and we can
[18:18] of course scale this up let's go ahead
[18:20] and let our 03 mini run the AI agent
[18:24] version and let's go ahead and take a
[18:25] look at the AI agent code okay so we'll
[18:28] go ahead kick this off and let's dive
[18:30] into what the AI agent version of this
[18:32] looks like so same deal on the top level
[18:34] just logging and setup and then this is
[18:36] where all the work happens okay so
[18:38] generate a cut deletions V3 so we'll hop
[18:41] in here and let's open this up couple
[18:43] things are different right away we have
[18:45] an entire class to support our AI agent
[18:48] why is that because we need to better
[18:50] manage State and Tool calls so just like
[18:52] the prompt chain you can see there's our
[18:54] Loop and we'll go into the class in just
[18:55] a moment here but you can see we're
[18:57] setting up the agent as a new class
[18:59] we're passing in our starting State and

### Minute 19

[19:01] then the agent just gets updated with
[19:03] this one call right we just run prompt
[19:05] over and over and then it just returns
[19:06] if it's done right because our agents
[19:09] know what work to do they know when to
[19:10] tell us when they're done it's just a
[19:12] matter of you know letting them Loop
[19:14] letting them do the work and then
[19:15] they'll let us know when they're done
[19:17] right this is kind of an interesting
[19:19] Paradigm Shift when we move into these
[19:20] longer running assistants and these
[19:22] longer running jobs you know a while
[19:24] back we put out this video called the
[19:26] two-way prompting and that video really
[19:28] does set up the future of how we'll be
[19:31] operating with agentic technology it
[19:33] might start out with us prompting them
[19:35] but then they will prompt us right and
[19:37] we just saw this with deep research once
[19:39] you kick it off it asks you questions
[19:42] right and I think we're going to see
[19:43] more of that as these tools progress but
[19:45] I digress let's jump into agent prompt
[19:48] and let me break down this class
[19:50] structure so I'll just collapse and we
[19:51] can look at it at a high level so this
[19:53] is the AI agent version you can see here
[19:54] we have state that we're keeping track
[19:56] of tool calls messages so on so forth we
[19:58] have our individual methods um the most

### Minute 20

[20:01] important thing is here inside the
[20:03] prompt you can see here more
[20:04] instructions I'm listing out the
[20:06] explicit tools it has access to you can
[20:08] see we just have three tools
[20:10] interestingly you know it doesn't take
[20:11] many tools to make your system in AI
[20:14] agent and then we have the state and
[20:17] this is really where the state becomes
[20:20] the environment okay if we open up
[20:22] anthropics building effective agents
[20:24] we're now in this state down here right
[20:26] so these are all different types of
[20:28] agentic workflows we have orchestrators
[20:30] parallelization we've talked about these
[20:32] on the channel before we'll bring them
[20:33] up again when they're relevant but we
[20:35] jumped all the way down here to agents
[20:38] okay and this is what's happening right
[20:40] we are prompting our AI agent it's going
[20:43] to run action and get feedback and the
[20:45] feedback that it's getting from its
[20:47] environment here is the edits that it's
[20:49] making right it's the edits and then the
[20:51] modifications to the original slice to
[20:53] the iteration slice okay so it's not far
[20:56] off at all from the prompt chain right
[20:58] that's something important to mention
[20:59] but this is a different design right

### Minute 21

[21:02] we're not just looping over a structured
[21:03] outputs call we're now saying hey here's
[21:06] a bunch of instructions here's your
[21:07] purpose here's your tools here's your
[21:09] current environment solve the problem so
[21:11] it's it's quite a bit different even
[21:12] though the outcome here as you'll see is
[21:14] going to be relatively similar so now we
[21:16] have our AI agent and the action it
[21:18] takes updates its environment and then
[21:20] once again it tells us when it's done
[21:22] right it has access to this complete
[21:24] edit tool call and it also has a reset
[21:27] to original so if it decides that it's
[21:30] gotten itself into a bad state it can
[21:31] just reset okay and I personally don't
[21:35] care what tools it calls or what order
[21:37] it calls them I just want a good edit
[21:39] right I have an outcome that I'm looking
[21:41] for and then I'm packaging via this
[21:43] prompt context and model I'm packaging
[21:46] the work that I want done the right way
[21:48] and then I'm handing it off to this AI
[21:51] agent okay so that's what this looks
[21:53] like we then have a you know classic
[21:54] open Ai call here we have reasoning
[21:57] effort if we want to go high and then
[21:59] you know just classic stuff here right

### Minute 22

[22:00] we're handling the tokens and making
[22:02] sure that we call the right tool and so
[22:03] this is the AI agent version so let's go
[22:06] ahead and take a look at the output
[22:08] right we just ran that with 03 mini
[22:10] let's see how it performed so you can
[22:11] see it got the answer correct let's see
[22:14] what it did okay so I'll close this 03
[22:17] mini logging session top to bottom make
[22:20] deletion it's going to remove a there's
[22:22] the before and after so you can see it
[22:24] just pulled out that single uh from the
[22:27] beginning right we have one deletion and
[22:29] then if we scroll down here so you can
[22:31] see these are all creating their own
[22:32] prompts and then we have a nicer larger
[22:35] edit I did change it so that it is
[22:37] making a single edit but you can still
[22:39] remove you know chunks of words right
[22:41] chunks of words at a time right you want
[22:42] to be able to remove phrases just like
[22:44] as if I were actually editing this it's
[22:46] important to make the AI agent or the
[22:49] promp chain or your AI tooling mirror
[22:51] the process you would take it's always
[22:53] removing one idea of an edit at a time
[22:57] right one piece of an edit at a time so
[22:59] you can see removed a and then removed

### Minute 23

[23:01] this the scratch Pad we can see here
[23:03] this the scratch Pad act and then we
[23:06] have this right the scratch pack active
[23:08] memory pattern is going to be really
[23:09] important and then you can see look at
[23:11] this once it got to this state it said
[23:14] Perfect Right the tool decided it was
[23:16] done and this is this is really really
[23:18] cool right it's not that different than
[23:20] the prompt chain right but it explicitly
[23:22] here called a different tool there are
[23:24] all the deletions there's the final
[23:26] transcript slice and if we scroll to the
[23:28] bottom B we have the original the final
[23:31] and the target okay so this is correct
[23:33] fantastic so now let's go ahead and look
[23:36] at the
[23:38] Benchmark instead of just a single
[23:41] problem running against one model at a
[23:42] time you know just like in our previous
[23:44] benchmarking video in order to
[23:46] understand and solve problems with
[23:48] general of AI at scale you need to
[23:51] create tests and tests are just another
[23:53] word for eval or benchmarks for this
[23:56] tool I'm starting to build up a suite of
[23:58] bench marks right now I only have 10
[23:59] problems but you can see here I'm taking

### Minute 24

[24:01] it and I'm multiplying it by whatever
[24:03] models I want to run against so this ran
[24:05] in the background let's go ahead and
[24:06] just take a peek at the results from
[24:09] this and let's see if we can answer some
[24:11] of the questions we put forth earlier in
[24:13] the video so if we look at the logging
[24:15] and if we open up logging Benchmark you
[24:18] can see here look at all these
[24:21] executions right you have to keep in
[24:23] mind you know it's two models running
[24:26] against 10 problems for for three
[24:29] different versions We have the prompt
[24:31] promp chain and AI agent that's 3 * 2 *
[24:35] 10 so let's go ahead and just look at
[24:37] the top level Benchmark session so a
[24:38] benchmarking session is just going to
[24:39] contain the kind of high Lev results and
[24:42] so it's going to tell us you know for
[24:44] the problem and for the model what it
[24:46] got right and what it got wrong across
[24:48] the three levels is a prompt chain
[24:50] always better than a prompt is an AI
[24:52] agent always better than a prompt chain
[24:54] let's see if we can find some answers by
[24:56] looking at this Benchmark here we have
[24:58] The Prompt running GPT 40 it got the

### Minute 25

[25:00] problem wrong and you can see here
[25:02] here's a start text here's our Target
[25:04] text it's incorrect it left this our
[25:06] prompt chain has four remaining compute
[25:09] uses so this is set at eight and our V3
[25:12] a agent this is set at 16 we have a
[25:14] little bit more leeway for our a agent
[25:16] because it can reset the entire state if
[25:18] it wants to so we can see here with gbt
[25:21] 40 we have two correct and one wrong now
[25:24] we have that exact same problem running
[25:26] on 03 mini right so these are are both
[25:28] problem zero there's gbt 40 and here's
[25:31] problem zero with O3 mini same deal
[25:34] except O3 mini right a powerful
[25:36] reasoning model gets every single
[25:38] version right so what this you know
[25:39] individual test is telling us is that we
[25:42] don't need any more compute to solve
[25:43] this problem a reasoning model and a
[25:45] prompt is enough okay but that is not
[25:47] always the case as we'll see here as we
[25:49] look at a few more problems right so gpg
[25:51] 40 problem two here's a simple one we're
[25:54] going to go right for we're going to go
[25:56] so how are we're going to Benchmark and
[25:58] then if we scroll here the correct edit

### Minute 26

[26:00] is so how are we going to Benchmark the
[26:02] M4 this is from the M4 benchmarking
[26:04] video if we scroll down here you can see
[26:06] gbg4 in every single variant gets this
[26:09] right so prompt prompt chain a agent
[26:11] it's all good okay 03 mini interestingly
[26:14] the 03 mini gets the individual prompt
[26:17] wrong but you can see here the prompt
[26:19] chain and the AI agent get this problem
[26:21] correct okay so very cool to see that
[26:24] now we're moving to problem two in gbg
[26:26] 40 so we can see here here this problem
[26:29] every single version of gbt 40 got it
[26:32] incorrect right false false false so
[26:35] this is a longer more interesting edit
[26:37] let's see how 03 mini has performed true
[26:40] true and then interestingly false so
[26:42] this is a case where more compute is not
[26:44] better interesting to see that and we
[26:46] can go on down the line here right I'm
[26:48] not going to bore you with every single
[26:49] thing here you can see here that this uh
[26:52] promp chain over edited so it ended up
[26:55] cutting out way too much text right it
[26:57] just kep kept going down this is the you

### Minute 27

[27:00] know one of the problems with just a
[27:01] prompt chain that just runs rampid it
[27:03] just edited everything down okay and it
[27:05] didn't have the tools right didn't have
[27:07] the tools available to reset or fix the
[27:09] edit so if we continue down the line
[27:11] here it's that same problem with O3 mini
[27:13] you can see here prompt was wrong the
[27:16] chain was correct but the AI agent was
[27:19] not correct and so you can see here it
[27:21] looks close right if we pull this text
[27:24] out right and we can just highlight this
[27:25] to see so let's go ahead and open up
[27:27] everyone's favorite local model tool
[27:29] we're going to be using oama and here's
[27:33] where it branched and we're going to be
[27:34] using a tool I'm building up called Beni
[27:36] and what we wanted was and a tool I'm
[27:39] building out called Beni okay so so this
[27:41] is a better failure in the AI agent you
[27:44] know it made a clean edit but it wasn't
[27:46] the exact edit we're looking for and
[27:48] this is where this is where making the
[27:49] prompt more specific to the exact
[27:52] editing decisions and subjective editing
[27:54] tastes it's going to be more and more
[27:56] important okay there are many of these
[27:58] in here that could have been marked

### Minute 28

[28:00] right um specifically with the 03 Mini
[28:02] model that could be marked true could be
[28:04] marked correct but it doesn't exactly
[28:07] hit the target text right this is where
[28:09] something like Leavin distance or some
[28:11] rough string comparison framework can
[28:13] come in okay so we're going to skip
[28:15] through these right there's a lot going
[28:16] on if we just scroll all the way to the
[28:18] bottom we can get some highlevel
[28:20] overarching Benchmark results okay
[28:22] here's everything that was correct and
[28:25] incorrect for a raw prompt we have
[28:29] across all models eight correct and if
[28:31] we break down by model we can see GPT 40
[28:35] got only two correct while 03 mini got
[28:38] eight of these problems correct with
[28:40] just a prompt even though O3 mini is
[28:43] half the price of gbg 40 it uses
[28:47] thinking tokens right it has to reason
[28:49] so the price is still you know something
[28:51] like almost four times as much right so
[28:53] there's just the raw prompt right so we
[28:55] have 8 out of 12 correct now when we
[28:58] move to the prompt chain we see
[28:59] something interesting right you can see

### Minute 29

[29:00] we have one more correct and you can see
[29:03] here that the point is going to 03 many
[29:05] so this is pretty good right so out of
[29:08] 10 problems 03 mini with a prompt chain
[29:11] solved 70% of them correctly okay and
[29:14] it's very likely like I mentioned um
[29:16] there are just some more subjective
[29:18] editing taste decisions in the language
[29:21] of you know what constitutes a correct
[29:23] edit maybe you can give a one or two
[29:25] point discount here if you wanted to
[29:27] okay that's the prompt chain
[29:28] interestingly here we can see that the
[29:29] costs have jumped up quite a bit for gbt
[29:32] 40 okay so for all 10 problems running
[29:35] on the prompt chain you know 30 cents
[29:39] now when we move to the AI agent we see
[29:42] something very interesting right uh the
[29:44] results don't improve okay the results
[29:47] get worse so we have seven correct 13
[29:50] wrong for every AI agent version of this
[29:54] so you can see here gpg 40 has a really
[29:58] hard time operating the AI agent in a

### Minute 30

[30:01] useful way and 03 mini half the time it
[30:03] gets it right half the time it gets it
[30:05] wrong again we can give or take a couple
[30:07] points for editing decisions so you know
[30:10] this leads me to kind of the big
[30:11] takeaway from the work I'm doing here
[30:14] and some you know potential advice and
[30:15] direction that you can take from this
[30:17] for your generative AI
[30:21] work very clearly you likely don't need
[30:25] an AI agent you know whenever there's a
[30:27] new tool that comes out we always want
[30:29] to use the tool and check out the tool
[30:32] and see what we can do with the tool
[30:33] that's fine but when you're really
[30:34] solving problems when you're really in
[30:36] the mindset of value creation you find
[30:38] problems first and then you apply tools
[30:40] to them from your tool belt you don't
[30:42] find tools first and then look for
[30:45] problems to solve it's just the wrong
[30:46] way it's the backward way to do things I
[30:48] was really happy to see that anthropic
[30:51] explicitly mentions this in their
[30:53] documentation it's about building the
[30:55] right systems for your needs start with
[30:58] with prompts then optimize them with

### Minute 31

[31:00] evals and then add multistep agentic
[31:03] systems AKA prompt chains workflows
[31:06] graphs right whatever you want to call
[31:08] it it doesn't matter you only do that
[31:10] when the simpler Solutions fail it looks
[31:13] like for my problem here for the problem
[31:17] space of editing down words in a
[31:21] transcript it looks like what I'm
[31:23] actually looking for here is for my step
[31:25] four right my AI agents they actually
[31:28] don't need to be AI agents they can just
[31:29] be prompt chains these are concrete
[31:32] steps right predefined steps of
[31:35] executing a prompt and then updating
[31:37] some State and then running another
[31:39] prompt it looks like for my you know
[31:40] intelligent editing system I really only
[31:43] need prompt chains and that means that
[31:47] you know inside of this for my
[31:48] intelligence I really only need to you
[31:51] know let my assistant run over and over
[31:53] on a series of steps now of course there
[31:56] are tons of caveat to that I don't
[31:58] really have enough data right this is
[31:59] not significant data to make a complete

### Minute 32

[32:02] decision to completely rule out AI
[32:04] agents obviously you know that's not
[32:05] enough but I think it's just really
[32:07] important to stress that point if a
[32:09] prompt chain can do the job for you use
[32:12] a prompt chain I think to push a little
[32:14] bit further you can experiment with an
[32:16] AI agent and see what that might look
[32:18] like to give your AI agent full autonomy
[32:21] over the system but I think that what
[32:22] we're going to see moving forward is
[32:24] that a lot of the AI agents that are
[32:26] going to to be built underneath the hood
[32:28] they're not actually going to be AI
[32:30] agents they're going to be agentic
[32:31] workflows and more specifically they're
[32:33] going to be uh just prompt chains so
[32:36] just to recap you know there are three
[32:37] levels to this you have just the raw
[32:39] prompt you have what are called
[32:40] workflows or prompt chains or graphs and
[32:44] then you have much more autonomous
[32:46] agents that just have a bunch of tools
[32:48] you give them a problem you give the
[32:49] right context and then you just say go
[32:52] solve my problem you know under the hood
[32:54] I think what's really going to happen is
[32:56] that we're going to see tons and tons of
[32:58] agentic workflows right or put simply

### Minute 33

[33:01] prompt chains right there are many very
[33:03] interesting very powerful ways to use
[33:05] promp chains right and anthropic has
[33:08] detailed a lot of them here we have
[33:09] routing we have parallelization I like
[33:11] to call this the fusion chain we put a
[33:14] video out on this in the past and then
[33:16] we have you know orchestrators there's
[33:17] definitely a good call for using an
[33:19] orchestrator for a cut evaluator
[33:21] Optimizer and then we can go down the
[33:23] line right all the way down to the AI
[33:25] agent and the AI agent workflow is the
[33:26] most interesting because in a certain
[33:28] way it's the most hands-off I think
[33:29] there's a lot of value to be created
[33:31] here but the trick is always
[33:34] benchmarking the performance of your AI
[33:36] agent versus a predefined series of
[33:39] steps that call prompts and tools AKA
[33:43] prompt chains a couple of improvements
[33:45] that I'm thinking about making for aut
[33:47] it's pretty clear that this super harsh
[33:49] yes no response framework that I have
[33:52] here where we just have correct true or
[33:54] false isn't going to be accurate enough
[33:56] to create comprehensive of benchmarks
[33:58] rolling out something like Lin distance

### Minute 34

[34:00] to allow for a 5 to 10 character
[34:02] difference is probably going to be a big
[34:05] win for improving these benchmarks going
[34:07] forward you know another big thing that
[34:09] piggybacks off this is that you know
[34:11] video editing even when you're just
[34:13] editing out transcripts it's a very
[34:16] subjective experience certain editing
[34:18] decisions that a model will make um are
[34:21] totally valid and legit and it might not
[34:24] match up with the exact target even
[34:26] within the five or 10 characters using
[34:28] the 11 scene distance that could
[34:29] actually work so I think a more concrete
[34:31] way to improve that is to add more
[34:33] comprehensive
[34:35] examples into the prompts themselves you
[34:38] know why is that important how can that
[34:40] change the outcome that's super
[34:41] important because you know when we add
[34:43] examples to our prompts to you know give
[34:45] it some idea about what types of edits
[34:47] we wanted to make it'll pick up on the
[34:49] taste of our editing and what words we
[34:51] like to keep in and keep out so on and
[34:52] so forth so more work to be done on that
[34:55] adding an examples tag here is going to
[34:58] be you know really important for making
[34:59] the model more consistent with my

### Minute 35

[35:01] personal editing style so something to
[35:03] think about for your prompt chains and
[35:05] AI agents examples that guide your model
[35:08] in these more creative more subjective
[35:11] decision-making domains is a great way
[35:14] to guide your model and to guide the
[35:17] outcome and of course the best way to do
[35:19] this is benchmarking but also run this
[35:21] against Real data and then in a
[35:23] reinforcement learning type of way take
[35:25] the edits that are working coming out of
[35:27] the model and update the prompt that was
[35:29] feeling that model with those correct
[35:31] edits as examples right so more on that
[35:33] in the future have some pretty
[35:34] interesting ideas around automatic
[35:36] feedback looped prompts to add more Auto
[35:39] self-improving Behavior into the prompt
[35:42] another interesting problem that I'm
[35:43] running into is that idea of not solving
[35:46] the problem at all I think one of the
[35:48] strongest signs of you know a highlevel
[35:51] problem solver a senior level engineer
[35:54] is the ability to look at a problem and
[35:56] decide that it doesn't need to be solved
[35:58] at all right and this is tricky to teach

### Minute 36

[36:01] or explain to an llm because you know
[36:04] these are next token generators not next
[36:06] token not generators for edits I've run
[36:09] into this several times with this tool
[36:11] already where the best thing to do is
[36:13] nothing right the the the slice in a
[36:15] real video will sometimes contain
[36:17] perfect script and nothing needs to be
[36:19] changed so you know I think probably
[36:22] more prompt engineering and explicitly
[36:24] mentioning when things need to be edited
[36:25] will be helpful for solving that problem
[36:28] inside of prompts prompt chains and AI
[36:30] agents so you know the next time you
[36:33] want to solve a problem with generative
[36:36] AI first start with a prompt then move
[36:38] to a prompt chain and only if your
[36:40] prompt chain and your you know graph of
[36:43] steps is not giving you the performance
[36:44] that you need only then should you move
[36:47] to a full-on AI agent that can operate
[36:49] in a domain for you automatically I
[36:52] highly recommend you know throughout
[36:54] that process the more important the
[36:55] problem you're trying to solve the more
[36:57] important it is to set up benchmarks so
[36:59] that you can know for a fact that your

### Minute 37

[37:01] prompt chain is outperforming your
[37:03] prompt and your AI agent is
[37:04] outperforming your prompt chain agents
[37:07] give us the ability to scale our impact
[37:09] even further Beyond we're going to be
[37:11] talking and more importantly building
[37:13] agents on the channel over 2025 like
[37:17] subscribe and comment to stay connected
[37:19] to this content and no matter what stay
[37:21] focused and keep building