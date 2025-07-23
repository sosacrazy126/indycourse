# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=yZGb9-Z9DG0
- **Duration:** 37:18
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 7180
- **Transcript Generated:** 2025-03-30 23:48:55

## Transcript


### Minute 0

[00:00] what's up Engineers welcome back I have
[00:02] a massive two for one grand slam for you
[00:04] today open AI 12 days of releases has
[00:08] kicked off with Chad GPT Pro and the new
[00:11] complete 01 model I absolutely had to
[00:15] purchase the insane chat GPT Pro
[00:18] subscription for 200 bucks a month I
[00:20] bought this because of course I'm
[00:22] addicted to being on the edge and also
[00:25] so you don't have to take on the risk
[00:27] before you see what it can do in this
[00:29] video you'll find out out if it's worth
[00:30] it we've been preparing for the o1
[00:32] launch for quite a while the trick with
[00:34] these highly capable reasoning models
[00:36] like 01 and o1 PR mode is knowing what
[00:39] to prompt to reveal and challenge its
[00:42] capabilities and oh boy do I have a
[00:45] challenge for 01 today we're challenging
[00:48] the new 01 series with meta prompting an
[00:50] advanced prompt engineering technique
[00:52] where you write a prompt that writes
[00:54] prompts for you this technique unlocks
[00:57] asymmetric productivity for you in the
[00:59] generative AI age that we live in we'll

### Minute 1

[01:02] talk about why and how to best utilize
[01:04] this pattern in this video Let's
[01:06] understand meta prompting with handson
[01:08] examples using the new 01 and 01 Pro
[01:12] mode and let's see if it's worth your
[01:14] hard earned
[01:18] cash this is a meta prompt at first
[01:21] glance this just looks like a standard
[01:24] information Rich XML prompt with a huge
[01:27] set of instructions you can see this
[01:29] prompt has has about 3,000 tokens so
[01:32] there's a lot going on here there's a
[01:33] lot of information packed into this
[01:35] prompt let's run our meta prompt in a
[01:37] static Way by replacing our user input
[01:40] variable here we'll generate prompts
[01:42] using the new 01 model and then we'll
[01:44] take those prompts and run it against
[01:46] both chat GPT 01 and 01 Pro mode at the
[01:51] same time so we can compare the results
[01:54] side by side together so let's start
[01:57] with some meta prompting in our
[01:59] directory here you can see we have three

### Minute 2

[02:01] examples that we're going to work
[02:02] through and some images that we'll talk
[02:03] about in a second let's go ahead and
[02:05] start out by just generating three new
[02:08] prompts from our meta prompt so what
[02:10] I'll do is I'll copy The Meta prompt
[02:13] just paste it in a brand new file here
[02:15] and then let's start with our Hacker
[02:16] News perspective so this is a simple
[02:19] user input where I'm basically walking
[02:22] through everything we want to pass into
[02:24] this prompt I'm using a semi-structured
[02:26] input format you can see we have purpose
[02:28] instructions sections and and variables
[02:30] and all I'll do here is copy this paste
[02:33] it into our meta prompt and replace our
[02:35] user input I'll then copy the entire
[02:37] meta prompt and go over to chat gbt
[02:40] using the new 01 model I'm just going to
[02:42] paste this in and we're going to let
[02:44] this rip so we want o1 to generate a new
[02:47] prompt based on this meta prompt and all
[02:50] the details for what the prompt will do
[02:52] is embedded in the user input here so
[02:54] you can see it took 9 seconds for 01 to
[02:57] spit out this result this is much f
[02:59] faster over 01 preview we can go ahead

### Minute 3

[03:02] and just copy this let's create a new
[03:04] file here we'll call this prompt hn
[03:06] perspectives we're going to use this
[03:08] prompt to analyze Hacker News commentary
[03:11] we have this new prompt here this is
[03:13] pretty incredible it's generated
[03:15] automatically for us thanks to our meta
[03:16] prompt in an XML is format we've talked
[03:19] about XML format on the channel in the
[03:21] past long story short there is that XML
[03:23] is the best way to get highquality
[03:25] results out of your prompts uh feel free
[03:27] to pause the video and check out you
[03:29] know the details of this prompt but it
[03:30] basically just took everything we asked
[03:32] for in our user input it read the entire
[03:36] meta prompt that we have here um you
[03:38] know tons of instructions here we have
[03:39] an input format and then of course
[03:41] several Rich examples and it generated a
[03:44] brand new prompt for us so you can see
[03:47] here you an expert at analyzing and
[03:48] aggregating perspectives from a given
[03:51] Hacker News Post so great start solid
[03:53] instructions here let's continue to our
[03:55] next prompt bug analysis this is a
[03:58] prompt that's going to analyze code and

### Minute 4

[04:00] Report bugs so as you'll see this is
[04:02] going to be a very useful prompt for
[04:04] reviewing code why have your coworker
[04:06] review your code when you can have ai
[04:07] review it first and save them and
[04:10] yourself a lot of time in the pr review
[04:12] process so this is a powerful prompt you
[04:14] can see here we actually have a example
[04:16] of what we want the examples in the
[04:18] prompt to look like so we're giving the
[04:20] meta prompt some additional information
[04:22] here to create a great High equality
[04:24] prompt to solve the problem we're aiming
[04:25] to solve in this case we want to analyze
[04:28] and review code fixes to be recommended
[04:30] we wanted to look for critical bugs that
[04:32] would crash the program and we also
[04:34] wanted to give us a ranking so when
[04:36] you're writing the input to The Meta
[04:38] prompt that defines the prompt you're
[04:40] looking for you can just kind of write
[04:42] out you know in natural language what
[04:44] you want the sections to look like what
[04:45] are the variables what are the sections
[04:47] what do you want your examples to look
[04:48] like copy this and we can replace the
[04:51] previous user input here copy this and
[04:54] same deal so I'm going to start a new
[04:55] chat here paste this in and run this
[04:58] once again on o we don't need 01 Pro

### Minute 5

[05:01] mode yet the real comparison will be uh
[05:03] in executing these large intense prompts
[05:06] in 01 Pro mode so let's go ahead and
[05:08] copy this out you can see we have a uh
[05:11] great prompt written here let's go ahead
[05:13] and take a look at this so this is
[05:14] prompt bug
[05:17] analysis if we paste this in you know we
[05:19] have three examples so these were
[05:21] automatically generated examples thanks
[05:23] to our meta prompt you can see the
[05:25] format you know it's giving us severity
[05:26] the file the description and then
[05:29] something cool added to the example we
[05:31] want a contrl f lookup to figure out
[05:33] where that issue is and it's going to
[05:35] give us a recommended fix so this is you
[05:37] know the importance of good prompt
[05:39] engineering you're never going to get
[05:40] this format by just saying find bugs in
[05:42] my code right by doing something like
[05:44] this right find bugs in my code and then
[05:48] you just place your code here right this
[05:50] is why prompt engineering is a very very
[05:53] real skill by specifying examples by
[05:56] creating instructions by defining a
[05:58] clear purpose this prompt output is

### Minute 6

[06:00] going to be very very rich and useful as
[06:04] you'll see in a second here so this is
[06:06] great we have a bug analysis prompt
[06:08] let's go ahead and generate one more
[06:09] prompt here's our last prompt here and
[06:11] this is going to be a oh let me actually
[06:13] create this uh update this to XML here
[06:15] and our last prompt here is going to be
[06:17] a script to blog we're going to take the
[06:20] script from a previous YouTube video and
[06:22] then we're going to pass in the topic or
[06:23] the title of that video and it's going
[06:25] to generate a HTML CSS only blog basic
[06:29] on the script okay so we're just going
[06:30] to copy this follow that same process
[06:32] we're going to replace our user input
[06:34] from our meta
[06:36] prompt and you know I just have these
[06:38] all pre-typed out I don't want to waste
[06:39] your time writing out these user inputs
[06:42] so I'm just going to copy this we're
[06:43] going to start a new session so that the
[06:45] chat history does not affect the meta
[06:47] prompt and you know let's actually go
[06:49] ahead and use o1 prom mode for this
[06:52] final meta prompt I'm going to run that
[06:53] here and we can do this side by side
[06:56] just for fun so we'll do this side by
[06:57] side you can see a big difference here

### Minute 7

[07:00] um 01 Pro mode is taking some time to
[07:02] think right away and you can see 01 the
[07:05] 01 base model is already done it's it's
[07:08] written this great uh instruction Rich
[07:11] prompt it has the two variables I asked
[07:13] for it has the lead in for the
[07:16] completion for the llm that's going to
[07:17] run this prompt this is quite fantastic
[07:20] right you're an expert web designer and
[07:22] writer who specializes in creating
[07:24] engaging humanlike blog posts using only
[07:27] HTML and CSS okay so um right away we
[07:31] can see just by running our meta promps
[07:33] 01 is very very powerful um I'm still
[07:36] kind of in shocked that this ran for 4
[07:38] seconds and it was able to work through
[07:41] the meta prompt that quickly so uh this
[07:43] is a task that GPT 4 o l models
[07:46] typically have problems with if you look
[07:48] at the meta prompt it's kind of complex
[07:51] especially when you get to the examples
[07:53] because in the examples we have input
[07:56] prompts and the expected outputs which
[07:58] are themselves prompts right so you can

### Minute 8

[08:01] imagine lower quality even middle tier
[08:04] models have problems with the meta
[08:07] prompt and you know we can see the new
[08:10] 01 did this task with no problem in 4
[08:13] seconds okay so let's go ahead and just
[08:15] use this I'll say prompt gript to blog.
[08:19] XML file I'll paste this and now we have
[08:23] a new prompt right this new generative
[08:25] AI mini program that takes in a script
[08:30] and a topic and we'll generate a HTML
[08:34] and CSS blog for us we'll see how the
[08:37] outputs perform between 01 PR mode and
[08:40] 01 in just a moment but you can see here
[08:42] we have a very very similar output from
[08:45] 01 Pro mode for the use case of meta
[08:47] prompting 01 and 01 Pro mode put out
[08:50] very similar results you can see avoid
[08:53] overhype and keep it real avoid sounding
[08:56] like an AI aim for natural human-like
[08:58] voice actually prefer the 01 output here

### Minute 9

[09:00] a little bit more for that specific
[09:02] instruction but very very similar
[09:04] outputs here we're not going to worry
[09:05] about this this is not really what we
[09:07] were aiming to compare let's go ahead
[09:09] and open up new sessions and start
[09:11] running our prompts that are meta
[09:14] prompts generated for
[09:17] us before we move on let me just quick
[09:20] highlight again the value of meta
[09:22] prompting why is meta prompting so
[09:24] important if you haven't noticed uh The
[09:26] Prompt is everything Engineers product
[09:28] builders managers anyone who can get
[09:31] their hands on a highquality prompt can
[09:33] do a lot more with a lot less prompts
[09:36] give you superh human abilities thanks
[09:39] to the language models underneath them
[09:41] as every engineer with their eyes
[09:43] actually open is noticing you know
[09:45] software engineering has completely
[09:47] changed right language models prompting
[09:50] has completely changed the way software
[09:53] is written this is just a single domain
[09:55] there are many others actively being
[09:57] transformed by llms prompts and gen AI

### Minute 10

[10:00] as a whole right there are many more to
[10:02] come and they're all fueled by one thing
[10:05] the prompt in the age of generative AI
[10:07] your ability to generate prompts is your
[10:09] ability to generate results so the
[10:11] quality and the quantity of prompts
[10:14] right highlighting here The Meta prompt
[10:16] the quality and quantity of prompts you
[10:19] can generate will determine how
[10:22] effective you are in the generative AI
[10:24] age that's what meta prompting is all
[10:26] about more prompts at higher quality
[10:29] based on your meta prompt you can start
[10:31] with the one we're experimenting with
[10:33] right here I've been using this meta
[10:35] prompt here for uh about half a year now
[10:38] 3K tokens great clear instructions Some
[10:41] solid examples you can start with the
[10:43] meta prompt here link will be in the
[10:45] description this is a very very valuable
[10:48] resource and an important pattern I'm
[10:50] giving to you here and it's going to
[10:52] become more important especially when we
[10:54] embed our meta prompt into AI agents
[10:58] that can then automate the process of

### Minute 11

[11:00] executing the meta prompt which
[11:02] generates new prompts for us hint hint
[11:05] more on that coming in 2025 you can
[11:07] really hear the agentic recursive Auto
[11:10] looping nature of handing off this meta
[11:12] prompt to an AI agent right so smash the
[11:15] like comment subscribe stay connected to
[11:17] this information and be on the lookout
[11:19] for the weekly video every Monday in
[11:22] 2025 um everything we're doing here is
[11:24] going parabolic especially as the
[11:26] technology of generative AI continues to
[11:28] evolve so so that's the important of the
[11:30] meta prompt let's go ahead and run it
[11:33] let's make sure that you know it's
[11:35] actually generating some great high
[11:36] quality prompts for
[11:39] us I thought it would be interesting and
[11:41] cool to actually look at The Hacker News
[11:45] Post on chat GPT for this we're going to
[11:47] paste in a block of Json which contains
[11:49] all the kind of comments and the
[11:51] commentary we can go to the Post here so
[11:54] here's the you know chat TPT Pro Hacker
[11:56] News Post and you know a bunch of Rich
[11:59] commentary no AI summary will ever

### Minute 12

[12:02] replace the learning and the growth
[12:04] you'll have when you actually just read
[12:06] everyone's thoughts and opinion so you
[12:08] know highly recommend you do that we can
[12:10] go ahead take this post ID and go to
[12:12] algolia and paste that here and you know
[12:16] with this link what you'll see is the
[12:18] entire Hacker News Post broken down in
[12:21] this Json format so we can copy this
[12:23] I'll create a new file uh this is hn
[12:25] post. Json paste the results in here
[12:29] automatically format you can see this is
[12:30] a 200k token Json blob that is too many
[12:34] tokens I think that 01 and ow and pro
[12:38] mode run with about a Max of 128k tokens
[12:41] which is still quite a lot so let's go
[12:43] ahead and pair this down a little bit we
[12:44] can open up the terminal and use JQ for
[12:47] this so if i r on
[12:49] jq. and then we pass in h& post you can
[12:52] see all the children getting printed out
[12:55] there and you can see all the comments
[12:57] are going to be in this first children
[12:59] block okay so this is all we need to get

### Minute 13

[13:01] all the Hacker News comments and if we
[13:04] hit up again and we do a length check on
[13:06] this I think it's just pipe length yeah
[13:09] so you can see we have 145 items let's
[13:11] pair this down
[13:14] to um we can do 50 so we'll get the
[13:17] first 50 and I want to Output this to hn
[13:20] poost 50.
[13:22] Json okay and then we can just look at
[13:25] this new file that's a 100K tokens this
[13:28] is going to be more manageable so I'll
[13:31] it's kind of wild to say 100K tokens is
[13:32] going to be more manageable but it's
[13:34] true that's how powerful these 01 models
[13:36] are so I'm going to copy this I'll open
[13:38] up our prompt hn perspectives I'll paste
[13:41] this in and I'll actually copy this into
[13:42] a new file here I'll revert this and now
[13:45] we have our prompt hent perspectives
[13:48] prompt filled out so if I go back to XML
[13:52] here you can see we have user prompt
[13:53] with all that Json and now we have a
[13:57] 100K token prompt this is the moment of
[13:59] truth we can open up chat gpg Pro

### Minute 14

[14:01] instances here let's make sure we're in
[14:03] fresh sessions and let's see how both of
[14:06] these models perform okay same prompt
[14:09] both sides 01 Pro mode 01 and let's fire
[14:13] these off so right away first thing to
[14:15] notice is that these models are thinking
[14:17] a little bit and you can see how long
[14:19] this scroll takes this is a huge huge
[14:21] prompt right away they're thinking okay
[14:23] o1 is outputting results already this is
[14:26] very very impressive it it thought for
[14:28] one
[14:30] second uh wow okay so they really really
[14:34] punch this model forward 01 is very fast
[14:37] I mean that's uh non reasing models are
[14:40] slower than this so very impressive you
[14:42] can see on the left side 01 Pro mode if
[14:44] we open up the details actually doesn't
[14:46] have any details here for us yet it's
[14:49] thinking uh so that's fine but you can
[14:51] see you know taking some time this is
[14:53] the you know typical UI for 01 Pro mode
[14:55] you pay something in and then it takes
[14:57] some time to really think through me
[14:59] meanwhile we can work through our output

### Minute 15

[15:02] on okay okay very nice 01 promoe just
[15:05] wrapped up for us and it just spit out
[15:06] this massive result so this fantastic I
[15:09] thought for one minute you can see that
[15:11] here let's kind of walk through this
[15:12] right so main points perspectives from
[15:14] the discussion so we have price value
[15:16] justification debate over the 200 month
[15:19] price tag of course that makes sense
[15:21] many users urge it's expensive compared
[15:23] to 20 of course it's a basically a 10x
[15:25] jump I think the big kicker here which I
[15:27] completely agree with so users find it
[15:29] absurd While others see it Justified if
[15:32] it can give you the productivity rates
[15:35] or if you can basically pay it back by
[15:37] Saving Time from using it right the idea
[15:39] is that if it saves you multiples hours
[15:40] on time monthly it's worth it for others
[15:42] it's simply too expensive right so
[15:43] totally understandable you can see that
[15:46] same type of perspective here broken
[15:48] down in 01 Pro mode comparison to
[15:51] Alternatives is a big topic here and you
[15:53] can see both models kind of going down
[15:55] the line here this all looks great uh I
[15:58] do like the shorter more concise bullet

### Minute 16

[16:00] points from 01 Pro mode but if we scroll
[16:02] down here and look for top three
[16:04] representative comments for each one of
[16:06] the perspectives this was a great
[16:08] comment right uh if you save 4.5 hours
[16:12] in a Google sheet the 200 bucks a month
[16:14] is cheap right I mean that's paid itself
[16:16] off very very quickly so we have you
[16:19] know if you don't have the use case for
[16:21] 01 reasoning models which a lot of
[16:23] Engineers and Builders don't need the 01
[16:26] model and also my opinion here is that
[16:28] that most engineers and product Builders
[16:30] don't know how to use these powerful
[16:32] reasoning models you really do need
[16:34] interesting hard uh complex problems to
[16:37] even get value out of these otherwise 40
[16:41] Gemini Sonet is going to cover you know
[16:43] most cases but you can just kind of see
[16:44] here you know we're getting very similar
[16:46] results I'm leaning more toward 01 Pro
[16:49] here but these are where things get kind
[16:50] of interesting right we have a breakdown
[16:51] of the table right so we have five
[16:53] different perspectives we have sentiment
[16:55] we have summaries these are great you
[16:57] can you know stop you can pause the
[16:58] video Read these if you're interested

### Minute 17

[17:00] and then we have a nice flowchart here
[17:01] so I actually want to copy out these
[17:02] flowcharts I did also ask for a
[17:04] flowchart at the ending here which is
[17:06] kind of hilarious to ask for that and
[17:08] let's just open this up and take a look
[17:10] at this flowchart okay so this is really
[17:12] interesting so users uh assesses value
[17:15] price debates 200 is too high cheap
[17:18] Alternatives uh logical flow here right
[17:21] if you're using claw open source just
[17:23] skip it quality is uncertain still
[17:25] hallucinates so I I don't know about
[17:27] this this this model does doesn't really
[17:29] hallucinate yeah if it saves time if
[17:31] you're a high earner if you have complex
[17:33] use cases then it's completely Justified
[17:36] right so you have business
[17:37] specifications where youou the losses so
[17:39] this is a decent chart right this kind
[17:41] of breaks down I think the sentiment
[17:43] around chpt Pro so let's go ahead and
[17:46] look at the as we're talking about it
[17:47] let's go ahead and look at the results
[17:49] from uh chpt Pro 01 Pro mode so let's
[17:52] just paste this in and let's see this
[17:54] break down right so open ey introduces
[17:56] pro at 200 worth it so I like this slow
[17:59] better uh yes High income Pros uh

### Minute 18

[18:02] justify time-saving less time spent on
[18:04] complex task worth it no individuals uh
[18:07] you know too expensive not enough value
[18:09] stick with cheaper alternatives make
[18:10] sense we have the open source block here
[18:13] and then we have adoption and Reliance
[18:15] right addiction leads to potential
[18:17] higher price skeptical llm hype question
[18:20] so all makes sense I love the breakdown
[18:22] from both of these models let's go ahead
[18:24] and close this up and move on to our
[18:26] next prompt so far how are you liking
[18:28] the output of of 01 prom mode and 01 as
[18:31] you can see I think the difference is
[18:33] marginal based on these examples and
[18:35] based on this you know one promp for
[18:37] running here but you can already start
[18:39] to see some differences right just a
[18:41] little bit of detail here a little bit
[18:43] of extra kind of information uh I like
[18:46] how it's breaking down the information a
[18:48] little bit more in O Pro mode let's run
[18:50] some more prompts and then we can make a
[18:51] better decision
[18:54] here let's go ahead and run script to
[18:58] blogs so this is pretty interesting

### Minute 19

[19:00] let's close this let's close this and
[19:02] let's focus in on our script to blog
[19:05] what I'll do here is I'll open up a
[19:08] script from our previous YouTube video
[19:10] so this is from the qwq local reasoning
[19:14] model video that we put out last week
[19:16] and what I'll do is I'll paste that
[19:18] script in here so you can see this
[19:19] entire script right here and then I'll
[19:22] paste in the video title so we have our
[19:26] title in here as well so we have a a 4K
[19:29] token prompt not too large but there's
[19:32] not nearly as much information to work
[19:34] through as our Hacker News perspectives
[19:36] prompt let's copy this hop back over to
[19:39] chpt Pro let's use new fresh windows so
[19:42] we don't contaminate and then let's just
[19:45] paste these prompts in and let's see how
[19:47] 01 and 01 Pro mode generates a HTML CSS
[19:52] only blog post based on the transcript
[19:55] from the last video we did on the
[19:57] channel so right away you can see the
[19:58] same deal happening we do get a detail

### Minute 20

[20:01] of the inner monologue okay 01 is
[20:04] finished already this model is insanely
[20:07] fast this is one of the most advanced
[20:09] okay so it's it's it's in progress um
[20:12] this model is just absolutely incredible
[20:14] uh the speed here is really making me
[20:17] appreciate the intelligence it has even
[20:19] more 0 and preview would have taken
[20:21] probably about double the time to Output
[20:23] this but okay so copy code let's go
[20:25] ahead and create a blog file here so
[20:29] this is 01 qwq blogpost HTML we'll paste
[20:34] this in and something important to note
[20:36] about this prompt here is that I also
[20:39] have image references so you can see
[20:41] here inside the prompt The Meta prompt
[20:43] picked up on this perfectly it didn't
[20:45] change the file references at all we
[20:47] have a couple pgs which will uh link
[20:50] directly to this images directory right
[20:53] with some images so you know we do have
[20:54] images for this blog post let's see how
[20:57] 01 has down here and generating this

### Minute 21

[21:00] let's go ahead and open up uh preview
[21:03] okay sorry if my screen blinded you
[21:05] there interesting right so we have the
[21:06] title uh we have the hook that's
[21:08] something that we explicitly mentioned
[21:10] um in the instructions start with a
[21:11] strong hook that captures the reader
[21:13] attention and we have a table of
[21:15] contents here this is perfect we did ask
[21:17] for that uh search for table of contents
[21:19] right highlighting the three main points
[21:21] good and then it kind of jumps into it
[21:23] right so this is really really cool
[21:24] right this is a automatically generated
[21:26] blog post let me actually read this hook
[21:28] and see if like this so ever wonder if
[21:30] local reasoning models can deliver the
[21:32] same Nuance on the Fly insights we've
[21:34] come to expect from Big cloud-based
[21:37] systems good news it just got a whole
[21:38] lot more interesting meet qwq Quinn with
[21:41] questions the model that's raising
[21:43] eyebrows in the world of local a
[21:45] reasoning this is really good in this
[21:47] post we'll explore a trick that makes
[21:49] qwq instantly more useful prompt
[21:51] chaining okay so this is this is solid
[21:54] you know again comment down below let me
[21:56] know what you think about this hook
[21:57] automatically generated by 01 it's it's

### Minute 22

[22:00] pulling from the ideas of you know my
[22:03] intro from the previous YouTube video
[22:05] and I'll of course link this video in
[22:07] the description check it out and then
[22:08] you know this blog post will make uh
[22:10] quite a bit more sense but this is right
[22:12] on topic you know anyone that's seen our
[22:14] last video you know this is exactly what
[22:16] it's all about the whole idea in that
[22:18] video is we want to make qwq more useful
[22:21] with prompt chaining so this is
[22:22] excellent table of contents just like we
[22:23] asked rise of the qwq reasoning models
[22:26] nicknamed it qdb in the intro here's the
[22:29] thumbnail for that video breaking down
[22:31] promp chaining it's talking about the
[22:32] Reasoner and or and the extractor just
[22:35] like we talked about in the video you
[22:37] can use qwq to generate the long
[22:39] thinking output with the Chain of
[22:41] Thought and then you can use a Quinn 2.5
[22:43] or now llama 3.3 to extract the result
[22:47] right and simplify the output you can
[22:49] also now use ama's uh structured outputs
[22:52] so this just got released just wanted to
[22:54] quickly bring this up Alama now has
[22:55] support for structured outputs more
[22:57] reliability and consist
[22:59] in Json mode so just something to bring

### Minute 23

[23:00] up quickly here uh you know you can now
[23:02] use a model like qwq that thinks and you
[23:05] can extract the final result right with
[23:07] an extractor model that pulls out uh the
[23:10] example so anyway refocusing here on the
[23:12] 01 blog post output we can see we have
[23:15] that prompt chain image placed really
[23:18] really well and you know I actually
[23:20] meant to paste in the images inside of
[23:23] chat gbt here I completely just missed
[23:26] out on that the 01 models now have image
[23:28] support but it looks like very clearly
[23:30] 01 did not need to see these images to
[23:33] place them properly so the last bit of
[23:35] our blog here I do like these cards
[23:37] right a little bit of box shadow image
[23:39] right in the center here and you know
[23:42] simple kind of lightweight section so
[23:45] this is 01 let's go ahead and look at
[23:47] the output from 01 in PR mode so I'm
[23:50] going to just copy the output here open
[23:51] up a new file this is going to be 01
[23:54] promode blogpost
[23:56] HTML we can paste this and let's go into

### Minute 24

[24:00] HTML preview mode so crack open qwq
[24:04] ready for so this is already better
[24:06] right it's not prefixing with hook but
[24:08] let's open up 0 one's output so it had
[24:10] this hook prefix right there's no reason
[24:12] to show that so already 01 prom mode
[24:15] understands the problem a little bit
[24:17] better than 01 so QQ also known as CHR
[24:20] questions is stirring excitement because
[24:21] it's not just another a model it's a
[24:24] reasoning Powerhouse you can run right
[24:26] on your machine let's be honest qq's raw
[24:29] output can be a bit messy don't worry
[24:31] there's a brilliant solution prompt
[24:33] chaining in this post we'll walk through
[24:35] how prompt chaining transform qwq into a
[24:38] super useful OnDemand idea machine Let's
[24:40] dive in okay so pretty interesting a
[24:42] little more exciting than I would like
[24:44] the language to be but it's fine we can
[24:46] tweak that very easily by updating the
[24:48] prompt we have the table of contents
[24:50] that's good problem with local reging
[24:51] models I like this so setting up a kind
[24:53] of intro solution example structure uh
[24:57] we can see these images here we we get
[24:59] this nice centered caption which I think

### Minute 25

[25:01] is a nice addition here introduction to
[25:03] prompt chaining a game changer promp
[25:04] chaining clever technique and it it's
[25:07] really nailing exactly everything in
[25:10] that YouTube video it's nailing every
[25:11] one of the ideas um you can use to
[25:14] generate Rich thought out answers then
[25:16] use another model like a streamlined
[25:18] Quinn 2.5 model to neatly extract
[25:20] results it's fantastic how prompt
[25:23] training Works in a nutshell great
[25:24] breakdown here I do like that it you
[25:26] know kind of created this little howto
[25:28] in in the center here putting it all
[25:29] together you can see we have our 01
[25:32] image there and Prof for reasing models
[25:35] through our prompt engineering at the
[25:37] bottom here this is really cool Pro tip
[25:39] start simple this is this is pretty nice
[25:41] right gave us a little Pro tip uh item
[25:44] here why wait for tomorrow's models or
[25:46] next week's new code releases with
[25:48] prompt chain you can harness qq's
[25:49] reasoning capabilities today and keep a
[25:52] tidy usable final result every time so
[25:54] this is fantastic to me the language of
[25:57] 01 PR mode is a lot more human maybe

### Minute 26

[26:01] minus this this intro that the intro is
[26:03] kind of annoying to me but you know
[26:05] that's fine you might like intros like
[26:06] this uh nothing wrong with it I will say
[26:08] I did like the format like the the
[26:11] visual format of the base1 model a
[26:13] little bit better but I think that
[26:15] content wise 01 Pro mode is a bit better
[26:19] here right these howtos and this tip
[26:22] here and the you know image captions I
[26:25] think provides quite a bit more value
[26:28] than the 01 base output blog but again
[26:30] you know comment down below let me know
[26:32] what you think do you see one model
[26:34] beating the other out or is it just
[26:36] close enough I feel like it is kind of
[26:38] hard to tell and these results could
[26:40] just be about the non-deterministic
[26:42] nature of llms as a whole right to me a
[26:46] consistent theme Here 01 prom mode is
[26:48] giving me just a little Edge is it worth
[26:51] $200 a month well that really just
[26:53] depends on the volume of reasoning that
[26:56] I need solved over the course of a month
[26:58] right I think that's the big kind of

### Minute 27

[27:00] delineation with the decision of whether
[27:02] chat GPT Pro is actually worth it so we
[27:04] have one more prompt to run let's go
[27:06] ahead and fire that
[27:08] off open up our bug analysis and so this
[27:11] is a really interesting one our bug
[27:13] analysis here ignore the syntax here
[27:15] that just looks like we clipped image a
[27:17] little bit there all we need to do here
[27:19] is paste in some code so I have this
[27:21] previous code base Beni from our live
[27:24] benchmarking uh repository and what I'll
[27:27] do here is I have this kind of
[27:28] pre-command loaded here I'll be sharing
[27:30] more on this tool in 2025 but what I can
[27:33] do here is basically pull together
[27:35] context files so if I run alo1 gather
[27:38] files yeah we can just see this command
[27:41] here basically all I'm doing here is I'm
[27:42] pulling all The View files in the source
[27:46] directory typescript files and every
[27:48] python file in the server okay so this
[27:50] is a simple client server application
[27:52] I'll also link the live benchmarking
[27:55] videos in the description if you're
[27:56] interested in checking out this code
[27:58] base and some of the cool live
[27:59] benchmarks we've done on the channel so

### Minute 28

[28:01] I'll copy this and this is going to be
[28:03] really cool so I'll close this and now
[28:04] if I print this right if I paste this
[28:07] you can see um if I run Source or if I
[28:09] just search for Source here you can see
[28:12] every file from this code base
[28:15] right so this is really cool so we have
[28:18] every python file we have every
[28:20] typescript and every vue.js file that we
[28:24] need and this is great right so
[28:26] basically we have a bunch of code you
[28:27] can see we have have 20K token code base
[28:30] so I'm just going to take this paste it
[28:32] in our user prompt now our expert code
[28:35] analysis prompt is going to run an
[28:37] analysis on that code so as usual we'll
[28:40] copy this we'll start fresh sessions and
[28:43] then I'll just paste in both sides and
[28:45] let's see how 01 and 01 Pro mode reviews
[28:49] our code for us so I'll paste this in
[28:51] both sides um you know a decent size
[28:54] prompt there this is a 20K token prompt
[28:57] and let's go aad and scroll to the
[28:58] bottom here let's see what 01 promote is

### Minute 29

[29:00] doing you can see it working through
[29:02] nice we have a decent chain of details
[29:05] here I have noticed that after a while
[29:08] 01 Pro mode sometimes just stops
[29:10] outputting its details to you and you
[29:12] know just kind of keeps it to itself
[29:14] after a while but this is nice to see
[29:15] examining code managing async bugs it
[29:18] found a couple async bugs there after 32
[29:20] seconds so this is a more complex thing
[29:22] to work through 01 thinking for about 32
[29:25] seconds and it found a decent chunk of
[29:27] issues for right so let's go ahead and
[29:29] just copy this out everything's always
[29:30] easier to read in your own text editor
[29:33] so we can see here for 01 base a decent
[29:36] slew of responses from our bug analysis
[29:39] prompt we have a potential crash if
[29:42] messes. content is empty from our
[29:44] anthropic llm model yep that's super
[29:46] solid everyone just kind of assumes that
[29:49] this will always exist uh that was my
[29:50] bad to not you know place an if there so
[29:53] we have our is loading resetting
[29:55] prematurely due to an unawed a sync Loop
[29:59] okay so this is actually kind of

### Minute 30

[30:00] interesting let me let me actually just
[30:01] pull this up thankfully we have this
[30:03] nice contr F that we can use and let's
[30:06] go and quick look for that what file was
[30:08] that it's it's in it's in both of these
[30:10] files so this is great right uh thanks
[30:12] to our meta prompt and our prompt it
[30:14] actually you know respected this output
[30:16] format we want to see every file and
[30:19] every instance of this issue and it
[30:21] found it in both of these files if we
[30:23] search for each async which it gave us
[30:25] here with a contrl f lookup um we can
[30:28] see both of these issues here right so
[30:30] we have this four each async Loop and
[30:33] yeah okay that's that's a bug that's a
[30:37] bug um you can see here we're not ever
[30:39] awaiting the results here and that means
[30:43] that is loading will arbitrarily just
[30:45] fire off so it found it there and it
[30:47] also found it I assume I just kind of
[30:49] blazed through this and so it also found
[30:52] it here probably just copy and paste it
[30:53] via an AI coding prompt so you can see
[30:56] here we are actually getting some
[30:57] concrete Val out of this prompt that was
[30:59] generated by our meta prompt that we

### Minute 31

[31:01] then pass back into 01 um you can see
[31:04] here we have some smaller lower quality
[31:06] lower tier issues here lower severity um
[31:09] fantastic right let's hop back over to
[31:12] 01 prom mode and let's work through
[31:14] everything that it gave us here you can
[31:15] see here uh we have quite a bit more
[31:17] information this took a minute 34
[31:20] seconds so this took about three times
[31:22] longer to run let's just copy out
[31:23] everything here and let's look at the o
[31:28] 1 prom mode so we do have some js here
[31:31] let me just go ahead and do this we can
[31:33] see 01 prom mode picked up on that same
[31:35] message content issue picked up on the
[31:37] same for each async but so this is
[31:39] another issue that was caught here looks
[31:41] like an additional issue on an empty
[31:44] array when calculating okay recommended
[31:46] fix um or you want to check to see if
[31:48] the array is empty before calling
[31:50] math.min makes sense this is kind of
[31:52] nice it gave us more example code on how
[31:55] to fix the issue exactly if we look at
[31:57] our bug analysis prompt here that is

### Minute 32

[32:00] kind of what we were looking for here
[32:02] right we didn't explicitly say in our
[32:04] examples you know show code as well but
[32:07] 01 PR mode went ahead and generated
[32:09] output code for us the the theme Here of
[32:11] 01 prom mode being just a little bit you
[32:14] know giving you a slight edge here um I
[32:16] think is continuing it's giving us some
[32:18] nice code breakdown couple other issues
[32:20] there fantastic we don't need to you
[32:22] know dig too much into
[32:25] this in terms of which model is better
[32:28] and if you need chat GPT Pro to me the
[32:31] answer is very clear if you are a kind
[32:34] of super pro user of compute reasoning
[32:39] models large language models like myself
[32:41] then 01 Pro mode is kind of a no-brainer
[32:44] must have this puts you closer to the
[32:46] edge of what's possible even if it's
[32:48] just marginal gains right an important
[32:51] thing to call out here as well openai
[32:54] did explicitly mention that they're
[32:55] going to be uh adding more powerful
[32:59] compute intensive productivity features

### Minute 33

[33:00] to this plan the first version of
[33:02] something is always a little rougher on
[33:04] the edges it always kind of seems like
[33:06] uh it's good but is the value really
[33:08] there they will be adding more to this
[33:10] right so that's something important to
[33:11] highlight the question of whether you
[33:14] should really buy chbt Pro is really you
[33:17] know how far are you really pushing
[33:19] compute and do you understand what it
[33:21] can do for you this is something that I
[33:23] that I try to aim to reveal and Aid
[33:25] other Engineers like yourself with is
[33:27] really trying to push what you can do
[33:30] with compute with llms with prompts
[33:32] there's so much value so much untapped
[33:35] value here with all these incredible
[33:37] releases coming out from open AI the
[33:39] question is can you tap into it do you
[33:42] know how to write highquality prompts do
[33:45] you know how to use Advanced Techniques
[33:46] like prompt chaining and meta prompts do
[33:48] you know which model do you need to do
[33:50] the job are you constantly pushing your
[33:53] capabilities are you constantly asking
[33:55] okay I know how I would do this but can
[33:58] I pass off to an llm what's the prompt

### Minute 34

[34:00] look like what if I built it into an AI
[34:03] agent what if I made this part of my
[34:05] collection of prompts and tools and
[34:08] accessed it all through a single unified
[34:11] personal AI assistant right what if I
[34:13] made this entirely agentic what if this
[34:16] worked on its own by itself without my
[34:18] intervention these are all ideas we
[34:20] discuss on the channel quite a bit this
[34:22] is where we're headed on the channel um
[34:24] it's all about building up these larger
[34:27] pieces of of compute and of prompts
[34:29] right The Prompt is the fundamental unit
[34:32] of knowledge work right this is kind of
[34:33] our theme tagline for the indid dev Dan
[34:36] Channel and for the generative AI age as
[34:39] a whole The Prompt is everything you
[34:41] know in this video we've discussed the
[34:42] meta prompt we've compared you know two
[34:45] new Innovations from open AI the full 01
[34:48] model 01 Pro mode it's all building up
[34:52] it's all stacking on top of each other
[34:54] the only question is can you use the
[34:56] compute video after video we focus on
[34:59] how can we best use this compute I have

### Minute 35

[35:01] a ton of exciting content um focusing on
[35:04] that key idea The Meta prompt is a
[35:07] really really key concept because it
[35:08] allows your AI agents to write prompts
[35:10] for you based on specific scenarios
[35:13] right so this is a really big uh
[35:15] Advanced idea I wanted to share that
[35:16] with you here on the channel I think
[35:19] Chach bt01 Pro mode is definitely worth
[35:21] it if you're really pushing what you can
[35:23] do with generative AI I think for
[35:27] probably 9 95% of Engineers product
[35:29] Builders 01 will suffice for most of
[35:31] your cases there will be some gains that
[35:34] will be left on the table by not having
[35:36] 01 prom mode and I think that's okay as
[35:38] long as you understand the trade-off
[35:40] right the way I measure it 01 prom mode
[35:42] is anywhere from 0o to about 20% better
[35:46] on a prompt by prompt basis that's my
[35:49] understanding of prom mode thus far
[35:51] after just 3 days of using it so we'll
[35:53] see where this goes I'll be of course
[35:55] reporting on all of the releases from
[35:57] open AI over this week and the next week

### Minute 36

[36:00] I'm super super excited about every
[36:01] release that they have coming um it's an
[36:03] incredible time to be an engineer and to
[36:06] be plugged into the generative AI space
[36:08] like we are here on the channel if
[36:10] you're not and you made it to the end
[36:12] definitely subscribe I'm super stoked to
[36:14] share new AI coding patterns based on
[36:17] these powerful reasoning models I'm sure
[36:19] we're going to get 01 through the API
[36:22] really soon here exciting news I am
[36:24] nearly complete with the AI coding
[36:26] course I've been building for engineers
[36:29] like you and viewers of the channel um I
[36:31] can't wait to share this with you we do
[36:32] have to wait for all the Innovation
[36:34] coming out of open AI to complete before
[36:36] I can ship this so you know maybe on the
[36:38] 13th day I'll be able to launch this
[36:41] foundational AI coding course but we'll
[36:44] see what open AI releases I have to make
[36:46] sure that I incorporate all the latest
[36:47] and greatest uh Technologies and more
[36:50] importantly ideas and patterns that may
[36:52] come out of their release so I have to
[36:54] wait for them to you know finish
[36:55] shipping everything finish re shaping
[36:57] the industry and then I can fully launch
[36:59] the AI coding course stay tuned for that

### Minute 37

[37:01] we'll have more AI coding coming on the
[37:03] channel that's it long one I hope you
[37:05] enjoyed this one if you made it to the
[37:06] end drop the like drop the sub this is
[37:08] an incredible time we're living in it's
[37:10] a great time to be an engineer and a
[37:12] builder stay focused keep building and
[37:15] I'll see you next week