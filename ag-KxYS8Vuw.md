# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=ag-KxYS8Vuw
- **Duration:** 22:04
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 4057
- **Transcript Generated:** 2025-03-30 23:49:18

## Transcript


### Minute 0

[00:00] what's up Engineers Andy Dev Dan here
[00:02] cursor has been absolutely popping off
[00:04] in the tech ecosphere this is due to the
[00:07] new multifile editing composer feature
[00:09] we covered this in the previous video
[00:11] I'm a huge fan of cursor but the truth
[00:14] is cursor is a Clos Source commercial
[00:16] application and putting all your eggs in
[00:19] one basket this early in the generative
[00:21] AI age is a mistake on the channel we've
[00:24] been benefiting from AI coding and
[00:26] multifile editing for over a year now
[00:30] all thanks to the original llm based AI
[00:33] coding tool AER this is a coding tool
[00:36] that as you'll see in this video
[00:39] typically outperforms cursor while
[00:41] giving you more control over the AI
[00:43] coding process not to mention AER is
[00:46] completely free with tons of llm
[00:49] providers and Paul the engineer that
[00:51] built AER puts out some incredible blogs
[00:53] to keep you updated on AI coding so in
[00:56] this video I want to show you another
[00:58] option outside of cursor to help you

### Minute 1

[01:00] diversify your AI coding tools and we're
[01:02] going to look at AER by making a change
[01:05] to a brand new mermaid AI agent that I'm
[01:07] building that can help you build
[01:09] diagrams faster than ever if you don't
[01:11] know what mermaid is it is a awesome
[01:13] textbase diagramming and charting tool
[01:16] you can basically pass in simple blocks
[01:18] of text and get out node Edge based
[01:22] diagrams let's Dive In by first showing
[01:24] off how our mermaid diagram AI agent
[01:27] works
[01:30] so the mermaid agent is really simple
[01:32] you run a command you ask for the
[01:34] diagram that you're looking for you
[01:36] specify an output image and then
[01:37] optionally you can pass in a input file
[01:40] that the mermaid AI agent then reads
[01:42] generates diagrams and then you can on a
[01:44] loop improve the diagram let me just
[01:46] show you what that looks like I'll open
[01:47] up the terminal and I'm going to run
[01:49] this command so I'm just going to go
[01:50] ahead and kick this off and then we'll
[01:52] walk through exactly what's going on
[01:53] here so you can see the diagrams getting
[01:55] generated there and now we have this
[01:58] image fully generated so let's go ahead

### Minute 2

[02:00] and just dissect that prompt a little
[02:02] bit right so we're using typer so I have
[02:04] this function called mer iter and then
[02:06] we have this prompt right flowchart
[02:08] explaining why communication via
[02:10] diagramming is so important for
[02:12] engineering great products and then I
[02:14] say include things like time saved
[02:16] faster iteration increase trust and more
[02:19] then I specify the output file so based
[02:21] on that we got this really really cool
[02:23] diagram the cool part about this tool is
[02:25] we can continue to iterate so I'm
[02:27] running the iterate command and I can
[02:29] just say add additional nodes Group by
[02:33] benefit okay and so now with this human
[02:36] in the loop pattern we're going to Loop
[02:40] and hopefully we'll have our elements
[02:42] combined together it's kind of squished
[02:45] so let's go ahead and clean this up a
[02:46] little bit I'll say drop
[02:49] subgraphs and make diagram LR so now
[02:53] we're going to make it run left to
[02:58] right a awesome so it looks pretty good

### Minute 3

[03:01] right we can see that our benefits of
[03:03] diagramming are grouped together by time
[03:06] saved clear communication team alignment
[03:08] and then the last thing I want to do
[03:09] here is I want every single node to go
[03:11] into engineering great products so I'm
[03:13] just going to go ahead and add that as a
[03:15] final prompt right create an edge
[03:18] between the last notes and Engineering
[03:22] grade products so we're going to ask
[03:25] that La for that last change there and
[03:28] we should get a full perfect we should
[03:30] get a diagram generated there right this
[03:32] is a killer use case for generative AI
[03:35] when you combine it with a fantastic
[03:37] text based tool like mermaid you can
[03:39] rapidly iterate on asset generation so
[03:41] if we go ahead and look at the generated
[03:43] output file you can see this is awesome
[03:46] but inside of our code base here we're
[03:48] only saving the last generated file so
[03:51] our task here today is going to be to
[03:53] take this file move it into the output
[03:56] directory you can see we have a couple
[03:57] other items generated here and we also

### Minute 4

[04:00] want to save all of the previous
[04:01] iterations of this file getting
[04:03] generated right so let's go ahead and
[04:05] just make a couple tweaks to this code
[04:06] base let's get into the AI coding of
[04:08] this I have a couple key pieces of value
[04:10] I want to share with you
[04:13] here one of the great Parts about ader
[04:15] is that it runs right in the terminal so
[04:17] all I'm going to do is type
[04:19] AER no autoc commits we're going to run
[04:23] with-- Sonet so you can see here we're
[04:27] running Sonet with the diff edit format
[04:30] we have infinite output and in this
[04:32] codebase we have 19 files let's go ahead
[04:34] and add files to our context window to
[04:36] do that I'll type SL add and if we look
[04:39] at the code base here I want everything
[04:41] under Source mermaid agent so I'll
[04:44] literally just type Source mermaid agent
[04:48] slashstar now you can see I have every
[04:50] single file in that directory I have all
[04:52] my python files so now if I type SL
[04:54] tokens you can see exactly how much
[04:57] every single run costs and you can see
[04:59] all the files in your context window so

### Minute 5

[05:02] this is fantastic let's go ahead and
[05:04] just ask the codebase let's ask AER
[05:06] let's ask our llm what changes we need
[05:09] to make in order to move our generated
[05:12] image into the output directory we also
[05:14] want to add the iteration number and
[05:16] save that as well so back in the
[05:18] terminal I'll clear and I'll just type
[05:20] slash ask in what function are we saving
[05:24] the mermaid diagram images and so with
[05:28] all the context of the code base claw
[05:30] 3.5 running on AER has shown us exactly
[05:34] where this is there's this function
[05:36] called mm and we have this save image
[05:38] locally if we go ahead and search all
[05:41] hop to this you can see that we just
[05:43] have this simple save command it's just
[05:45] saving the file name that gets passed in
[05:47] right and the mm just builds the image
[05:51] based on the graph that gets generated
[05:52] by our llm and then we just save that
[05:54] image right so fairly simple let's go
[05:56] ahead and ask for the changes we'll need
[05:59] to move this to the output directory

### Minute 6

[06:01] right and I'm being super verbose here
[06:03] right just cuz we're walking this
[06:04] through and I want to share how I think
[06:06] about AI coding with you but normally I
[06:08] would like I already know where this
[06:10] code is I don't need to ask I would just
[06:12] go ahead and prompt it although I do
[06:14] want to highlight something here that
[06:15] we'll talk about in a second building up
[06:17] these conversations with AER with the
[06:19] slash ask command is super super
[06:21] important and you'll see why in a second
[06:23] here so I'll go ahead and type SL ask
[06:26] can we reuse existing functionality to
[06:30] save that file to the
[06:38] uper okay so as you can see here there's
[06:42] this build file path utilities function
[06:46] and we can go ahead and just grab this
[06:48] right and search all so you can see here
[06:50] we already have this pattern set up of
[06:53] using the build file path to right to
[06:56] our output directory right so it works
[06:59] just like this right we have this

### Minute 7

[07:00] function we have this simple constant
[07:02] that gets combined with the file name
[07:04] and make sure that the directory exists
[07:06] right so simple enough so this is really
[07:08] cool right and our AI coding assistant
[07:10] picked up on this and now we can do
[07:13] something really really cool so before I
[07:14] mentioned that you know normally you can
[07:16] just type the changes that you want I've
[07:18] been using this pattern of running the
[07:20] slash ask command to have more
[07:23] conversations with your AI coding
[07:25] assistant and then after you know the
[07:27] changes it's going to make then you say
[07:28] go ahead make the changes so that's
[07:30] literally what we're going to do here go
[07:32] ahead and make that
[07:35] change so you can see there we got the
[07:38] import and we have the update using the
[07:42] new output path so go ahead and close
[07:44] this let's open up that file we go to
[07:46] the mermaid py our save image locally is
[07:49] now going to first run the build file
[07:52] path from our utils right so really
[07:56] simple I just wanted to walk through
[07:57] that so you can see exactly how ater

### Minute 8

[08:00] using the ask command can build this up
[08:02] for us right so that's a simple change
[08:05] that looks good before we go ahead and
[08:06] run the example let's go ahead and get
[08:08] that second change in there right so ask
[08:11] draft the change needed every iter file
[08:15] in our merer function and I'll say every
[08:21] iter mermaid chart okay and I'll run
[08:24] that sometimes when you run these
[08:26] changes and you run your AI coding
[08:28] prompts it changes too much and it makes
[08:31] mistakes and it does things wrong by
[08:33] running the ask command you can ask for
[08:36] a full-on draft you can see the
[08:38] reasoning behind your AI coding
[08:40] assistant and then you can say make
[08:42] these tweaks or go ahead and Implement
[08:43] that so overall that looks good but all
[08:46] I wanted to do is save the new output
[08:49] file name and I basically only want this
[08:52] right so we're going to iterate while
[08:54] we're running this while true and we can
[08:56] go ahead and just take a look at this
[08:57] code in the main file here so you can
[08:59] see we have we have this Loop during our

### Minute 9

[09:00] main Eder call and all we want to do is
[09:03] update to make sure that saves a new
[09:05] file in the output directory right you
[09:07] know I'm just going to highlight this
[09:09] and only implement this portion and I'm
[09:14] just going to paste that
[09:22] in okay so let's go ahead and see how
[09:26] it's done there so now we have iteration
[09:28] count we now have the initial output
[09:30] file that's good so that's getting
[09:32] saved and then we should see our file
[09:36] getting incremented here right exactly
[09:38] like what we were looking for we have
[09:39] the iteration count and then we're
[09:41] saving this in a loop awesome so this
[09:43] looks right let's go ahead and um what
[09:45] we'll do is we'll open up a new terminal
[09:47] we'll go full screen here and now let's
[09:48] go ahead and iterate on a pie chart
[09:51] let's use a pie chart as an example
[09:52] right this is one of the cool Parts
[09:53] about mermaid there are varieties of
[09:55] charts you can build so if we look at
[09:57] our read me we'll have an example here
[09:59] here of a uh pie chart where is that pie

### Minute 10

[10:02] chart there it is so I'm just going to
[10:03] copy this command
[10:05] here paste this and go ahead and update
[10:09] to use the mer iter
[10:12] command Okay so our merid AI agent is
[10:15] going to go ahead and create this pie
[10:17] chart for us awesome so you can see that
[10:19] looks great it's iterating right now so
[10:21] what I'm going to do is ask for a change
[10:23] I'll say you know coding testing
[10:26] documentation meetings go ahead and add
[10:28] a new activity here we're going to say
[10:30] um add new pie slice mastering AI coding
[10:34] with Indy Dev Dan go ahead and get that
[10:39] slice added there all right so this
[10:41] looks great let's go ahead and check our
[10:43] files so if we open this up you can see
[10:45] we created this under an additional
[10:47] inter session that's fine but if we look
[10:48] at these images we can see we have time
[10:51] spent on Project task and then we have
[10:53] that additional you know 5% U mastering
[10:56] a coding with any de by the way if
[10:58] you're interested in the interest
[10:59] section of AI coding and AI agents

### Minute 11

[11:01] definitely drop a like and consider
[11:03] subscribing to the channel the way I see
[11:05] it the world of generative AI is
[11:08] extraordinarily simple you're either
[11:10] learning and using gen AI Tech like AER
[11:14] cursor and tools like our mermaid AI
[11:16] agent or you're getting left behind fast
[11:19] on the channel AI coding and agentic is
[11:22] our bread and butter here we spot Trends
[11:24] before they happen we extract value we
[11:26] learn and we move on don't fall behind
[11:29] enjoying the journey so let's keep going
[11:33] here let's go ahead and do something
[11:36] bigger we go up to the top level here
[11:38] collapse all of our code you can see
[11:39] here we have two commands we have myrr
[11:42] and then we have myr iter so we've been
[11:44] working on mer iter we you know created
[11:46] this additional session directory it
[11:48] made that change for us that's awesome I
[11:50] want to go ahead and create one more
[11:52] command here I want this bulk command
[11:55] and what this is going to do is
[11:57] basically create five versions of of a
[11:59] flowchart right so sometimes you're not

### Minute 12

[12:01] sure what you're looking for and you
[12:03] just want you know n iterations of it so
[12:06] all we should need to do here is pass in
[12:07] an additional - c flag and that should
[12:11] do the trick for us we're going to use
[12:12] our favorite open source free AI coding
[12:14] tool AER and we're just going to ask for
[12:17] this change let's hop back to the
[12:19] terminal I'll go ahead and clear the
[12:22] chat and I'll also clear all of our
[12:25] files I'm going to go/ add I'm going to
[12:28] add the read me and then I'll say you
[12:30] know add of course we're going to need
[12:31] the main and let's go ahead and add our
[12:34] mermaid agent and let's go Ahad and add
[12:38] um our mermaid call as well and that
[12:41] should be good so with these files we
[12:43] can go ahead and type SL tokens to see
[12:46] what our context Windows like that looks
[12:48] good and now let's go ahead and request
[12:50] a change so um read read me and let's
[12:55] build out our new my bulk command
[12:59] but add another- C create inv verions of

### Minute 13

[13:05] our diagram I also forgot to add our
[13:09] type file so I'm just going to copy this
[13:11] command and then I'll add our typings
[13:14] file here this has all the types all the
[13:17] pantic types for this code so you can
[13:20] see here we have a couple different
[13:21] types for every function I have this you
[13:24] know oneshot mermaid prams and then our
[13:26] iterate mermaid prams this is what gets
[13:28] passed in and created on the top of the
[13:31] the method right so this gets passed
[13:33] into this actual functionality so I'm
[13:35] going to say that so I'll paste this
[13:36] back in and then I'll say create a new
[13:39] pram type for this method and let's call
[13:44] it bulk mermaid
[13:47] params okay so I'm going to go ahead and
[13:50] let AER make these multifile changes for
[13:54] us automatically I'm hoping in just one
[13:57] shot without having to do anything here

### Minute 14

[14:00] it's going to make all these changes for
[14:01] it so let's go ahead and see if AER and
[14:04] Sonic 3.5 can oneshot this new
[14:09] feature all right nice so we got a
[14:11] little
[14:12] anthropic server eror but this is
[14:14] awesome so it's going through it's
[14:16] making those changes it added the type
[14:17] it added the new command it's importing
[14:19] it it's updating the mermaid agent to
[14:22] make these changes and now it wants to
[14:25] know if we need to create this input
[14:27] file.txt I'm not sure what this is let's
[14:31] go ahead and hit yes we'll see what that
[14:32] looks like in the end so all right so
[14:34] let's go ahead and hop back to our
[14:35] editor and now we should be able
[14:38] to look through all of our commands here
[14:41] so we can see we have our new merb
[14:44] command and you know what I'm not even
[14:45] going to look at this code right uh we
[14:47] can kind of see that it looks like it's
[14:48] in the right form um all I'm going to do
[14:50] is Rerun a prompt so I'm just going to
[14:53] go ahead and copy this so you can see
[14:54] here uh we have the prompt so this is a
[14:57] flowchart of the setup instruction
[14:59] we're going to call this setup

### Minute 15

[15:00] diagram.png we're loading our readme so
[15:04] literally this readme file right here
[15:06] right and then we're going to say- C5
[15:09] and that's the new flag that we have
[15:12] right here and this is going to be the
[15:14] count and so let's just go ahead and run
[15:16] this let's see um if AER did this all
[15:19] for us in one shot
[15:36] okay so interesting results there um it
[15:41] looks like it did generate a couple
[15:44] different versions you know we have
[15:46] install uh UV install dependencies and
[15:49] you know before we look through these
[15:50] diagrams you can see here that that's
[15:52] exactly what our setup instructions look
[15:54] like right we're using UV the brand new
[15:57] hyper fast python manager you use UV

### Minute 16

[16:00] sync to download all the requirements
[16:02] set up the open AI key and we have a
[16:04] couple optional setups and then we have
[16:06] just running our commands right so if we
[16:09] look at the diagrams um these look
[16:11] really great right so we have install UV
[16:13] install dependencies setup key uh we run
[16:15] single run interactive and then we have
[16:17] our brand new run bulk right so this was
[16:19] one version we can go ahead and close
[16:21] this we have another version right here
[16:23] this also looks good has an additional
[16:25] done node some of the node titles are a
[16:28] little simpler looks good also um this
[16:30] one's really interesting right so this
[16:32] is the power of generating multiple
[16:33] versions right you might you might want
[16:35] something more verbose like this so we
[16:37] have start install UV install
[16:39] dependencies with UV sync nice I like
[16:42] the additional detail there and then we
[16:44] have setup open AI key as invar awesome
[16:48] then we have this optional decision
[16:49] diagram this is really cool you know we
[16:51] can also in this code base setup
[16:53] anthropic Vertex or Gro and then we have
[16:56] run a single generation and then if we
[16:58] want the interactive generation you know

### Minute 17

[17:00] we want our my- so um we also have that
[17:04] as an option and then we have just a
[17:06] simpler version here right so just top
[17:07] to bottom optionally set the other keys
[17:10] and then we can run single run
[17:12] interactive or run bulk so it actually
[17:14] look like this this did work perfectly
[17:16] in a single shot right I won't bother
[17:18] you with going through the code but uh
[17:20] you know we can see that um AER
[17:23] generated all this in one shot if we
[17:25] look back at this run it needed to edit
[17:29] three files to make this happen right
[17:31] and we could also see which I really
[17:33] love you can see we sent 18K tokens
[17:35] received 1K that cost 7 cents total
[17:38] session total is 30 cents really really
[17:41] nice to see those metrics right at the
[17:42] top here as we discuss on the Channel
[17:44] all the time the cost of LM is going to
[17:46] zero the context window is going to
[17:49] 150100 million and Beyond a really
[17:51] interesting post just came out backing
[17:54] that we have 100 million context token
[17:56] Long window with this company called the
[17:58] magic team um which they're new on my

### Minute 18

[18:01] radar apparently they've been teaming up
[18:03] with Google Cloud to crack the 100
[18:05] million token context we'll be keeping
[18:07] an eye on this on the channel you know
[18:09] if we hop back here we can see that you
[18:11] know across three files AER and Claude
[18:14] 3.5 Sonet just nailed everything that
[18:17] needed to happen to generate this change
[18:20] and we even got you know this uh the
[18:23] mermaid uh bulk progams which is exactly
[18:25] what we we asked for right if we open up
[18:27] our typings file we can see we have bulk
[18:30] mermaid prams right here and it looks
[18:32] perfect right we got the prompt output
[18:34] input count and uh this is really
[18:36] awesome to see so big shout out to ader
[18:38] this is a fantastic tool I wanted to
[18:40] share this with you because I don't want
[18:42] you to be locked in to the close Source
[18:44] tools like I mentioned I love cursor I
[18:46] use cursor but I also love AER and use
[18:49] AER this one's free it's open source
[18:51] it's a lot more customizable Paul also
[18:53] has some really really killer insights
[18:57] and some incredible benchmarks
[18:59] so you know if you check out the AER llm

### Minute 19

[19:01] leaderboards a large portion of the AI
[19:04] coding ecosystem looks at this web page
[19:08] right here to know what is the
[19:09] performance of this new model on real
[19:12] code bases using AER right so this is
[19:15] really cool you can see claw 3.5 Sonet
[19:18] as we've been saying on the channel it
[19:19] is the best AI coding assistant large
[19:21] language model by far hands down this is
[19:24] The Benchmark to look at Paul with his
[19:26] work on AER is just the leader here in
[19:29] the AI coding space I would love to see
[19:31] cursor put out some benchmarks like this
[19:33] where they compare and use their tool
[19:35] their prompts to um you know create some
[19:38] uh concise benchmarks for us to
[19:41] understand and internalize how they see
[19:43] model performance with their tool so
[19:45] anyway tons of value here definitely
[19:48] check out AER as an alternative to
[19:50] cursor as I've mentioned in the past I
[19:52] go back and forth between these tools
[19:54] but when I'm coding deeply when I'm
[19:56] working fast uh there is just no more

### Minute 20

[20:00] precise tool than AER you come in you
[20:02] can check your token usage you can add
[20:04] and remove files you can add directories
[20:07] huge fan of this it's a lot simpler AER
[20:10] really leans on the power of the llm and
[20:12] the Simplicity of a just a really clean
[20:15] AI coding architecture so anyway that's
[20:17] the Mermaid diagram AI agent this is
[20:20] going to be in the description for you
[20:21] feel free to check this out regardless
[20:23] of how you generate your diagrams I
[20:25] highly recommend you dig into some type
[20:27] of gen AI tool like this even if you
[20:30] just go for you know right for the
[20:31] simple claw or chat gpg interface
[20:34] generating diagrams on the Fly is so so
[20:37] important and so valuable as an engineer
[20:39] right and if you are a mid senior plus
[20:42] level engineer you know that
[20:44] communicating the value of your work is
[20:46] incredibly important and creating
[20:48] diagrams helps you do that in a faster
[20:52] more concise way so that's the power of
[20:54] a AI agent like this just being able to
[20:57] generate diagrams on the Fly iterate on
[20:59] them and having a quick iteration

### Minute 21

[21:01] humanin the loop pattern to do that will
[21:04] help you generate these diagrams faster
[21:06] which will help you communicate your
[21:07] ideas faster for both your personal and
[21:09] career work definitely spend time
[21:11] communicate your ideas well use diagrams
[21:13] to help you do that and use gen AI to
[21:16] help you build your diagrams to help you
[21:18] drive that effort forward again I'm a
[21:20] huge fan of cursor I use it but it's
[21:23] important to diversify it's just too
[21:25] early in the AI coding game and the
[21:29] generative AI age to be committing and
[21:32] putting all your eggs into one basket
[21:34] into one tool I like to stay close to
[21:36] the prompt stay close to the metal stay
[21:38] close to the tooling and tools like AER
[21:41] allow you to do that we've been at this
[21:43] for longer than a year and a half almost
[21:46] 2 years now and we are just scratching
[21:48] the surface of what's possible with
[21:50] these incredible AI coding tools and
[21:52] with generative AI if you want to stay
[21:54] up to date and catch these Trends before
[21:56] they happen join the journey drop the
[21:58] like drop the sub and I'll see you in

### Minute 22

[22:01] the next one