# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=K5xs669ANQo
- **Duration:** 23:42
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 4543
- **Transcript Generated:** 2025-03-30 23:48:43

## Transcript


### Minute 0

[00:00] you've probably already been swarmed
[00:01] with tons of hype alarmist click bity
[00:05] videos about 03 mini deep seek and the
[00:09] US tech ecosystem falling apart let's
[00:13] push through the narrative and hype and
[00:15] focus on how 03 mini is a differentiated
[00:19] model that can help us accomplish real
[00:21] engineering work like every model 03 has
[00:26] tradeoffs in this video we'll break them
[00:28] down and all share my three-step process
[00:31] I use to understand new models at a
[00:34] fundamental level Vibe compare eval
[00:38] instead of asking O3 mini to solve
[00:41] riddles for us and to do arbitrary
[00:43] problems that don't actually create
[00:45] value let's use o03 mini to solve a
[00:48] legitimate
[00:50] [Applause]
[00:52] problem meta fourth quarter and full
[00:55] year 2024 report were just published and
[00:58] that means we can extract

### Minute 1

[01:00] key information to help us inform
[01:03] potential investment decisions we'll
[01:05] start by taking a look at metas Q4
[01:07] earnings call transcript let's go ahead
[01:10] and open up our brand new reasoning
[01:12] model and compare it side by side we're
[01:14] going to look at 03 mini in high
[01:16] reasoning mode next to the previous
[01:18] state-of-the-art so how we're going to
[01:20] extract information from this earnings
[01:23] call we're going to use a prompt that I
[01:25] built here this is a 12K token prompt in
[01:28] a highly structured XML format you can
[01:30] see here we have the quarterly report
[01:32] here and then we have a unique structure
[01:35] here that we'll break down in a second
[01:36] for now I'm just going to copy this and
[01:38] paste it in 01 and 03 mini in high
[01:42] reasoning effort mode and we'll just
[01:44] kick these off side by side so while
[01:46] these are running let's break down the
[01:48] stats of 03 mini next to the previous
[01:51] state-of-the-art so the big headline for
[01:53] me when I'm looking at 03 mini is that
[01:56] it is effectively 01 at an eighth of the
[01:59] price

### Minute 2

[02:00] I think that's the most concise way to
[02:02] look at this model so just running
[02:03] through some insights here it's 8 times
[02:05] cheaper than 01 eight times more
[02:07] expensive than deep seek R1 important to
[02:10] note 03 mini maintains the 200k context
[02:15] window and the 100K Max output tokens
[02:19] this is absolutely incredible especially
[02:21] when you compare it to deepy car 1 when
[02:23] you realize it only has a
[02:25] 64,000 token context window and a measly
[02:29] 8K Max output tokens R1 is a great model
[02:33] for many many reasons most importantly
[02:35] the cost but this is something that if
[02:37] you're a advanced user of generative AI
[02:40] if you have large prompts if you have
[02:42] lots of information on the input and
[02:44] output side you likely ran into this
[02:47] issue as I did relatively early on with
[02:49] this model uh 64k and 8K out is very
[02:53] limiting a couple other insights more of
[02:55] a qualitative thing but O3 mini provides
[02:58] state-of-the-art instruction following
[02:59] I've never seen a model that follows

### Minute 3

[03:01] instructions better than o03 mini couple
[03:04] other key features reasoning effort lets
[03:06] us trade off speed and cost for
[03:09] performance I love this feature I want
[03:11] to see them add additional settings for
[03:12] reasoning effort I want more control
[03:14] here with how much the model is thinking
[03:17] okay and then on the speed side O3 mini
[03:19] is fastest um specifically when you're
[03:21] in low mode when you use medium and High
[03:23] um it's about as fast as o01 so again
[03:26] guys none of this is a take away from R1
[03:29] it's an incredible model but we just
[03:30] have to look at the stats okay my
[03:33] oneline summary for 03 mini is that it
[03:35] is 01 but 0 to 15% better at an eighth
[03:39] of the price with all the capabilities
[03:42] it's built to help you accomplish coding
[03:44] math reasoning planning and large
[03:46] context tasks let's return to our result
[03:50] here let's see what our meta quarterly
[03:52] report parsing prompt has returned for
[03:55] us so we can see a nice markdown
[03:57] formatted blob coming out of 01 and then

### Minute 4

[04:00] on the 03 mini high side you'll see
[04:02] something interesting this is more
[04:04] precise we explicitly ask for a Json
[04:06] response and O3 mini is being more
[04:09] precise and let's take a look at the
[04:10] result and the prompt we use to get this
[04:12] result so this is really cool this is
[04:14] something that only powerful reasoning
[04:16] models can do what we have here is
[04:18] effectively a list of prompts you can
[04:21] see the purpose here right given a
[04:22] quarterly report extract the information
[04:24] requested and the information to extract
[04:27] so we have this Dynamic variable that we
[04:28] filled out and let's just start top to
[04:33] bottom we're looking for total revenue
[04:36] for quarter so if we look at this prompt
[04:38] search this you can see that that
[04:40] information was parsed perfectly we can
[04:43] copy this and go over to meta's
[04:46] quarterly earnings call you can see Q4
[04:49] total revenue was
[04:51] 48.4 billion all right so our prompt
[04:54] running on 03 mini parsed that out for
[04:56] us perfectly and so you can see this
[04:58] prompt is a effectively a Json object

### Minute 5

[05:01] where the keys and the values are
[05:03] themselves prompts that we want a
[05:05] reasoning model to pull information out
[05:08] of the quarterly report for so if we go
[05:10] down the line here you can see we have
[05:11] llama 4 information we have speakers
[05:14] which is every speaker on the call we
[05:15] have your over your growth we have deep
[05:17] seek response I want to see Mark's
[05:19] thoughts on deep seek I have operator AI
[05:22] agent thoughts I want to get marks
[05:24] thoughts on open ai's operator and then
[05:26] we have the largest Department growth
[05:28] and in this list of prompts we can
[05:30] basically query anything we want in one
[05:32] shot and get precise answers thanks to
[05:34] the capabilities of the reasoning model
[05:37] if we just ask for one piece of
[05:38] information here this is something that
[05:40] a powerful base model like GPT 40 or clo
[05:44] 5 Sonet could definitely pull off and in
[05:46] a benchmark you'll see in a moment they
[05:48] can pull that off but when you start
[05:49] adding additional information and you
[05:51] start asking for the response to be
[05:54] itself a specific type of structure this
[05:57] is where reasoning models really shine
[05:58] right because they can iterate over your

### Minute 6

[06:00] instruction so anyway let's continue you
[06:02] know let's learn about Lama 4 Lama 4 is
[06:05] an advanced development Lama 4 mini has
[06:08] completed pre-training and its reasoning
[06:10] models as well as larger model are
[06:12] performing well so this is potentially
[06:15] really important news if we look at the
[06:16] call transcripts and we search mini we
[06:19] can find exactly where Zuckerberg is
[06:21] talking about llama 4 so we can scroll
[06:23] up here we can see you know Markus zberg
[06:25] CEO this is him responding talking about
[06:28] llama 4 saying here you know llama 4
[06:30] mini is done with pre-training and our
[06:33] reasoning models and larger model notice
[06:36] the plural there that's really
[06:37] interesting multiple reasoning models
[06:39] one plural One Mini are looking good too
[06:43] super interestingly our goal with llama
[06:45] 3 was to make open source competitive
[06:47] with closed Source our goal for llama 4
[06:50] is to lead okay very bold very bold we
[06:53] don't have a release date you can see
[06:54] here in the query I asked for three
[06:57] pieces of information here right llama 4
[06:59] in production expected release date

### Minute 7

[07:01] reasoning model right just really quick
[07:03] offthe cuff questions we can see
[07:04] speakers we can see year-over-year
[07:06] growth and deep secret response so
[07:08] something really interesting about the
[07:10] list every speaker is that I actually
[07:12] asked the model inside this prompt to
[07:15] respond in a Json list with this format
[07:18] okay this is a really interesting
[07:20] capability that you can tap into with
[07:22] these powerful reasoning models this is
[07:24] not exclusive to o03 mini this is not a
[07:26] you know emergent capability that only
[07:29] O3 three many can do all reasoning
[07:30] models have this capability so respond
[07:32] in Json list and then we give it a
[07:34] format here right so name and Rule and
[07:36] if we look at the response here you can
[07:38] see speakers and we have all the names
[07:40] and all the roles right and this makes
[07:42] for a really really interesting
[07:44] Benchmark as you'll see later on in the
[07:46] video so you can see here really cool we
[07:48] have all the names all the roles we even
[07:50] got the operator right conference call
[07:52] Operator you have your growth 21% deep
[07:54] seek response Mark noted that deep seek
[07:56] has introduced several novel advances
[07:59] that meta is still ingesting okay so

### Minute 8

[08:03] some interesting information there C
[08:04] also asked for sentiment if we look back
[08:06] at the prompt I wanted you know at least
[08:08] three items in objects that look like
[08:10] this right I want sentiment and thoughts
[08:12] and know3 many understood this well and
[08:14] processed it he believes meta can learn
[08:16] from Deep seeks Innovation and
[08:18] potentially incorporate similar
[08:19] improvements into its own systems good
[08:21] stuff he mentioned that it's too early
[08:23] to definitively assess deep seeks
[08:25] long-term impact on infrastructure and
[08:27] capb backs so this is part of the reason
[08:30] the markets are in complete shambles
[08:31] right now deep seek came out at a very
[08:33] low price point um us companies are
[08:35] putting up models at a much much higher
[08:37] price point okay so you can see Mark
[08:39] explicitly mentioning that that's cool
[08:41] to see we're not going to focus on that
[08:42] too much we're here to get worked on
[08:44] we're here to understand model
[08:46] capabilities so then you can see here we
[08:48] have a guidance for next quarter good
[08:50] stuff his thoughts on the operator a
[08:52] browser agent that open AI released very
[08:54] interesting I've been talking about uh
[08:56] how we need new uis new uxs new systems

### Minute 9

[09:00] for interacting with our models that are
[09:02] not just a chat interface really looking
[09:04] forward to this and uh I'm working on a
[09:07] couple of my own very cool and then we
[09:08] have the largest Department percentage
[09:10] increase I thought this is really
[09:11] interesting information approximately
[09:12] 90% of the year-over-year headcount
[09:15] growth was concentrated in the research
[09:17] and development driven by aggressive
[09:19] hiring in technical areas such as
[09:20] infrastructure gen monetization reality
[09:24] lab so VR AR so this is a powerful
[09:26] prompt I'm going to link this prompt for
[09:28] you in the description deson it's going
[09:30] to be in a Guist so you can just try
[09:31] this out if you're interested find a
[09:33] quarterly report paste it in and then
[09:35] specify key value pairs that are
[09:37] effectively prompts themselves and then
[09:39] go ahead and run it against your
[09:42] favorite powerful reasoning model feel
[09:43] free to use this prompting technique
[09:45] where you effectively have a list of
[09:47] prompts within a prompt you can do a lot
[09:49] more than you think with these powerful
[09:51] reasoning models especially as they
[09:52] progress O3 many represents an
[09:54] improvement of what you can do inside of
[09:57] the prompt this is one of many prompt
[09:59] engineering and AI coding techniques we

### Minute 10

[10:01] explore on the channel like sub and
[10:03] comment to let the YouTube algorithm
[10:05] know you want more actionable
[10:07] information like this remember that we
[10:09] fired off both in 01 and in 03 mini
[10:13] prompts right if we copy 01 and just
[10:15] take a look at this side by side 01 03
[10:19] mini High see a couple of things here
[10:21] okay so 01 missed some speakers you can
[10:24] see it got the information about llama 4
[10:26] right so we have llama 4 we have mini we
[10:29] have we have reasoning and we have
[10:31] larger okay so it got all this so that
[10:33] looks great uh it missed a bunch of
[10:35] speakers you can see here 03 many found
[10:37] a bunch of speakers it got our
[10:39] year-over-year growth correct right we
[10:41] have 21 year-over-year solid responses
[10:44] for deep seek in that exact object
[10:46] structure we were looking for good to
[10:47] see and then it filled out our last
[10:49] three prompts here and it looks like
[10:51] they did a great job right nearly 90%
[10:53] year-over-year headcount growth okay so
[10:54] when you see this you can see that their
[10:56] outputs are fairly similar we can see
[10:58] that 03 mini High outperforms or1 just a

### Minute 11

[11:01] little bit in this single case and that
[11:03] brings us to you know the question you
[11:05] should be asking at this point after you
[11:07] run a couple Vibe checks after you run
[11:09] the new model a couple times what
[11:11] happens next now that we have an okay
[11:13] feel of the capabilities right it looks
[11:14] like it's doing work a little bit better
[11:16] than 01 how can we push this further how
[11:18] can we understand the model at a more
[11:21] intimate foundational level this is
[11:22] where we move to the second step in the
[11:25] three-step process First We Vibe check
[11:27] and now we're going to compare
[11:32] so we've already kind of done a small
[11:33] comparison here but let's scale this up
[11:36] so in the Second Step the comparison
[11:37] step when you're interested in the model
[11:39] and it has something to offer you that
[11:41] previous models did not right the vibe
[11:43] check is telling you there's something
[11:44] here there's something more to learn
[11:46] then you can take it to the next step
[11:48] which is the comparison step this is
[11:50] where we compare the model against a
[11:52] series of additional models okay so we
[11:55] start with a single node and now we're
[11:57] going wide right so now we have multiple
[11:59] nodes that we want to look into multiple

### Minute 12

[12:01] models that we want to compare so this
[12:02] is where a tool like thought bench from
[12:05] Beni comes in you can use any tool you
[12:07] want but basically you just need the
[12:09] capability of having multiple models
[12:11] running side by side we're going to do
[12:13] the exact same thing we have our
[12:14] quarterly report here we're going to
[12:15] paste this in and we're just going to
[12:17] run it something really awesome about
[12:18] the o03 mini series o03 mini gives you
[12:21] three reasoning level efforts low medium
[12:24] and high by default o03 mini is going to
[12:26] run in medium mode but you can see here
[12:28] our O3 Mini in low reasoning effort mode
[12:31] completed already right it's done now
[12:33] we're starting to look at multiple model
[12:35] responses we have 03 Min in low medium
[12:38] and high mode so if we just want to take
[12:41] a look at these three we can see that
[12:42] low mode dropped some of our speakers
[12:44] right we have those three speakers while
[12:47] medium and high gave us all of our
[12:49] speakers right if we look through this
[12:50] we have all of our speakers year overy
[12:52] year Revenue growth 21% across the board
[12:55] that looks great total revenue right we
[12:58] have that exact same number here across

### Minute 13

[13:00] the board that looks great and we can
[13:02] continue to look down the line right we
[13:04] can look at our 01 mini you can see 01
[13:07] mini giving us a nice response there
[13:08] formatted we have 01 across the board
[13:11] multiple models can perform this task
[13:14] okay looks like multiple mods are doing
[13:16] a decent job here once we get to deep
[13:17] seek we can see something kind of
[13:19] interesting we are kind of falling off
[13:21] the bucket a little bit here deep seek
[13:23] has split up our guidance and our
[13:26] operator AI agent thoughts into key
[13:28] value Pairs and our last uh key value
[13:31] pair here which is not what we asked for
[13:33] so we can see a little bit of deviation
[13:34] there and then as we scroll down away
[13:36] from the powerful models deep seek 32
[13:38] just had to run this on my device just
[13:40] to check it out and you can see it's got
[13:41] some Naas here it's got uh you know
[13:43] multiple things wrong here so obviously
[13:45] a much smaller model but we can see
[13:47] Gemini flash thinking um missing
[13:49] speakers but putting out a good effort
[13:51] here overall it nailed the structure and
[13:54] it looks pretty good right so step two
[13:56] in the process is to compare models side

### Minute 14

[14:00] by side when you're looking for brand
[14:01] new capabilities in models you need to
[14:03] compare them to the previous versions
[14:06] right and you need to compare them
[14:07] across all capabilities so here we have
[14:09] low medium and high so this is pretty
[14:11] straightforward right I don't need to go
[14:13] on about this much longer you can see
[14:14] exactly what we're doing here in step
[14:16] two We compare now step three is where
[14:18] things get really interesting after you
[14:20] Vibe check after you go wide now we go
[14:23] tall now we're adding a additional
[14:26] Dimension this is where we EV valve this
[14:27] is where we actually run
[14:29] [Applause]
[14:31] benchmarks and so for benchmarks of
[14:34] course um I've been building up Beni a
[14:36] suite of interactive benchmarks you can
[14:38] feel Link in the description we've
[14:39] covered this in a couple previous videos
[14:41] this is something I'm building up
[14:42] putting a lot of effort into right now
[14:43] because it's helping me gain insight
[14:45] into these models in a more interesting
[14:47] interactive way go ahead and drag in a
[14:49] completed Benchmark file this is the
[14:52] final stage in the benchmarking process
[14:55] once you run a Vibe check once you
[14:57] compare the model side by side to other
[14:59] models finally you run multiple models

### Minute 15

[15:02] against multiple use cases right
[15:04] multiple instances of the prompt so here
[15:07] if we run flash Benchmark we'll
[15:09] autocomplete everything and you can see
[15:11] we have multiple prompts running against
[15:14] multiple models okay and if we scroll
[15:16] all the way down here we can see our O3
[15:18] minis as expected and as we would assume
[15:21] we have O3 mini in high mode getting 96%
[15:25] correct with only one incorrect answer
[15:28] if we click into this we can see the
[15:30] prompt and the information Ed right so
[15:32] we have the expected result and we have
[15:34] the execution request okay so this is
[15:37] effectively the same prompt we have the
[15:39] meta quarterly earnings report pasted in
[15:42] here if we scroll all the way to the
[15:43] bottom here you can see the information
[15:45] we're extracting once you've gone to
[15:46] step one and step two most Engineers
[15:49] most Builders stop at step one some make
[15:51] it to step two but if you want to go all
[15:53] the way and dig deep and truly
[15:56] understand the capabilities of your
[15:57] models you need to set up benchmarks and
[15:59] EV valves and it doesn't matter how you

### Minute 16

[16:01] do it it doesn't matter what tool you
[16:02] use I'm not trying to sell you on my
[16:04] tool this is completely open source I'm
[16:06] building this in public just in case
[16:08] there are other Engineers that want to
[16:09] check it out use it get ideas from it so
[16:11] on and so forth you know the third step
[16:13] for truly understanding models in the
[16:15] generative AI age is evaluations you
[16:18] need to take a use case you're
[16:20] interested in and then you need to run
[16:22] multiple versions multiple use cases
[16:25] against multiple models okay this is
[16:28] super super important there's going to
[16:29] be a point where you can't do anymore if
[16:32] you don't Benchmark what you're trying
[16:34] to accomplish okay if you're not
[16:36] building a product if you're not using
[16:38] you know level four prompts with Dynamic
[16:41] variables I'll link our prompt framework
[16:43] video in the description so you can
[16:45] understand how to write high quality
[16:46] prompts if you're interested if you're
[16:47] not writing you know high quality
[16:49] prompts with information right with you
[16:52] know tens 20 50,000 plus tokens
[16:54] benchmarking probably doesn't matter for
[16:56] you and that's okay but if you are this
[16:58] is the most most important step for

### Minute 17

[17:00] scaling your impact for repeat prompt
[17:03] usage right for prompt templates for
[17:05] prompts that you're going to improve
[17:06] over time to solve a specific problem
[17:09] very well so that's why we Benchmark
[17:11] that's step three let's go ahead and
[17:12] take a look at some Data Insights so as
[17:14] I was scrolling down here you might have
[17:15] noticed something really interesting
[17:17] right GPT 40 got at 83% correct okay 25
[17:21] correct only five wrong to be super
[17:23] clear I have simplified The Prompt like
[17:25] I mentioned before only asking for you
[17:28] know one piece of of information it's a
[17:29] lot simpler I'm not asking for eight
[17:31] pieces of information right I'm not
[17:33] running eight prompts at once with you
[17:36] know structured responses inside the
[17:38] prompts okay this is a little bit easier
[17:40] right I've scaled down this Benchmark
[17:42] here I'm in the process here of adding
[17:44] some more complexity uh some more
[17:46] problems for 03 mini in high reasoning
[17:49] mode to handle because as you can see
[17:52] it's completely saturated this Benchmark
[17:54] right The Benchmark is is almost solved
[17:56] by o03 mini really cool to see that and
[17:58] we can see here 01 preview and 01

### Minute 18

[18:00] performing really well but look at this
[18:02] price tag right let's just zoom in on
[18:04] that price tag look at this right to run
[18:07] 30 prompts of 12K tokens each I'm
[18:10] burning s bucks here right and even more
[18:13] here we likely had more reasoning tokens
[18:15] here right so the total cost is so so so
[18:18] important when you're looking at these
[18:20] models and this is how you can really
[18:22] understand the value again benchmarking
[18:23] just allows you to understand models
[18:26] with more Dimensions we can also see the
[18:28] average duration here 01 preview you
[18:31] know 15 seconds on average 01 about 9
[18:34] seconds on average when we look at 03
[18:36] mini right we are seeing Our Time
[18:39] Savings come in here right both time and
[18:41] cost right let's look at that look at
[18:42] the cost uh 7 bucks for 03 40 cents okay
[18:46] 42 cents 03 mini medium 45 cents okay 03
[18:51] mini High 57 cents okay so you can see
[18:54] the step increase in both the low medium
[18:57] and high effort and and this is what we
[18:59] love to see right we love to see when

### Minute 19

[19:02] you know these blog posts these you know
[19:04] release posts actually back up what
[19:07] they're saying right you always want to
[19:08] see your benchmarks align at some level
[19:11] with what they're showing right even if
[19:13] it's a you know simpler use case data
[19:15] extraction Benchmark like this right we
[19:17] can still see that relationship you know
[19:19] no difference here in performance we
[19:21] paid a little bit more time and money
[19:23] here but then when we went to high mode
[19:25] our model turned on for us and it solved
[19:28] three additional problems out of 30
[19:30] right that's significant you know once
[19:32] you have a benchmark you can really
[19:34] start to improve the prompt at scale and
[19:37] really understand the capabilities of
[19:39] the model because you're seeing it side
[19:40] by side by side against models and
[19:43] against prompts right so if we go into
[19:45] this prompt here that 03 mini and high
[19:48] effort mode got wrong if we scroll down
[19:50] here let me zoom out you can see here it
[19:53] made one very silly mistake out of all
[19:55] the things to get wrong you can see here
[19:57] it returned 600 million instead of 700

### Minute 20

[20:01] million right so very silly very silly
[20:03] mistake I'll bet if I ran this again it
[20:05] would get that right and it would get
[20:07] something harder wrong um although you
[20:09] know if we look across what was correct
[20:11] and what was incorrect um this is what
[20:14] you want to see right you don't want to
[20:15] see 26 26 26 incorrect because that
[20:18] means something's probably wrong with
[20:20] The Prompt or the prompt itself is
[20:22] really difficult right it's a hard hard
[20:23] thing to answer what you really want to
[20:25] see is the variance and the
[20:27] non-deterministic nature of the models
[20:29] come through which looks more like this
[20:30] right 03 mini High mode it only got this
[20:33] one wrong medium Got 5 16 21 and 22
[20:37] incorrect right but then we go to low it
[20:39] got 1 17 30 and 23 wrong right so so I
[20:43] think it's good to see that versus
[20:45] saying you know something like this
[20:47] right you see problem one wrong 01
[20:50] preview got problem one wrong 01 got one
[20:53] wrong 01 mini also got one wrong right
[20:56] so on and so forth right this means that
[20:58] uh the models just cannot solve the

### Minute 21

[21:00] problem right and this is if we look at
[21:03] this problem this is a really
[21:04] interesting one too this is where we're
[21:05] saying list all the speakers and this is
[21:08] where we're asking for that list of
[21:09] speakers and I hope you can see why this
[21:11] is important right benchmarking gives
[21:13] you a deeper understanding Beyond model
[21:16] comparison side by side against one
[21:17] prompt and Beyond uh the vibe cheat
[21:20] which is just when we come in here and
[21:22] just play and type a couple things and
[21:25] and go oh wow it's amazing at five RS in
[21:27] Strawberry or whatever people are
[21:29] running right that's not how you
[21:31] understand model capabilities so this is
[21:32] really interesting um I'm a huge fan of
[21:35] open ai's work I do agree with the Bold
[21:38] statement Sam put out a while back it is
[21:41] much easier to copy than it is to
[21:43] innovate I'm not saying that R1 hasn't
[21:46] innovated they definitely have I'm not
[21:48] you know making a commentary on that but
[21:50] just in general overall they took the
[21:53] Transformers architecture from Google
[21:55] and they have created immense immense
[21:58] value with it and mostly you know 60 70

### Minute 22

[22:01] 80% everyone else is playing copy with a
[22:04] couple variants and again I'm not saying
[22:06] that's bad I'm not saying it's wrong I'm
[22:08] just saying that's the way it is right
[22:11] open AI as I predicted so far are the
[22:14] leaders we obviously want to see the
[22:16] price point come down I'm hoping we're
[22:18] going to see 03 base model come out
[22:21] something like five bucks per input and
[22:23] 10 bucks per output something you know
[22:25] more affordable than 01 but at the same
[22:28] time if these models are giving us
[22:30] state-of-the-art powerful capabilities I
[22:32] think paying the price is always worth
[22:34] it to understand what's coming next
[22:36] don't look at where the ball is look at
[22:38] where the ball's going prices are coming
[22:40] down reasoning capabilities are going up
[22:42] and models are becoming more accessible
[22:45] deep seek and 03 mini are both
[22:48] Testaments to that and it looks like
[22:50] meta is going to be following that up
[22:52] with llama 4 very very soon so first you
[22:56] run a Vibe check then you compare models
[22:58] side by side to each other so you can

### Minute 23

[23:00] see how they compare and then finally
[23:02] you run additional models with
[23:05] additional prompts the more variations
[23:07] of your prompt you throw at your models
[23:09] the better your benchmark is going to be
[23:11] and the better your understanding of the
[23:13] models are going to be okay not everyone
[23:16] has a ton of money to blow this is just
[23:18] one test and I literally torched $7 you
[23:21] know let me do the hard work you know
[23:23] let myself let uh other leading
[23:25] Engineers like Simon Willison and Paul
[23:28] the creator of Aer do the hard
[23:30] benchmarking work for you if you don't
[23:32] want to go all the way I completely
[23:33] understand all you have to do drop the
[23:35] like drop the sub stay focused and keep
[23:39] building