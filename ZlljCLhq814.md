# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=ZlljCLhq814
- **Duration:** 23:23
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 4322
- **Transcript Generated:** 2025-03-30 23:49:00

## Transcript


### Minute 0

[00:00] what's up Engineers Andy Dev Dan here
[00:02] it's time we talk about the crucial
[00:04] pieces to creating long running agentic
[00:08] workflows the North Star for this
[00:10] channel is to become agentic engineers
[00:13] Engineers that wield massive amounts of
[00:15] compute that work for us while we sleep
[00:18] if you want to build powerful long
[00:20] running multi-agent systems you need two
[00:23] things a slew of specialized battle
[00:27] tested AI agents that accomplish your
[00:29] domain specific tasks extraordinarily
[00:32] well and a reliable tool calling
[00:34] mechanism to take your prompts your
[00:37] plans and call not just one tool but 5
[00:40] 10 30 plus Tools in one shot with zero
[00:44] mistakes to build powerful agentic
[00:46] workflows you need every single tool
[00:49] call to work in sequence in this video I
[00:52] want to break down which llms and which
[00:55] tool calling mechanisms is best for
[00:57] reliably calling massive long chains of

### Minute 1

[01:00] tool calls doing this will give us a
[01:02] better understanding of how to build
[01:05] long running agentic
[01:07] [Music]
[01:10] systems this is a simple live tool
[01:12] calling prompt benchmarking tool it
[01:14] works like this you select your
[01:16] expectations for tools that you want
[01:18] called you then write a prompt which
[01:20] should trigger each one of your tools
[01:22] and then you see the results drip in one
[01:25] at a time where you can monitor the
[01:27] performance speed and cost let's run
[01:30] this with a simple example and build up
[01:32] to a massive chain of tools if I kick
[01:35] this off
[01:36] here you can see that all of our models
[01:39] are coming in one at a time here so this
[01:42] is really cool if I open up the tool
[01:44] call here everyone of our models called
[01:47] the right tool so this is going to be a
[01:49] comma separated list of ordered tool
[01:52] calls we have several valuable columns
[01:54] including execution time total time cost
[01:57] for the execution total costs we have
[01:59] the this really cool relative cost

### Minute 2

[02:01] column and then of course we have the
[02:03] most important Benchmark here number
[02:05] correct and percentage correct let's run
[02:08] this again so we're just going to run
[02:09] our tool call Prompt once more this
[02:11] prompt is simple it's going to call one
[02:13] tool for each task and you can see here
[02:16] we got an error here claw 3.5 H coup
[02:18] latest returning Json could not complete
[02:21] the result for us so it got this
[02:23] incorrect let's go ahead and select
[02:25] another tool so let's say we want to run
[02:28] a git agent after their
[02:30] now we can add a new task to this tool
[02:32] calling prompt we'll say something like
[02:34] this get commit these changes and now we
[02:37] can rerun our tool call Prompt and we
[02:40] now expect all of our calls to return
[02:43] multiple tool calls right so we're
[02:45] taking a highlevel planning prompt and
[02:48] passing it off to a slew of models and
[02:52] model techniques and the idea here is
[02:54] that we want to understand which model
[02:56] and which techniques give us the best
[02:58] speed cost C and performance when it

### Minute 3

[03:01] comes to calling long chains of tool
[03:03] calls let's keep building this up and
[03:05] see how the models really perform so I'm
[03:07] going to go ahead and kick this off
[03:09] again I always like running these
[03:10] prompts over and over just to see if
[03:13] there's any variance on individual runs
[03:15] LMS are non-deterministic so it's always
[03:18] important to run multiple runs multiple
[03:21] sessions of whatever prompts you're
[03:23] running so that it represents a more
[03:25] true real world scenario we can see here
[03:28] we have a bunch of models getting called
[03:30] with their various LM techniques let's
[03:32] pull over our number correct we can see
[03:35] IOU is not performing very well at all
[03:38] let me pull over percent correct as well
[03:40] if we sort percent correct here most of
[03:42] our models most of our model techniques
[03:43] are having no real problem here so let's
[03:46] go ahead and extend even further we want
[03:48] long chains of tool calls let's add
[03:50] another tool call so let's go ahead and
[03:52] ask for another coder agent and we'll
[03:54] update our prompt we'll say write code
[03:57] to update our utils

### Minute 4

[04:00] py with a new parser for XML and so in
[04:04] these tasks in the prompts I'm really
[04:06] saying anything but it must make enough
[04:08] sense to kick off the tool we want
[04:09] called right so we're saying right code
[04:12] this should be pretty obvious for our
[04:15] llms what we want to happen here right
[04:17] and you can see here we have this Dash
[04:19] Json I'll explain that in a second not
[04:21] every one of these models has tool
[04:23] calling support so we needed to work
[04:24] around it by using structured outputs
[04:26] and Json schemas we have several models
[04:28] kicking off every single one of these
[04:31] tool calls in order this is what we want
[04:33] to see so far it looks like we have a
[04:35] lot of options for running tool calls up
[04:38] to length three let's add a docs agent
[04:41] and now our fourth task must discuss
[04:43] generating documentation right so I'll
[04:45] say create documentation XML parser
[04:48] let's kick this off and let's see our
[04:51] tool calls come in here now in order to
[04:52] be successful our llm and the llm
[04:55] technique we use must call all four of
[04:57] these tools in order we see things

### Minute 5

[05:00] looking pretty great so far we do have
[05:02] the new Gemini experimental model here
[05:04] in Json mode um let's go and look at
[05:06] some of our execution time so far right
[05:08] let's kick this off again and um let's
[05:10] see how things are performing right so
[05:12] we have our relative cost on the right
[05:13] here and we have our individual cost
[05:17] there I want to see the execution time
[05:19] let me kick off another run here so we
[05:21] can get up to 10 okay nice so 10
[05:23] executions let's go ahead and sort by uh
[05:26] execution time so for this individual
[05:28] run we can see here our flash is
[05:31] performing really really well uh Gemini
[05:33] 1.5 flash this is a model that's gone
[05:35] under my radar for quite some time we
[05:37] also have many right below that for
[05:38] Speed we have 40 in Json mode flash Json
[05:42] mode performing pretty well and then
[05:44] things kind of scale up from there right
[05:46] so interestingly here we can see gp24 is
[05:48] not performing well right let's just
[05:49] keep kicking off these prompts let's get
[05:51] some more data you really want tens and
[05:53] hundreds of runs when you're creating
[05:55] these benchmarks and when you're
[05:56] creating your tests and your evals ha
[05:59] cou just really can't pull it together

### Minute 6

[06:01] here this is the old claw 3 H coup it's
[06:04] losing its crap on these tool calls it
[06:06] just can't figure this out I threw this
[06:07] in there just because I want to see how
[06:09] models have improved with the tool
[06:10] calling capabilities I am pretty shocked
[06:12] to see GPT 40 this low but you can see
[06:14] here if we sort by um percent correct we
[06:17] have a great variety of models that are
[06:19] performing and if we look at total time
[06:21] currently the winner here the the big
[06:23] winner frankly is Gemini 1.5 flash
[06:26] version 2 because it's gotten everything
[06:29] correct it's the fastest and it's also
[06:32] the cheapest right we we haven't even
[06:34] cracked uh a tenth of a scent yet not
[06:37] even a half of a tenth of a scent and uh
[06:40] it's it's running every single tool we
[06:42] need for our agentic system perfectly
[06:45] and that's the whole idea here that's
[06:46] the high level idea when you're building
[06:48] these long running agenic systems where
[06:50] you're passing in your own personal plan
[06:52] prompt or a plan prompt that a powerful
[06:56] reasoning model like 01 has
[06:58] automatically created based on some

### Minute 7

[07:00] information you want it to be able to
[07:02] kick off long sequences of tasks so
[07:04] let's keep going I want to get this up
[07:05] to 10 15 plus and see which models are
[07:07] really calling the tools we need when we
[07:10] need them so let's add another we have
[07:11] code g coder docs you can see here we
[07:15] only have three tools obviously in
[07:16] production environments we'll have 10
[07:18] plus tools but three is enough obviously
[07:20] here to Showcase running long sequences
[07:23] in order so let's add another coder
[07:25] agent we'll say update the API for our
[07:28] XML parser let's let's go ah and kick
[07:30] this off so this looks good looks like
[07:32] we had a blip on latest hku and Json mod
[07:35] let's run this again so in previous
[07:37] videos we talked about moving from
[07:39] prompts to AI agents to personal AI
[07:42] assistants all the way to agentic
[07:44] systems we're starting to dip into the
[07:48] agentic 100x improvements we can get but
[07:52] in order to get there we need long
[07:54] chains of tool calls so that we can have
[07:56] this agentic system generate these long
[07:59] planning prompts and then hand them off

### Minute 8

[08:02] to whatever AI agent it needs to to get
[08:05] the job done right and this can also be
[08:06] used in the personal AI assistant level
[08:09] as well but I hope you can see you know
[08:11] why this is so important if you want
[08:13] long running agenting systems you need
[08:15] long reliable tool calls so we're
[08:18] getting up there we have about 14 runs
[08:19] here let's just keep hammering our llms
[08:22] we want to see not just the individual
[08:24] results uh we want to see a you know a
[08:27] set of results over time we want to see
[08:29] who's really really performing over long
[08:32] run the experimental is performing well
[08:34] but we also just have a lot of great
[08:36] models performing really well here one
[08:38] thing I am missing from this Benchmark
[08:40] here obviously you can see these are
[08:42] only the top tier cloud provider models
[08:44] um I don't have any local or llama
[08:47] models that's something we can add in
[08:48] future benchmarks in future videos and
[08:51] you know comment down below you can see
[08:53] we're getting some really interesting
[08:54] results here comment down below what
[08:57] benchmarks and what information you want
[08:59] to see in a live benchmarking tool like

### Minute 9

[09:02] this the ux of benchmarking has a ton of
[09:05] room for improvement let's go ahead and
[09:06] kick this off again in our previous
[09:08] video we benchmarked how models perform
[09:10] against each other in a live
[09:12] autocomplete scenario to test speed cost
[09:14] and performance and that was a great way
[09:17] to test out a small use case across
[09:19] multiple models in a kind of Benchmark
[09:21] that you can feel so we can see a lot of
[09:23] just top performing models here things
[09:25] are going really well let's keep adding
[09:27] our tool calls let's run a git agent and
[09:29] and then let's run another let's run
[09:31] another git agent so this is something
[09:33] that can often confuse models when you
[09:35] run the same tool back to back I'm sure
[09:38] we're going to lose some 100% here let's
[09:40] go ahe and try this out so I'll say uh
[09:41] get commit these changes and then I'll
[09:44] say get checkout a new Branch for a new
[09:47] feature so kick this off and let's see
[09:51] how our llms do here in order for our
[09:55] models to be correct they need to call
[09:57] every one of these tasks in in order so

### Minute 10

[10:00] you can see this long chain of tool
[10:01] calls coming back in the response for
[10:03] some of these models this looks awesome
[10:05] I'm really I'm really happy to see this
[10:06] and uh I got to say once again I'm so
[10:09] impressed with the Gemini 1.5 flash
[10:11] model I think a lot of engineers in
[10:12] general are sleeping on Google uh
[10:14] because they're
[10:15] Google but they're building some really
[10:18] incredible llm technology here and the
[10:21] new experimental model although very
[10:24] slow if we sort by total run time let's
[10:26] sort descending this is the slowest
[10:28] model by far but it's performing quite
[10:30] well here I'm sure it's just not
[10:31] optimized or maybe there's something
[10:33] else going on under the hood maybe it's
[10:34] a more complex model not sure but it is
[10:36] performing well love to see that and for
[10:38] the costs you can see here I just priced
[10:40] it the same as 1.5 Pro um let's go ahead
[10:43] and keep kicking these off and see how
[10:46] things look very nice uh we can see here
[10:49] that 01 mini Json so this is a 01 model
[10:53] where we're asking it to return these
[10:55] tool calls and their respective prompt
[10:57] parameter in order is not too bad it's

### Minute 11

[11:00] gotten too wrong so far across 18
[11:03] executions for the cost of 01 and for
[11:05] the speed of 01 which is you know not
[11:07] the best we can see here further down
[11:09] the list in total time execution we have
[11:11] 40 in Json mode performing at 100% we
[11:15] have 40 mini Json 100% And then flash
[11:18] and flash really the the winner here so
[11:21] far is Flash right there's just there's
[11:23] just no debate about it it's our
[11:24] cheapest model you can see here our
[11:26] relative cost has 1.5 Flash as the
[11:29] cheapest model for the task of calling
[11:32] the right list of tools in sequence so
[11:35] really enjoying seeing that again this
[11:37] is a model that I think most people are
[11:39] sleeping on uh it's so powerful and it's
[11:42] so cheap look at the total cost again
[11:43] not not even a tenth of a scent yet
[11:45] whereas if we look at the top here uh
[11:47] Pro 01 mini right these have all cracked
[11:51] Ascent right we have the latest 3.5 high
[11:53] cou all costing us quite a bit and
[11:56] actually I didn't even realize this the
[11:58] Sonet model is costing us uh 10 cents

### Minute 12

[12:01] here wow yeah let me get the relative
[12:03] cost on this yeah wow Sonet very very
[12:06] expensive and you can see I have Sonet
[12:08] with the function calls and then I have
[12:10] Sonet with just Json response and let me
[12:14] talk about the Json response a little
[12:15] bit more so that makes sense so let me
[12:17] save this and you can see here we have
[12:19] this Json prompt Tab and this is the
[12:22] prompt we're using to format our
[12:25] responses for models that don't have
[12:28] function calling support this is a hack
[12:30] that you may have you know come across
[12:31] and used yourself tool calling really is
[12:34] a list of objects that look like this
[12:36] right what's the tool name and then what
[12:38] are the parameters for us we're just
[12:39] using a single parameter prompt because
[12:42] we're effectively thinking about
[12:43] designing systems we're passing off
[12:45] prompts to uh fine-tuned specialized AI
[12:48] agents so that's the pattern we're using
[12:50] here and then we have the options for
[12:53] our tool name options right and you know
[12:55] there are some tools let's kick off
[12:56] another run there are some llm
[12:59] like gpg 40 Json that can run structured

### Minute 13

[13:02] outputs same with 40 mini but then there
[13:04] are others that um like for instance the
[13:08] anthropic models you just ask for the
[13:10] right Json format and then they return
[13:13] the result right so that's what our Dash
[13:14] Json models are doing here it's either
[13:17] structured outputs or just raw pantic uh
[13:20] Json parsing and I got to say all the
[13:22] models are doing really well at that the
[13:24] question is are they actually returning
[13:27] the right list of tool calls in order
[13:30] right so we can see 40 for whatever
[13:32] reason um is just doing a terrible job
[13:34] it's having a really hard time with this
[13:37] long sequence of tasks so let's go ahead
[13:39] and just keep kicking these off and then
[13:40] let's add some more items here I'm kind
[13:43] of surprised to see let me pull back
[13:45] over this and let me pull back our
[13:48] number correct you know I'm really
[13:50] surprised to see Sonet is actually not
[13:53] doing well here uh down at 64% um so
[13:57] it's not doing well let me sort
[13:58] descending
[13:59] uh but we have a ton of great options

### Minute 14

[14:01] for long chains of tool calls with the
[14:04] Gemini models you know performing here
[14:06] at the top which is really great to see
[14:07] so this is good let's keep pushing this
[14:09] these long running agenting systems must
[14:11] be able to do many many many tasks in
[14:15] sequence so again we're just going to
[14:16] keep pushing let's run a couple doc
[14:19] agents and then let's run a another
[14:23] coder agent the initial documentation
[14:25] Json Parson update this documentation
[14:29] support for yaml and we'll say now
[14:32] Implement now our new Json and yaml
[14:36] parsing features so again we're just
[14:37] kind of saying random tasks here
[14:40] obviously in your real agentic system
[14:42] these will be tasks that correspond to
[14:45] tools you have so I think this looks
[14:47] good 1 through 10 let's go ahead and
[14:48] kick this off and now things are
[14:50] interesting right now we have a tool
[14:53] call expectation of 10 Tools in a row
[14:56] and we need our llms to to give us all
[14:59] the results in order it looks like we've

### Minute 15

[15:03] had some pretty great success here
[15:04] Gemini quite a bit of time here but yeah
[15:06] Gemini so reliable this new experimental
[15:08] model seems really really interesting
[15:11] it's running really slowly as we can see
[15:13] here sorting descending total time sort
[15:15] descending uh it's running extremely
[15:17] slow it's you know some 10 seconds
[15:19] slower than the previous pro version but
[15:22] um it's super accurate so I'm curious to
[15:24] see what's going on here with this new
[15:25] Gemini model we can see results continue
[15:27] to trickle in here let's go ahead and
[15:28] continue
[15:29] so this this Hau model just continuously
[15:32] is spinning out the Run coder agent so
[15:35] gbg4 has just completely given up you
[15:38] can see here it gets kind of close if we
[15:41] go Ahad and scroll here look at all
[15:43] these tool calls look at this massive
[15:45] chain right 10 Tools in a row we can see
[15:48] gb40 gets the second tool wrong so this
[15:51] is the trick right and this is why it's
[15:52] so important we need to get every tool
[15:54] call in order gp40 is having a lot of
[15:57] trouble with that we have Sonic in
[15:59] function calling mode having quite a bit

### Minute 16

[16:01] of trouble and you know that's a kind of
[16:03] an interesting takeaway here if we
[16:06] collapse everything here so we can get
[16:07] the full view it looks like manually
[16:10] building a Json parsing prompt is going
[16:13] to outperform the function calling
[16:16] mechanism for the new Sonet model now
[16:18] that's kind of an interesting thing
[16:20] right because you would expect the
[16:21] models buil-in tool calling capabilities
[16:24] to be more accurate than a Json run
[16:27] right but that's not what we're seeing
[16:28] here it it looks like having a uh Json
[16:31] prompt structured like this is actually
[16:34] better very interesting to see that we
[16:36] have 01 mini running that same Json
[16:38] prompt it's interesting to see that um
[16:39] the performance here isn't a big deal
[16:42] right let's go and pull these columns
[16:44] back over the performance sort by model
[16:47] name here the reasoning models don't
[16:50] always perform better and even in a task
[16:53] like this where you would think it would
[16:54] help to have some reasoning looping
[16:56] Chain of Thought capabilities uh that's
[16:58] actually not the case right a One Mini
[16:59] Json is not performing better than some

### Minute 17

[17:02] other models right we can just keep
[17:03] kicking this off a model probably
[17:05] fractions of the size gb40 mini in with
[17:09] that same prompt is performing uh you
[17:11] know a little bit better right 8% better
[17:13] here across 25 executions it's also
[17:16] doing it uh much faster so let's sort
[17:19] descending here and let's run up to 15
[17:23] tool calls so let's go ahead and add uh
[17:25] several more let's add two coder agents
[17:28] two G agents
[17:29] and then we'll add one document update
[17:32] the Json code update yaml to support
[17:35] yaml and yaml G commit these changes uh
[17:40] get push these changes document Json
[17:44] yaml capabilities okay so now we have a
[17:48] expected tool call list of length 15
[17:51] right we need all 15 of these tools to
[17:53] run in order we have what I like to call
[17:56] a planner prompt and you know the cool
[17:59] thing again just to call this out the

### Minute 18

[18:00] great thing about the planner prompt is
[18:02] that you can have a reasoning model or a
[18:05] a a dedicated agent to generate this
[18:07] prompt for you given some inputs you
[18:09] know as we're thinking about Building
[18:11] agentic Systems you need to think about
[18:13] having an agent do the planning and do
[18:16] the setup work for your smaller
[18:19] specialized agents right and this is
[18:21] what long sequences of tool calls is
[18:22] helping us unlock so we have 15 let's go
[18:25] ahead and execute this and let's see
[18:27] which models can do the job wow I'm I'm
[18:30] so impressed with uh 1.5 flash here it's
[18:33] just such a great model it's performing
[18:35] so well here okay so we're getting all
[18:37] results trickling in and you know again
[18:40] uh we really have to open this up to see
[18:42] how complicated this actually is right
[18:44] you need to run 15 Tools in order based
[18:47] on the content of each task okay so this
[18:51] is not a trivial task and the longer and
[18:54] more complex your agentic workflows
[18:57] become and the more you can plan uh the

### Minute 19

[19:00] more powerful and the more capable
[19:02] they'll become but also the more
[19:03] important it is to have these tool calls
[19:06] run in order top to bottom with the
[19:09] exact order you need let's get this up
[19:11] to 30 executions we can see Sonet 3.5 in
[19:15] Json mode taking a hit there we can see
[19:18] the new Gemini experimental this is
[19:20] going to come in it's just going to take
[19:21] some time yep very nice love to see the
[19:23] 100% success rate here on so many models
[19:26] right because what what does that mean
[19:28] when many models can do a specific job
[19:30] that means you have options and that
[19:32] means there's likely a model here and
[19:34] we've pointed it out several times
[19:35] there's likely a model here that uh is
[19:38] the best option at the best speed at the
[19:40] lowest cost or there's going to be some
[19:42] opportunity for you to have a trade-off
[19:44] right do you want to optimize for Speed
[19:46] or cost in some scenario right this is
[19:49] why benchmarking writing tasks writing
[19:51] evals is so important if you don't know
[19:53] what options are available to you you
[19:55] might be stuck using a tool using a llm
[19:58] using a technique that is just lesser

### Minute 20

[20:01] that is not performing as well as
[20:03] another technique could so it is
[20:05] interesting to see running this manual
[20:07] Json prompting mode is actually quite
[20:09] powerful it allows llms without function
[20:12] calling capabilities to have you know
[20:14] function calling capabilities let's go
[20:15] ahead and run one more and round out
[20:17] here at 30 correct tool calls so so this
[20:23] is really impressive for these models
[20:24] performing at 100% success rate here 30
[20:26] test cases where we have an expected
[20:29] tool call length of 15 it's fairly
[20:32] significant right like this is actual
[20:33] useful information you can pull from a
[20:35] live benchmarking tool like this so
[20:37] again comment down below let me know
[20:40] what other types of benchmarks you want
[20:41] to see in a live interactive fashion
[20:44] where we can dive in and understand
[20:46] performance speed and cost at a more you
[20:49] know intimate uh you know in-depth level
[20:51] so it looks like as you and I are
[20:53] building out personal AI assistant AI
[20:55] tools AI agents and fullon a agentic
[20:59] workflows that are self-operating it

### Minute 21

[21:01] looks like we have quite a few options
[21:03] here right that's what this Benchmark
[21:05] that's what this test is telling us if
[21:06] we sort execution time here 1.5 flash
[21:09] this is a killer model very
[21:11] underappreciated very underhyped and
[21:14] it's performing insanely well we can see
[21:15] the relative cost here flash is the best
[21:18] model for long chains of tool calls in
[21:21] this Benchmark hands down no questions
[21:24] this is running using Gemini's API with
[21:27] their function calling capabilities this
[21:30] is the highest performing function
[21:32] calling llm in this Benchmark this is
[21:35] really incredible it's not using any
[21:36] Json formatting at all we're passing
[21:39] just this prompt in here and you can see
[21:42] it's the fastest on average by almost 20
[21:46] seconds it's the cheapest by at least by
[21:50] uh quite a bit here I haven't even spent
[21:53] a single scent on this and I've used 14
[21:57] cents with 27 % accuracy on claw 3.5

### Minute 22

[22:00] Sonet for Tool calling this is why you
[22:02] Benchmark right everyone you know you
[22:04] might initially think as I did that claw
[22:07] 3.5 Sonet is going to smash tool calling
[22:09] out of the box no 27% only8 correct 14
[22:14] cents down the drain okay this is why we
[22:16] Benchmark this is why we test this is
[22:18] why we dig deeper we are Engineers we
[22:21] don't follow the hype we don't take news
[22:24] at face value we don't take hype at face
[22:26] value we don't care about others
[22:29] opinions that isn't backed by stats data
[22:33] and raw information right if you want to
[22:35] make data driven decisions and get the
[22:37] highest Roi look at the tests look at
[22:40] the evals look at the data and most
[22:42] importantly run your own benchmarks are
[22:45] flawed this Benchmark is flawed we can
[22:47] see here by running tests we understand
[22:51] with prompts we can see I can now make
[22:53] better decisions about how to build
[22:55] multi-agent agentic applications if you
[22:58] enjoy this video and you want to see

### Minute 23

[23:00] more benchmarks like this like drop a
[23:03] comment and subscribe I'm really excited
[23:05] to be wrapping up the AI coding course
[23:08] that's going to ship in December this is
[23:10] going to be a foundational AI coding
[23:12] course that I've been working on all
[23:14] year for you I'm really excited to share
[23:16] that with you stay tuned for that in
[23:18] December stay focused and keep building