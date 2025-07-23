# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=tElgVPUargw
- **Duration:** 34:12
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 6617
- **Transcript Generated:** 2025-03-30 23:49:03

## Transcript


### Minute 0

[00:00] it's been a wild few months in the AI
[00:02] coding ecosystem with the biggest
[00:05] players racing to outdo each other
[00:07] curser is leveling up fast and gaining
[00:10] market share as the go-to AI editor
[00:13] while GitHub claps back with their own
[00:16] revamped co-pilot and their own rapid
[00:19] prototyping tool spark ader's new
[00:22] architect mode is setting new standards
[00:25] and 01 based coding is changing the AI
[00:28] coding game before the official model
[00:31] has even dropped and then there's
[00:33] anthropic quietly releasing powerful
[00:36] bash and editor tools that most
[00:38] Engineers haven't fully appreciated yet
[00:41] with all these moves my own AI coding
[00:44] workflows have transformed completely
[00:47] today I'll share one of my fine-tuned AI
[00:50] coding development workflows to show how
[00:52] you can do more code faster get more
[00:54] done in less time great AI coding is
[00:57] much like great engineering it all

### Minute 1

[01:00] starts with a great
[01:04] plan so our goal today is going to be
[01:06] create a simple generative AI UI client
[01:10] server application it's going to be
[01:12] built with a simple chat interface that
[01:14] allows us to prompt specific generative
[01:17] UI components we have a simple Cloud
[01:20] chat application we can type hello and
[01:22] we'll get back to typical response I've
[01:24] been eyeing the generative UI pattern
[01:27] for a while and finally have a use case
[01:29] for product I'm building open AI just
[01:31] released their GPT search and you may
[01:34] have noticed they're using some version
[01:36] of generative UI with a few of their
[01:39] components to build this we're going to
[01:41] use a combination of my favorite AI
[01:44] coding tools AER and cursor it's just
[01:47] too early in the generative AI age to
[01:50] think you can confidently pick out the
[01:52] single best tool for any problem I
[01:54] recommend one closed source and one open
[01:57] source tool so here's the outline for
[01:59] the plan we're going to execute on today

### Minute 2

[02:02] this specification or plan consists of
[02:05] three sections we have our highle
[02:06] overview this is the highle steps we're
[02:09] going to take we then have our team
[02:11] which is our set of AI agents that we're
[02:14] going to delegate all of our work to
[02:16] we're using architect mode in both of
[02:18] our scripts here the AER architect mode
[02:20] is gamechanging and leads to highquality
[02:23] code generation we'll Circle back to
[02:25] that in just a moment and then lastly we
[02:26] have our task breakdown and in the task
[02:29] break down we have our setup step and
[02:32] our individual tasks each task has a
[02:34] highlevel item and then the actual AI
[02:37] coding prompt that we're going to
[02:38] execute so you can see here we have all
[02:41] the work we want to get done in a mid to
[02:43] highle outcome and then a low-level
[02:45] detailed prompt so here we're going to
[02:47] operate with four agents total we're
[02:49] going to be using two AER instances one
[02:52] for the client one for the server and
[02:53] then we're going to be using anthropic
[02:55] based document editor agent and Bash
[02:58] agent sh scripts AER client here sh

### Minute 3

[03:02] scripts AER server okay so we have our
[03:06] client editor on the left server editor
[03:08] on the right and then let's open up two
[03:10] additional agents so this is our
[03:11] document editor I'll run sh scripts doc
[03:14] get this started and this is a AI agent
[03:17] that wraps anthropics file editing tools
[03:20] we'll do the same with the bash agent
[03:22] same deal scripts bash it's the same
[03:25] type of wrapper but this wrapper is
[03:26] around anthropics bash editing tool
[03:29] let's let's start with the setup so
[03:31] let's add our context to our client and
[03:33] server we'll say add server slash and we
[03:36] can open up our file editor here front
[03:39] end and the source directory and then we
[03:41] have a couple server items in the server
[03:44] directory so you can see we have the LM
[03:46] and the server add source and in AER you
[03:49] can recursively add files by just
[03:53] specifying a directory you can see here
[03:55] we imported all of our files into the
[03:57] chat and all these are now editable on

### Minute 4

[04:00] both instances we're going to add a
[04:01] couple additional items so we want the
[04:04] server to be aware of our geni chat but
[04:06] we don't want to update I want to
[04:08] separate the concerns here into server
[04:10] only and client only this allows us to
[04:12] move faster and reduces error so I'm
[04:15] going to say SL readon and we're going
[04:17] to add this
[04:19] genui component as a readon context file
[04:23] and same thing on the left side I want
[04:24] to actually read only all of the server
[04:27] files I'm just going to say server slash
[04:29] and then start so you can see we now
[04:30] have these two readon files and we have
[04:33] the one readon here couple things we're
[04:35] going to do now we need to get some
[04:37] documentation around how to use tool
[04:39] calls with Sonet and we also need to add
[04:42] documentation around using Dynamic
[04:44] components in vue.js many front-end
[04:48] component Frameworks will have support
[04:49] for some type of dynamic component we're
[04:51] using VJs for our frontend and we're
[04:53] using Express for a
[04:57] backend documentation collection is a

### Minute 5

[05:00] common pattern when you're integrating
[05:02] with thirdparty applications so much so
[05:04] that I've built out a tool to help me
[05:06] collect information I highly recommend
[05:08] you set something like this up Gathering
[05:09] documentation and having it local on
[05:12] your device means that you can pass in
[05:14] the context into your AI agents so in
[05:17] order to pull in this documentation you
[05:19] can see I have this empty AI docs
[05:22] directory I like to set this up in every
[05:24] code base that I work in now and what
[05:26] we're going to do is just scrape a
[05:28] website add the content here and then
[05:30] have our file editor agent clean it up
[05:32] so that it's easier for other agents to
[05:34] read so we're going to do that now let's
[05:36] open up a new terminal here and run the
[05:38] following commands we're going to use
[05:40] anthropics tool use docs to generate the
[05:43] generative UI components automatically
[05:46] for us and so what we're going to do
[05:48] here is just collect tool use documents
[05:50] I'm going to run imp going to run Alo
[05:52] one this is a new agentic tool I'll be
[05:54] discussing on the channel more in 2025
[05:57] we have this command collect and now we
[05:59] pass in a URL and so all we're going to

### Minute 6

[06:01] do here is take the URL for this and
[06:04] we're going to run this collect method
[06:06] on this and then we're going to save it
[06:08] to our AI docs in tool use raw. MD so
[06:12] this is going to scrape this URL for us
[06:15] and place the content in our tool use
[06:17] raw so you'll see this come in here and
[06:19] you can see that that's done so this is
[06:21] great but you'll notice that there's 9k
[06:24] tokens in this file it's messy it's got
[06:26] a lot of content that we don't really
[06:27] care about this is where our file
[06:29] editing agent is going to come in and
[06:31] clean this file up for us so if we go
[06:33] back to our specification document and
[06:35] run our next command we're going to ask
[06:37] our editor agent read the tool use raw
[06:40] and then create tool use MD with
[06:42] examples and docs specifically around
[06:45] tool use so we'll copy
[06:47] this and go to our file editing agent
[06:50] and just paste this in and run it and so
[06:52] you can see our anthropic file editing
[06:55] tool thinking through what needs to
[06:57] happen here you can see it's running the
[06:58] view command and I'm going to link the

### Minute 7

[07:01] previous video where we discussed the
[07:03] anthropic tools specifically the editor
[07:05] and The Bash tool that are super
[07:07] underrated super underappreciated
[07:09] that'll be linked in the description
[07:10] definitely check out that video this is
[07:11] a huge huge win for engineering and so
[07:14] right now it's scraping and it just
[07:16] wrote this brand new file and let's go
[07:18] ahead and hop in here and we can see how
[07:20] much cleaner this looks right we're down
[07:23] to 1.4k tokens from 9k and if we just
[07:27] scroll through this file we can see how
[07:30] much cleaner this is and how much value
[07:32] we can get by asking a file editing
[07:34] agent to clean up the larger markdown
[07:36] file for us so all we do was write a
[07:38] prompt for this and the Sonet file
[07:41] editing tool now has cleaned up this
[07:43] documentation for us it's got a ton of
[07:45] great breakdowns for us it's even got
[07:48] their links to other documentation in
[07:49] here as well let's go ahead and close
[07:51] these files and we're going to repeat
[07:53] this process for the vue.js dynamic
[07:56] component because this is what we're
[07:58] going to use to automatically swap out

### Minute 8

[08:01] which generative UI component gets
[08:03] generated so we'll run the same process
[08:05] here we're running our collect URL and
[08:09] then we have our output file so I'll
[08:10] just copy this go back to our blank
[08:14] instance paste this let's go ahead and
[08:17] get this content scraped into this file
[08:19] you can see that that's done and if we
[08:22] scroll you know not too bad only 1,300
[08:24] tokens but let's run our file editing
[08:27] agent to clean this up for us same deal
[08:29] I'll just hop back to the file editing
[08:31] agent paste this in and now it's going
[08:33] to generate the non-raw formatted
[08:36] version for us so our anthropic file
[08:38] editing tool is Reading in the Raw
[08:41] format and then creating this new
[08:43] document with examples and docs
[08:45] specifically around Dynamic components
[08:48] and it's going to clean it up for us so
[08:49] that it looks more like this right so
[08:51] this is the new reformatted version you
[08:54] can see how clean this is it's easier
[08:56] for you and I to read and that means
[08:58] it's likely easier here for a large

### Minute 9

[09:00] language model to read and this is great
[09:02] in this developer workflow it works like
[09:04] this first you make a plan right which
[09:06] we have here then you collect all the
[09:08] information you get it into your
[09:09] codebase now we have our AI docs then
[09:11] you run your prompts let's move back to
[09:14] our AER assistants for ader to see these
[09:16] files we need these files committed so
[09:18] I'm just going to go ahead and run a
[09:19] slash run get stage dots now we should
[09:22] have access to/ readon and AI docs there
[09:26] we go now we can see all these files for
[09:28] the front end we only want want the
[09:30] dynamic components we'll just add that
[09:32] formatted file and for the backend slash
[09:35] readon the a do tool use markdown file
[09:40] now we have all of our collection
[09:42] complete right our AI coding assistants
[09:44] have everything they need to accomplish
[09:46] the tasks we want them to accomplish
[09:48] let's go ahead and Shrink our screen
[09:49] here and get to work so we'll close this
[09:51] get back to our genui chat and let's
[09:53] move to the actual task execution so I
[09:57] know you might be thinking wow that's a
[09:58] lot of setup but this is going to be

### Minute 10

[10:00] worth it for us as we're just going to
[10:01] start rolling through these a coding
[10:04] prompts at first will be helpful to just
[10:07] look through what we have so far so if
[10:08] we open up server you can see we just
[10:10] have this simple prompt endpoint and
[10:12] this prompt endpoint is just hitting a
[10:14] classic anthropic chat call what's your
[10:17] favorite programming
[10:19] language it will you know create this
[10:21] typing interface and then give us a you
[10:24] know stock I don't have a favorite cuz
[10:26] I'm an AI assistant blah blah blah this
[10:27] is what's happening here on the back end
[10:29] we just just have our llm file and we
[10:31] have our server file as well and our
[10:34] front end looks like this so This Is A
[10:36] View application frankly all the
[10:39] frontend Frameworks are converging to
[10:41] basically being the same thing now so it
[10:42] doesn't really matter what you're using
[10:44] if we open up our template you can see
[10:46] we have our list of messages and we have
[10:48] our input field pretty simple you can
[10:50] see We're looping through a bunch of
[10:51] messages and displaying them so let's go
[10:53] ahead with our first
[10:57] change the first thing we need to do to
[10:59] get our generative UI is create a new

### Minute 11

[11:03] tool end point my Approach for creating
[11:05] generative UI components is to make
[11:08] every response that we're getting back a
[11:11] tool call so let's just go ahead copy
[11:12] this paste this in let's let ader get to
[11:14] work and then let's open up server so
[11:17] that we can see these changes get
[11:18] streamed in and we can full screen while
[11:20] we're working on this earlier I
[11:22] mentioned that we're running in
[11:23] architect mode this is an incredible
[11:26] mode that AER has that essentially runs
[11:28] your prompt twice once as a planner and
[11:32] then as a editor and you can see here we
[11:35] have a linting issue it didn't get
[11:36] imported this got automatically fixed
[11:38] ader saw that automatically fixed it as
[11:40] you'll see in a moment inside of our uh
[11:43] scripts here inside of our setup scripts
[11:45] we are automatically having AER
[11:48] self-correct itself and confirm every
[11:51] change that it wants to make let's go
[11:52] and close this we'll get to that in a
[11:53] second so if we review our changes you
[11:55] can see we have this new tool command we
[11:57] can go ahead and Auto Import this and we

### Minute 12

[12:00] actually want to import this from our
[12:02] tool file let's make sure that this is
[12:06] exported and so now we have that tool
[12:08] there we can see we have our new / tool
[12:11] endpoint and we're passing in our tool
[12:14] parameter if we hop into our tool prompt
[12:17] we can see we have this brand new tool
[12:19] created we are missing the tool call
[12:22] here so we can just go ahead and add
[12:24] this right we can just do Force tools
[12:26] and then we also want one more thing if
[12:28] I remember correctly we want to use the
[12:32] force tool mode here so we can pass this
[12:36] in here so if we say a tool
[12:40] choice because we always want this to
[12:42] run this is something that we just you
[12:44] know missed in the prompt I always want
[12:46] this tool to execute every single time
[12:48] we call this we have the wrong tool type
[12:51] here I think we probably want anthropics
[12:53] tool so we'll just say I believe we can
[12:55] look for anthropic do messages

### Minute 13

[13:00] tool there we go and then we can update
[13:03] our uh type here we can actually just
[13:05] get rid of this type yeah just
[13:06] completely get rid of this and then we
[13:08] can just have our server also import
[13:12] from here and yeah there we go get our
[13:14] tool using cursor here to tap through
[13:18] changes and now we can see we have our
[13:20] generative UI component that's getting
[13:21] passed in right and the idea here is
[13:24] quite simple basically you have a tool
[13:26] that will always run and generate one of
[13:30] these items okay so let's go ahead and
[13:32] hop back to our spec documentation this
[13:34] was our first prompt let's go ahead and
[13:36] run our next one so now we're going to
[13:37] go to the client and now we're going to
[13:39] ask our client to actually use this tool
[13:42] call after the enter key is pressed
[13:43] right so you can see this prompt this is
[13:45] exactly what this is going to do let's
[13:46] go ahead and open up our editors here
[13:49] and let's run our client side now right
[13:52] at the left of the client just go ahead
[13:54] and execute on our client side and we're
[13:56] going to update this component and call
[13:58] SL tool tool instead of if we run that

### Minute 14

[14:01] and quickly switch back we are running
[14:03] SL prompt right now so we're going to go
[14:06] ahead and run this
[14:08] and great so now this is running SL tool
[14:11] we saw that get updated and let's go
[14:12] ahead and just see if we can run this
[14:14] now so we'll refresh we'll type hello
[14:17] and you can see there we have an empty
[14:19] response so let's go ahead and figure
[14:21] out what's going on here printing out
[14:23] our data let's just go ahead and see
[14:24] what's in this and response is just an
[14:26] empty string so let's go ahead and clean
[14:27] up our response format okay so this is
[14:30] what's happening right let's change this
[14:32] what we're actually looking for is we
[14:35] always know this is going to be a tool
[14:36] use return and so we just want to pass
[14:39] back this entire block refresh and type
[14:42] hello wonderful so now we're getting
[14:43] that entire response block back if we
[14:46] look at this you can see we're getting
[14:48] that tool use response back from Sonet
[14:52] which is perfect and you can see we're
[14:54] calling this component type text right
[14:56] so we just passed in hello forcing the
[14:58] ex execution of this tool to run every

### Minute 15

[15:00] single time and if we hop back to server
[15:02] where this tool lives the component type
[15:05] is always going to be one of these enums
[15:07] so we're having Sonet pick which one of
[15:10] these uis do we want to generate based
[15:12] on the incoming prompt so if I type
[15:14] something like I want to leave a rating
[15:18] you can see we're going to get this
[15:19] component type star rating okay so this
[15:22] is really cool so we can also get the
[15:23] Color Picker and the contact form these
[15:25] are going to be components will be you
[15:27] know having our AI coding assistant
[15:29] automatically generate for us and then
[15:31] we have just the plan all text response
[15:34] I think as a pattern here you know if we
[15:36] needed responses from star rating Color
[15:39] Picker or contact form what we would do
[15:41] is you know add them here so we would
[15:43] say uh star rating response and then
[15:47] have the response exactly get added just
[15:50] like this for these other components
[15:51] though we don't need it we're just
[15:53] testing out this as a proof of concept
[15:55] for generative UI so let's go ah and
[15:57] continue so that's our first two prompts
[15:59] you can see how we're starting to speed

### Minute 16

[16:01] things up a little bit and now let's go
[16:03] ahead and update our client to store
[16:06] more information right so I've got this
[16:08] all planned out we do want to be saving
[16:10] these messages over time if we look at
[16:12] the client you know we have this simple
[16:15] messages typescript interface let's go
[16:18] ahead and enhance it right we need some
[16:19] more information we need to be able to
[16:20] store responses and submission so let's
[16:23] just go ahead and grab this prompt and
[16:25] execute this on our client side
[16:29] and we're just going to update this
[16:30] message type and when we create these
[16:31] new messages we're going to make sure
[16:32] that our code is actually you know
[16:35] filling in all of these items here right
[16:38] so let's see that change gets synced in
[16:40] and it's important to note with this two
[16:42] agent configuration we have two AER
[16:44] instances with this setup we can execute
[16:48] client and server prompts simultaneously
[16:51] if I wasn't filming this video that's
[16:52] what I would be doing right I'd be going
[16:54] top to bottom I'd run these both at the
[16:56] same time unless there's some context
[16:59] conflict then we can just stream these

### Minute 17

[17:00] both down side by side and execute them
[17:03] together right okay so that changed got
[17:05] submitted there let's go ahead and take
[17:07] a look at what's happening here so the
[17:09] great part about planning everything out
[17:10] is that we can just take a look at what
[17:12] step we're on in our you know feature
[17:14] building process and then just review
[17:16] the code that was generated right so
[17:18] we're going to go ahead and check our
[17:19] message to see if we have these new
[17:21] Fields ID create app component type so
[17:24] on and so forth fields we have our new
[17:26] generate ID function we can search this
[17:28] and see this getting used throughout so
[17:31] when we submit a new message we're
[17:32] getting that brand new message attached
[17:35] and let's go ahead and run this let's
[17:36] see if all of our responses are still
[17:38] looking okay let's say hello okay so we
[17:42] can see that this is coming back all
[17:43] right so let's go ahead to step three so
[17:46] here we're actually going to create our
[17:48] UI components and our Dynamic component
[17:51] we have all these steps laid out and
[17:54] we're just once again going to copy this
[17:56] and you can see here we have these cool
[17:58] component generation prompt so we're
[17:59] saying create Source components geni

### Minute 18

[18:02] text one for each type and at the bottom
[18:04] we have you know update use component
[18:06] instead of raw text of response right so
[18:09] we're going to use the dynamic component
[18:11] instead so let's go ahead and highlight
[18:12] these and go to our front end AI coding
[18:16] assistant paste the send fire that off
[18:18] while this is running let me just go
[18:19] ahead and show you how we're
[18:20] instantiating these AER architect
[18:25] instances if I click on ader client you
[18:28] can see this exact run command so here
[18:30] we're running AER with the Sonet model
[18:34] and we're running in architect mode and
[18:37] then we have our editor model also Sonet
[18:40] model and we're running with yes always
[18:42] so what is architect the architect mode
[18:44] means AER is going to run two prompts
[18:46] right this is going to be a prompt chain
[18:47] of length two and it's saying our first
[18:50] prompt is just going to be about
[18:52] drafting the changes and then our second
[18:54] prompt is going to be about executing
[18:56] the draft changes
[18:59] if I did not have yes always I would

### Minute 19

[19:01] have to constantly hit yes and confirm
[19:04] the change by just having yes always
[19:06] here as a flag this will have AER draft
[19:09] the change using the Sonet model in
[19:12] architect mode and then once the change
[19:14] is ready and fully drafted it will then
[19:16] pass it to the editor model which will
[19:18] actually implement the changes so by
[19:21] using a prompt chain of length two AER
[19:23] is able to increase the AI coding
[19:26] accuracy by quite a substantial am
[19:28] amount by having one model draft and one
[19:31] model execute you can think of this as a
[19:33] manager Builder pattern or a draft
[19:36] editor pattern or as AER you know aply
[19:39] put it in architect mode we've talked
[19:41] about prompt chaining quite a bit on the
[19:43] channel I'll link a couple of videos if
[19:44] you want to learn more about prompt
[19:46] chaining and it's more powerful
[19:48] varieties so that you can use it in your
[19:50] own agentic workflows there are tons of
[19:52] variants of the architect editor prompt
[19:56] chain that can be used to improve AI
[19:58] coding even further we'll explore that

### Minute 20

[20:00] in upcoming videos I'm really excited
[20:01] and I want to wait till the official 01
[20:03] reasoning model comes out and then we'll
[20:05] explore a bunch of heavy hitting AI code
[20:09] generation using the architect pattern
[20:11] with 01 and then a you know fast high
[20:14] quality editing model like claw 3.5 you
[20:17] can imagine different variants of this
[20:19] pattern for instance we could have a
[20:21] architect an editor and a reviewer or a
[20:24] mode where we have two architects and
[20:26] then a lead engineer that merges the
[20:29] best of both drafts and then an editor
[20:31] right there's really no limit to the
[20:33] types of combinations you can make with
[20:35] a gentic workflows like this I really
[20:37] like that AER took a little bit of risk
[20:39] and implemented one pattern like this
[20:42] that gives really concrete results but I
[20:44] like that AER is still keeping itself
[20:46] simple lightweight and unopinionated
[20:49] this is how you build great AI agents so
[20:51] that's what's going on in the ader
[20:53] client we're doing effectively the same
[20:54] thing in the ader server and let's go
[20:56] ahead and move on from that let's check
[20:59] out our generative UI components if we

### Minute 21

[21:01] look at our UI you can see it generated
[21:04] four new components we have this massive
[21:06] multifile edit we got all these new
[21:08] components we can open up the file
[21:10] explorer and just see these right we now
[21:11] have genui text star contact and picker
[21:15] open up text you can see we just have a
[21:18] text response and a submit button and
[21:19] then some styling so you know looks like
[21:21] A's doing a great job it's running all
[21:23] the modern V3 script setup syntax that's
[21:27] great to see let's go ahead and look at
[21:29] the top level UI so if we close script
[21:31] here you can see we're now using the
[21:34] dynamic component and really important
[21:36] to really plan out all your work and
[21:39] give your AI agents all the information
[21:41] they need to solve the problem you have
[21:44] in this block if we're not the user we
[21:46] now have this V else that's wrapping our
[21:49] Dynamic component if we refresh here
[21:51] that documentation came right out of
[21:54] dynamic component. MD and so we have
[21:56] this cool Dynamic component and and
[21:58] we're looking for component type and we

### Minute 22

[22:00] want to make sure that it's in our
[22:01] component map so it created a component
[22:03] map for us let's look at that perfect so
[22:05] now we have a map from the component
[22:07] type to the actual generative UI
[22:10] component and again this is really great
[22:12] context management we have three readon
[22:16] files so our client AER coding agent can
[22:19] see our server files but it does not
[22:22] edit them right so it knows that in our
[22:24] server. TS and we can go ahead and just
[22:26] command click this in our server TS it
[22:29] sees these enum types right it knows
[22:32] that's what component type is going to
[22:33] be and that means it knows that it can
[22:36] map them right here okay so a lot of
[22:39] really awesome stuff coming together
[22:40] here the tricky part is going to be
[22:42] seeing if our a coding assistant mapped
[22:45] the message properly in the response
[22:48] because this is just a little tricky in
[22:49] general so let's go ahead and make a
[22:51] couple tweaks to this and first off
[22:53] let's just run it right so let's just go
[22:55] ahead and say hello so let's see if we
[22:57] get our text component okay so not quite

### Minute 23

[23:00] we need to modify the response here a
[23:02] little bit what we really want to have
[23:04] happen is we want our component type to
[23:08] get set and we want our component props
[23:11] to get set to this entire output block
[23:15] so we can go and just copy
[23:17] this and we'll just paste it down here
[23:19] just for reference this is not the
[23:22] correct response so let's just go ahead
[23:24] and close this out and all we want to do
[23:27] here cuz we're remember we're always
[23:28] going to be calling this tool call so
[23:30] we're always getting this format back so
[23:32] we can paste this and then we can just
[23:33] tab this this is giving us our response
[23:36] component type and we can look at data
[23:37] here right we have this nice log message
[23:39] and we have response and all we want to
[23:42] do here is pass input into both of these
[23:45] so not quite right but close so we want
[23:48] input and then we want Dot and then we
[23:50] have component type and then component
[23:51] props we just want to pass everything
[23:53] into that so component props is just
[23:55] going to be our input so whatever is
[23:57] here like text response we just want
[23:59] that to stream in so let's refresh type

### Minute 24

[24:02] hello and now you can see we have our
[24:06] generative UI text component we don't
[24:08] need submit here let's open up our AI
[24:10] assistant and let's just say remove
[24:13] submit from gen UI text and I missed the
[24:17] T there but doesn't matter that's going
[24:19] to get removed and cleaned up so you can
[24:22] see there we had the architect draft the
[24:24] change and now we have the editor making
[24:26] the change and so now this component is
[24:28] it's just text wonderful so let's
[24:30] refresh and say hello how are you
[24:33] there's no reason to generate any other
[24:35] type of component here so of course this
[24:37] component type coming back is just a
[24:39] text component but if we say I want to
[24:42] leave a review you can see here we now
[24:46] have our star component right our our
[24:49] rating component let's go ahead and open
[24:50] this up and see what this looks like
[24:52] this was all generated in one shot by a
[24:56] CLA upgraded and and you know we can
[24:59] review this prompt here we can see here

### Minute 25

[25:01] that it generated everything we needed
[25:03] right it created all these components it
[25:04] inferred based on all this context you
[25:07] know this is why it's so important to
[25:08] specify the right context with your AI
[25:10] coding assistant and inferred everything
[25:12] we wanted to have happen inside of our
[25:15] individual components right so now if I
[25:16] hit let's see how this works now if I
[25:18] hit four right we can see that four star
[25:20] rating and then if I hit submit we can
[25:21] see component submitted type rating
[25:23] value 4 so let's go ahead and look at
[25:25] that we can now handle Dynamics
[25:26] submission let's goad and create a quick
[25:28] prompt for this so when we submit this
[25:30] we want to say update this function
[25:34] update the tempbot message right so our
[25:37] temp Bop message is the one is our most
[25:39] recent message and all we want to do is
[25:41] set the submit response set submit
[25:44] response so pretty simple and let's go
[25:47] ahead we can hold on this and we can see
[25:48] the architect and the editor making
[25:50] those changes for us so archetype drafts
[25:53] editor writes the change okay so we can
[25:55] see it finding that most recent message
[25:57] and saving this let's update the color

### Minute 26

[26:01] so we also have the Color Picker right
[26:02] so this is going to select the Color
[26:04] Picker and we have a little UI issue
[26:06] here so I'll just highlight and I'll say
[26:09] update Flex call and now we can pick a
[26:12] color here and hit submit and now that
[26:15] was submitted so when we click submit I
[26:17] also want to update the state of our so
[26:19] there we go we got that Flex called
[26:21] change rolled in so when I click submit
[26:23] I also want to lock the UI right so that
[26:26] we don't keep making changes the
[26:28] generative UI component update all gen
[26:31] UI
[26:33] components when we have submit response
[26:37] say uh response
[26:39] submitted and then value so that we can
[26:43] see what exactly was submitted in every
[26:45] message right our AI coding assistant is
[26:47] going to again in architect mode make
[26:49] all these changes and then editor mode
[26:50] is going to actually write all the
[26:52] actual changes so this is really
[26:54] incredible right um that's quite a
[26:56] significant change to go through and add
[26:59] a submission text state to every one of

### Minute 27

[27:02] these you know to every one of our
[27:04] generative UI components but you can see
[27:06] here AER on sonnet 3.5 with architect
[27:09] mode is just plugging away right it had
[27:12] a clear draft to work with it can see
[27:14] all these files it has the right prompt
[27:16] now it's just working through all the
[27:17] changes wonderful so that was submitted
[27:20] so you can see there we have that
[27:20] submitted response and we can go ahead
[27:23] and update the Color Run submitted
[27:24] response again this will update the
[27:26] component awesome so that looks good um
[27:29] what other component do we have we have
[27:30] one more right so I want to I want to
[27:34] contact uh someone and if we type that
[27:38] you know you can see here we have our
[27:40] submitted contact form and response
[27:42] submitted should not show if there is no
[27:45] value so again we're just going to throw
[27:47] a prompt in here should not show unless
[27:51] there is a value hide it let's go ahead
[27:54] and just keep working through this so
[27:55] I'll type Dan Dan at indie
[27:59] message and then if we hit submit you

### Minute 28

[28:01] can see we have that submitted value and
[28:04] property is going to get upgraded that's
[28:05] awesome so this video is getting really
[28:07] long uh there's a lot of value here in
[28:09] writing out your specification prompts
[28:12] let me just show you one more thing here
[28:13] let's go ahead and create the SQL light
[28:16] database to save our messages so what
[28:19] we'll do next is have our bash anthropic
[28:21] agent just do all this work for us right
[28:23] so we need a new SQL light database and
[28:25] we need a new table setup and we we want
[28:28] them to have you know all the basically
[28:31] the exact same structure as our chat
[28:33] messages here right so here's our file
[28:36] editing agent we'll open up our bash
[28:38] agent and then we'll just copy this
[28:40] prompt here and fire this off and you
[28:42] know the key thing here to look up for
[28:44] is this is going to generate server app.
[28:46] DB so it's going to create this brand
[28:48] new sqli database in this file right
[28:50] here so I'm going to hit enter there and
[28:51] then let's go ahead and watch our server
[28:53] directory so the agent is making sure
[28:56] that the file exists this it's creating
[28:59] this you can see the create table

### Minute 29

[29:00] statement there and that's it it's done
[29:03] so you know we can test and you know we
[29:05] can use the bash agent to just validate
[29:08] for us show all the tables generated in
[29:12] app. DB perfect I wanted to touch on
[29:14] this agent just at least a little bit to
[29:16] show how powerful this is you can type
[29:18] in natural language and have your bash
[29:20] agent accomplish tasks for you
[29:22] automatically in the terminal right so
[29:23] we just had it create an SQL light
[29:25] database at this specific file path and
[29:27] create a brand new table right with
[29:29] these specific columns and it just did
[29:31] that for us right so this is right here
[29:33] but this video is getting really long
[29:34] I'm going to cut it here you can see
[29:35] where this is going right we're going to
[29:37] set up load and save commands next
[29:39] here's the prompt for that basically
[29:41] contining down the same line a great
[29:43] kind of lowlevel prompt specifying where
[29:45] things are you know we're going to
[29:46] update the server to have these load and
[29:49] save endpoints and then we'll have our
[29:52] genui chat update to just call the load
[29:54] and the save on mounted and on key press
[29:58] right so you can see where this is going
[29:59] I think we've gotten to the kind of Core

### Minute 30

[30:01] theme of this video by creating a great
[30:04] comprehensive plan and by using AI
[30:06] agents you can get a lot of work done
[30:08] with new AI coding paradigms like aer's
[30:11] architect mode you can just do a lot
[30:13] more and when the 01 models are released
[30:16] this trend is going to continue right
[30:19] we're going to continue seeing the
[30:20] amount of code you can generate go
[30:22] absolutely parabolic and you know with
[30:25] 01 preview which we're going to cover
[30:26] I'm really really excited to do video on
[30:28] 01 when that drops for AI coding
[30:30] specifically because the amount of code
[30:32] we be able to create with a very well
[30:35] planned out spec document specification
[30:37] document also just known as a plan right
[30:40] when you plan out all of your work for
[30:42] whatever feature that's coming up that
[30:43] you want to build and you have it in
[30:45] this document I can almost guarantee you
[30:47] in the future we're going to be able to
[30:48] just contrl C this entire document boot
[30:52] up in AER window with the1 model and
[30:57] pass this into it and it's going to do
[30:58] all the work right it will literally do

### Minute 31

[31:00] all the work that we're walking through
[31:01] right now I've run this experiment with
[31:03] 01 preview it gets close you still need
[31:06] to kind of come in and you know make
[31:08] improvements make changes make tweaks
[31:09] but I do think with 01 we'll be able to
[31:12] write comprehensive plans that detail
[31:14] all the work we want done for a feature
[31:16] for a tool for an application and then
[31:19] you just fire that off into a powerful
[31:22] AI coding assistant that can actually
[31:24] make the changes for you using a
[31:25] powerful reasoning model right right now
[31:27] now we have 01 preview this gets Us
[31:30] close 01 is going to take us all the way
[31:31] so I'm really excited for that video uh
[31:33] November or December so really stucked
[31:35] on that and I hope you can see the power
[31:37] of planning in the age of generative AI
[31:40] right we have a team of AI agents that
[31:42] can do arbitrary work for us in the
[31:44] beginning we use our doc agent to pull
[31:46] in documentation clean it up for us so
[31:49] that we can use it and then we have two
[31:51] AI coding assistant both on the server
[31:53] and the client side it's nice to split
[31:55] up our agents like this so that we can
[31:57] run work in parallel Al to create
[31:59] another video on that where I showcase

### Minute 32

[32:01] that a little bit better in this coding
[32:03] session we were running very
[32:04] sequentially but you can see where that
[32:06] can go right we have one instance on the
[32:08] server we have one instance on the
[32:09] client and then we can prompt at the
[32:11] same time in parallel it's also great
[32:13] for reducing context our front-end AER
[32:16] instance is only modifying and creating
[32:18] front-end related components while being
[32:20] able to read the server components
[32:22] thanks to aer's read only context
[32:24] management solution and our server of
[32:27] course you you know is really only
[32:29] looking at these two files so
[32:31] specification AKA plan based AI coding
[32:35] is a huge Advantage I recommend you dig
[32:37] into not only are AI coding tools
[32:40] evolving but models like the upgraded
[32:42] son 3.5 and soon the full 01 reasoning
[32:45] model will enable you to hand off 90% if
[32:48] not nearly all of the coding process
[32:51] tier AI agent the full version of 01 is
[32:54] going to push that AI coding developer
[32:57] work worklow into reality it's going to
[32:59] make that a real thing that we can do

### Minute 33

[33:01] you write a great document you write a
[33:03] great plan and frankly you use um your
[33:07] editor and Bash tools to help you create
[33:10] your great plan by collecting you know
[33:14] documentation by collecting uh specific
[33:17] files that you need and then you have a
[33:20] powerful reasoning model execute that
[33:23] using a great AI coding assistant build
[33:26] that change out you use a powerful mode
[33:27] like AER architect mode so that you get
[33:30] a clean draft of everything that's going
[33:32] to happen and then you have an editor
[33:34] model something fast like son that can
[33:36] read through all the changes and
[33:37] actually make the changes for you and
[33:39] that improves the performance even
[33:41] further right so you have a draft agent
[33:42] and you have an editor agent the big
[33:44] theme for us moving forward here is more
[33:46] capable models that can reason process
[33:49] and generate output more accurately that
[33:51] means we need to scale up our prompts
[33:53] and therefore scale up our planning
[33:56] abilities if you enjoy this video Drop
[33:59] the like drop the sub to stay on the

### Minute 34

[34:01] edge of what you can do and what you can
[34:03] build with these next level generative
[34:06] AI tools thanks for watching and I'll
[34:08] see you in the next one