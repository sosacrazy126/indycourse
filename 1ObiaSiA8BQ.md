# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=1ObiaSiA8BQ
- **Duration:** 24:41
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 4635
- **Transcript Generated:** 2025-03-30 23:49:02

## Transcript


### Minute 0

[00:00] the developer experience around
[00:02] benchmarks is let's just say rough to
[00:06] terrible they're always cherry-picked
[00:09] and often leave out the true competition
[00:12] and it's hard to understand how a model
[00:14] truly performs when you take into
[00:17] account speed price and performance
[00:20] bundled together with the release of
[00:22] claud's 3.5 H coup and open AI predicted
[00:26] outputs we need a benchmark that we can
[00:29] really feel to understand and digest the
[00:33] cost Speed and Performance of these
[00:35] Technologies compared to existing llms
[00:39] so I wanted to take another crack at
[00:40] this and I built a simple tool that can
[00:43] be used to get a decent understanding of
[00:46] model performance speed and cost by
[00:48] looking at the simple use case of single
[00:51] word autocompletes across large language
[00:54] models as you know Claude 3.5 haou is
[00:58] interestingly priced let's see of the

### Minute 1

[01:00] performance cost and speed of the new
[01:03] claw 3.5 model and the new predicted
[01:06] outputs feature from open AI is really
[01:08] worth your time and
[01:10] [Music]
[01:13] money if we type in analyze into our
[01:16] input field after 2 seconds it's going
[01:20] to fire off a debounced autocompletion
[01:22] call to every single llm we have listed
[01:26] in this table so we have this completion
[01:28] for every single model fired off thanks
[01:30] to our prompt which we'll get to in a
[01:32] second and you can see a bunch of useful
[01:34] metrics alongside this let's go ahead
[01:36] and break these down execution time if
[01:38] we go ahead and just sort this you can
[01:40] see which models were actually the
[01:42] fastest for this response the total time
[01:45] is going to keep track of the sum of all
[01:47] of our execution times we have the
[01:48] execution cost and this of course is
[01:50] going to keep track of our cost for
[01:53] every run of this prompt our total costs
[01:55] is going to be the sum of our costs and
[01:57] then we have this really interesting
[01:59] column relative cost is super

### Minute 2

[02:02] interesting and it's been helpful
[02:03] already for me just to set the stage to
[02:06] how aggressively some of these llms are
[02:09] priced you can see our cheapest model
[02:12] Gemini 1.5 flash 8B is our cheapest
[02:16] version so we're going to say that this
[02:17] costs you know 100% from there
[02:19] everything scales up Gemini 1.5 flash is
[02:22] going to be two times more expensive
[02:24] right 2.1 times more expensive to be
[02:27] precise and then things go kind of you
[02:29] know Bonkers from there with the most
[02:31] expensive model that we're comparing
[02:33] today claw 3.5 Sonet latest is going to
[02:36] be 100 times more expensive than Gemini
[02:40] 1.5 flash 8B that's pretty wild and as
[02:44] we look through this you know one of the
[02:46] big takeaways from this video is going
[02:48] to be wow there are some really
[02:50] incredible lowcost highpe Speed high
[02:53] performing models that are really worth
[02:56] spending more time looking at and
[02:58] utilizing so anyway relative cost is

### Minute 3

[03:00] going to be really important we have
[03:01] that and then we have actions so actions
[03:03] is simple if one of our completions
[03:05] makes an error we can simply downvote it
[03:07] so that we can mark them incorrect so by
[03:09] down voting a model for one of its
[03:12] completions we can quickly just analyze
[03:14] the performance that's all of our
[03:16] columns let's go ahead and run a few
[03:17] more examples and then let's look at how
[03:19] this simple autocomplete prompt actually
[03:21] works I'm going to save the results as
[03:23] we go along here this is just saving
[03:24] into local storage and let's run another
[03:26] Auto completion so let's go ahead and
[03:28] type calc and let's see our models fire
[03:31] off you can see after a 2C debounce
[03:33] we're getting a bunch of responses and
[03:34] now we have some bad completions uh
[03:38] flash 8B made a mistake we're going to
[03:40] go ahead and dock a point we can see
[03:42] mini and mini predictive this is using
[03:44] the new predictive outputs also made a
[03:46] mistake so we're going to go ahead dock
[03:48] from those two and everything else
[03:50] nailed it let's run update and we should
[03:53] get this new update so you can see
[03:55] everything getting streamed in there and
[03:57] update inventory that's perfect so this
[03:59] is the you know completion we're looking

### Minute 4

[04:01] for go ahead and dock 8B this should be
[04:04] update inventory and doc from Gemini Pro
[04:07] some key differences in model
[04:08] performance already let's go and run one
[04:10] more here if we run send we should get
[04:12] an auto completion here send
[04:14] notification okay not bad Hau Hau taking
[04:17] quite a bit of time there right 3
[04:19] seconds almost 4 seconds let's going in
[04:21] Doc gbg4 and four predictive um although
[04:25] we can see some interesting data here
[04:27] GPT 40 is running really quickly let's
[04:29] go and sort execution time for that run
[04:31] we can see you know some pretty
[04:32] interesting results actually across the
[04:34] board our slower models in general at
[04:37] the bottom here you can see you know
[04:39] Sonet and the latest IU uh they're
[04:41] taking quite a bit of time you know our
[04:43] total time is quite High here but you
[04:45] can see that they're correct over our
[04:48] you know very small very minuscule
[04:50] sample size of four you can already see
[04:52] some deviation in correctness but we can
[04:54] see here 40 and 40 mini are running
[04:58] incredibly fast in the not T here I have

### Minute 5

[05:00] some details about the application the
[05:02] models were running uh some of the
[05:03] features but most importantly some
[05:05] limitations right this is not a perfect
[05:07] Benchmark there is no such thing as a
[05:09] perfect Benchmark you know there's
[05:10] Network latency I could be closer to
[05:13] open AI models geographically resulting
[05:16] in you know higher performance speed
[05:17] wise I'm not taking into account
[05:19] Gemini's price increases after 128k I'm
[05:23] not including any token caching cost
[05:25] saving so there are ways to improve this
[05:27] Benchmark this is just a general purpose
[05:29] quick ad hoc way to understand models so
[05:32] we're getting some interesting results
[05:34] already we can see our slowest model in
[05:37] total time is surprisingly our ha cou
[05:42] latest 3.5 ha cou is the slowest model
[05:46] which is not right uh to be fair again I
[05:49] have a really small sample size here
[05:51] let's go ahead and look at the prompt
[05:53] and then let's run some more autoc
[05:55] completions so that we can get our
[05:56] numbers up a little bit and you know
[05:57] make these make these numbers make a
[05:59] little more sense hopefully switch over

### Minute 6

[06:00] to the prompt Tab and one of the
[06:03] important use cases I needed solved for
[06:06] in a benchmark like this is I needed it
[06:09] to be dynamic so we can come in here and
[06:11] adjust this and then rerun our Benchmark
[06:13] our prompt will include the updated
[06:16] information here that we change how does
[06:18] this work how does this prompt actually
[06:19] work and we can go ahead and pull this
[06:21] out into a code editor this is a simple
[06:24] single word autocomplete prompt the idea
[06:26] here is we pass in some instructions our
[06:29] completion content and then our input
[06:31] text right so this is the user input our
[06:33] completion content is what we're going
[06:35] to autocomplete against and then of
[06:37] course our instructions breaking down
[06:39] exactly how to do this the most
[06:41] important thing here is that we are
[06:42] replacing the last word in the input
[06:45] text and then we have an example of what
[06:47] that actually looks like so this is the
[06:49] prompt it's quite simple the key idea
[06:51] for this Benchmark is to create a
[06:53] concise prompt that has a yes no
[06:56] validatable response just by looking at
[06:59] our single words and by seeing the

### Minute 7

[07:01] responses of every model in our
[07:03] Benchmark we can just say you know
[07:05] thumbs up thumbs down this is correct
[07:07] this is not correct and this gives us a
[07:09] simple way to compare models against
[07:11] each other and basically extract the
[07:14] information like runtime cost relative
[07:17] costs and a light performance Benchmark
[07:20] so let's go ahead and make a tweak to
[07:21] this we can add a couple more items here
[07:24] since this is fully reactive I can come
[07:26] in here and just say something like this
[07:27] I can say user list set that to an empty
[07:30] array um it's also important to know
[07:32] that this can be anything I just happen
[07:34] to be completing on um code you know
[07:37] this is like simple python code so we're
[07:39] mocking like a autocomplete application
[07:42] for a coding assistant but this could
[07:43] really be anything you can autocomplete
[07:45] phrases sentences help documentation API
[07:48] documentation really anything you want
[07:49] to again the goal is to create a simple
[07:52] prompt that you can quickly validate and
[07:54] compare your llms and new llm techniques
[07:58] like predicted outputs against so let's

### Minute 8

[08:00] go ahead and finish up here we'll say
[08:02] tax rate and we'll just set that to 0.10
[08:06] and we'll create a new function right so
[08:07] confirm user sale pass and user and
[08:10] we'll just do the same as we have below
[08:13] here right we'll just say pass we don't
[08:14] really care um about the implementation
[08:16] detail because we're just running the
[08:17] simple autoc completion so this prompt
[08:19] is complete it's reactive it's
[08:21] automatically updating here and if we
[08:23] hit save if we type something like tax
[08:27] we should see our Auto completion come
[08:29] through some of these cases so very
[08:32] interesting apparently this was a hard
[08:34] one to complete only Sonet got this one
[08:37] right so let's go ahead and dock a bunch
[08:38] of points here so down down doc doc doc
[08:42] doc doc doc when our llm responds with
[08:45] none this is one of our uh instructions
[08:47] the input does not make sense it will
[08:49] try to autocomplete uh with none so
[08:52] maybe I'm being a little unfair there
[08:53] let me go ahead and try to give it a
[08:54] little bit more help and I'll type
[08:56] underscore here and let's see how we do
[08:57] now so after 2 second debounce there we
[08:59] go so we got got a lot more improved

### Minute 9

[09:00] answers there I'll dock from flash 40
[09:04] and 40 predictive and we'll just keep
[09:06] rolling so use your list so I'll just
[09:08] type USC and let's see if we get a nice
[09:10] auto complete here after the 2C debounce
[09:12] okay nice right so you can see some
[09:14] results coming in dock these so just
[09:17] removing some points there go ahead and
[09:18] push this a little further let's try
[09:20] with an R let's see if we can get the
[09:21] user list
[09:24] here okay so a little bit better Haiku
[09:27] making a mistake there we have
[09:30] AB mini predictive mini predictive
[09:33] making a mistake you can see quite
[09:35] clearly who the the winner is if we sort
[09:38] by you know success it is good to see
[09:40] that you know for everything you're
[09:42] paying with Sonet Sonet is still the
[09:44] best model overall of course I'm
[09:47] excluding reasoning models reasoning
[09:49] models are frankly in their own entire
[09:51] category we need to think about how to
[09:53] Benchmark those in a you know different
[09:55] class of their own gen let see what our
[09:58] results look like here

### Minute 10

[10:00] nice so everyone nailed that generate
[10:02] invoice let's go ahead and run update so
[10:06] we have this update here maybe I ran
[10:08] that one not sure we'll dock a point
[10:10] from AP flash here 40 40 predictive and
[10:15] what else do we have we also have our
[10:17] noncase so if there's no logical
[10:20] completion that can be made based on the
[10:22] last word we return none so let's go and
[10:24] just type in some nonsense abc123 and
[10:27] now we should get none responses from
[10:29] from all of our models there we go
[10:31] perfect perfect and we can just you know
[10:33] continue typing in complete nonsense and
[10:36] great so love to see that how many runs
[10:38] do we have here so we have 12 runs total
[10:41] let's try to trick up Sonic just a
[10:43] little bit so I'm going to type Cal and
[10:46] either one of these responses will be
[10:47] acceptable let's just go ahead and type
[10:49] Cal and see what we get here there we go
[10:51] okay yeah so great responses overall all
[10:53] Doc The Flash and mini predictive here
[10:57] and we have calculate discount that's
[10:59] fine the rest are calculate total so

### Minute 11

[11:01] this all looks great so far and you can
[11:02] kind of see where this is going right we
[11:04] have a quick ad hoc way to look at the
[11:06] performance of multiple models against
[11:09] each other running in parallel we're
[11:11] tracking the results the costs comment
[11:13] down below what you'd like to see in a
[11:16] live Benchmark like this it can be
[11:17] anything from stats to individual
[11:20] features I think the next most obvious
[11:22] feature to add here is a list of dynamic
[11:25] models right basically a multi- select
[11:27] list where we can you know choose all
[11:29] these I have all these hardcoded in the
[11:30] codee base because these were the only
[11:32] models I wanted to look at and compare
[11:34] so let me know what you want to see in a
[11:36] benchmark like this and I'll plan it for
[11:38] a future video with the new Macbook
[11:41] releases I think we're going to have to
[11:43] be paying a lot more attention to local
[11:46] models like And subscribe so that you
[11:48] don't miss that Benchmark we will be
[11:50] getting a new Fresh high-end MacBook Pro
[11:54] with the M4 chip I'm really really
[11:55] excited for that to show up when that
[11:57] does we're going to run a bunch bunch of
[11:59] benchmarks using tools like this to

### Minute 12

[12:02] really compare and see how are local
[12:04] models doing in comparison to the you
[12:07] know high class cloud provider models so
[12:10] stay tuned for that like And subscribe
[12:12] so you don't miss those videos decent
[12:14] number of results here let's go ahead
[12:16] and look at some interesting insights
[12:19] [Music]
[12:21] right let's look at total time to
[12:23] execute I would expect ha coup to be one
[12:27] of the fastest models here and what
[12:29] we're seeing is it's the slowest model
[12:32] something is going wrong there to give
[12:34] hku some Grace uh we do have it
[12:37] performing really really well so you can
[12:39] see here out of our 13 requests uh Sonet
[12:42] of course in first place making zero
[12:44] mistakes across this Auto completion we
[12:46] have 1.5 Pro performing next best and
[12:49] it's tied with Haiku so that is good to
[12:52] see right it is good to see that hku is
[12:54] a high performing model but you know
[12:56] previously I think part of a lot of the
[12:58] drama around the CL 3.5 H coup release

### Minute 13

[13:02] is that the price is just significantly
[13:05] higher than what we were expecting for a
[13:07] model like this right we were really
[13:09] expecting CL 3.5 hu to be a model on the
[13:13] level and on the speed well beyond the
[13:15] level but at the speed of models like 40
[13:18] mini and 1.5 flash right in the kind of
[13:22] fast series I like to put these models
[13:24] in their own kind of category it's the
[13:26] fast cheap intelligence what what we're
[13:29] actually seeing here in the data in The
[13:31] Benchmark is claw 3.5 haou is actually a
[13:36] a high tier High performing model this
[13:38] is really really interesting to see
[13:40] right when we look at the relative costs
[13:42] when you compare a claw 3.5 ha coup to
[13:46] even Gemini 1.5 flash it is something
[13:49] like 15 times more expensive and it's 30
[13:53] times more expensive than Flash B this
[13:55] is definitely something to take into
[13:56] account when you're selecting these
[13:58] models right you know when we look at

### Minute 14

[14:00] this data here when we look at even a
[14:02] small Benchmark like this and I
[14:04] definitely implore you and you know I
[14:06] definitely suggest you run your own
[14:07] every single Benchmark is flawed in some
[14:09] sense in some way I think there are
[14:11] interesting ways we can make this better
[14:13] we can do you know we can run each one
[14:14] of these models three times and take the
[14:17] best two out of three we can run
[14:19] multiple instances of each model you
[14:21] know there are many ways to improve uh
[14:24] the truth and to reduce the randomness
[14:26] of these models but nevertheless my
[14:28] notes on clot 3 5 I cou it's really like
[14:31] sonnet's little brother not that much
[14:33] smaller right we're talking like 2 years
[14:37] in age difference right like not little
[14:39] little brother just little brother we
[14:41] can see of course if we flip our
[14:43] relative costs we can also see something
[14:45] really interesting our 40 and 40
[14:48] predictive are quite pricey there are
[14:51] ways to improve this by the way I'm very
[14:53] sloppily passing in the entire prompt
[14:56] the code for this tool is in the
[14:58] description by the way I don't don't
[14:59] always have time to complete and ship

### Minute 15

[15:01] code bases to share with you for two
[15:03] reasons time or it's proprietary pieces
[15:06] in the code bases so if you ever don't
[15:08] see a code base after a video that's why
[15:10] anytime I can and when there's no IP in
[15:13] the code bases I'm working on I always
[15:15] like to share with you on the channel so
[15:18] just a note there um I know I've been
[15:20] getting some comments about where's the
[15:21] code base the codebase will be there 80%
[15:23] of the time 80% of videos 20% of the
[15:25] time it just cannot be there anyway so
[15:27] if you end up taking a look at the code
[15:29] you'll see that for the predictive GPT
[15:31] 40 and the predictive 40 mini I actually
[15:34] just pass in this entire prompt
[15:36] including the input text into the
[15:38] predictive variable and if we take a
[15:41] quick look at open ai's predicted
[15:43] documentation you can see here you pass
[15:45] in your prompt as you normally would but
[15:47] then you also pass in your prediction so
[15:50] I'm blowing up the context a little bit
[15:52] more than it needs to be I think
[15:53] autocompletes is an okay use of
[15:56] predicted outputs but I think really all
[15:59] I should be doing is passing in our um

### Minute 16

[16:01] completion content and not the you know
[16:04] instructions or the rest of the prompt
[16:06] basically so just a quick note there it
[16:08] is interesting to see though if we look
[16:10] at our price we do see a price increase
[16:12] between GPT 40 and 40 uh predictive
[16:16] right and same thing with mini right
[16:17] from mini it's about you know 100% more
[16:20] expensive and that's a very small amount
[16:23] to be uh completely Frank because the
[16:24] 100% is our base price which is our you
[16:27] know Gemini 1.5 flash 8B so there's a
[16:30] lot of interesting stuff here in the
[16:31] data let's look at the total time again
[16:32] I really just want to digest this on the
[16:35] fast end here we can see that 40 mini
[16:38] predictive and 40 predictive are the
[16:40] fastest across all of our runs right
[16:43] even though they made some mistakes here
[16:44] you know we're looking at 60% accuracy
[16:46] here it is great to see predictive
[16:49] running very quickly it looks like this
[16:51] is a real advantage that that you can
[16:53] gain from using predicted outputs so
[16:56] that's really good to see in a quick
[16:58] benchmark I am super curious why uh TP

### Minute 17

[17:02] 40 is the fastest maybe it's um usage
[17:06] maybe people aren't relying on 40 uh as
[17:10] the kind of go-to model for most cases
[17:12] I'm not really sure I could just be
[17:14] closer to a open AI server but with
[17:18] multiple runs we're going to see the
[17:19] times really start to average out
[17:21] interestingly we do see flash a bit
[17:23] slower than 40 so you know just an
[17:26] interesting note there a mini is coming
[17:28] in way slower than I'd like to see it on
[17:30] average uh 2 seconds slower than every
[17:33] 40 model so that's odd to see we do have
[17:36] to call up though 40 mini is very very
[17:40] cheap very very cheap you can see our
[17:42] three cheapest models right in the
[17:44] center here flash 8B Flash and 40 mini I
[17:48] think most of us were really hoping to
[17:50] see claw 3.55 coup in that cheap price
[17:53] bracket but it's just not that's just
[17:55] not the model they put out so when we
[17:57] look at the percentage correct there's a
[17:59] pretty clear pattern here for the most

### Minute 18

[18:01] part you know I would expect flash 8B to
[18:04] perform the worse here so it is you know
[18:06] good to see that the cheapest and one of
[18:08] the fastest models should be performing
[18:10] the worst right that's just the
[18:12] trade-off that we're making right now in
[18:14] the llm Eos system if you have a fast
[18:16] cheap model it's likely going to perform
[18:18] worse and this is why local models
[18:20] haven't really taken off in a major way
[18:23] yet unless you have a massive rig they
[18:25] just cannot perform at the more
[18:27] difficult tasks and any meaningful way
[18:30] when we move up the ladder here we can
[18:31] see a big kind of 60% range all of the
[18:35] kind of fast predictive techniques and
[18:39] models are kind of all in this 60% range
[18:42] I would expect gbg 40 to be in the
[18:44] higher tier of performance but we don't
[18:46] really see that it feels silly to
[18:47] continuously caveat but this is a very
[18:49] small sample size 10 13 runs is not
[18:52] significant definitely be something we
[18:53] improve on in future videos running
[18:55] probably 20 30 to 100 of these is going
[18:58] to get us better sample sizes but it's

### Minute 19

[19:00] still interesting to look at and you
[19:02] know just kind of think about how we can
[19:03] dissect performance versus cost versus
[19:07] speed and then we have our kind of top
[19:09] three high- hitting models here claw 3.5
[19:12] ha coup pro version two and then of
[19:14] course Sonet I do love seeing Sonet just
[19:17] remain at the top of every chart this is
[19:20] the improved version also it may have
[19:21] been helpful to add the previous onet
[19:23] although honestly I think they both
[19:25] would get 100% with this relative cost
[19:27] pricing like if we just sort relative
[19:29] cost here Sonet better
[19:31] be it better be the best you know just
[19:34] because within this price range um Sonet
[19:37] is quite expensive when you compare it
[19:39] to any you know cheaper model it just is
[19:43] very expensive so if we sort total costs
[19:45] here you know pretty obviously about 1
[19:47] cent here predictive also hitting about
[19:50] a Cent and then we get down to 40 just
[19:52] under a scent and then it you know
[19:54] pretty rapidly falls off from there
[19:56] again it is a a bummer to see how at
[19:59] this price I think the important thing

### Minute 20

[20:01] to note here with Haiku is it's not in
[20:03] that class of cheap fast models anymore
[20:05] it just isn't it's also not fast right
[20:08] if we sort by runtime for whatever
[20:11] reason Haiku is the slowest model here
[20:13] so um anyway that's enough time to ramp
[20:16] I'm I'm starting to go in circles
[20:17] looking at this small sample size of
[20:19] data you know couple things to note here
[20:20] having a reactive benchmarking tool like
[20:23] this where you can quickly test out new
[20:25] capabilities for with Dynamic prompts
[20:28] against existing llms is super valuable
[20:30] for understanding not just model
[20:32] performance but cost and speed as well
[20:34] right those are the three kind of top
[20:36] level benchmarks that really matter with
[20:38] models and model techniques like
[20:40] predicted outputs it's performance cost
[20:43] and speed you know this Benchmark as I
[20:45] mentioned several times it's not perfect
[20:47] we can go ahead and run another one
[20:49] right you know sometimes the models will
[20:50] get things right sometimes they'll get
[20:52] them wrong that happens and you know
[20:54] it's not a massive deal all of our
[20:56] models got this one right on average you
[20:59] know as we scale this up I think we'll

### Minute 21

[21:01] see for this prompt the numbers I was
[21:03] seeing you know you get past 20 30
[21:06] sample size everything pushes up above
[21:09] 70 80% correct so all the models in this
[21:13] list at least are quite capable the one
[21:15] exception maybe is 8B just because it's
[21:18] so small it's packing a lot of
[21:19] intelligence at a fantastic price um so
[21:22] it's bound to make some mistakes right
[21:24] from this Benchmark we can see Haiku is
[21:26] good but you have to make sure it's
[21:28] worth the costs especially when you
[21:30] compare it to other models right if we
[21:32] resort our costs here you can see the
[21:34] relative pricing in a really blunt
[21:36] forward way right starting at flash 8B
[21:40] that's our base price of you know just
[21:42] fractions of a fraction of a fraction of
[21:44] a scent which is just beautiful to see
[21:47] flash bumps it up quite a bit mini
[21:49] triple the price uh mini predictive four
[21:52] times the price and then all of the
[21:53] sudden Hau is charging it's a dollar per
[21:56] million tokens right yeah dollar per
[21:59] million tokens and as you can see that

### Minute 22

[22:02] really kicks up the price right it it
[22:04] just really explodes these cheap fast
[22:07] models contain incredible intelligence
[22:10] fast intelligence at a really really
[22:12] cheap price so definitely a clear
[22:14] takeaway from running experiments like
[22:16] this is that we should probably be
[22:18] leaning on these fast models a little
[22:20] bit more another takeaway it's pretty
[22:21] clear that CL 3.5 Haku is not a cheap
[22:25] fast model it is a high- performing
[22:27] slower model model um much like claw 3.5
[22:31] Sonet but just a tier below claw 3.5
[22:33] Sonet uh we can see 1.5 Pro performing
[22:36] quite well it is interesting to see you
[22:39] can think of claw 3.5 H coup and 1.5 pro
[22:43] at about the same level right they
[22:45] scored the same and they have nearly the
[22:47] same price so again small experiment you
[22:50] want to add more data to this and most
[22:52] importantly you want to test against
[22:53] your use cases to make it all really
[22:55] make sense you know when we sort by just
[22:58] pure performance if all you care about

### Minute 23

[23:00] is getting the job done right no matter
[23:02] the costs the answer is still very
[23:04] clearly Claude 3.5 Sonet followed by Pro
[23:09] and followed by Hau a note on predictive
[23:12] outputs it does seem to be if we sort
[23:16] let's go ah and sort by model here if we
[23:18] look at the um 40 mini predictive we do
[23:22] see a small pretty much non-existent um
[23:25] performance hit again we need more data
[23:27] to really show that that's meaningful
[23:29] and we see a slight price increase but
[23:32] what we'll notice here generally is that
[23:35] the predictive models are quite a bit
[23:38] faster especially for mini we may have
[23:40] had some data flukes here with the 40
[23:43] model 40 is fast foro predictive is fast
[23:46] and many predictive seems to be
[23:48] extraordinarily fast so these are all
[23:50] preliminary notes you know like all
[23:52] benchmarks take this with a grain of
[23:53] salt and be sure to test as many times
[23:56] as you can against your specific use
[23:58] case that's the only Benchmark that

### Minute 24

[24:00] matters in the end I recommend Gathering
[24:03] hundreds of prompts and expectations for
[24:06] each prompt and then you can really see
[24:08] how the models perform drop a comment
[24:11] let me know what you want to see in
[24:12] benchmarks like this moving forward if
[24:14] there are any models or features that
[24:16] you want to see I'll make a plan for a
[24:18] future video where we dig into more
[24:20] benchmarks like this if you want to dive
[24:22] into this this code is going to be
[24:23] linked in the description for you to
[24:24] check out and test subscribe if you want
[24:26] to stay up todate on useful ways to
[24:28] digest new llms and new features so that
[24:32] you can better understand what you can
[24:34] do in the age of generative AI stay
[24:37] focused and keep building