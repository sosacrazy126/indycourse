# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=ujnLJru2LIs
- **Duration:** 29:07
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 5333
- **Transcript Generated:** 2025-03-30 23:48:59

## Transcript


### Minute 0

[00:00] 2025 is just a few clicks away AI agents
[00:04] are emerging Next Generation language
[00:07] models are right around the corner and
[00:10] Quinn 2.5 is proving that local models
[00:13] are no longer a Dream It's become
[00:16] absolutely clear to me that your success
[00:19] and My Success hinges on one thing among
[00:23] all the change over the past year one
[00:26] thing has stayed constant the foundation
[00:28] of it all the UN hero that we now take
[00:31] for granted it's the way we talk to
[00:34] information itself I'm of course talking
[00:37] about the prompt at first prompt
[00:40] engineering was a complete joke now
[00:43] prompt engineering is not just a good
[00:46] skill to have it may be the most
[00:48] valuable skill you can develop for 2025
[00:52] and Beyond before we continue this
[00:55] Channel's mission of building living
[00:57] software with Advanced Techniques like

### Minute 1

[01:00] meta prompting let's hit pause for a
[01:02] moment right here in Q4 2024 and take
[01:07] time to review the new fundamental unit
[01:10] of knowledge work the prompt this way
[01:12] we'll set ourselves up to win in 2025
[01:15] with all the advancements right around
[01:18] the corner in this video I'll reveal my
[01:21] four level framework that turns good
[01:24] prompts into great ones and great
[01:26] prompts into reusable assets that scale
[01:29] across your tools and
[01:32] [Music]
[01:34] applications all right so I'm going to
[01:36] open up the terminal move to a temporary
[01:39] directory and crack open cursor create a
[01:42] empty file touch prompt. txt and this
[01:45] will create an empty text file you can
[01:46] see there's nothing else going on in
[01:47] this directory I'll write ping save this
[01:50] file and we're going to run prompts on
[01:51] this file using the llm library by Simon
[01:54] Willison and the olama library link will
[01:57] be in the description for this llm is a
[01:59] tool that let to run prompts right from

### Minute 2

[02:01] your terminal the basics are everything
[02:03] let's start with the level one prompt we
[02:04] can type llm and then direct The Prompt
[02:07] file into this CLI tool and then we'll
[02:10] get a response like this pong how can I
[02:12] assist you today this is all we need to
[02:13] run our prompt on a large language model
[02:16] we can tweak this to get different
[02:18] outputs we can say count to 10 then back
[02:21] to zero and then we can hit up and just
[02:24] rerun our prompt and you can see here of
[02:26] course we're counting up to 10 and back
[02:28] to zero we can make a couple tweaks to
[02:31] the prompt to get different outputs we
[02:32] can say python colon save and then rerun
[02:36] and now we'll get that exact same output
[02:38] in Python we can tweak it again we can
[02:40] say in XML rerun and of course we'll get
[02:44] something like an XML output nice so
[02:46] we're going to get count up countd down
[02:48] so just by adding a few keywords we can
[02:50] change the prompt completely anyone
[02:52] that's still saying prompt engineering
[02:54] isn't a real skill isn't denial they
[02:57] don't know what they're talking about or
[02:58] they just don't know how to prompt

### Minute 3

[03:00] themselves so what about the model we're
[03:02] using using this Library we can type llm
[03:05] models to get a breakdown of all of the
[03:07] models available to us I've installed a
[03:10] couple additional llm plugins you can
[03:12] see I have the Gemini models here I have
[03:15] anthropic and of course we have open AI
[03:17] models as well let's go ahead and run
[03:19] this exact same prompt using the new
[03:21] Gemini experimental I'll just copy this
[03:23] here and we can run this with- m paste
[03:27] the model and then we'll do the exact
[03:29] same thing right I'm going to direct our
[03:31] prompt into this CLI tool okay and now
[03:35] we're getting that output from Gemini
[03:38] experimental and that looks great it's
[03:40] giving us an explanation fantastic so
[03:42] let's go ahead and tweak this prompt a
[03:44] little bit let's say we want to Output a
[03:47] SQL light table user and then we'll give
[03:50] it a pseudo Json format so I'll just say
[03:53] ID email address and is member and now
[03:58] let's go ahead and rerun that and let's
[03:59] let's go ahead and use um let's use a 40

### Minute 4

[04:02] Mini model okay so now we're running GPT
[04:04] 40 mini fantastic let's tweak this
[04:07] prompt a little bit and we'll say
[04:09] exclusively so now we're tuning this ad
[04:12] hoc level one prompt a little bit and
[04:15] we'll hit up and just rerun this on for
[04:17] many and you can see we're exclusively
[04:19] getting the output for this SQL table
[04:22] that looks great we can also run with
[04:25] local model providers so we can use o
[04:27] Lama for this of course and we can just
[04:29] type o Lama run llama
[04:32] 3.2 um and I have the 1B installed and
[04:37] then same thing we can direct the prompt
[04:39] into the tool okay so you can see llama
[04:42] 3.2 1 billion parameter not following
[04:45] the instructions perfectly but this is a
[04:47] small model this is to be expected let's
[04:49] go ahead and run a more powerful model
[04:51] let's run AMA run Quinn
[04:55] 2.5 coder 14b and we'll do the same
[04:59] thing we pass the prompt into the output

### Minute 5

[05:01] and let's see what Quinn gives us here
[05:03] okay so also not perfect but not bad
[05:05] either right we're getting a SQL light
[05:08] database table generated from a simple
[05:11] Json like structure so the great part
[05:14] about using libraries like llm or olama
[05:17] in the terminal is that you have full
[05:19] control over rapid prototyping and
[05:22] experimenting with prompts across models
[05:25] and model providers what does that mean
[05:27] exactly you can see here we're rapidly
[05:29] protyping on several models if I hit up
[05:31] here a couple times we can come in here
[05:33] tweak this and if we wanted to we can
[05:35] run CL 3.5 IU we're on the exact same
[05:38] thing and you can see IOU giving us a
[05:40] super precise output here we can say
[05:43] postgress table instead and rerun it and
[05:47] we'll get a slightly different syntax
[05:48] because now we're requesting a postgress
[05:51] table okay so we're just playing with
[05:53] this level one prompt if we want to we
[05:55] can do something like this right I can
[05:56] say touch um many models. sh and if we

### Minute 6

[06:00] open that up and go back to llm models
[06:03] and just list out all of our models I
[06:05] can come in here and just copy a couple
[06:07] models paste in let's go ahead and grab
[06:10] a couple of open AI models let's grab a
[06:14] couple of clawed models as well and then
[06:17] since we're here in cursor I'm just
[06:18] going to highlight this and run a quick
[06:20] prompt on this and say create lm- M for
[06:25] mini redirect prompt.
[06:28] txt place- M with each model Alias okay
[06:33] so I'm just running an ad hoc AI coding
[06:35] prompt here to automatically build a run
[06:38] command for all of these models that
[06:41] we're running using the llm library by
[06:44] Simon Willison right so I'm just going
[06:45] to write all these out and let's get rid
[06:47] of a couple here I don't really need to
[06:48] run all these models that looks good and
[06:51] now we can do this right now we can just
[06:53] say s many models and let this kick off
[06:56] right so now our prompt is going to run
[06:59] over over each one of these models and

### Minute 7

[07:01] give us the output so you can see we're
[07:03] getting a lot of great consistent
[07:04] outputs and this is the power of really
[07:07] having control over your prompt and
[07:10] having great tools like olama and llm to
[07:14] work with you want to control your
[07:16] prompts you want to be working with them
[07:17] in a quick way you want to be
[07:19] prototyping with them and you want to be
[07:21] understanding the outputs of individual
[07:24] models right next to other models right
[07:27] whenever new models come out or whenever
[07:28] I have an idea for a prompt this is how
[07:31] I like to explore create a simple prompt
[07:33] file come in here with a couple CLI
[07:36] tools like llm or ol Lama dig in
[07:38] experiment and really understand the
[07:40] most important piece of the generative
[07:43] AI Age The Prompt all right so if you're
[07:46] enjoying this so far and you're learning
[07:47] something new hit the like smash the sub
[07:50] and let's move on to level two
[07:54] [Music]
[07:56] prompts a level two prompt is a reusable
[07:59] prompt that you can use to solve

### Minute 8

[08:01] welldefined simple problems the big
[08:04] difference is that you specify
[08:06] additional information up front that you
[08:08] change over time as you improve your
[08:10] prompt and learn more about the problem
[08:12] you're trying to solve you do this by
[08:14] setting and creating static variables
[08:17] inside your prompt let me show you
[08:19] exactly what that means so I'll clear
[08:21] with the prompt and I'll use one of my
[08:23] code Snippets this code snippet is
[08:24] prefixed with px1 and if I hit tab here
[08:28] on this code snippet you can see we now
[08:30] have this XML prompt structure let's
[08:33] take our previous Json to SQL prompt and
[08:36] upgrade it to a level two prompt where
[08:38] it's much more reusable adding structure
[08:41] to your prompt like this generally
[08:43] increases performance a link a video
[08:46] where we discuss the best prompt format
[08:48] in the description the tldr there is XML
[08:52] gives you top performance especially as
[08:54] your prompts become more complex why is
[08:57] this it's because large language models
[08:58] were trained on the web and the web is

### Minute 9

[09:00] full of HTML and HTML is a subset of XML
[09:05] so let's fill out this prompt and start
[09:07] with the purpose let's start by saying
[09:09] convert the typescript interface so
[09:11] we're going to expand this a little bit
[09:13] into a SQL table okay so that is the
[09:17] purpose of this prompt now we've clearly
[09:19] defined this let's go ahead and add
[09:21] instructions on exactly how to
[09:23] accomplish this goal use postgress
[09:25] dialect respond only with a table
[09:28] definition
[09:29] and we'll just keep it to two
[09:31] instructions for now right so we have a
[09:33] list of instructions here and the
[09:34] important part here is that we can
[09:36] whenever we need to come in here and
[09:39] just add uh I think I have xxi we can
[09:42] come in here and just add instructions
[09:44] as we need to right so you can come in
[09:46] here and Define as many specific rules
[09:48] and situations to solve the problem by
[09:50] adding additional instructions just like
[09:53] this right so we're going to start with
[09:54] just two instructions and then we're
[09:56] going to have one kind of primary
[09:58] variable here inter face block what

### Minute 10

[10:00] we're going to do here is save this
[10:03] prompt right here right now this prompt
[10:05] is now reusable we are not just writing
[10:08] ad hoc natural language and handing it
[10:10] off to an llm we're defining a solution
[10:13] to a problem in a reusable way now
[10:15] whenever we need to right so you know we
[10:18] can come in here and just say CP prompt
[10:20] and this is going to be TS
[10:22] tosql
[10:24] table.xml now whenever we want to we can
[10:26] open up this file and copy copy this
[10:30] let's go ahead and replace our prompt as
[10:32] if we were you know starting up a new
[10:34] prompting session and now we can execute
[10:37] this prompt so let's come in here and
[10:39] we'll say
[10:40] interface users ID string paste that a
[10:44] couple times and then tweak it right so
[10:47] email created and then we'll say is
[10:51] member okay and this will be a bing
[10:54] we'll have a number here let's go ahead
[10:56] and run this with uh 40 so we can get
[10:59] that 40 command fired back up and you

### Minute 11

[11:01] can see we got that output perfectly
[11:04] right only respond with table definition
[11:07] we can tweak this so say we wanted to
[11:08] name it something else um say this is uh
[11:12] Avatar right and we also have image
[11:15] right we just tweak The Prompt a little
[11:16] bit fire it back off and what do you
[11:18] know our prompt solves the same type of
[11:21] problem in many different ways thanks to
[11:24] our static variable here so why is it a
[11:27] static variable as we'll see with level
[11:28] four prompts this can be updated
[11:31] automatically with the help of code
[11:33] we'll get to that in a second and we
[11:35] need to properly spell interface perfect
[11:37] so this is great right we can run this
[11:39] with any model we want to so we can hop
[11:41] back into our o Lama and run this with
[11:43] Quinn and you can see something
[11:44] interesting here remember before Quinn
[11:46] actually bombed on our previous ad hoc
[11:49] prompt when we were just running at ad
[11:51] hoc with the exclusive you know the
[11:53] exclusive language and just the kind of
[11:55] single line but in our XML format it
[11:57] created the output we wanted perfectly
[11:59] for us right so just a kind of an

### Minute 12

[12:01] interesting thing to note here as we
[12:03] move through the levels of the prompt
[12:05] you're going to see lower tier local
[12:07] models perform better and you're going
[12:08] to see your top higher tier models right
[12:11] your sonnets your Gemini Pros your
[12:13] reasoning models 01 you're going to see
[12:16] those perform even better than they were
[12:17] before this structure really pays off
[12:20] definitely spend some time again I'm
[12:21] going to link that video in the
[12:22] description spend some time to really
[12:25] dial in your prompts and your prompting
[12:27] structures okay so another incredible
[12:29] thing about creating more reusable
[12:32] prompts like this um we can come in here
[12:34] and add I'll say xxi
[12:37] instruction and now we can just tweak
[12:39] this for instance let's say also respond
[12:41] with create update select and delete
[12:46] statements for this table so say you
[12:48] just wanted to you know get a head start
[12:50] on I don't know creating some test data
[12:52] or mock data or writing up a bunch of
[12:55] queries that allow you to get a head
[12:57] start on working with this table right
[12:59] you could come in here add a single

### Minute 13

[13:00] instruction and then rerun let's go
[13:02] ahead and give this to Quinn and let's
[13:04] see Quinn get to work so you can see
[13:06] here we have the create table statement
[13:08] we have the insert now we're getting the
[13:11] update and now we're getting the select
[13:13] and the delete just by adding one line
[13:15] we now have this great reusable prompt
[13:18] that we can expand and capabilities as
[13:20] we're working through the use case and
[13:23] the domain problem set that we're aiming
[13:25] to solve okay so level two prompts
[13:27] really powerful you can see where this
[13:29] is going and I hope you can see why it's
[13:31] so important to not just run random
[13:34] prompts into you know chat gbt CLA and
[13:36] Gemini that's great that's powerful it's
[13:39] not like one level is better than the
[13:40] other but as you move up these levels
[13:43] you're going to be able to do more and
[13:46] just so it's super clear you know you
[13:47] can take this prompt and fire it off
[13:50] into uh chat GPT and you can also fire
[13:53] it off into claw right and they're going
[13:55] to give you a great high quality answer
[13:58] uh just as before right we can even go
[13:59] to Gemini put this out here and you can

### Minute 14

[14:02] see it's giving us uh you know
[14:04] legitimate responses we have that here
[14:07] we have Clause response that looks great
[14:09] and it looks like chat GPT is giving us
[14:12] two versions this looks great one is
[14:14] templated one is full out so these
[14:16] prompts work in any chat interface
[14:19] talking to any model and level one
[14:22] prompts are just as important as 2 3 and
[14:25] four you're going to want to be using
[14:27] every one of these levels but you want
[14:29] to understand what level you're at and
[14:31] when you need to bump up to the next
[14:33] level So speaking of bumping up let's go
[14:35] ahead and move on to level three
[14:38] [Music]
[14:41] prompts level three prompts continue the
[14:43] trend of reusability through prompt
[14:46] templating but as an essential element
[14:49] you've definitely heard of by now
[14:51] examples so I'm going to go aead and
[14:52] just clear this out let's create a level
[14:54] three prompt for a classic LM use case
[14:57] summarizing content we're going to add a
[14:59] spicy take to it you can use examples to

### Minute 15

[15:02] guide the output you're looking for
[15:04] let's go ahead and write a prompt I'm
[15:05] going to run px2 so I'm going to create
[15:07] two additional blocks and let's just
[15:09] walk through this so I'll say summarize
[15:12] the given content based on the
[15:16] instructions and example output okay so
[15:19] I'm going to tab a couple times here
[15:21] there's going to be our example output
[15:23] and then we're going to have our content
[15:24] down here so we can go ahead and create
[15:26] a placeholder here output in markdown
[15:28] format so we're just walking through our
[15:30] instructions for the prompt we're
[15:32] telling the llm how we want it to act
[15:34] summarize into four
[15:37] sections um high level summary let's do
[15:42] main
[15:43] points
[15:45] sentiment three hot takes biased
[15:49] toward the author and three hot takes
[15:53] biased against the author right just so
[15:56] we can create some diversity of thought
[15:58] there and then we're going to say uh

### Minute 16

[16:00] write the summary in the same format as
[16:03] the example output so this is super
[16:06] important you want to be using a
[16:08] consistent prompt format for another
[16:11] really important reason you can see here
[16:12] we have example output listed four times
[16:16] in total right two times as a reference
[16:18] and the last time as the actual
[16:21] reference point so this is really
[16:22] important because when you have sections
[16:24] like this your llm knows where to look
[16:27] right it creates structure for for the
[16:29] llm you can see we reference
[16:31] instructions right here and you know
[16:34] again we have this referencing
[16:35] capability our llm is now you know
[16:37] reading this top to bottom understanding
[16:40] everything we wanted to do because we're
[16:42] referencing other sections inside of the
[16:44] prompt okay so this is good let's go
[16:46] ahead and create our example output I'm
[16:48] just going to walk through the sections
[16:49] and I think we actually have uh four
[16:51] sections here right uh who cares let's
[16:53] walk through them highle summary and let
[16:55] me turn on cursor tab here for some
[16:57] autoc completion help I'll type dot dot
[16:59] dot and then it should be auto complete

### Minute 17

[17:01] for me after this perfect perfect and
[17:05] then let's walk through the hot takes
[17:06] exactly okay and I actually want to add
[17:09] Title Here yep
[17:10] exactly and then I want double hashtags
[17:14] here and you know I'm just walking
[17:16] through creating this format there we go
[17:18] shout out to the cursor Bros for
[17:20] creating a great tabbing experience okay
[17:23] we have this great prompt we don't have
[17:25] any content yet because right now what
[17:28] we have is a prompt template let's go
[17:30] ahead and copy our template into a file
[17:32] CP prompt and we'll call this uh spicy
[17:36] summarize okay we have a couple prompts
[17:39] and actually we want this to be um an
[17:40] XML file so I'll just say CP
[17:44] spicy and I'll change that to XML okay
[17:47] great so now we have this XML file now
[17:50] whenever you need to you can come into
[17:51] your personal prompt Library copy this
[17:54] out paste it into a prompt and then
[17:57] actually fill in some content so so I'm
[17:59] going to go ahead and pull in this blog

### Minute 18

[18:01] post from Simon Willison shout out Simon
[18:04] Willison absolutely legendary engineer
[18:06] and we're just going to copy this whole
[18:07] thing and use this as our content
[18:09] normally I would use a CLI tool for this
[18:11] but it's short enough that we can just
[18:13] copy and paste in to our content let's
[18:17] clear the output and let's run our spicy
[18:20] summarization prompt here right so we'll
[18:23] go ahead and say let's see who do we
[18:24] want to run here let's go ahead and give
[18:25] uh the new experimental a shot and let's
[18:27] fire this off so you can see here we
[18:29] have that title we have our highle
[18:32] summary and now we're getting our main
[18:34] points right just as we specified there
[18:36] are main points right there it's giving
[18:38] us a clear sentiment and now we're
[18:40] getting our hot takes biased toward and
[18:43] biased against the author okay so if we
[18:46] copy these out here open up a new file
[18:49] and if we open up the preview here we
[18:51] can walk through this in a nice
[18:53] formatted markdown document here right
[18:55] this is great right we now have this
[18:57] kind of clean write up of this blog uh
[18:59] we can look at the main points here

### Minute 19

[19:01] sentiment Quin 2.5 coder Game Changer
[19:04] local coding powerful running locally no
[19:06] dependencies new era where AI tools more
[19:09] accessible 100% And then you know I
[19:12] think this is always great to see
[19:13] whatever information sources you're
[19:15] getting you want to have the opposite
[19:16] take as well right benchmarks are
[19:18] promising but need further validation
[19:20] OKAY model performance good lags behind
[19:22] top tier also true uh huge resource
[19:25] requirements also true right so it's
[19:27] nice to have this kind of balanced take
[19:28] and now we have a prompt that allows us
[19:31] to you know very quickly very rapidly um
[19:34] you know create summaries for us right
[19:37] and again you can always take this
[19:38] prompt and you know you don't have to
[19:40] use a tool like this right you don't
[19:42] have to use llm or AMA you can take it
[19:45] and throw it into whatever your favorite
[19:47] uh chat interface is you know always
[19:49] keep in mind I think it's really
[19:50] important to have a prompt library and
[19:51] you want to have the capabilities
[19:53] especially as an engineer to be able to
[19:55] run these prompts in a fast ad hoc way
[19:58] and we want to remember we have this

### Minute 20

[20:00] mini models shell script that we quickly
[20:02] created um we can just fire this off
[20:05] against our new uh prompt here so we can
[20:08] run many and just have this give us uh
[20:11] multiple takes of our summary for this
[20:14] blog right kind of interesting to see
[20:16] I'll I'll let uh two fire off here I
[20:18] want to see 1.5 flash spit this out
[20:21] super quickly here there we go love to
[20:22] see that speed yep yep yep very nice and
[20:25] then it's going to hit Pro two which is
[20:27] probably going to be the same as latest
[20:29] and we'll just stop it there right we
[20:30] don't actually need to walk through
[20:31] every model so really cool stuff right
[20:34] this is our level three prompt and I
[20:35] hope you can see why this is
[20:37] gamechanging the level three prompts are
[20:39] defined by having concrete examples that
[20:42] steer the output if we remove the
[20:44] example what we have here is a great
[20:47] level two prompt we don't need a
[20:49] specific output so it's just kind of a
[20:51] you know highly defined well structured
[20:54] prompt that solves a specific problem
[20:56] well we can hop into this prompt replace
[20:58] the content and get a nice dynamic range

### Minute 21

[21:01] of output but if we need to go that
[21:03] extra level and we're looking for
[21:05] information to be in a specific form
[21:07] which as Engineers as product Builders
[21:09] we often are right we're often tweaking
[21:12] modifying and reformatting information
[21:15] into a new package you'll often times
[21:18] want example outputs right and just a
[21:21] list of outputs that show exactly how
[21:24] you want your model to respond one more
[21:26] cool thing here I want to show you that
[21:28] you do with CLI tools like this if you
[21:31] want to you can run something like this
[21:33] we can say um lm- M and I want to run
[21:37] Gemini flash actually let me see the
[21:40] models again I forget what this model's
[21:41] called there we go yeah I want to run
[21:43] Flash 2 this is one of my new favorite
[21:46] models then we can run llmm flash2 and
[21:51] direct our prompt into the file let me
[21:53] go ahead and paste that back in then we
[21:55] can direct the output right to a file so
[21:58] we don't need this information in our

### Minute 22

[22:00] terminal usually what we want to do is
[22:02] act on this information right so we can
[22:03] sore this directly to a file uh using
[22:06] the greater than
[22:07] when uh is awesome and I always like to
[22:11] add the model so we're going to say G
[22:13] flash2 this is going to be a markdown
[22:16] file okay so we're going to let Gemini
[22:17] flash just blast through this and now if
[22:20] we open up our files we'll see that
[22:22] right here right and of course we can
[22:24] see the preview and once again we have a
[22:27] solid breakdown right this is a
[22:28] fantastic blog post by the way um this
[22:31] is Simon Willison writing a note on
[22:34] Paul's aers Benchmark talking about you
[22:37] know AI cing benchmarks really really
[22:38] great stuff here I was super happy to
[22:40] read through this and then he goes on to
[22:43] you know talk about the mlx version
[22:45] anyway great blog post I'll link this
[22:46] below let's move on to level four
[22:49] [Music]
[22:52] prompts as a level four prompt we would
[22:54] basically just replace this with content
[22:57] and if you've built any llm based tool

### Minute 23

[23:00] or application you already know where
[23:02] this is going right and you know why
[23:04] this is so important uh that this is it
[23:06] this is the difference between a level
[23:08] three and a level four prompt now this
[23:09] prompt is infinitely scalable right
[23:11] we're no longer ad hoc coming in and
[23:14] updating our prompts which don't get me
[23:16] wrong that's a very useful practice it's
[23:18] very quick but this lets us scale our
[23:20] prompt into code into production this
[23:23] allows us to create Dynamic variables
[23:26] and allows us to create prompts that we
[23:28] can up update on the Fly we can add as
[23:30] many variables here as we need right
[23:33] based on whatever problem we're trying
[23:34] to solve this is a real prompt that I
[23:36] use to generate YouTube video chapters
[23:40] so you can see here we have a dense
[23:42] purpose have a whole set of instructions
[23:45] here that Define how to solve this
[23:47] problem and then we walk through several
[23:50] examples let me change the uh language
[23:52] mode here our XML mode okay you can see
[23:54] we have several examples so not just one
[23:57] example but we have three examples of

### Minute 24

[24:00] how we want the YouTube chapters to look
[24:03] like and if you you know of course click
[24:04] into a description of a YouTube video
[24:06] with chapters you'll see this exactly so
[24:08] this is just a really Hands-On example
[24:10] of using a prompt to solve a real
[24:12] problem we have examples showing the
[24:14] exact output and then down here at the
[24:16] bottom we have two Dynamic variables and
[24:20] if we search this references to this
[24:23] right and we have references to this as
[24:26] well right so we have our SEO keyword
[24:28] that we want to hit in our chapters and
[24:30] then we have the transcript with
[24:33] timestamps every single generative AI
[24:36] application that is not a chatbot is
[24:38] effectively a L4 prompt it's a level
[24:41] four prompt a prompt that has a specific
[24:44] purpose it has a set of you know static
[24:47] variables a set of static instructions
[24:50] that they update to improve the prompt
[24:53] but are not usually updated they have a
[24:55] set of examples to guide the output of
[24:58] the llm and then lastly and most

### Minute 25

[25:00] importantly they have Dynamic variables
[25:03] making the prompt infinitely scalable if
[25:05] you're using uh AER cursor wind Surfer
[25:09] and really just any non chatbot tool
[25:12] it's effectively a level four prompt
[25:14] right that brings us full circle like
[25:16] everything that's happening right now in
[25:18] the generative AI age all these brand
[25:21] new tools and ideas and applications
[25:23] it's all just prompts right it's all
[25:26] prompts that you can execute with
[25:28] something as simple as the llm library
[25:31] right llm ping this is all it is and you
[25:35] know this is why I ditched autogen this
[25:37] is why I ditched Lang chain I ditched
[25:39] all of these kind of uh premature
[25:41] abstracting tools it's been over a year
[25:43] since I've you know ditch these tools
[25:45] and it's for this reason the prompt is
[25:48] the new fundamental unit of knowledge
[25:50] work I've said that on the channel
[25:51] before and I'm going to keep saying it
[25:53] because it is so important that you stay
[25:55] close to the metal and master the
[25:58] currency of the generative AI age right

### Minute 26

[26:00] the the unit of intelligence right it's
[26:03] the tokens that build the prompt and the
[26:06] prompt is what gives you the
[26:08] extraordinary abilities to modify create
[26:11] update and delete information at
[26:14] incredible rates everything is about the
[26:17] prompt great you have a prompt now it's
[26:19] time to build a unique tool that allows
[26:22] you to use and tap into your prompt
[26:25] libraries and all of your prompt
[26:26] templates like this that you've built up
[26:29] right this is something that we've
[26:30] covered on the channel I have this tool
[26:32] if I type PFS it automatically opens up
[26:34] for me and this is my prompt Library if
[26:37] we search and we select a couple of
[26:39] models I like to use 01 mini here and of
[26:43] course Sonet and Flash Just For Speed
[26:46] and then if we hit submit you can see we
[26:48] have text areas for those two variables
[26:52] you can see here we have the selected
[26:53] prompt click to show you can see that
[26:55] exact prompt we were just looking at
[26:57] clean EX ml format ready to go ready to

### Minute 27

[27:00] get their Dynamic variables replaced in
[27:03] this simple prompt Library this is using
[27:06] a tool we've covered on the channel
[27:08] called Maro I'll go ahead and Link that
[27:10] video in the description where we built
[27:12] our own personal prompt Library this is
[27:14] going to be a really important trend for
[27:16] us moving forward you want to be able to
[27:19] tap into your prompts to tap into the
[27:21] intelligence of the llms as quickly as
[27:24] you possibly can so I'm not going to run
[27:26] this go ahead and check out that video
[27:27] if you're interested to see see where
[27:28] this is going generative AI enables us
[27:31] to solve a massive array of problems
[27:34] faster than ever before the question is
[27:37] do you have the AI tooling and more
[27:40] importantly the right prompt to solve
[27:43] the problem after you build the prompt
[27:45] it's time to scale It Up by moving it
[27:47] through the levels of prompts levels 1 2
[27:49] 3 and 4 so that you can scale it up and
[27:52] put it inside a tool or application that
[27:55] solves a specific problem for you
[27:58] very well after you take your prompt and

### Minute 28

[28:00] you put it inside a piece of code that
[28:03] solves a specific problem very well
[28:05] you've built the key piece of your AI
[28:08] agent let me know in the comments what
[28:10] you think about this four-level prompt
[28:13] framework I've personally use it to
[28:15] create hundreds of prompts across
[28:17] several domains we have exciting videos
[28:19] coming up on the channel to wrap up 2024
[28:22] including meta prompting and our 2025
[28:25] predictions video I'll make predictions
[28:27] on what I think will happen in 2025 and
[28:29] how I'm going to prepare for it we
[28:31] touched on this a little bit in a video
[28:33] I did a couple weeks ago I'll link that
[28:35] as well we're also going to take the
[28:36] time to recap on my 2024 predictions so
[28:39] that's going to be an interesting one
[28:40] we're of course going to cover the
[28:42] release of 01 Opus 3.5 and the new
[28:45] Gemini model that are all set up to be
[28:47] released in the next month or so we're
[28:50] going to be building our own custom AI
[28:52] coding benchmarks and of course as I've
[28:54] mentioned the foundational AI coding
[28:56] course is coming in De December like
[28:59] subscribe drop a comment you don't want

### Minute 29

[29:01] to miss what's coming next stay focused
[29:03] and keep building