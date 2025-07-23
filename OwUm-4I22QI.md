# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=OwUm-4I22QI
- **Duration:** 37:56
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 6933
- **Transcript Generated:** 2025-03-30 23:48:48

## Transcript


### Minute 0

[00:03] [Music]
[00:28] [Music]
[00:59] for

### Minute 1

[01:15] [Music]
[01:23] [Music]
[01:48] what's up Engineers welcome back Andy
[01:50] Deb Dan here powerful local models like
[01:53] llama 4 are coming now the only question
[01:55] we have to answer is are we ready for
[01:58] them and more importantly how will we

### Minute 2

[02:00] know this is where benchmarking becomes
[02:03] Ultra important today we're going to
[02:05] look at the two most important metrics
[02:08] for local language models tokens per
[02:11] second and accuracy we're going to do
[02:13] this on my brand new M4 Max MacBook Pro
[02:17] this is a fully specked out
[02:19] top-of-the-line M4 as you'll see in this
[02:21] video on a top-end device like the M4
[02:24] Max the gbt 40 level models may already
[02:28] be here let's understand local llms and
[02:31] really slms at a fundamental level with
[02:34] benchmarks to prepare us for 202's local
[02:40] models so how are we going to Benchmark
[02:42] the M4 let's go ahead and open up
[02:44] everyone's favorite we're going to be
[02:45] using o Lama we're also going to be
[02:47] using a tool I'm building out called
[02:50] Beni Beni is all about building out
[02:52] benchmarks you can feel if we scroll
[02:55] down here you can see here we're running
[02:57] the Llama 3.21 billion parameter model
[02:59] model we have some stats and we have a

### Minute 3

[03:02] nice huge list of prompts that we're
[03:04] going to be testing against you can see
[03:06] here we're also going to be looking at
[03:07] llama 3.2 Falcon 3 54 this is an insane
[03:11] 14 billion parameter model we're going
[03:13] to dig into these stats in just a moment
[03:14] here and then of course we also have
[03:16] Quin 2.5 coder 14 billion parameters 32
[03:20] billion parameters then we're going to
[03:21] compare it all to a top and multi 100
[03:25] billion parameter model deep seek
[03:27] version 3 whenever I'm running these
[03:30] benchmarks I like to have a powerful
[03:32] control kind of cloud model to give me a
[03:34] good relative Mark of where local models
[03:37] really stand you can imagine these local
[03:39] models will always lag behind powerful
[03:42] Cloud models that can run on massive
[03:45] Nvidia GPU rigs so we're going to run
[03:47] this and if I hit play Benchmark here
[03:49] you can see this kind of kicking off
[03:51] automatically but before we look at all
[03:54] these stats and before we really dig
[03:55] into this let's just run a simple test
[03:58] so on the right here I have my M2 Max

### Minute 4

[04:01] MacBook Pro this was my previous primary
[04:04] developer device and I thought it would
[04:06] be cool to first you know take a step
[04:08] back start simple and just run the M2
[04:11] and the M4 side by side and to see if I
[04:14] really got my money's worth right I know
[04:16] a lot of people thinking about upgrading
[04:18] to these MCH devices are always
[04:19] wondering and comparing you know is it
[04:21] really worth it so in this video you're
[04:23] going to find out if upgrading to the M4
[04:26] is really worth it if you have an M2 and
[04:28] you're just looking for that local model
[04:30] performance let's open up the terminal
[04:32] on both sides here all we're going to do
[04:35] is run this prompt paste it in here and
[04:37] so we have this exact same prompt that
[04:39] we're going to run on both sides so
[04:41] let's break down this command piece by
[04:43] piece right we're running o l run llama
[04:45] 3.21 billion parameter we're running in
[04:48] verbose mode so that we can see our
[04:49] tokens per second then we have this
[04:52] simple AI coding prompt we want python
[04:55] code and we want our prompt to Output
[04:57] code exclusively and then we're passing

### Minute 5

[05:00] in this information dense function
[05:03] definition def csvs to SQL light tables
[05:07] then we're specifying two parameters for
[05:09] this function CSV paths and SQL light
[05:12] path the plural here is really important
[05:14] we're giving the model a lot of
[05:15] information just by passing in this
[05:17] function definition if you've taken
[05:19] principal AI coding you know exactly
[05:21] what this is and how this works if you
[05:23] haven't you'll see exactly what this
[05:24] prpt is going to do here in just a
[05:26] moment we have this running on both
[05:27] sides and all we're going to do here is
[05:29] hit enter at the exact same time so here
[05:31] we're going to be looking at one of the
[05:33] two most important metrics for local
[05:35] language models tokens per second we'll
[05:38] get to the second metric when we look at
[05:40] our Benchmark Suite but let's go ahead
[05:41] and just fire this off and let's see the
[05:43] performance between the M4 and the M2 so
[05:46] here we
[05:48] go so you can see both devices are
[05:51] extremely fast let's see what the final
[05:53] output was here so we can see on the M4
[05:55] Max we have 200 tokens per second and on
[05:59] the m two Max we have 160 tokens per

### Minute 6

[06:02] second if we go ahead hit up and just
[06:04] give them another shot we should see a
[06:06] similar output
[06:09] here nice so around the same thing right
[06:12] 200 here 160 here so what we're seeing
[06:14] here with our first comparison between
[06:16] the M2 and the M4 is that the M4
[06:19] definitely has a significant Advantage
[06:21] right 40 tokens per second is quite a
[06:24] lot this means that the M4 so far is
[06:26] about 20% faster right 20 to 25% faster
[06:30] so let's go ahead and scale this up
[06:32] let's see if this trend continues when
[06:33] we bump up the model size what we're
[06:36] going to do is Bump this up to a Falon 3
[06:39] 10 billion parameter model same thing
[06:41] for the M2 and we're running that exact
[06:43] same AI coding prompt we want to get a
[06:46] function written out for us that
[06:47] converts csvs into SQL light tables the
[06:52] big difference here is that we're
[06:53] running a 10 billion parameter model
[06:55] shout out Falcon 3 big shout out to the
[06:58] local llama subreddit I was completely

### Minute 7

[07:00] unaware of Falcon 3 10 billion
[07:02] parameters and as you'll see in our
[07:04] Benchmark uh this is quite a powerful
[07:06] small model let's see how the M4 Max
[07:09] compares to the M2 Max on a 10 billion
[07:12] parameter
[07:15] model okay so they're both kicking off
[07:18] they're a lot more precise we're getting
[07:20] a lot less text and a lot more actual
[07:23] function definition if we look at the
[07:25] stats here you can see that difference
[07:27] has shrunk quite a bit okay we're now
[07:30] getting 55 tokens per second on the M4
[07:34] and we're getting 42 tokens per second
[07:37] on the M2 let's go ahead and hit up and
[07:39] let's run this again I want to note that
[07:41] we're still getting great performance
[07:43] out of both of these devices we have 55
[07:47] tokens per second 41 on the M2 you can
[07:51] also see that the model performance has
[07:54] improved quite a bit right we're getting
[07:56] a more concise response you can see it's
[07:58] very similar on both devices as you

### Minute 8

[08:00] would expect and uh you know it's
[08:02] outputting more code exclusively we are
[08:05] getting a description here but this
[08:08] happens let's go ahead and move on to an
[08:10] even larger model right let's scale this
[08:12] up and what I want to do here is give
[08:13] you a good sense of when you're running
[08:15] local models on device what's the
[08:17] performance you can expect as you scale
[08:20] up the parameter count of the model
[08:22] because that's the biggest correlation
[08:24] that you can draw the tokens per second
[08:26] of your language model and the total
[08:28] duration it takes to is going to
[08:30] correlate strongly with the parameter
[08:32] count let's scale it up once again let's
[08:33] use an even more powerful model we're
[08:36] going to paste this in and we're now
[08:37] using Quinn 2.5 coder 32 billion
[08:40] parameters so we're tripling the size of
[08:43] the model let's see how our M4 and M2
[08:47] Mac devices can perform while operating
[08:49] on a 32 billion parameter model here we
[08:51] go we're going to head enter at the same
[08:53] time we're running that exact same AI
[08:55] cring prompt on AMA in verbose mode

### Minute 9

[09:03] all right so the M2 is now taking some
[09:05] time to load here uh it may just need to
[09:08] you know load the model I've noticed
[09:10] that the Quinn 2.5 coder 32 billion
[09:13] parameter is a bit more chatty so it
[09:15] adds a bit more textual information
[09:17] we're getting about 20 tokens per second
[09:19] on the M4 and on the M2 we're getting 14
[09:23] tokens per second if we round these both
[09:24] up we're getting 20 and 15 let's go
[09:26] ahead and run this again
[09:30] now they're kicking off at the same time
[09:32] that's good to
[09:36] see all right the M4 has completed and
[09:40] about the same stats right so we're
[09:42] getting about 20 tokens per second on
[09:44] the M4 and we're getting 15 tokens per
[09:46] second on the M2 really interesting to
[09:48] see this right we're continuing that
[09:50] trend of seeing about a 15 to 25%
[09:54] Improvement on the M4 Max over the M2
[09:57] Max so let's push this one step further

### Minute 10

[10:01] we're nearing what I like to call the
[10:02] dead zone right now we're running you
[10:04] know still above 10 tokens per second
[10:07] when you dip below 10 tokens per second
[10:09] the model truly becomes unusable in my
[10:12] opinion comment down below let me know
[10:14] what's the minimum tokens per second
[10:16] that you run a local model at that
[10:18] you're willing to accept for me it's 10
[10:20] once we get below 10 it's just not
[10:22] usable it's too slow so when I'm looking
[10:25] at both these devices the M2 Max is
[10:28] going to kind of stop that out at this
[10:30] 32 billion parameter count level right
[10:32] anything below this is good the M4 on
[10:35] the other hand is handling this at 20
[10:37] tokens per second that's still a pretty
[10:39] solid speed let's see if the M4 and the
[10:42] M2 can handle 72 billion parameter
[10:45] models final test here before we jump
[10:47] into our benchmarks let's see how both
[10:50] these devices handle 72 billion
[10:53] parameters okay this is a big model
[10:55] right for an on device model uh these
[10:57] are huge let's go ahead and kick these
[10:58] off and let's look at the performance on

### Minute 11

[11:00] the M4 Max versus the M2 Max here we
[11:05] go all right so now they're both just
[11:08] spinning the M4 Max has kicked off M2 is
[11:13] still thinking still spending some time
[11:16] uh we can see here uh we are almost
[11:19] crawling here yeah we're below that 10
[11:21] tokens per second on the M4 Max it has
[11:24] completed and now we're kicking off on
[11:26] the M2 this is also crawling but but
[11:29] doesn't look as slow as I would expect
[11:32] it let's go ahead and give it some time
[11:34] here okay we're coming in at s tokens
[11:36] per second on the M2 and we're coming in
[11:38] at 9 tokens per second on the M4 so
[11:42] definitely the 72 billion parameter
[11:44] model is the hard drop off point it
[11:47] looks like we can run this on the M4 but
[11:50] as I mentioned this is my drop off point
[11:52] anything below 10 tokens per second is
[11:54] not really bearable it's not really
[11:55] functional I don't have the patience to
[11:57] wait for 10 tokens per second Maybe you
[11:59] do I'm going to run this one more time

### Minute 12

[12:01] here now they're both kicking off at the
[12:03] same time there is some like initial
[12:04] model loading that happens fantastic
[12:07] okay so about the same thing right nine
[12:08] tokens per second and seven so again
[12:10] we're seeing that kind of 15 to 25%
[12:13] advantage to the M4 max if you fully
[12:17] spec it out over the M2 again fully spec
[12:19] out so really really interesting to see
[12:22] now what we're going to do is let's
[12:24] scale this up we're just looking at one
[12:26] prompt we're looking at one example M2
[12:28] versus the M4 you can kind of see the
[12:30] difference here if you're thinking about
[12:32] upgrading to the M4 my advice is if you
[12:34] have an M2 and you're not using local
[12:36] models every single day um I would just
[12:39] hold off for the next Generation if
[12:40] you're running on the M1 or anything
[12:42] older upgrading to the M4 will be a
[12:45] massive massive update and a massive
[12:47] upgrade for you especially if you're
[12:49] looking to position yourself ahead of
[12:51] the curve for local models in 2025 you
[12:54] can see on a 72 billion parameter model
[12:58] I'm getting about 10 tokens per second

### Minute 13

[13:00] out of my M4 Max with 128 GB of unified
[13:05] Ram to make it absolutely clear the M4
[13:08] Max again with Max specs as many
[13:11] performance and efficiency cores as you
[13:13] can get and with the maxed out unified
[13:15] Ram of 128 GB this is the best single
[13:20] device purchase you can make if you want
[13:22] to get a ton of performance for language
[13:25] models out of the box without doing any
[13:27] configuration I know know there are ways
[13:29] to improve these numbers I know there
[13:31] are tools like mlx and LL file that I'm
[13:34] going to be spending time with to see if
[13:37] I can get these numbers cranked up like
[13:39] subscribe and comment if you want to see
[13:40] additional videos on how to crank up
[13:43] local model performance on your device
[13:45] now let's scale this up we're getting a
[13:47] good idea of the relative performance of
[13:49] tokens per second between the M4 and the
[13:52] M2 but in order to really understand how
[13:54] models perform for your specific use
[13:56] case we need to look at large Suites of
[13:59] benchmarks so let's go ahead and do that

### Minute 14

[14:04] now so focusing in on the M4 here let's
[14:07] look at Beni so Beni is a benchmarking
[14:09] tool that I'm working on to build
[14:12] benchmarks that I can feel that I can
[14:14] understand and get a deeper sense of how
[14:16] models perform by looking at the
[14:18] performance of models relative to each
[14:20] other so let's break down this simple
[14:23] function coder Benchmark so first off
[14:25] let's configure this a little bit so we
[14:26] can see all of our models so I'm going
[14:28] to hit show settings I'm going to go
[14:29] into bench mode so that we can collapse
[14:32] the headers I'm going to move our model
[14:34] stats to simple mode so we can just get
[14:36] a reduced look here I just want to see
[14:38] accuracy and tokens per second we can
[14:40] see Lama 3.2 1 billion parameter is
[14:43] blazingly fast and if we reduce the
[14:45] block size here we can see all of our
[14:48] models so if we shrink down to about
[14:50] this size we can see the performance of
[14:52] all of our models side by side so you
[14:55] know just looking here top to bottom we
[14:56] can get some valuable information we can
[14:58] hide the settings and we can get some

### Minute 15

[15:00] good information here right I'm using
[15:01] deep seek V3 as our control group
[15:05] whenever I'm creating benchmarks I like
[15:07] to have a powerful Cloud Model I like to
[15:10] have this as a control group to really
[15:11] see how powerful are these local models
[15:14] we can see here deeps V3 aced this
[15:17] Benchmark we can see Quinn 2.5 coder 32
[15:20] billion parameters aced it 14 billion
[15:22] also Ace it and then five acing it as
[15:25] well we pick up a couple errors when we
[15:27] drop down to Falcon 3 10 billion
[15:29] parameters and of course lber 3.2 latest
[15:32] this is the 3 billion parameter model
[15:34] you know the tokens per second here is
[15:36] really important to pay attention to
[15:37] right of course deep seek Cloud Model so
[15:39] there's no tokens per second information
[15:41] for us but you can see here you know by
[15:44] running this Benchmark and we'll dig
[15:45] into what exactly this Benchmark is
[15:47] testing in a second here but by running
[15:49] this Benchmark we can see that we don't
[15:51] need coin 2.5 Cod 32 billion right we
[15:54] can settle on a 14 billion parameter
[15:57] model coming out of AMA we can use use
[15:59] 54 we can use uh 2.5 coder 14 billion

### Minute 16

[16:03] and if we're okay with accepting some
[16:05] errors and you're willing to sacrifice
[16:07] for Speed you can do that here right we
[16:09] can even push it even further to get
[16:12] four times the tokens per second by
[16:14] using a 3 billion parameter model of
[16:16] course our accuracy is dropping down
[16:18] 177% so this is the idea behind you know
[16:20] benchmarking and benchmarking tools and
[16:22] Beni specifically right so I'm building
[16:24] this benchmarking tool link is going to
[16:26] be in the description for you if you
[16:27] want to check this out it's a work in
[16:29] progress but this is something I'm
[16:30] working on to really understand the
[16:32] performance of local models against each
[16:35] other and also I'm just setting up a
[16:37] bunch of benchmarks for some really
[16:39] exciting work that I'm working on I'm
[16:41] setting up a lot of benchmarking work
[16:43] for upcoming releases around principled
[16:45] AI coding stay tuned for that but
[16:47] benchmarking is ultra Ultra important if
[16:50] you want to understand what capabilities
[16:53] are available to you today and tomorrow
[16:56] right because once you have the
[16:57] Benchmark up it's so easy to just plug
[16:59] in another model and then get results

### Minute 17

[17:01] out of it all right so let's go ahead
[17:02] and just scale this up a little bit and
[17:03] we can see more details on a per prompt
[17:06] basis okay let's double click into this
[17:09] prompt and let's see what's going on
[17:10] here this is our llama 3.2 it's made a
[17:13] mistake on the first prompt here and if
[17:15] we just go ahead and open this up we can
[17:16] take a look at this prompt and matter of
[17:18] fact we can just copy the input prompt
[17:19] out let's open up code and before we dig
[17:22] into the actual prompt configuration
[17:24] file let's just look at the prompt and
[17:26] let's go to XML and we can see here we
[17:28] have have this very simple prompt
[17:30] generate a function for the given
[17:32] function request so you can see we have
[17:33] a dynamic variable here and we're
[17:35] passing in an AI coding prompt for a
[17:38] function definition this is a powerful
[17:41] AI coding technique you can use just by
[17:43] specifying the definition of the
[17:46] function and a small detail you can
[17:49] generate the entire function right so
[17:50] here's a super super simple example in
[17:52] this prompt we're saying you know
[17:53] generate the add function and then we're
[17:55] also passing in the function arguments
[17:58] Okay so so we saying use the provided

### Minute 18

[18:00] arguments one and two and of course it's
[18:02] going to generate this we wanted to also
[18:05] print the result and this is the prompt
[18:07] we're building so you can see here we're
[18:09] building this prompt in a very unique
[18:11] way how is it unique it's a
[18:12] self-contained prompt that we can
[18:14] immediately evaluate in a pass fail way
[18:18] why is this so important if we look at
[18:20] this prompt again we can see our models
[18:22] response llama 3.21 billion parameter
[18:26] just completely fudged this okay misread
[18:28] the instructions completely and just got
[18:30] this answer completely wrong look at a
[18:32] successful model here so let's look at
[18:33] the 3 billion parameter response and if
[18:35] we click into this we can see a perfect
[18:38] model response so take a look at this
[18:40] model response output this is a unique
[18:43] type of output that is evaluatable okay
[18:46] so that means that we can build up
[18:48] benchmarks in a past fail way this is
[18:50] really important because it makes the
[18:52] benchmarking process much simpler we
[18:55] take this code and we run it through a
[18:57] python execute computer evaluator and

### Minute 19

[19:00] it's giving us a fullon execution result
[19:03] right so inside of our Benchmark Suite
[19:05] we can then just set up the expected
[19:07] result and if it's not that it's wrong
[19:10] okay so obviously there are some parsing
[19:12] related things that go around this but
[19:14] this pass fail mechanism this fullon
[19:17] evaluation makes for really simple
[19:20] benchmarking really simple testing with
[19:23] your language models so let's go ahead
[19:25] and take a look at this exact
[19:27] benchmarking format so you can see here
[19:29] a couple of things let's go ahead and
[19:31] collapse everything and break it down
[19:32] one by one so you can see we have our
[19:34] Benchmark name we have the purpose and
[19:37] then we have our base prompt okay and
[19:40] the base prompt is of course what we
[19:42] were looking at before and here we have
[19:44] a XML is concise level for prompt I'll
[19:49] link the four levels of prompts video in
[19:52] the description if you want to check
[19:53] that out we have a powerful prompt here
[19:55] because it has a purpose clear
[19:57] instructions and then
[19:59] Dynamic variables we definitely could

### Minute 20

[20:00] have added examples to this to improve
[20:03] it as well but it's not necessary this
[20:05] is the prompt that we're working with
[20:06] now the cool part about this
[20:07] benchmarking framework that I'm building
[20:09] out is that you can of course list
[20:12] several models so these are all the
[20:13] models that you want to run this prompt
[20:15] against but most importantly we have the
[20:18] prompts okay and so we have a list of
[20:20] prompts let's go ahead and just collapse
[20:22] to this level here so we have a whole
[20:24] list of dynamic variables and
[20:26] expectations and what happens here as
[20:28] you can see in our benchmarking test
[20:31] here is that for each model we're going
[20:32] to Loop over every set of dynamic
[20:36] variables right every set of prompts and
[20:38] the prompt has Dynamic variables and an
[20:40] expectation right so if we look at uh
[20:43] deep seek chat of course it's going to
[20:45] have every answer correct this is what
[20:47] we pay for so if we you know scroll down
[20:49] here you can see we have this test here
[20:51] where we're passing in the function
[20:54] definition count vowels and we're
[20:57] getting this nice clean simple python
[20:59] response out of deep seek in the

### Minute 21

[21:01] instructions we say generate the
[21:03] function call the function and print the
[21:05] result and so you can see here we're
[21:07] passing in that function definition and
[21:08] then we're also replacing the dynamic
[21:11] variables right so for each run you can
[21:13] see here if we open this up we're
[21:15] replacing function and we can go ahead
[21:17] and open these up here so for each
[21:20] prompt we're replacing every one of the
[21:22] dynamic variables and that becomes a
[21:24] brand new execution right and so this is
[21:26] a great way to run your test run your
[21:29] llms and run your functionality at scale
[21:31] in a quick way so you can see here we're
[21:33] generating an ad method multiply list
[21:36] reverse string so on and so forth right
[21:38] I have you know 30 different unique
[21:40] prompts here that we're running to test
[21:43] all of these models in a specific way
[21:45] right and a really important piece of
[21:46] this like I mentioned you need to
[21:48] specify an evaluator a way to actually
[21:51] say that your models output was correct
[21:53] or not in code you can take a look at
[21:54] the code base if you're interested we
[21:56] have this execute python code with
[21:58] string output evaluator and of course

### Minute 22

[22:01] you can build out different evaluators
[22:03] to test different outputs from your llms
[22:06] there are popular benchmarking tools I
[22:09] also like prompt Fu this is my take on
[22:12] building out a you know really kind of
[22:14] opinionated benchmarking tool again link
[22:16] is going to be in the description for
[22:17] this if you want to check out the
[22:19] benchmarking tool that I'm building up
[22:20] for my work products and projects so
[22:22] this is what this looks like right it's
[22:24] simple it's intuitive it scales well and
[22:27] it's all about just defining the right
[22:28] evaluators and then building up a nice
[22:30] Suite of tests so this is cool let's go
[22:33] ahead and look at some additional tests
[22:36] right this is just one set of tests that
[22:38] we can run if we hit reset here we can
[22:40] drag or drop our configuration file or a
[22:43] completed execution of a bunch of tests
[22:46] let's go ahead and run this simple math
[22:48] benchmarking file if I drag and drop
[22:50] simple math. yaml it's going to kick off
[22:53] the benchmarks and if we open up the
[22:56] server here you can see we're kicking
[22:58] off these benchmarks we're running llama

### Minute 23

[23:00] 3.2 running at a nice speed here then
[23:04] it's going to run the next model and you
[23:05] know you can see the list of models that
[23:06] we're going to run here 3.21 billion
[23:09] 3.23 billion Falcon 3 54 two Quinn
[23:13] models we're looking at the 14 the 32
[23:16] and then of course deep seek V3 as a
[23:19] control Cloud Model so while this is
[23:21] kicking off let's go ahead and just look
[23:23] at the base prompt if you understand
[23:24] what the base prompt is doing you can
[23:26] really understand what's going on what
[23:27] we're doing here in this benchmark is
[23:28] we're evaluating the ability of a
[23:30] language model to perform simple
[23:31] mathematical operations in Python so
[23:34] here's another simple way to Benchmark
[23:36] local language models we're asking it to
[23:38] do simple math by writing the math
[23:42] operation in Python and then it just
[23:43] prints the result so a big key element
[23:46] of benchmarking and testing your prompts
[23:48] and testing your language models is
[23:50] making sure that it's evaluatable and
[23:53] the simpler the evaluation the less
[23:55] noise there is in the evaluation step
[23:57] the more confident you can be be that
[23:59] the changes that you're making to your

### Minute 24

[24:00] prompt and the strength of the model is
[24:03] actually coming through your benchmarks
[24:06] we're saying simply evaluate statement
[24:08] in Python and print the result and then
[24:10] we're passing in the statement here
[24:13] right so super simple we can take a look
[24:15] at the dynamic variables here add five
[24:17] and five and our expectation is of
[24:19] course 10 add five and five then split
[24:22] in half then triple 15 multiply 3 by 4
[24:25] and add 7 19 so on and so forth right so
[24:29] you can add entire sets of these this is
[24:31] why using Dynamic variables in your
[24:33] prompts is so important because it
[24:34] allows you to scale to 10 hundreds
[24:37] thousands millions of executions right
[24:39] anyone building products with language
[24:42] models knows this Dynamic variables and
[24:44] level four prompts are essential for
[24:47] scaling your prompts into products and
[24:49] tools our execution should be about
[24:52] finished we're running Quin 2.5 coder 32
[24:55] billion nice ran through that and now of
[24:57] course we're running deep seek this is
[24:59] just hitting their API so this should be

### Minute 25

[25:01] finished relatively soon I've been
[25:03] really impressed with deep seek V3 it
[25:06] does appear to be near the level of claw
[25:09] 3.5 Sonet it's definitely fractions of
[25:12] the price and it's giving effectively
[25:14] the same performance it's allowing me to
[25:16] scale up a lot of my AI coding work
[25:18] using spec prompts to a insane level
[25:21] more on that in upcoming videos but you
[25:22] can see our Benchmark has completed so
[25:25] if we scale this down a little bit we
[25:26] can get you know a nice nice nice view
[25:28] of this let's look at the stats here
[25:30] right so kind of interesting right away
[25:31] let me open up to verbose mode here you
[25:34] can see we're getting 18 right 12 wrong
[25:38] from L 3.2 1 billion the 3 billion model
[25:41] is doing really really well look at this
[25:43] right looks like simple math operations
[25:46] you only really need a 3 billion
[25:47] parameter model to do simple mathematics
[25:49] right so this is a good thing to see and
[25:51] again this is why you make benchmarks
[25:53] you really want to know what parameter
[25:55] count do I really need for my use case
[25:58] how powerful does the local model or

### Minute 26

[26:00] even the cloud model if you're
[26:01] benchmarking Cloud models how powerful
[26:03] does it really need to be to do this
[26:05] specific thing for me Falcon 3 same
[26:07] level of performance 54 gets everything
[26:10] perfect love to see that shout out
[26:12] Microsoft code Bros Quinn 215 perfect
[26:15] Quin 32 billion getting quite a few
[26:17] mistakes here that's very interesting we
[26:19] can dig into why that is but let's go a
[26:20] and just kick this off so to be clear
[26:21] you know this Benchmark runs and
[26:24] executes all the prompts and then it
[26:25] saves all the results if you look at the
[26:28] codebase here if we collapse inside of
[26:30] the server directory we have our
[26:32] Benchmark data so you know this is our
[26:34] you know yaml files here I'm going to
[26:35] commit this codebase with all these
[26:38] simple benchmarks for you if you're
[26:39] interested and then we have these
[26:41] reports so this is really cool right so
[26:43] every Benchmark that you run generates a
[26:45] full report and so what we've just done
[26:47] here is generated this new math report
[26:50] and you can see here we have all the
[26:52] results so what we're doing here when
[26:55] we're clicking play Benchmark is we're
[26:57] just replaying it as if it was live but

### Minute 27

[27:00] we've already collected all the data so
[27:01] here we go we're kicking this off um
[27:03] it's really just incredible to see what
[27:06] 200 tokens per seconds look like right
[27:08] llama is done let me uh scale this a
[27:10] little
[27:13] bit there we go so we got 30 Falcon
[27:16] still running coming in at you know 57
[27:18] tokens per second so this is what that
[27:20] looks like right uh we can see here 54
[27:23] 39 tokens per second that's finished
[27:26] Falcon finished uh Quinn 14 and you can
[27:29] see here right as the parameter size
[27:31] grows tokens per seconds goes down right
[27:34] if I just highlight this you can see as
[27:36] the model grows larger tokens per
[27:39] seconds goes down right this is just a
[27:41] simple Trend really important to keep in
[27:43] your mind a simple mental model that you
[27:45] can use and build up as you're
[27:47] understanding local models and models in
[27:49] general right interestingly though
[27:51] accuracy isn't always going to scale
[27:53] parameter size it correlates very
[27:55] strongly but you can see here coder 32
[27:58] has made several mistakes that smaller

### Minute 28

[28:00] models have not so if we click into one
[28:02] of these we can kind of see um it's just
[28:05] outputting the answer okay so it's kind
[28:07] of being a so it's being kind of too
[28:09] smart for its own good right instead of
[28:11] actually writing the python code you're
[28:12] looking for it just outputs the answer
[28:14] right that's not what we're looking for
[28:16] we can't execute that okay so let's look
[28:18] at another one yeah it also outputs the
[28:20] answer here um this is just wrong so
[28:22] it's printing the wrong answer again
[28:25] printing the answer and what we really
[28:27] are looking for for from this test is we
[28:29] wanted to generate the code in Python so
[28:32] that we can execute it right so you can
[28:33] see this is a correct answer and of
[28:36] course if we look at Deep seek we can go
[28:37] to problem 30 here and you can see this
[28:40] was correct right so the problem here
[28:41] was convert the fraction 38 to decimal
[28:44] form so you can see nailed that 100% for
[28:47] deep seek 100% for Quinn 2.5 coder 14b
[28:51] 100% for 54 14 billion 96% for Falcon
[28:55] 10B I am uh very impressed with Falcon
[28:59] um I had no idea this model even existed

### Minute 29

[29:02] 10 billion parameters uh performing
[29:03] really well performing really quickly
[29:05] take note of this right uh 67 tokens per
[29:09] second very very powerful model it is
[29:11] pretty crazy to see the difference
[29:13] though between if we just rerun this
[29:15] like watch the difference between the
[29:16] tokens per second between these top
[29:18] three right let's let's go ahead and
[29:19] scale these down a little bit um watch
[29:21] the difference between the speed of 210
[29:24] tokens per
[29:25] second and 50 first time we go up by 50
[29:28] then we go up by 100 so let's just
[29:30] replay this and then like look look at
[29:32] how quickly this is right 200 tokens per
[29:34] second is
[29:36] insane right so 1B is done uh the
[29:40] billion is done and you can see here
[29:42] Falcon had a slow start it had some boot
[29:44] up time but this is what 60 tokens per
[29:46] second looks like running 30 prompts
[29:49] right not as fast as you would think but
[29:51] again it is running 30 prompts and it's
[29:53] maybe running a I don't know how how
[29:55] large is this let's let that finish nice
[29:58] and if we look at this prompt we can see

### Minute 30

[30:00] the size right so if we just highlight
[30:03] the base prompt we can see we're running
[30:05] 154 token prompt very tiny prompt so
[30:08] this all looks great you know just by
[30:10] looking at this and by looking at our AI
[30:12] coding function generator and our simple
[30:15] math benchmark it kind of looks like
[30:17] local models are great already right not
[30:20] so fast let me show you a much more
[30:23] difficult problem that uh these language
[30:25] models will just trip up on pretty
[30:27] rapidly
[30:31] I'll hit reset here and let me pull up
[30:34] instead of dropping in a full
[30:36] configuration file for it to execute on
[30:38] what I'm going to do is open up a
[30:40] existing completion and I'll just drag
[30:43] and drop this over this is a completed
[30:45] Benchmark report so it's going to
[30:47] automatically just open up with the
[30:49] prompts completed it doesn't need to run
[30:50] these right if we just scale everything
[30:52] down if we go to simple you can see here
[30:55] we're only running uh five models and we
[30:58] have 15 prompts and look at the

### Minute 31

[31:01] scores right 0% 0% 0% 0% 26% there are
[31:06] many problems out there there are many
[31:08] prompts that local models cannot tackle
[31:12] yet okay and I want to bring this to
[31:13] your attention I am very balanced in my
[31:17] uh portrayal of these tools and
[31:19] Technology great engineering is balance
[31:21] you need to always consider trade-offs
[31:23] in order to build out the best tools
[31:25] features products and to really use
[31:27] gener of Technology properly you need to
[31:29] be honest about where they're falling
[31:31] apart okay so I have this much harder
[31:33] problem we can go ahead and kick this
[31:35] off and talk about it so I'll just hit
[31:37] play Benchmark and I'll go into verose
[31:40] mode you can see the horrendous stats
[31:43] from basically every one of these models
[31:44] and then while this is running let's
[31:46] quickly just look at what this prompt is
[31:47] and why it's so challenging let's look
[31:49] at something that was correct so we have
[31:51] this first prompt here by Deep seek V3
[31:54] what is this so what's going on here so
[31:56] we wanted an llm to parse the given
[31:59] natural language request this is going

### Minute 32

[32:01] to be a speech to text request and then
[32:03] produce the right CLI command so we want
[32:06] a command output to our terminal it's
[32:08] going to run typer commands and it's
[32:10] going to run that against a python
[32:12] script main.py so we're looking for
[32:14] something very precise here okay so how
[32:16] does this work right let me just pull up
[32:17] this full prompt let me just copy this
[32:18] all out let's go to vs code open this up
[32:21] we have a few instructions here we have
[32:23] four instructions and what we want to
[32:25] have happen here is we want our speech
[32:28] to text request basically our natural
[32:29] language query right ping the server
[32:32] quickly and what we want this to do is
[32:34] call the proper Command right call the
[32:37] proper typer command automatically for
[32:40] us with the right params based on the
[32:42] function definition so this prompt needs
[32:44] to read this code and there's quite a
[32:46] few commands here right you can see we
[32:48] have over what 20 maybe 30 commands here
[32:51] in this command set and our language
[32:53] model needs to read all these read in
[32:56] the natural language request and then
[32:58] give us the right command where we can

### Minute 33

[33:00] immediately call this method right so
[33:03] you can think of it like function
[33:05] calling it's not exactly function
[33:06] calling because you need to position
[33:07] everything perfectly uh but it's very
[33:09] similar you definitely could use Json
[33:11] parsing to to get this moving but this
[33:12] is another great tests for language
[33:14] models so we can see here our expected
[33:16] result was python main.py pink server
[33:19] and the execution result nailed it right
[33:21] so this is a correct response so this
[33:24] evaluation gets marked as correct if we
[33:27] go over to to our typer command
[33:29] configuration file and we open
[33:31] everything up let's close the base
[33:33] prompt we're using a raw string
[33:35] evaluator and so again I just want to
[33:37] talk about evaluators they're really
[33:38] important they allow you to pass fail
[33:41] the response of your language model and
[33:43] so when we look at these prompts here we
[33:45] have a whole list of prompts and you can
[33:47] see that exactly right so we're passing
[33:49] in this variable that gets replaced from
[33:51] our base prompt let me go ahead and
[33:53] collapse the XML here we have one
[33:54] Dynamic variable here right spech of
[33:57] text request so that's getting replaced
[33:59] and we're expecting this result to come

### Minute 34

[34:02] out right and so if this comes out you
[34:04] can imagine we're talking to our
[34:07] personal AI assistant and we say you
[34:08] know ping the server quickly we wanted
[34:10] to automatically execute this method for
[34:13] us okay and so this continues all the
[34:16] way down the line you can see we have a
[34:17] ton of failures basically every one of
[34:19] our small models bombed this we can
[34:21] click in and inspect why so you know
[34:24] Falcon 3 10 billion just responded with
[34:27] check Health okay so that's just wrong f
[34:31] for latest you can see here we pass in
[34:33] the natural language query delete user
[34:36] ID user 123 skip confirmation and so
[34:40] this is the expected result right delete
[34:41] user so we're calling this typer command
[34:43] user 123 confirm okay and you can see fi
[34:48] just talking giving us a lot of
[34:50] information not relevant we just want
[34:52] this one command so this is an example
[34:54] of a prompt that just completely falls
[34:57] apart even for powerful models now 100%

### Minute 35

[35:00] um I can improve this prompt and you've
[35:03] caught me literally in the act of
[35:05] improving this prompt I wanted to create
[35:06] this video to kind of share my process
[35:08] share what I'm working on and share why
[35:10] benchmarks are so important right so I
[35:12] am literally in the process of improving
[35:14] this prompt when I'm writing prompts at
[35:16] scale what I always do is I make the
[35:19] prompt work for a powerful cloud model
[35:21] and then I try to improve it to scale it
[35:24] down to smaller models right often times
[35:26] this means you need to add additional
[35:28] information additional instructions and
[35:31] examples and you know we need to clean
[35:33] up the purpose and maybe you need to add
[35:35] additional um static or dynamic
[35:38] variables whatever the case is you'll
[35:40] often need to add more and more
[35:42] instructions to your prompt in order for
[35:44] it to work for you know the 10 to 30
[35:46] billion parameter model uh size once you
[35:49] get below 10 adding more things doesn't
[35:51] really help right because the model just
[35:53] can't handle it it cannot handle the
[35:55] complexity if we click into you know
[35:57] even llama 3.23 billion parameter um

### Minute 36

[36:00] it's just completely wrong like this is
[36:02] just wrong it's giving us a whole set of
[36:05] it's giving us python code right it's
[36:07] just completely irrelevant if we go to
[36:09] 13 here you can see it's writing code
[36:11] for us we don't need code we need a
[36:14] single answer you can see Falcon 3 also
[36:16] having some trouble right remove user
[36:18] with ID user 123 skipping confirmation I
[36:22] need the actual CLI command I don't need
[36:24] you to say this back right so this is
[36:28] the execution result this is what Falcon
[36:30] said back after we passed in this prompt
[36:33] okay so local models are improving it's
[36:35] important to have a way to understand
[36:37] their capabilities by benchmarking we
[36:39] can do that and we can position
[36:40] ourselves ahead of the curve you can see
[36:43] here I have the brand new M4 um I don't
[36:45] just make predictions I make predictions
[36:47] and I bet on them I am predicting we're
[36:49] going to get powerful local models and I
[36:51] would to be ready for it that's why I
[36:52] have this device I'm betting on my
[36:54] predictions so you can see that here I'm
[36:56] going to link last week's 2025
[36:58] predictions video that was a really
[36:59] important video everything we're going

### Minute 37

[37:01] to be working on on the channel we
[37:02] talked about we discussed and really
[37:04] broke down in that video big shout out
[37:06] to everyone over the past couple weeks
[37:08] that's been digging into principal ad
[37:10] coding I am continuously constantly
[37:13] working on upcoming improvements
[37:14] stabilizing the product so that we can
[37:16] expand it and do new cool things with it
[37:18] hint hint that's why these benchmarks
[37:21] are going to be you know increasingly
[37:22] important over time if you're interested
[37:24] in benchmarks you can check out this
[37:26] tool called prompt Fu I'll also link our
[37:29] previous prompt Fu videos that we've
[37:31] worked on in the past that's a great
[37:33] benchmarking framework if you just want
[37:34] something out of the box if you want to
[37:36] experiment with Beni The Prompt
[37:38] framework that I'm actively building up
[37:40] right now you can go ahead and do that
[37:41] it's a work in progress but it's here if
[37:43] you're interested and you want to check
[37:44] it out thanks for watching if you like
[37:46] the video you know what to do drop the
[37:47] like drop the comment drop the sub and I
[37:49] will see you next week stay focused and
[37:53] keep building