# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=GUVrOa4V8iE
- **Duration:** 33:03
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 6423
- **Transcript Generated:** 2025-03-30 23:49:16

## Transcript


### Minute 0

[00:00] welcome back Engineers Andy Dev Dan here
[00:03] well we were right prompt chaining AKA
[00:06] Chain of Thought is the key for improved
[00:09] Model results on the channel we've
[00:11] released three big prompt chaining
[00:14] videos over the past year emphasizing
[00:16] the importance and the power that promp
[00:18] chaining gives your tools products and
[00:20] ultimately your users this pattern was
[00:23] so spot on that the geni leader open AI
[00:27] embedded the pattern into their new 01
[00:30] series with this release open AI reset
[00:34] the counter because it's such a powerful
[00:36] difference in the way the model performs
[00:39] by now you've seen all the click baity
[00:41] highlevel videos you know what this is
[00:43] about and if you're a subscriber to the
[00:45] channel you know what we're about here
[00:47] let's really dive in to the value
[00:49] proposition of the new 01 Series in this
[00:52] video we're going to walk through three
[00:54] viable examples showing how exactly to
[00:57] use these new reasoning models let me be

### Minute 1

[01:00] super straightforward with you this
[01:01] model is not easy to use properly as
[01:05] open AI explicitly mentions the array of
[01:08] prompt engineering abilities you and I
[01:10] have been building up don't all apply
[01:12] here we'll be using two tools from one
[01:15] of my favorite engineers in the Gen AI
[01:17] space and we're going to work through
[01:19] these examples so you can know exactly
[01:22] when it's time to double click into the
[01:25] new 01 reasoning models so you can
[01:27] maximize the value they give you
[01:33] content generation is a killer obvious
[01:35] use case of large language models one
[01:38] more difficult interesting example of
[01:40] content generation is generating YouTube
[01:43] chapters you can see here on our
[01:45] previous a coding video we have these
[01:47] chapters generated and they have the
[01:49] simple form minutes seconds title this
[01:52] problem is simple to understand but
[01:54] harder to implement so let's use chapter
[01:57] generation to show off a concrete
[01:59] example of 01 beating out the previous

### Minute 2

[02:01] state-of-the-art model Claude 3.5 let's
[02:05] look at a concrete example of what this
[02:06] looks like so I have the transcript for
[02:09] that YouTube video right here and it
[02:11] looks like this right I also have a
[02:13] prompt here that generates the YouTube
[02:16] chapters based on the transcription with
[02:18] a Tim stamp so you can see here I have
[02:20] the entire transcript pasted here and
[02:23] this is a block in this prompt so this
[02:26] is a great use case for llms but this is
[02:28] also a use case where llms typically
[02:32] fall short so let's go ahead and use a
[02:34] tool from one of my favorite Engineers
[02:36] Simon W he's built a CLI based llm tool
[02:40] that lets you run prompts directly in
[02:41] your terminal so if I type lm-
[02:45] M1 mini ping and we'll just get a simple
[02:48] response back for
[02:50] Ping so nothing special happening here
[02:52] I'll link this library in the
[02:53] description the key value proposition of
[02:55] this library is that it allows us to do
[02:57] something like this so if we CD into to

### Minute 3

[03:00] YouTube chapters and focus in on this
[03:02] specific prompt so we can see we have
[03:04] the transcript and we have the prompt
[03:06] here llm DM Claude 3.5 Sonet redirect
[03:12] this
[03:14] prompt into the llm so now we're just
[03:17] going to run Cloud 3.5 Sonet with this
[03:20] entire prompt so let's just go ahead and
[03:22] fire this off Cloud 3.5 Sonet is running
[03:25] through this it's generating results
[03:27] generating chapters for US based on this
[03:29] prompt here right and you can see some
[03:31] of the instructions right we're just
[03:32] being detailed time stamps are in minut
[03:34] seconds use the example output so we
[03:37] have a couple examples right here and
[03:38] then we have some SEO keywords we're
[03:40] trying to hit and then we have a couple
[03:41] additional instructions I can tell you
[03:43] that claw 3.5 Sonet performs okay here
[03:47] it's not the best if you watch that
[03:48] video you know we don't actually reveal
[03:50] the secret sauce of AI coating at the
[03:52] beginning of the video it's something
[03:54] like it's minute 5 or I think minute 14
[03:57] this is good what we can do here with
[03:58] this tool is redirect this output to a

### Minute 4

[04:01] new text file so I'll just say YouTube
[04:03] chapter Sonet results.txt run the prompt
[04:07] again generate the output save it to
[04:09] this text file so let's go ahead and run
[04:12] the brand new 01 reasoning models I'll
[04:14] just hit up and then I'll make a couple
[04:15] tweaks here right I'm going to do the
[04:17] exact same thing except we want to run
[04:18] the topof thee line 01 preview model and
[04:22] then we're just going to update the name
[04:24] of the output file 01 preview results
[04:26] okay so we're going to fire that off and
[04:29] let's go and take a look at our Sonic
[04:31] results right so you can see here we got
[04:33] this clean chapter generation here and
[04:35] now let's go ahead and get the results
[04:37] for 01 preview so this is going to take
[04:39] some time I'm going to go ahead and cut
[04:41] this part out all right so we got a
[04:42] result let's go ahead and take a look
[04:44] side by side so here's the 01 results
[04:48] and here's the Sonet 3.5 results so we
[04:50] still have the unveiling secret sauce
[04:53] right at
[04:54] o29 um but we do also get the correct
[04:58] time stamp at about 1354 right so

### Minute 5

[05:01] revealing the secret sauce effective
[05:03] coding patterns we can see that that
[05:04] pattern is revealed there you know we
[05:06] have some more options here we can see
[05:08] that Sonic gave us fewer chapters
[05:10] whereas 01 gave us quite a few more I'm
[05:13] curious what you think about this do you
[05:14] prefer more chapters or fewer it's
[05:17] easier to trim chapters down than to add
[05:20] chapters but if we just look through
[05:22] here I would come in I would delete this
[05:24] item here I do like the mentioning of
[05:27] Aer and cursor there's a really
[05:30] important block here SEO keywords to hit
[05:34] and you know we can just kind of go
[05:35] through and make sure you know we can
[05:36] see everything that's match we can say
[05:38] AI
[05:39] devlog um AI coding devlog that's there
[05:42] we can see Andy Dev Dan that's there
[05:46] what else do we have here we have of
[05:47] course ader cursor a devlog and then we
[05:50] have you know Secret Sauce that does get
[05:52] mentioned so you know that's good there
[05:54] if we search this on the Sonic 3.5 side
[05:58] uh you you'll see something really
[05:59] interesting right we're actually missing

### Minute 6

[06:02] a lot of our keywords even if you you
[06:05] know drop this down to 12 lines just to
[06:07] match of this reg search that we're
[06:10] doing here uh Sonet actually missed out
[06:12] a ton on our SEO keywords that we're
[06:16] asking for in our prompt so this is a
[06:19] pretty big deal and it hints at one of
[06:21] the key value propositions when you're
[06:23] wondering if you should pull up the big
[06:25] guns and use the new 01 reasoning model
[06:27] series one of the questions you should
[06:29] ask yourself is do you need the model to
[06:32] follow your instructions to a T is
[06:35] precision and accuracy important for
[06:38] your prompts if I had to explain the
[06:40] value proposition of the 01 reasoning
[06:42] models in one sentence it would be the
[06:44] 01 reasoning models are profoundly
[06:46] exceptional at instruction following and
[06:49] iterating on proposed Solutions based on
[06:52] your instructions and of course we know
[06:54] why it's better it's because it's
[06:56] thinking over and over it's creating
[06:58] drafts and then it's outputting the

### Minute 7

[07:00] results after thinking about the
[07:02] solution and iterating on it so this is
[07:04] one example where we can see although
[07:06] claw 3.5 Sonic performs well enough you
[07:09] can simply swap out the model in this
[07:11] case and you'll get a lot more
[07:13] performance and instruction following
[07:14] out of the new 01 reasoning models we
[07:17] can also dial directly into the
[07:18] transcript and just search to verify
[07:21] right so we have the secret sauce
[07:23] revealed if we go ahead and search this
[07:25] timestamp you can see that it's
[07:27] following the instructions really really
[07:28] well at the 1354 minute mark this is
[07:31] where I explicitly say this is the
[07:33] secret sauce of AI coding right our code
[07:35] is automatically getting validated for
[07:37] us this is a secret sa of coding I've
[07:40] run 01 versus Sonic 3.5 in many cases
[07:43] and the typical trend is 01 models
[07:46] although they really make you appreciate
[07:48] how fast claw 3.5 and GPT 40 mini are
[07:52] the 01 models will outclass most of your
[07:55] previous prompts especially the ones
[07:58] with more

### Minute 8

[08:00] [Music]
[08:02] detail so let's look at another really
[08:05] interesting use case for these models
[08:07] there are some things that are just too
[08:09] hard to do for the current stateof the
[08:11] art let's look at an example related to
[08:13] AI coding so let's go ahead and crack
[08:15] open this prompt here we have this
[08:16] prompt here that given a diff
[08:19] automatically looks for bugs and
[08:21] provides solutions to an AI coding
[08:23] assistant llm to automatically fix the
[08:27] code there's a lot of value here in this
[08:28] prompt if we look at the output format
[08:31] you can see that we're specifying in
[08:33] typescript using interfaces the AI
[08:36] assistant fix so we want a list of fixes
[08:38] and then you can see here and we can go
[08:40] ahead and just pull these out into a
[08:43] quick uh typescript format so it's
[08:45] easier to read right so you can see here
[08:48] that uh we have oh that's actually a
[08:50] good catch here I didn't see that so you
[08:53] can see here that we have a simple
[08:55] structure we want the file we want the
[08:57] starting line and then we want the AI
[08:59] coding resolution prompt so this is

### Minute 9

[09:01] really important this is getting kind of
[09:02] meta right we have a prompt here that is
[09:05] going to run on your code on your diff
[09:07] and then it's going to tell the LM how
[09:10] to fix the problem right we want a
[09:12] description of the bug and we want a
[09:14] severity right and that's going to be
[09:16] the output format for this prompt so
[09:17] what we need to do is get a diff of
[09:20] whatever code changes that we want
[09:22] checked and then we want the code files
[09:25] so let's look at the code files first
[09:26] this this really cool tool from s W and
[09:30] he has this tool that converts files to
[09:32] prompts and he just added this really
[09:34] great flag cxml so this is a CLA XML
[09:37] format this converts your files from a
[09:41] directory that also respects your you
[09:44] know ignore and your hidden files and it
[09:46] converts that into a prompt that you can
[09:48] use inside of prompts right so let's go
[09:51] ahead I'm just going to copy this and
[09:53] all I'm going to do is open up the
[09:54] terminal here and to paste this in I'm
[09:57] going to change the directory so I just

### Minute 10

[10:00] want it in this you know I want every
[10:01] file here copy that to the clipboard
[10:05] right so we'll just say cop it's going
[10:07] to skip the bond lock file that's
[10:09] totally fine and now I'm just going to
[10:11] add this as a file in this code base in
[10:14] API wrapper code bundle I'll just call
[10:18] that txt and then we'll just paste this
[10:20] and actually we can do axml file okay so
[10:24] you can see here this tool is really
[10:25] powerful what it's done here is it's
[10:27] gone through and it's pulled all the
[10:30] files in this code base and you can see
[10:32] here we have our notion utils we have
[10:35] our modules notion. TS constant and you
[10:37] can see right those are the contents we
[10:39] had in the previous video and it's
[10:40] basically pulled all of our content into
[10:44] a single file right so we can save this
[10:46] copy all this go back to our prompt and
[10:48] paste this in our code files right so
[10:50] I'll just go ahead and paste that and
[10:52] what I'll actually do is before I paste
[10:53] I'll use a uh C data block just to
[10:56] prevent any formatting from happening so
[10:58] I'll save that
[10:59] and let's go back up to code files

### Minute 11

[11:02] collapse that now let's get the diff
[11:04] right so I'll just create a simple diff
[11:06] um we'll say get diff uh head one and
[11:11] we'll just copy
[11:13] that and you can see that's just one
[11:15] commit backward so I'll just paste that
[11:19] diff in and so this is just all the
[11:21] changes made and now what we have is a
[11:23] let me actually wrap this in the C data
[11:25] as
[11:26] well so now what we have is a diff of
[11:31] our current code changes and all the
[11:33] related files right so you can see here
[11:34] 22,000 token prompt larger medium siiz
[11:37] prompt and what we can do now is open up
[11:41] our terminal check our files and let's
[11:43] just go ahead and run this prompt right
[11:46] this is one of the prompts that is much
[11:47] harder for the previous generation
[11:49] models to run so I'm just going to go
[11:50] ahead and go right for gold so I'll say
[11:52] llm DM topof the line o1 preview and
[11:56] then once again we're going to redirect
[11:58] the file F of our AI coding diff prompt

### Minute 12

[12:01] and let's go ahead and get this solution
[12:04] redirected into a AI coding o1 preview
[12:08] Json right because we're getting a Json
[12:10] file back here so you can see that file
[12:12] got generated there so while we're
[12:13] waiting for this to complete just want
[12:15] to you know mention the prompt format
[12:17] we're using here we're using the classic
[12:19] XML prompt format this is really
[12:22] powerful we did a video all Link in the
[12:24] description where we created some
[12:25] benchmarks to see what is the best
[12:27] prompt format this is one of the things
[12:29] that the open AI team explicitly
[12:32] mentions in their reasoning page to be
[12:34] valuable when using the new reasoning
[12:36] models right so it says use delimiters
[12:38] for clarity triple quotes XML tags
[12:41] section titles so this is one of our
[12:42] learnings from our prompt engineering
[12:44] Journey on the channel that can
[12:46] definitely stick around I don't see this
[12:47] going anywhere over the Long Haul so
[12:49] this is a really important Discovery
[12:50] really important pattern to separate
[12:53] portions of your prompt using
[12:55] specifically XML and we'll put out a
[12:57] video in the future validating that for
[12:59] the reasoning models we're going to get

### Minute 13

[13:01] about the same results using the XML
[13:03] tags versus markdown format or just
[13:06] plain text format right so let's go
[13:08] ahead and look at our preview model so
[13:10] that's completed let's go ahead and look
[13:12] at the results right so what we should
[13:14] see here is a uh you know Json file
[13:17] which is good we did get the markdown
[13:19] syntax there that's fine but this is
[13:22] really cool right so what you can see
[13:24] here is a list of fixes and the AI
[13:26] coding resolution prompt right we now
[13:29] have a highly effective reasoning model
[13:32] looking at our code looking at the diff
[13:35] it's telling us the exact issue of our
[13:37] code base right so we're getting a nice
[13:38] kind of clean code review from our
[13:40] language model but it's also giving us
[13:42] let's go ahead and do a multi-line wrap
[13:44] we're also getting the solution to pass
[13:48] back into our AI coding assistant right
[13:51] so whether it's AER cursor continue
[13:53] whatever you're using uh you can use a
[13:55] prompt like this with the 01 reasoning
[13:58] series to work through a bunch of code

### Minute 14

[14:00] remember we just you know we just ran
[14:02] this prompt on 20K tokens at the 01
[14:07] preview prices uh you know hit the like
[14:09] hit the sub support the channel we are
[14:11] definitely lighting some money on fire
[14:13] here but it is well worth it to show you
[14:14] the value of these models again we have
[14:17] the output format we're specifying
[14:19] typescript interfaces we're getting
[14:20] really detailed here with what we want
[14:22] the output to look like we're placing
[14:25] all of our code files right so this
[14:27] could be a lot larger this is kind of an
[14:29] anti- pattern because opening ey does
[14:32] explicitly mention um you know you do
[14:35] want to avoid rag as much as possible so
[14:37] pulling in a bunch of content but at the
[14:39] same time this is super relevant for um
[14:42] the model to perform so you know we're
[14:44] kind of on the line there but we have
[14:46] our code files thanks to Simon W's files
[14:49] to prompt library and then we also have
[14:52] just a raw diff right so we're just
[14:53] using get diff here and then we have
[14:55] some detailed instructions on how things
[14:57] work that's the secret SCE of the prom
[14:59] promp and then of course just a highle

### Minute 15

[15:00] purpose so that gives us this great
[15:03] result thanks to the 01 preview model so
[15:06] if this is all making sense and you're
[15:08] understanding how and when to use the 01
[15:10] series drop the like drop the sub show
[15:13] your appreciation it helps the channel
[15:14] grow and helps other Engineers like you
[15:16] find this content so you can kind of
[15:18] work through these things uh readability
[15:20] this doesn't matter who cares minor who
[15:22] cares minor who cares but it did detect
[15:25] a major bug for us right and it said
[15:27] that Imports should be place at the top
[15:29] of the file uh this can cause issues
[15:32] with module loading definitely if your
[15:34] Imports are in the wrong place there are
[15:36] some issues that can arise so if we go
[15:38] ahead and look at this this file here in
[15:41] this code base we just quickly search
[15:43] this and we just look for import yes so
[15:45] we can see this import is happening in a
[15:47] wrong location it's really interesting
[15:49] to see 01 giving us High Fidelity
[15:51] answers like this on our code so this
[15:54] kind of hits at that same reoccurring
[15:56] theme the 01 series is really really
[15:58] great at following your instructions why

### Minute 16

[16:01] because it's iterating over potential
[16:03] answers and you've seen this inside of
[16:06] chat GPT right if we just let it fire
[16:08] off here it's going to think and all the
[16:11] value here is in the fact that it's
[16:14] looking over things it's thinking things
[16:16] through step by step and it's iterating
[16:19] over potential results right this is the
[16:21] whole thing step- bystep effectively you
[16:24] know prompt chaining inside the model
[16:26] it's really really cool to see the
[16:27] actual thinking portion although as we
[16:30] know some of the reasoning is actually
[16:32] hidden on the open AI server so this is
[16:34] really cool this is going to keep
[16:35] running and you know create some result
[16:36] we don't have to wait for that let's
[16:38] [Music]
[16:40] continue all right so let's focus in on
[16:43] our last use case here so let's take a
[16:45] look at a sentiment analysis prompt let
[16:47] me show you the purpose of this prompt
[16:49] here and then we'll change the language
[16:50] mode to XML and recollapse analyze the
[16:54] aggregate sentiment of a list of
[16:57] comments from hacker news right so this
[16:59] is a Hacker News sentiment analysis and

### Minute 17

[17:02] we're actually looking at this post here
[17:05] which you know directly discuss open
[17:07] ai's new 01 Chain of Thought models uh
[17:09] again big shout out to Simon W he's the
[17:11] author of The linked content and what
[17:13] we're going to do is just do a sentiment
[17:15] analysis on this post this prompt is
[17:17] likely an entire product in itself but
[17:19] what we're going to do here is lean on
[17:21] the reasoning iterative capabilities of
[17:23] the 01 preview model we're going to
[17:25] create three segments of sentiment
[17:27] analysis and let me just show you what
[17:29] the response format looks like right so
[17:30] we have we have this kind of wild um two
[17:32] format sentiment right so let me again
[17:34] pull these into separate files we have
[17:37] both the markdown format of this
[17:39] analysis and then we have the aggregate
[17:41] sentiment right so we have this Json
[17:43] structure you can see here we have
[17:44] positive negative and nuanced and so
[17:48] this is really interesting right we have
[17:49] an entire sentiment analysis for more
[17:51] complex positive negative or neither
[17:54] content right and if we open this up we
[17:55] can see we have themes a list of themes
[17:59] we have an idea that describes the

### Minute 18

[18:00] nuanced sentiment we have the number of
[18:03] times themes like this was uh hinted at
[18:05] or mentioned and then we have a couple
[18:07] standout comments so let's pull down
[18:09] this post we're going to use a tool
[18:11] called algolia and they have the
[18:13] responses here essentially cached so we
[18:15] have all this Json we're just going to
[18:16] go ahead and just copy this
[18:18] down and we're going to paste this here
[18:21] this is going to be
[18:23] hn1 model discussion and we're going to
[18:27] make this a Json file P that in and you
[18:30] can see here we have a 100K we have
[18:32] 130,000 tokens so I have a massive
[18:34] prompt here 130k tokens let's go ahead
[18:36] and dial this prompt down a little bit
[18:39] we're going to use a classic Tool uh JQ
[18:41] we're going to run JQ uh dot on hn model
[18:45] discussion so that's the entire thing
[18:48] and now what we want to do is dial this
[18:49] down right so let's just get the
[18:51] children and so you know children
[18:53] contains all the comments so what we
[18:55] want to do here is just get children and
[18:57] let's get the first
[18:59] uh three children right let's see what

### Minute 19

[19:00] that looks like and let's go ahead and
[19:03] output that to a new file we'll say
[19:06] hn1 iter children. Json so we have that
[19:09] new file it's just the children and you
[19:11] can see there we're down to 10K tokens
[19:13] so much more manageable let's go ahead
[19:15] and just work on a you know smaller
[19:16] segmented version of this and let's
[19:18] operate on these 10K tokens right so if
[19:20] we line collapse we can see we're still
[19:22] getting a lot of decent comments here um
[19:24] a lot of good stuff happening right so
[19:26] let's go ahead and run our sentiment
[19:27] analysis prompt on this file if we go
[19:30] ahead close this go back to our prompt
[19:32] here you can see that we have hn. Json
[19:35] so we're going to pass in our Json here
[19:37] paste in our new set of results
[19:40] here right so now we have all those
[19:43] comments if we open up the instructions
[19:44] here we can kind of reveal some of the
[19:46] secret sauce here basically we're saying
[19:48] respond in this you know specific
[19:49] response format I'm referring to the
[19:51] block there and what we want to do is
[19:54] you know basically create the Nuance
[19:56] sentiment and the the you know positive
[19:59] and negative as well and again the great

### Minute 20

[20:02] part about the 01 series is that it's
[20:05] going to run the prompt it's going to
[20:07] iterate on it and it's going to continue
[20:10] reflecting on the results based on my
[20:12] instructions right so let's go ahead and
[20:13] just fire this off using Simon W's llm
[20:16] tool so we have the prompt here let's go
[20:18] ahead and just kick that off we'll say
[20:20] lm- M1 preview left direct our sentiment
[20:25] prompt and let's go ahead and pipe the
[20:26] results out results 01
[20:29] Json and this is going to give us a Json
[20:30] file back so we'll go ahead let that
[20:32] prompt kick off and that should generate
[20:35] a brand new sentiment analysis for us
[20:37] automatically and you know we can reuse
[20:39] this it's all about what you're passing
[20:41] into the hn. Json and again you know one
[20:44] of the great Parts about structuring
[20:46] your prompt like this and having them in
[20:47] text and using a great tool like llm
[20:50] from the CLI is that everything is
[20:52] reproducible I have the static prompt
[20:54] that I can improve over time I can run
[20:56] benchmarks against it I can run a test
[20:58] Library like prompt Fu on this prompt

### Minute 21

[21:00] and compare to others and we can know
[21:03] with certainty that this prompt is going
[21:05] to outperform other prompts I'm really
[21:07] excited to you know share more about
[21:09] this model this video is already getting
[21:10] really long I'm going to try to edit it
[21:12] down a lot for you guys but there are so
[21:14] many new things so many new ideas to
[21:16] cover with the 01 reasoning models the
[21:18] capabilities here are super off the
[21:20] charts you know drop the like drop the
[21:21] sub if you're seeing a lot of the value
[21:23] that these models can give you part of
[21:26] the complexity in this prompt is that
[21:28] this response format is asking for a lot
[21:31] right I can guarantee you this is going
[21:32] to run for you know two maybe 3 minutes
[21:35] based on all my work with this model so
[21:37] far I'm asking for a lot here right
[21:40] think about what this is asking first
[21:41] off do a sentiment analysis with both
[21:44] positive negative and Nuance right so
[21:46] this is new or or it's a newer idea
[21:49] right comments on each one of these I
[21:51] probably could have pulled it out into a
[21:52] separate type but you know I just place
[21:54] it all here and you know I want some
[21:57] standout comments that you know reflect
[21:59] the idea that creates the theme and it

### Minute 22

[22:01] has to be positive right so this is an
[22:03] action-packed prompt normally I would
[22:06] create my own prompt chain to you know
[22:08] do segments of what this is doing so not
[22:11] only am I asking for three perspectives
[22:14] with multiple themes I'm also asking 01
[22:17] to give me a entire markdown version of
[22:21] this right so you can see here it's
[22:23] still spinning while I'm yapping off um
[22:26] but this is really really incredible
[22:28] right so you know you can see we have
[22:29] this instruction and the markdown
[22:30] response respond with your results from
[22:34] you know this object type right but in
[22:37] human readable markdown format right so
[22:39] there's a lot going on in this prompt
[22:41] this is something that you just
[22:43] absolutely could not give to a previous
[22:46] generation model and expect great
[22:47] results out of but you know for my
[22:49] testing from some benchmarking I can
[22:51] guarantee you this is going to give us
[22:52] some really incredible results and you
[22:55] know this is why I said in the beginning
[22:57] um it is hard to use the new 01

### Minute 23

[23:00] reasoning models properly and what do I
[23:02] mean by properly I mean you can really
[23:04] push these models to do incredible
[23:07] things and you can you know actionpack
[23:09] your instructions and your rules and you
[23:12] know some of the content right some of
[23:14] your XML or formatted blocks you can
[23:16] really pack it in and while it's working
[23:19] while it's iterating it's going to keep
[23:21] looking back at your prompt and it's
[23:23] going to you know keep analyzing the
[23:25] results that it's iteratively building
[23:27] up behind the scen scenes and check it
[23:30] against what you're asking you know
[23:33] there's a much simpler version of this
[23:34] prompt where it's already returned with
[23:36] the result right because it's just
[23:38] simpler I'm not asking a lot from it but
[23:41] you know that's that's kind of a good
[23:42] way to phrase it you can ask a lot more
[23:44] from these reasoning models because
[23:46] again they have some version of thinking
[23:48] step by step of reasoning so on and so
[23:50] forth so there we go we just got our
[23:52] result let's go ahead and take a
[23:54] look okay so here's our sentiment
[23:56] analysis right so first off let's check
[23:58] the structure Perfect Right Json

### Minute 24

[24:01] markdown let's first browse through the
[24:04] Json and just make sure we have all of
[24:06] our section so great we have negative
[24:08] nuance and positive right so let's just
[24:10] dial into one of these you can see here
[24:11] we have our themes so this is really
[24:13] great right we have let's see how many
[24:15] themes we have here right we have two
[24:17] concrete themes let's see what the theme
[24:19] is right so there's a positive theme
[24:21] excitement about advancements and
[24:22] potential of GPT models right including
[24:24] GPT 5 there's some really great comments
[24:26] in here we can you know validate I know
[24:28] some Engineers you might be one of them
[24:30] that are always worried about
[24:31] hallucinations you can easily double
[24:33] check this we just search right we have
[24:35] a great response here right and we can
[24:37] see that response is here in The Hacker
[24:39] News thread that's great you we have
[24:41] another one here I know sometimes sketch
[24:43] if AI can do this on 64k tokens
[24:46] iteratively full multi loal I don't
[24:49] think I've actually been scared of super
[24:50] intelligence singularly until just now
[24:53] now this is AI yeah totally right great
[24:55] take completely agree right so you know
[24:57] we have some positive Stand Out comments
[24:59] with this theme um let's go ahead and

### Minute 25

[25:01] look at another positive theme right
[25:02] what was our other theme Here Right
[25:04] anticipation on ai's impact uh totally
[25:07] yeah that makes sense so you know this
[25:09] this user uh the homie
[25:13] L he's talking about the data shortage
[25:16] problem this is true iterative
[25:18] development these models are going to
[25:19] get deeply embedded into idees like
[25:21] cursor heads right so you know this is
[25:23] something that's happening right now
[25:24] they already have this model and you
[25:26] know you can already run it on cursor
[25:27] and AER if we just search this you know
[25:29] you can just kind of see that there
[25:31] we've already taken a look at that um
[25:32] and then we can dig into more Nuance
[25:34] takes right so this is kind of cool
[25:36] right so we have positive negative and
[25:38] then we have nuance and let's go ahead
[25:39] and format our markdown this is pretty
[25:42] gnarly right I asked for a sentiment
[25:44] analysis with positive nuance and
[25:46] negative in Json format then I ask for a
[25:49] markdown version of that in the same
[25:51] prompt right so let's go ahead and just
[25:52] take a look at this let's go a and move
[25:54] this to markdown and let me go ahead and
[25:56] format this
[25:58] and just get that formatted so this is

### Minute 26

[26:01] really great right let me goad and open
[26:02] up a preview and move that here so you
[26:05] know you know we could almost just take
[26:08] this and post it to a blog or something
[26:11] right you know we have our positive
[26:12] sentiment go ahead and look for our
[26:14] Nuance sentiment right so mixed feelings
[26:16] about hidden reasoning tokens with
[26:18] concerns about transparency and
[26:20] debugging okay so you know that makes
[26:22] sense right as a developer This is
[26:23] highly concerning harder to debug uh
[26:25] what went wrong pricing is silly totally
[26:27] makes sense right as a user I really
[26:29] don't care okay also makes sense LMS can
[26:32] be magic black boxes and I only care
[26:34] about the end result itself not the end
[26:36] path it'll be interesting to see how
[26:38] this progresses a great take definitely
[26:40] more nuanced right it's not just as
[26:41] straightforward as this is a good thing
[26:43] or a bad thing but uh it is true you
[26:45] know as a developer we would like to see
[26:47] into what's going on under the hood how
[26:50] can I change my inputs to get different
[26:52] outputs but um you know this definitely
[26:54] makes it harder you know we can't really
[26:56] see into the model at the same time this
[26:58] is more my perspective especially as

### Minute 27

[27:00] time goes on I care more about user
[27:02] output related things right as a user I
[27:04] don't really care um llms are already
[27:07] magical black boxes we only truly care
[27:10] about the end result I think that's
[27:11] super true but so you know we hop back
[27:13] here so that's you know a great Nuance
[27:16] take we have a couple more here and then
[27:17] of course at the end here we have our
[27:19] negative sentiments um we don't have to
[27:22] go through all these you know go on
[27:23] Hacker News read this yourself digest it
[27:26] um this is just a really interesting use
[27:27] case for you know these 01 reasoning
[27:30] models again just really really kind of
[27:32] gnarly that it was able to do everything
[27:35] I'm asking for here then create a
[27:37] markdown format version of it right
[27:39] really really powerful stuff Let's uh
[27:42] let's wrap up let's talk about some
[27:43] ending thoughts here let's talk about
[27:44] where this is going what we're going to
[27:46] do next here on the channel based on
[27:47] this model and this new paradigm of
[27:52] models so like I mentioned if I had to
[27:55] really explain the value proposition in
[27:57] one sentence it's that the 01 reasoning

### Minute 28

[28:00] models are profoundly exceptional at
[28:03] instruction following and iterating on
[28:05] proposed Solutions based on your
[28:08] instructions so you know let me just
[28:10] compress that again for you the real
[28:12] value here is instruction following plus
[28:15] iteration and all of the results that
[28:18] they mention all the benchmarks they all
[28:20] back that up all my time so far has
[28:23] revealed the exact same thing that the
[28:26] more complex The Prompt is the more
[28:29] steps there are the better results
[28:31] you're going to get it is a stem focused
[28:34] set of models it's focused on reasoning
[28:36] is focusing on you know problem solving
[28:38] so that's something to take into account
[28:40] although I have to say most of the
[28:42] benchmarks and most of the experiments
[28:45] I've run show this model beating out
[28:48] Sonet almost across the board and I know
[28:51] that they do have a mentioning here of
[28:54] uh the fact that some people prefer the
[28:56] previous models for you know writing and
[28:58] editing text I think this is probably Up

### Minute 29

[29:00] For Debate honestly whether this is
[29:03] actually functionally true this is this
[29:05] is just preference okay um I think that
[29:09] the reality is is that this new
[29:10] reasoning model can perform all these
[29:12] things at an accelerated level because
[29:14] it is thinking step by step but you know
[29:16] more details there more to kind of work
[29:18] through I don't know if that's actually
[29:19] true or if I'm just super high on this
[29:22] model right now right so you know a
[29:24] couple more things to note in terms of
[29:26] upcoming videos in terms of where the
[29:27] channel is going it's the same as always
[29:29] we have been predicting this we knew
[29:31] that better models were coming out we've
[29:33] been preparing for the 100x this is not
[29:35] a 100x so we're definitely overprepared
[29:38] but uh you know we have lots of
[29:39] interesting content coming up I'm really
[29:40] excited to share with you we're going to
[29:42] be AI coding with these models the
[29:44] creator of ader Paul just put out a
[29:46] brand new Benchmark showing that um the
[29:49] King has been usurped 01 preview does
[29:51] actually beat out Claude 3.5 Sonet of
[29:54] course it's not functionally going to be
[29:57] better it's one of those things things
[29:58] where in theory it's better but based on

### Minute 30

[30:00] the speed no one's going to be firing
[30:02] off 01 prompts as much as they are claw
[30:04] 3.5 Sonic prompts right so we're getting
[30:07] there uh this is a massive Improvement
[30:09] there are many tricks that we can employ
[30:12] to push the performance of 01 even
[30:14] further as we mentioned in previous
[30:16] video hint hint promp chaining is still
[30:19] a great technique to use so they do say
[30:22] to avoid Chain of Thought prompts but
[30:24] they don't ever mention here prompt
[30:26] chaining and as we've explored on the
[30:28] channel prop chaining only gets better
[30:31] and scales with these new models so you
[30:33] can imagine we have three uh uh 01 mini
[30:37] or 301 preview calls chained together so
[30:40] these are some kind of you know deeper
[30:42] State bleeding edge ideas that we'll be
[30:44] exploring on the channel uh there's also
[30:45] the insane epic idea of the fusion chain
[30:49] um if you know you know we'll talk about
[30:51] that more in future videos so a couple
[30:52] interesting things to mention here about
[30:54] pricing if you look at claw 3 Opus we
[30:56] have 15 in 75 out per million the new 01

### Minute 31

[31:01] models the new 01 preview top of the
[31:03] line is actually cheaper than CLA 3 Opus
[31:08] so even though it seems expensive
[31:10] remember what Opus was like it's a great
[31:12] model but it is not doing anything like
[31:16] 01 preview is it is nowhere near as
[31:18] great as 01 preview things are still
[31:20] getting cheaper which reiterates one of
[31:22] the themes we have been holding on to
[31:24] over the course of this channel so years
[31:26] now the price of llms is still going to
[31:30] zero this is a consistent Trend we're
[31:31] seeing even though this is a marked up
[31:33] model and you might be more hesitant to
[31:35] use this um you know keep in mind this
[31:37] is the first version of this of course
[31:39] it's the expensive version of this open
[31:41] aai and other providers are going to
[31:42] keep pushing these costs down there are
[31:44] a lot of cases and a lot of prompts that
[31:46] we ran today that 01 mini would have
[31:48] performed just as well as 01 preview but
[31:51] you know as we're testing out these
[31:52] models I highly recommend you focus on
[31:54] the state-of-the-art see what's really
[31:56] possible and then down size um and save
[31:59] you know some resources after you know

### Minute 32

[32:01] that many can perform on the same level
[32:03] as1 preview so open AI has played their
[32:05] hand now it's time for anthropic to drop
[32:09] the new 3.5 Opus 3.5 H coup it's time
[32:11] for Google to you know drop Gemini 1.5
[32:14] Ultra or two time to see what the other
[32:16] players do so you know in summary these
[32:18] new reasoning models open up a whole new
[32:20] world of possibilities for generative Ai
[32:24] and for you and I as Engineers with our
[32:26] boots on the ground building tools
[32:28] building products and building valuable
[32:30] software for ourselves and our users if
[32:33] you're not subscribed and you made it
[32:34] this far on the video Drop the sub drop
[32:36] the like drop a comment let me know what
[32:38] you think about these models do you see
[32:41] the value proposition in these models
[32:42] that I see do you see something else are
[32:44] there some aspects of these models that
[32:46] you think I missed drop a comment down
[32:47] below whatever comes next we'll cover it
[32:50] here on the Channel with useful in-depth
[32:52] guides like this where we really find
[32:55] the value of it all thanks for watching
[32:57] keep keep building stay focused and I'll
[32:59] see you in the next one