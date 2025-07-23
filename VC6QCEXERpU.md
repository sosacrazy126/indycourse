# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=VC6QCEXERpU
- **Duration:** 24:12
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 4560
- **Transcript Generated:** 2025-03-30 23:49:13

## Transcript


### Minute 0

[00:00] what's up Engineers welcome back I got
[00:02] to be honest this is the first time I am
[00:04] genuinely impressed by a local on device
[00:08] small language model lva 3.2 came out a
[00:11] couple days ago in several varieties I
[00:13] want to focus our attention today on the
[00:16] 1 billion and 3 billion parameter models
[00:18] that were created to run specifically on
[00:21] device up until now I've largely ignored
[00:24] local models we've created a couple
[00:25] videos on them over the course of the
[00:27] channel but I don't use them at all in
[00:29] my day-to-day developer workflows I
[00:31] think that's going to be changing very
[00:33] soon often times as these models come
[00:35] out though you likely have the same
[00:36] question I do how good is llama 3.2
[00:41] really it's important to understand when
[00:43] to use local models and that all comes
[00:45] down to knowing what they can do in
[00:48] comparison to other slms and big-
[00:51] hitting state-of-the-art large language
[00:53] models what do you know I've created a
[00:55] notebook for you and I to do that very
[00:59] thing this notebook is built on top of

### Minute 1

[01:02] AMA and Maro in this video I want to
[01:05] share with you how I'm breaking down
[01:07] both the llms and the slms and comparing
[01:10] them to know when local on device slms
[01:14] like llama 3.2 are ready for your use
[01:20] case so we've made a couple improvements
[01:22] to this notebook from our previous video
[01:24] you can see here we're now selecting
[01:26] three models let me go ahead and add
[01:28] 53.5 Quinn 2 .5 let's go ahead and do
[01:31] the Llama 321 billion parameter you can
[01:34] see I have Gemini 1.5 flash2 and let's
[01:37] go ahead and pick up Sonet as well so I
[01:39] have seven models selected and let's
[01:41] just go ahead and run a test uh ping
[01:44] prompt and hello prompt I'll drop the
[01:46] temperature to zero for maximum
[01:48] instruction following and hit submit so
[01:50] right away in this reactive notebook you
[01:52] can see here we have all of our selected
[01:55] models listed and we have our selected
[01:57] prompts as well so this notebook is
[01:59] loading from just a directory of prompts

### Minute 2

[02:02] you can see here we have a really simple
[02:03] ping prompt and a hello prompt right
[02:05] hello my name is Dan are you ready to
[02:07] build and Below you can see we have a
[02:09] nice clean progress bar we have our
[02:11] local models running on ama ama LS you
[02:16] can see a variety of local models I've
[02:18] installed recently and over the course
[02:20] of you know 6 months so these slms are
[02:22] running right on my M2 MacBook Pro which
[02:25] is really awesome given these models can
[02:28] perform so let's go ahead and see how
[02:30] they're performing on these basic
[02:31] introductory prompts so in this ping
[02:33] prompt here I'm looking for a simple
[02:35] pong response so let's see how every one
[02:38] of these models performs across this
[02:40] prompt so of course we have gpg 40 mini
[02:43] pong how can I assist you perfect we
[02:45] have llama 3.2 with a ping um you know
[02:49] it's starting to talk about the um bash
[02:52] ping command that's often where these
[02:55] models get kind of confused we have
[02:57] flash O2 um again same kind of deal

### Minute 3

[03:01] we're just looking for a pong response
[03:03] fi is giving me a entire lecture on PING
[03:07] which okay didn't ask for that Quinn 2.5
[03:10] really really good clean pong response
[03:12] we have the 1 billion blowing up and of
[03:15] course you know state-of-the-art CL 3.5
[03:18] pong I'm ready to help what can I do so
[03:21] that's great um you know kind of
[03:22] expected results so in this notebook not
[03:24] only can we compare prompts across
[03:27] several models we can also rank them so
[03:31] this is really cool I want to share this
[03:32] with you if we scroll down to the bottom
[03:33] here we have this table and we can go
[03:35] ahead and just check all these items and
[03:37] we can vote on these items so let me go
[03:39] ahe and reset so with the rankings reset
[03:41] you can see here we have SIMPLE
[03:42] scorecards and the idea for this
[03:44] notebook is to as you're walking through
[03:45] prompts and comparing prompts against
[03:48] multiple llms you can just come down
[03:49] here and vote on your selected outputs
[03:52] right so let's go ahead and keep a tally
[03:54] on which prompts are actually performing
[03:56] the way we want them to and which which
[03:57] ones are not passing the test right so
[03:59] let's go Ahad look at our hello prompt

### Minute 4

[04:01] so you know this is just another simple
[04:02] introductory prompt hello my name is Dan
[04:04] are you ready to build so if we look at
[04:05] the responses for this we can see a
[04:07] variety of things hello definitely ready
[04:09] to build nice uh 3.2 I'm more than ready
[04:13] to build all right let's let's go uh
[04:15] flash two you has some ready to build
[04:17] tell me what you have in mind F uh great
[04:20] giving me a whole lecture here again
[04:23] that's uh that's more than enough coin
[04:26] 2.5 you know giving me a pretty solid
[04:28] response here L 3 .1 super concise and
[04:31] of course Sonet uh you know decent uh
[04:34] response there right I'm going to go
[04:35] ahead and just select all these and
[04:36] we'll just give everyone a free couple
[04:38] points here right so that'll increment
[04:41] every model by two since we had you know
[04:44] two prompts running against every model
[04:46] so we'll do that and then let's go ahead
[04:47] and run some more prompts so so in this
[04:50] drop down here you can see I have a
[04:51] whole list of prompts across a couple
[04:54] different domains we have some basic
[04:56] ones here we have some coding we have
[04:57] some context window testing some bash

### Minute 5

[05:00] command generation string manipulation
[05:02] so on and so forth right so the whole
[05:03] idea with this notebook is to be able to
[05:05] walk through specific prompts that
[05:08] you've run in the past and walk through
[05:10] specific use cases for your prompts
[05:12] against different models to see how they
[05:14] perform side by side so let's go ahead
[05:17] and run some more right uh python count
[05:18] to 10 and python multi-length counting
[05:21] we submit here and you can see we're
[05:23] kicking off there remember we have two
[05:25] prompts seven models that's going to
[05:27] make for 14 executions so so let's look
[05:30] at our basic python count to 10 XML
[05:33] prompt you can see here we're using the
[05:34] XML format for the best most concise
[05:37] results the purpos is to count to 10 in
[05:39] Python then we have a couple
[05:40] instructions and then in our multi- lay
[05:42] counting we're basically doing the same
[05:44] thing count to 10 then zero and then
[05:46] we're asking the model to generate those
[05:48] results in several other languages and
[05:51] of course we have a couple instructions
[05:52] here the main one here is respond only
[05:54] with runable code and use markdown to
[05:56] format the languages with H1 and the
[05:59] code with back ticks so you know

### Minute 6

[06:01] starting at the top here let's look at
[06:03] our python count to 10 right so this is
[06:04] a really simple function and you know
[06:06] the first thing we're testing here is
[06:09] respond with only runnable code who is
[06:12] doing that who's going to lose some
[06:13] points right away we see L 3.2 adding
[06:15] some extra text here we don't care about
[06:17] the extra text um we wanted it to follow
[06:19] the instructions closely so we're going
[06:21] to dock a point from uh 3.2 flash nailed
[06:24] it mini nailed it as well uh fi giving
[06:28] us a whole block here of Tex we don't
[06:30] really care about that Quinn right on
[06:32] the dot Lama 3.2 1B giving us some extra
[06:35] stuff here we don't care and Claw 3.5
[06:38] Sonet doing the best it's kind of hard
[06:40] to see but this is actually being
[06:42] displayed in markdown and I did say
[06:44] respond with only runnable code so you
[06:47] know if I was being really strict the
[06:49] only winner here is Claud 3.5 but you
[06:52] know we're going to be lenient in
[06:54] markdown is you know acceptable as well
[06:56] so we're going to take off a point from
[06:58] a 3.2 2 F and uh 3.1 all these on and

### Minute 7

[07:03] then we'll remove here we'll remove F
[07:07] and 3.2 so let's see what our
[07:09] multi-length counting XML looks like
[07:11] right so we have 4 mini we have the nice
[07:13] H1 language code H1 language code H1
[07:18] language code same for SQL and Russ so
[07:21] 01 nailing it we have lamba 3.2 it did
[07:24] add an additional string here but that's
[07:26] fine language code so types script 10
[07:30] bash 10
[07:32] to0 it's it has a note for us SQL is not
[07:35] temply used for this for sure but it
[07:37] still did it for us love to see that
[07:39] then we have R so that looks good Gemini
[07:41] Flash 2 uh same deal language output
[07:45] language output language output that
[07:46] looks good fi it's added several
[07:49] additional bits of information here that
[07:51] we don't really care about um it did
[07:53] find a nice result here for uh MyQ and
[07:57] postgress with the generate series
[07:59] function so that's a nice find from Fi

### Minute 8

[08:02] Fi is invalidated here because it's just
[08:04] adding a bunch of extra stuff here right
[08:06] Quinn 2.5 python typescript bash SQL
[08:11] rust nice L 3.1 python typescript bash
[08:15] SQL rust has a note here so we'll dock
[08:18] that as well and then of course Sonet is
[08:20] going to be an absolute dream we know
[08:22] this is going to work perfectly so same
[08:24] Trend right in the end for the basic
[08:27] multi-length counting prompt uh we have
[08:29] to points from llama 3.2 from F and
[08:32] llama 3.1 1 billion parameters so we'll
[08:34] go ahead Mark those we'll cast our votes
[08:38] and you can see you know llama fi and
[08:42] llama 1 billion are a little bit behind
[08:44] here I got to say though they are doing
[08:46] a great job they're keeping up for the
[08:47] most part let's go ahead and clear our
[08:49] selections and let's run some more
[08:50] prompts so let's go ahead and run a
[08:53] single string manipulation prompt and
[08:55] we'll kick this off you know this is
[08:57] just a simple summary of the following
[08:59] test packs so here's a script from my

### Minute 9

[09:00] previous YouTube video and it's just
[09:02] going to create some simple bullet
[09:03] points this was from the two-way prompt
[09:06] video so this will be a pretty simple
[09:08] win for every model 3.2 There's a
[09:10] summary there's flash giving us a nice
[09:13] bullet point list Quinn llama 3.21
[09:16] billion parameter and of course son it
[09:18] so that looks good we're going to go
[09:19] ahead and give everyone points here and
[09:21] move on to another prompt so let's look
[09:23] at a few prompts that are a bit more
[09:24] interesting let's run a couple of our
[09:27] personal AI assistant responses you know
[09:29] this is the prompt that you have set up
[09:30] for um your personal AI assistant if we
[09:34] open up this prompt here you can see
[09:37] when you're building out personal AI
[09:38] assistants you want them to respond in a
[09:39] specific way with some context right so
[09:42] imagine these are variables you have
[09:43] your assistant name you have your uh
[09:45] human companion and then as you're
[09:48] prompting this to the llm to create a
[09:49] response we're saying something like
[09:51] this right concisely communicate the
[09:52] following message to your human
[09:54] companion and we're saying select an
[09:56] image to generate a view component from
[09:59] and so if we look at the responses we

### Minute 10

[10:01] want responses from our language models
[10:04] that communicate that back to the human
[10:06] companion of the AI assistant right so
[10:08] we have gpg 40 leading the way here Dan
[10:11] please select an image to generate a
[10:12] view component from perfect llama 3.2
[10:15] hey Dan can you please select an image
[10:17] perfect we have flash legit F great
[10:20] response as well and you can see here
[10:22] pretty much everyone PR everyone has
[10:24] done it right interestingly we have claw
[10:26] 3.5 kind of adding a bit of additional
[10:29] information
[10:30] um if we look at the second assistant
[10:32] prompt kind of the same setup right we
[10:34] have our assistant and then we have our
[10:35] name and then we want our a assistant to
[10:37] communicate I found the URL in your
[10:39] clipboard I'll scrape the URL and
[10:42] generate example code for you but first
[10:45] what about the example code would you
[10:46] like me to focus on right so it's going
[10:48] to actually ask a question oh mini
[10:51] perfect right I found the URL on your
[10:52] clipboard I'll scrape it but first what
[10:55] aspect of the code example do you want
[10:56] me to focus on right so that's good same
[10:58] deal from llama 3.2 so you know llama

### Minute 11

[11:02] doing a great job here it's it's keeping
[11:04] up it is making some mistakes but it is
[11:07] for the most part absolutely keeping up
[11:09] Gemini flash a nice kind of concise
[11:12] response I really like the response here
[11:14] from flash O2 uh we have five 3.5 Ada
[11:18] here got that link from Dan's clipboard
[11:20] that's kind of weird um ready to extract
[11:23] some scraping magic so this response is
[11:26] really interesting right it's a
[11:27] friendlier more kind of
[11:29] conversational uh response which uh you
[11:32] know isn't terrible not great we have
[11:35] Quinn 2.5 with a great concise response
[11:38] I'm really really impressed by Quin 2.5
[11:40] and then we have llama
[11:42] 3.21 billion performing totally fine
[11:44] here and then Sonic doing well looks
[11:46] like every model has done a solid job
[11:48] here we're going to go ahead and give
[11:50] every model a vote and move on to our
[11:54] next prompt here so far we're just
[11:55] lagging a little bit from the Llama
[11:58] models and the F models model let's go
[11:59] ahead and take a look at a couple SQL

### Minute 12

[12:02] generation prompts if we scroll to the
[12:04] bottom here we have a couple SQL
[12:06] statements let's go ahead and pull these
[12:07] in um let's run three prompts against
[12:11] our seven models so we'll go ahead and
[12:13] kick that off and as you can see here we
[12:16] now have our three nlq prompts and
[12:18] basically we're saying you know given a
[12:20] natural language query and a table
[12:22] definition generate the corresponding
[12:24] SQL statement we're converting natural
[12:27] language queries into SQL statements and
[12:29] and right away you can see here for
[12:30] omeni giving us a solid response this is
[12:33] correct it's off true and plan premium
[12:36] let's see if all the other slms follow
[12:39] we have Lama 3.2 nailed it flash nailed
[12:43] it fi nailing it but adding a little bit
[12:45] of ambiguity here with this premium with
[12:48] the Wild Card matcher here that's not
[12:50] exactly what we want um I am going to
[12:52] dock a point from fi for that but we can
[12:55] see Quinn llama Sonic performing great
[12:58] right so here another prompt um we're

### Minute 13

[13:00] just looking for created after 2022
[13:03] right so another really really simple
[13:05] prompt you wouldn't assume models would
[13:08] mess this up but this is something that
[13:09] you want to test right and you know as
[13:11] I'm saying that we can scroll down and
[13:13] see5 3.5 fudging this because it's also
[13:16] giving us a bunch of extra text that we
[13:18] don't want we don't care about in the
[13:19] response we can see Sonic is making sure
[13:22] that this is a Tim stamp so I'm going to
[13:24] go ahead and dock two points from five
[13:26] and let's get to our third prompt here
[13:28] this is a simple order by updated limit
[13:30] three so you know we want the latest
[13:33] three orders based on updated date
[13:35] descending descending descending this
[13:36] all looks good again VI bombing it here
[13:39] giving us more information than we want
[13:40] everyone else though looks great so I'm
[13:43] going to go ahead and select everything
[13:44] here and we're going to dock a point
[13:46] from fi right so we're going to dock
[13:49] every point from fi and then cast our
[13:51] votes everyone's moving along here fi is
[13:54] now in last
[13:55] [Music]
[13:57] place I hope you can see why this is

### Minute 14

[14:00] valuable right it's one thing to look at
[14:01] a bunch of benchmarks right like every
[14:03] one of these model providers throws up a
[14:06] bunch of benchmarks that you know you
[14:07] can assume more or less will be biased
[14:11] right you can assume more or less will
[14:12] be cherry-picked right like they're
[14:14] comparing L 3.2 90 billion parameter to
[14:17] ha coup and 40 mini they're kind of
[14:20] punching down in a way you know there's
[14:23] also the entire idea that the these
[14:25] models have contaminated test data so
[14:28] the benchmark test data is what's used
[14:30] to train the model so of course the
[14:32] answers are in there you know so there
[14:33] are a bunch of problems with these
[14:35] benchmarks and I think even more
[14:37] importantly than that having some
[14:39] multilanguage model tester or ranker for
[14:42] you to kind of check how it performs
[14:44] against your specific use case or is
[14:46] ultra Ultra valuable because it gives
[14:47] you that hands-on experience with
[14:50] running multiple models you know and
[14:52] there are a ton of other benefits of
[14:54] slm's you know local on device models
[14:57] privacy cost offline access content
[14:59] Freedom you can generate whatever you

### Minute 15

[15:01] want and of course just the personal
[15:03] integration of being able to you know
[15:06] combine with all your personal data
[15:08] everything is inhouse right so there are
[15:09] many advantages to these slms I think a
[15:12] notebook like this can help you figure
[15:14] out you know okay so llama 3.2 is out
[15:17] how does it compare to Quinn how does
[15:19] Quinn compare to 40 and how does 40
[15:21] compare to Sonet right cuz I think we
[15:24] all have a good idea of how these top
[15:26] state-of-the-art models perform because
[15:28] we use them all the time but this tool
[15:30] is super impactful and can be really
[15:32] helpful for you in helping you offload
[15:35] the work that these models are doing for
[15:37] you to a simpler local model especially
[15:40] as the model sizes decrease and the
[15:42] accuracy continues to increase there are
[15:44] a couple key pieces I want to share with
[15:45] you here let's go ahead and look at a
[15:47] couple of code generation prompts I'm
[15:49] going to run these two code generation
[15:51] prompts we'll keep the temperature at
[15:53] zero same models and we'll just hit
[15:55] submit here we can dive into this method
[15:58] and we can see exact what it looks like
[15:59] right so we have a super simple one

### Minute 16

[16:00] prefix string ABC 2 and then we have the
[16:04] proposed output right then we have
[16:06] another one is palindrome returns true
[16:08] if it's a palindrome false otherwise
[16:10] right so another really simple prompt
[16:12] we're just going to run through this and
[16:13] we're going to see are these models all
[16:16] good enough to do these really basic
[16:17] things I think the answer is pretty
[16:19] confidently yes it's so cool that I have
[16:21] some slms running all this on device so
[16:24] you can see here really simple right
[16:25] this is just prefix string you just
[16:27] multiply so along with 3.2 is going to
[16:29] lose a point here it's got the
[16:30] formatting a little fudged flash has the
[16:33] answer super concise super safe great
[16:35] code with examples love to see that it
[16:38] is adding a bunch of additional
[16:39] information though uh to be clear you
[16:42] know this is something that I could have
[16:43] improved in the prompt this prompt is
[16:45] just saying implement this function I'm
[16:47] not saying don't specify details so we
[16:49] can't really dock points for that so
[16:51] we'll allow flash to get away with that
[16:54] one uh we have fi 3.5 giving us a nice
[16:57] solid answer quein
[16:59] Sonet so on and so forth right and then

### Minute 17

[17:01] we have our second code generation
[17:02] function is palindrome it's really
[17:04] interesting to see how every model is
[17:06] going to come up with a slightly
[17:07] different answer of this let's go ahead
[17:08] and just look through this um again
[17:10] llama giving us some weird output there
[17:13] flash is looking really good here it's
[17:14] giving us several versions and then we
[17:17] have fi doing a decent job here giving
[17:20] us a really kind of simple pythonic
[17:21] answer Quin 2 decent answer there llama
[17:25] 1B uh frankly outperforming
[17:29] 3B which is super interesting to see and
[17:31] then of course claw 3.5 so again pretty
[17:34] good we're going to dock a point from um
[17:37] llama 3.2 for some weird formatting but
[17:40] everything else looks good so we're
[17:41] going to tell up our votes there so you
[17:43] can see the scores here so far we have
[17:45] Lambo 3.2 lagging a little bit fi in
[17:47] last place 1B kind of hilariously a
[17:50] little ahead but then you have kind of
[17:52] the next class of models all kind of
[17:54] lined up the big call out here is that
[17:57] coin 2.5 is eff L operating as a smaller

### Minute 18

[18:00] size you know state-of-the-art model
[18:02] which is really really cool to see again
[18:04] Quin 2 is running on my device right um
[18:07] that's coming right out of you know AMA
[18:10] and if we look at AMA a coin 2.5 this is
[18:14] a 7 billion parameter model so you know
[18:16] small this is this is running on my
[18:18] device locally for free 128k contact
[18:21] window very good model and honestly
[18:23] Quinn 2.5 was not on my map previous to
[18:27] actually running this experiment
[18:28] although I really expected a bit more
[18:30] from llama 3.2 we also have to consider
[18:33] that llama 3.2 is a 3 billion parameter
[18:36] model here so you know it's going to be
[18:39] not as great for
[18:43] now there's one more test I want to
[18:45] share with you that is kind of
[18:47] interesting so I have this needle in the
[18:49] haste deck context prompt where is that
[18:53] um yeah so we have these context window
[18:56] prompts and I'll just select one of
[18:57] these and and we can dig into what

### Minute 19

[19:00] exactly this is doing so if I hit submit
[19:01] here you can see that um I actually have
[19:04] a really really long script and I'm
[19:07] passing this in to my on device models
[19:10] and I'm asking a very very specific
[19:13] question about this script right so this
[19:16] is like the classic needle in the hstack
[19:17] test it's also you know specific
[19:20] information retrieval basically just
[19:21] asking what was the end year prediction
[19:24] made in this script below then I'm
[19:26] passing the script and the trick here is
[19:28] that it has to look through a bunch of
[19:30] text if we just copy this open up our
[19:33] editor and paste you can see here this
[19:35] is 5K token so not a massive amount we
[19:38] know that state-of-the-art models can
[19:39] handle this no problem but for our on
[19:42] device models like 53 this could very
[19:45] well this could very well nuke my AMA
[19:48] instance and kind of fry something or at
[19:50] least freeze so let's see how this
[19:52] performs hopefully this can push through
[19:54] I might have to drop 53 from this but
[19:57] we'll see all right so my computer has

### Minute 20

[20:00] absolutely Frozen up here 53.5 is going
[20:03] to lose a point it is not processing
[20:05] this I'm going to go ahead and stop the
[20:07] instance here and we're going to um go
[20:10] ahead and just move on it could not run
[20:13] this you know 5K token prompt there
[20:16] that's okay that happens you can hear my
[20:19] computer here it's in turbo mode uh
[20:22] trying to wind down that 5 3.5 llama
[20:24] call let's go ahead and wrap up on a
[20:26] code explanation run so go ahead kick
[20:29] this off close up the context window
[20:31] prompt hit submit and this is a much
[20:34] simpler prompt right we're just asking
[20:35] cisely explain how I can use list
[20:37] comprehensions in Python in less than
[20:40] 100 words so the 100w is the real test
[20:43] here and you can see here 4 mini nice
[20:46] concise response llama 3.2 also nice and
[20:49] concise flash is good we got to dock
[20:52] another point from
[20:53] f um throwing in some symbols there that
[20:57] doesn't make sense and actually this
[20:59] entire response does not make any sense

### Minute 21

[21:01] we have Quinn 2.5 great Lama 1B I'm
[21:06] really really impressed with llama 1B
[21:07] it's crazy that this is a 1 billion
[21:09] parameter model doing all this work and
[21:11] of course Claude is fantastic so we'll
[21:14] drop a point from fi and everyone else
[21:16] looks great so we'll vote and so this is
[21:19] our end result here fi last place 3.2
[21:23] second to last place and then llama 3.2
[21:26] 1 billion parameter doing a really
[21:28] really great job actually for a 1
[21:30] billion parameter model I mean if we
[21:32] look at the size on that on disk uh
[21:35] 3.2 1 billion is only taking up 1.3 uh
[21:39] gab of of memory here so really really
[21:42] impressive really great tiny model and
[21:46] then of course we have 40 mini
[21:48] performing fantastically Claude of
[21:50] course we would not expect anything less
[21:52] and then we have Quinn and then we have
[21:54] Quinn performing insanely well um I'm
[21:57] going to be taking a look at more models
[21:59] in this fashion this is this is helping

### Minute 22

[22:01] me understand where the rankings really
[22:04] really are in general and for you know
[22:06] my specific prompts my specific use
[22:08] cases I have a whole you know kind of uh
[22:11] personal library of these prompts that I
[22:14] like to test models against I'm going to
[22:16] load this up into this system and really
[22:18] give this some more testing so I hope
[22:20] the value of this makes sense by
[22:22] combining a kind of simple reusable
[22:25] notebook like Maro and the wonderful
[22:29] local model provider and deployer AMA we
[22:32] can really really quickly just test out
[22:35] these models in comparison to each other
[22:37] right it makes a whole world of
[22:39] difference to see these results side by
[22:41] side versus in some Benchmark or off
[22:45] some blog or off some Twitter post that
[22:47] someone randomly tweets out right
[22:49] language models are really interesting
[22:50] in that you kind of need to have a feel
[22:53] for them and the feel comes from testing
[22:56] and validating them side by side
[22:58] comparing these models in a relative

### Minute 23

[23:00] basis is a really great way to get
[23:02] results and to understand their True
[23:05] Performance another kind of shocker for
[23:07] me was a 1.5 flash O2 this model is
[23:11] performing really really great and it's
[23:12] a small cheap fast model obviously it's
[23:15] still from Google it's still a
[23:17] cloudbased model but I'm really really
[23:19] happy with the results here let me know
[23:21] in the comments sections what type of
[23:24] prompts do you want tested and what
[23:26] models do you want to see those prompts
[23:28] tested against we now have this reusable
[23:30] notebook where we can come in add models
[23:33] and select different prompts at
[23:35] different temperatures and really
[23:38] understand how these prompts run against
[23:40] multiple models so this notebook is
[23:42] going to be in the description for you
[23:44] you should definitely take this test it
[23:46] against your prompts test it against
[23:48] your use cases and get a better
[23:50] understanding of how these models
[23:52] actually perform because although the
[23:54] local models are not quite there these
[23:57] models will be ready for your specific
[23:59] use case and these slms will be able to

### Minute 24

[24:02] run right on your Hardware thanks for
[24:05] watching hit the like hit the sub and
[24:07] I'll see you in the next one