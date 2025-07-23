# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=YoeNwp9je6E
- **Duration:** 16:21
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 3265
- **Transcript Generated:** 2025-03-30 23:48:57

## Transcript


### Minute 0

[00:00] llama 3 models were good quinnn 2.5
[00:02] models have been amazing and alib Baba's
[00:05] new qwq also known as Quinn with
[00:08] questions or as I like to call it qdub
[00:11] is proving to be quite incredible
[00:13] because it gives you reasoning
[00:15] capabilities on your device this is the
[00:18] first local reasoning model that really
[00:21] caught my attention but it's not for the
[00:22] reason you think and let's be real here
[00:24] this model although impressive has flaws
[00:26] it can consume quite a ton of time due
[00:28] to its excessive Loop it randomly will
[00:31] spit out Chinese and its greatest
[00:33] Advantage The Chain of Thought Loop also
[00:36] makes it effectively useless since the
[00:38] outputs contain its internal thoughts in
[00:41] this video I want to share a couple
[00:42] ideas with you surrounding prompt
[00:44] chaining we're going to look at a two
[00:46] model prompt chain pattern where you use
[00:48] a Reasoner to generate the source of the
[00:50] output and then you use a highquality
[00:53] base model to extract the outputs by
[00:55] doing this we make qdb instantly useful
[00:58] I've been really impressed with this
[00:59] model it is hard to use so let's dig in

### Minute 1

[01:01] let's figure out how we can get value
[01:03] from powerful local reasoning models not
[01:06] tomorrow not next week not when the next
[01:08] model drops but
[01:09] [Music]
[01:12] today so for our generative AI stack
[01:15] we're going to be using qwq a Quinn 2.5
[01:19] model 01 mini 40 oama and llm libraries
[01:23] to run our prompt so here's the setup
[01:26] commands everything we're going to look
[01:27] at in the video is going to be linked in
[01:28] the description for you and a gist let's
[01:30] just go ahead and do some quick recap so
[01:33] we can run models like this I can copy
[01:35] this command and just run a Quinn model
[01:38] right out of AMA so we're all familiar
[01:40] with this AMA super powerful we're just
[01:42] passing in the simple pain command we
[01:44] can also run this with the brand new Q
[01:47] dub model and it's going to give us
[01:49] something similar there's not a lot for
[01:50] it to think about here so thankfully we
[01:52] don't get a super long Loop we just get
[01:54] the response pong and of course we can
[01:57] run the llm library and we'll get a

### Minute 2

[02:00] simple pong response from the 01 Mini
[02:03] model as well running the qwq model is
[02:05] really fantastic it's really powerful I
[02:07] think it's a fantastic model for
[02:10] planning designing Building architecture
[02:12] ideation and content generation the big
[02:15] problem with this model it's going to
[02:16] take quite a bit of time and the output
[02:19] of the model is going to be entangled
[02:21] with the thoughts so let me show a
[02:23] concrete example of what I mean by that
[02:24] exactly here we'll say code python CSV
[02:28] to DB we'll pass in a CSV path as the
[02:32] parameter and then we'll expect back a
[02:35] string let's see what Quin with
[02:36] questions does okay so first off you can
[02:38] see one of the issues with the model is
[02:41] that sometimes it just spits out Chinese
[02:43] so I'm going to break it here right away
[02:45] and prefix it with English and let's see
[02:48] if this helps here right so I'm going to
[02:49] fire it off one once again there we go
[02:51] so now we're getting the response back
[02:53] in English so it's walking through
[02:54] exactly how it would create this
[02:56] function so in this very kind of
[02:58] condensed prompt you see we're getting a
[02:59] a lot of information here right it's

### Minute 3

[03:02] really breaking things down and if we
[03:04] were to open up another terminal window
[03:06] here and fire off this goad and fire off
[03:08] the same prompt with a 01 mini call and
[03:12] just pass this in here right if we were
[03:14] to run that same thing we know that 0
[03:16] mini hides its thought process so 01
[03:19] mini is not going to show us the details
[03:22] it's just going to print out exactly
[03:24] what we are looking for so if we scroll
[03:26] up we can see the final output here from
[03:29] the o Mini model of course it's super
[03:31] fast it's running on open AI hyperfast
[03:33] servers while qwq or qdb is running
[03:36] right on my MacBook M2 Pro you can see
[03:38] here it's still going it's still
[03:40] spinning this is taking a crap ton of
[03:43] time and I'm just going to cut it off
[03:44] there right it takes a ton of time to
[03:47] run this model so as the Quinn team
[03:49] mentioned this model can get caught in
[03:51] recursive Loops maybe we were in one
[03:54] there it's hard to be sure so already
[03:56] when we compare this to 01 mini it's not
[03:58] really a fair comparison ubb is not

### Minute 4

[04:01] really that effective you can't really
[04:04] use this model out of the box so how do
[04:06] we resolve this issue of qwq outputting
[04:09] a ton of thought what we really want to
[04:11] do is extract its final
[04:14] [Music]
[04:17] response so what we can do is use a
[04:20] prompt chain and let's go ahead and just
[04:22] pull out an example here right this is a
[04:24] simple script that we've created you can
[04:26] run using bun or Python's UV and if we
[04:30] open our file explorer we can see two
[04:32] files chain. py and chain. TS let's look
[04:35] at the typescript version we can see we
[04:37] have read and replace and we have prompt
[04:39] chain so let's open up uh prompt simple
[04:43] and you can see we have a really really
[04:45] simple XML prompt here and we can run
[04:48] this with this command here let's bring
[04:50] this to a new file so we're going to run
[04:52] Bun Run chain we're going to pass in the
[04:55] original input so this is going to be
[04:57] the first value of this we want to use
[04:59] the prompts simple. txt file and then

### Minute 5

[05:01] we're going to use the olama Quin 2.5
[05:04] coder model we can just go and F this
[05:06] off it'll make tons of sense once I run
[05:07] this you can see we have an output and
[05:09] you can see what's happening here right
[05:10] our input is getting replaced with our
[05:13] start value okay start value with bun is
[05:17] the first input and it's replacing this
[05:19] template right in our previous video we
[05:21] talked about the four levels of the
[05:22] prompt from level one to level four
[05:24] definitely check that out to get a good
[05:26] understanding of how you can write high
[05:28] quality prompts here we have a super
[05:30] simple version of a prompt where we have
[05:32] a purpose and a dynamic variable so we
[05:35] can do something interesting with this
[05:37] simple script if we hop back to chain.
[05:40] TS or chain. py you'll notice something
[05:43] interesting here we're just looping
[05:44] through list of prompts and we're also
[05:46] looping through a list of models and
[05:49] then in this prom chain function if we
[05:51] see a model that's prefixed with AMA we
[05:53] go ahead and run the olama command if
[05:56] it's prefix with llm We Run The CLI l
[05:59] Lim man and this allows us to take the

### Minute 6

[06:02] output from a prompt and use it as the
[06:04] input to another prompt we've done a
[06:06] couple videos on prompt training in the
[06:08] past this is a super powerful pattern
[06:10] that doesn't get talked about a lot you
[06:12] can use this to compensate and
[06:15] strengthen model abilities by taking one
[06:17] prompt and using the output of a prompt
[06:20] as the input to another prompt so you
[06:22] can check out this code link of course
[06:23] is going to be in the description if you
[06:25] want to understand how prompt chaining
[06:26] works at a deeper level but basically we
[06:29] have this simple script here both a
[06:30] typescript and a python version that
[06:32] allows you to chain together output so
[06:34] we can do something interesting like
[06:35] this right if I hop back to the read me
[06:38] and if I go to prompt chain with two
[06:41] prompts I can just copy this let's go
[06:43] ahead and take a look at this and you'll
[06:45] see something really interesting here
[06:46] right we have the start value we have
[06:49] our list of prompts so what we're doing
[06:51] here is we're running simple prompt with
[06:53] start value and then we're taking the
[06:54] output from this first prompt and then
[06:57] we're passing it in to the second prompt
[06:59] prompt okay and for both prompts we're

### Minute 7

[07:01] going to run the exact same model of
[07:03] these items so if we go ahead kick this
[07:05] off you'll see something interesting
[07:06] start value is getting passed in the
[07:08] first prompt content and this prompt is
[07:10] basically just suffixing pong to the
[07:13] response and so you can see the result
[07:15] here start value pong then we run it
[07:17] again so we pass start value pong as the
[07:21] input to prompt two and then of course
[07:23] the output is start value pong pong
[07:27] right because we run the prompt chain
[07:28] twice and the the cool part about this
[07:30] of course is that you can scale this to
[07:32] whatever number of prompts you you like
[07:35] right so you can run this here again
[07:36] with three prompts and you can see you
[07:38] know the output getting treated as the
[07:40] input three times and then you know you
[07:42] can basically do this as many times as
[07:44] you want and as many times is as useful
[07:47] to you right so if we copy this paste it
[07:50] in here we have a prompt chain of length
[07:52] 10 that's going to take the previous
[07:54] prompt output and use it as the input to
[07:56] the next prompt so I hope you can see
[07:58] where this is going right if we want to

### Minute 8

[08:00] use qdub or Quinn with questions in an
[08:04] interesting way and really get value out
[08:06] of it right now we can create prompt
[08:09] chains so you can see here I've been
[08:10] experimenting with several prompt chains
[08:13] you can take prompt chains and use one
[08:16] on the qwq model to you know run your
[08:19] original prompt and then you can use an
[08:21] extraction model you know this can be
[08:23] gbg4 it can be another local model like
[08:25] Quinn 2.5 it can be whatever you want it
[08:27] to be then you can use another model to
[08:29] extract the output let's look at a real
[08:32] example of that and if this is making
[08:33] sense if you're understanding how prompt
[08:35] training can be useful drop the like
[08:36] drop the sub this is our bread and
[08:38] butter prompt engineering is super super
[08:40] core to the channel and it's super
[08:42] important in the age of generative AI
[08:44] The Prompt is everything if you can
[08:46] understand and use and manipulate
[08:48] prompts you are going to win over the
[08:50] next year and
[08:51] [Music]
[08:54] Beyond we can see here let me just go
[08:56] ahead and pull this into a file so we
[08:57] can take a look at this we have a base

### Minute 9

[09:00] prompt input value that's going to go
[09:02] into our prompt title generation
[09:05] Reasoner if we open up that prompt we
[09:07] can see what that looks like right here
[09:08] create ey catching High SEO click worthy
[09:10] titles so this is good for just content
[09:12] generation for blogs YouTube videos any
[09:15] type of content that you might be
[09:16] creating we have a prompt here with a
[09:18] dynamic variable instructions and a
[09:21] purpose and let's go ahead and fire this
[09:23] off this will take a little bit of time
[09:24] to run since we're running this all
[09:25] locally what's going to happen here is
[09:27] we'll see in the output but basically we
[09:29] going to have qwq walk through creating
[09:31] these titles and then we're going to
[09:33] have a olama Quin 2.5 model parse out
[09:36] the response and we can speed this up by
[09:39] running an open AI series prompt chain
[09:42] so let's use an 01 reasoning model and
[09:44] then gpg 40 as the base model running
[09:46] the exact same thing right so we can
[09:49] copy this go to a file and before we run
[09:52] this let's go ahead and just take a look
[09:53] so we understand what is happening here
[09:56] so we have the same thing right bun run
[09:58] chain. TS the first parameter is the

### Minute 10

[10:01] title that we want to create other
[10:03] titles based on and then we have our
[10:05] first prompt which is going to be our
[10:08] Reasoner prompt and then we have our
[10:09] second prompt right and our second
[10:11] prompt is our extraction prompt that
[10:13] looks like
[10:14] this okay so same kind of deal extract
[10:18] the titles from the final output of user
[10:21] input so we're referencing this Dynamic
[10:22] variable here we have some instructions
[10:25] and then we have example output telling
[10:26] us exactly how we want these titles form
[10:29] formatted fantastic we have this second
[10:31] prompt and you can see here we're
[10:32] running llm instead of olama because
[10:35] we're using Cloud models here and we're
[10:37] going to run an 01 reasoning model and
[10:39] then gpg 40 mini this is some pretty
[10:41] light work we don't need a more powerful
[10:43] model than this let's go ahead and in
[10:45] our second terminal window fire this off
[10:47] and we'll see this get created pretty
[10:49] quickly here since it's on open ai's you
[10:52] know GPU Tech fantastic and then we can
[10:54] just go ahead and open this up and take
[10:56] a look right so it's in that same format
[10:57] we have our first prompt you can see our

### Minute 11

[11:00] prompt content here so this is you know
[11:02] that full value it's getting populated
[11:05] here if we open up this prompt you can
[11:07] see exactly what that looked like and
[11:09] exactly how it was replaced thanks to
[11:12] this input Dynamic variable and then we
[11:13] have the result from 01 mini right so we
[11:16] have this result it's giving us 10 new
[11:18] titles feel free to choose the best one
[11:21] and then we run our second prompt right
[11:23] we directly take this output and if we
[11:25] scroll down here you can see in our user
[11:27] input this is is our input to our next
[11:31] prompt okay and then if we scroll down
[11:33] you can see 01 mini giving us a nice
[11:36] clean Json structure here all we have to
[11:38] do is parse it out of the markdown block
[11:42] really cool stuff here let's see if qwq
[11:44] has finished there it is let's go ahead
[11:45] and open it up and we can see the same
[11:47] thing from qwq of course we're going to
[11:50] see a much longer Chain of Thought right
[11:53] we're going to see its internal
[11:54] monologue I really like the fact that
[11:56] you can see its entire thought process
[11:58] right if we who search characters you

### Minute 12

[12:00] can see it keeping the character count
[12:03] between 40 and 85 right it explicitly
[12:06] mentions one of our instructions we do
[12:08] love to see that I'm sure it's going to
[12:10] mention at some point uh you know the
[12:12] number of titles that we want to create
[12:15] this is great it's giving us a breakdown
[12:17] of the characters against its new titles
[12:20] right making sure they're within the
[12:21] character limit make sure they're unique
[12:23] and not repetitive that's something we
[12:24] explicitly mentioned in one of our
[12:26] instructions so it's really great to see
[12:28] qdub uh you know explicitly mentioning
[12:30] that in its thought process this is
[12:32] really what you want to see from your
[12:33] reasoning models you want to see them
[12:35] reflecting on your prompt inputs and
[12:38] then we have the final titles list here
[12:40] right and now let's see if Quin 2.5
[12:42] coder was able to take the user output
[12:45] and actually return Json so you can see
[12:47] here we have the input for Quinn 2.5
[12:51] coder being the output of our previous
[12:54] model here so if we scroll down to final
[12:56] titles if we just search this
[12:59] we can see we're now inside the user

### Minute 13

[13:02] input on the Quin 2.5 model and if we
[13:06] scroll down to the output let's see how
[13:08] it's done nice fantastic so Quin 2.5 was
[13:11] able to nail this and it's all thanks to
[13:14] this prompt chaining pattern where we
[13:16] have a powerful reasoning model
[13:18] generating the request thinking through
[13:20] your prompt and then we have an
[13:21] extractor model so this is a traditional
[13:24] base model right this is going to be
[13:25] your average uh gpg 40 Gemini your
[13:29] flashes your minis uh your quins your
[13:32] base language model they can do the
[13:33] extraction work of pulling out the final
[13:36] result from your reasoning model so you
[13:38] know if we just search here you can see
[13:40] supercharge your NLP locally and if we
[13:42] scroll up here you can see that was in
[13:43] the final titles and that worked really
[13:46] well likely use inspiration from the
[13:48] example outputs and you can see where
[13:50] this is going right this is an important
[13:52] pattern that I want to share with you
[13:54] specifically for these reasoning models
[13:57] where we can see the Chain of Thought we

### Minute 14

[14:00] can see the internal monologue of models
[14:03] like qwq Quinn with questions it's
[14:05] possible that in the future we'll see
[14:07] the internal monologue from the new 01
[14:10] model or other reasoning models that are
[14:12] going to be coming out in the future
[14:14] this pattern is going to be ultra useful
[14:16] for cleaning out and parsing out the
[14:19] outputs from these powerful reasoning
[14:20] models right because otherwise you're
[14:21] limited to using qwq and other reasoning
[14:25] models just inside of a chat window
[14:28] where you have to man parse out the
[14:29] result every single time right I wanted
[14:31] to share this idea with you I wanted to
[14:32] bring prompt training back up on the
[14:34] channel this is something I use
[14:36] internally all the time when I'm
[14:38] building out my own AI agents personal
[14:40] AI assistants you can kind of see it
[14:42] littered across uh some of the code
[14:44] bases I share on the channel prompt
[14:45] training is ultra Ultra important and
[14:48] it's not discussed enough so I wanted to
[14:50] share that with you here on the channel
[14:52] feel free to check out our previous
[14:54] prompt engineering video where we walk
[14:56] through the four levels of prompts that
[14:58] allow you to write really powerful

### Minute 15

[15:00] really accurate prompts everything you
[15:02] saw here is going to be in the
[15:04] description in a Guist for you let me
[15:06] know what you think in the comments how
[15:07] do you feel about qwq are you finding it
[15:10] useful for your own work if so how are
[15:13] you using this model I have the 2025
[15:15] predictions video coming up for the
[15:17] channel one of my big predictions to
[15:19] kind of give a little bit away we're
[15:21] going to see local models become truly
[15:24] viable truly useful um in a more
[15:27] mainstream way and qwq qdub Quinn with
[15:31] questions is absolutely Paving the way
[15:33] here I got to say I am shocked with this
[15:36] model it is finicky it's stingy it's the
[15:39] preview version there are a lot of
[15:41] problems with this model as we've
[15:42] discussed there's language mixing it's
[15:44] slow you need a prompt chain to extract
[15:47] the actual final result but we're going
[15:49] down a great path here AI is becoming
[15:51] democratized that's really important we
[15:53] don't want any one of these large AI
[15:55] companies to own all of this technology
[15:58] I found Q to be a bit more interesting

### Minute 16

[16:00] than the model context Provider from
[16:02] anthropic that's a super important
[16:05] release we're going to cover that on the
[16:06] channel as well I want to see that get
[16:08] developed a little more and I'm still
[16:10] working through how to best use that
[16:12] technology if you enjoyed this video you
[16:14] know what to do drop the like drop the
[16:16] sub and I'll see you in the next one