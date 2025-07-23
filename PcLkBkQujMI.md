# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=PcLkBkQujMI
- **Duration:** 26:42
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 5149
- **Transcript Generated:** 2025-03-30 23:49:15

## Transcript


### Minute 0

[00:00] what's up Engineers Andy Deb Dan here
[00:02] today I have something incredible to
[00:04] share with you I want to introduce you
[00:07] to marimo a Next Generation python
[00:11] notebook I've got a three course special
[00:13] for you today these three pieces of
[00:16] value will help you win in the age of
[00:18] generative AI first we're going to break
[00:21] down the marimo reactive notebooks and
[00:24] talk about why it's so important to have
[00:26] a rapid prototyping tool like this well
[00:29] then see how we can use marimo to
[00:32] quickly run individual prompts and run a
[00:34] single prompt against every
[00:36] state-of-the-art large language model by
[00:38] clicking a single check box lastly I
[00:41] want to share the early stages of what
[00:44] my prompt Library looks like to give you
[00:46] ideas on how you can build maintain and
[00:48] grow your own agentic Library so first
[00:52] things first we have to talk about
[00:54] marimo this is a brand new tool that
[00:56] aims to replace Jupiter notebooks python
[00:59] notebooks and notebooks in general are

### Minute 1

[01:01] places where Engineers can rapidly build
[01:03] out ideas and features it's often used
[01:06] in Ai and ml engineering to pull in data
[01:09] to experiment on data to get insights
[01:11] build artifacts test out ideas so on and
[01:14] so
[01:17] forth marimo has a couple of really
[01:20] really interesting killer features first
[01:23] they're importing they're then creating
[01:25] a markdown item and you can see here the
[01:27] markdown H1 gets rendered directly
[01:29] directly above the block they created a
[01:31] variable in items let me go and zoom in
[01:33] on this a little bit they created a
[01:35] variable in items as soon as they
[01:37] changed it the cells that reference that
[01:40] variable you can see here there are n
[01:42] items it automatically gets updated now
[01:45] they've changed it to a slider and the
[01:46] slider automatically updates that value
[01:49] and every other cell that has a
[01:51] reference now they're pulling in a chart
[01:53] and this chart then of course is getting
[01:55] fully rendered and is reactively
[01:58] updating based on this slider they're

### Minute 2

[02:00] then going to hop into some data
[02:01] exploration and honestly things are
[02:03] moving so quickly here it's better if we
[02:05] just jump into this ourselves and really
[02:08] see how these notebooks can help you
[02:11] build and rapidly prototype software in
[02:14] the age of
[02:17] AI here we have a code base that we're
[02:20] going to slowly build up on so we have
[02:22] three notebooks here we're going to
[02:24] start with this after you run the
[02:25] installation instructions you'll be able
[02:27] to kick off this command here we're just
[02:29] going to go ahead and fire this off so
[02:31] right away a notebook gets opened up for
[02:33] us and the first thing I'm going to do
[02:35] here is get out of Dev mode and go into
[02:38] what I like to call user mode I'm going
[02:39] to hit command Dot and now we're
[02:41] presented with this simple UI now a key
[02:45] part about marimo that differentiates it
[02:47] between other notebooks is that it is
[02:49] reactive so if I look at the slider here
[02:51] and I slide this you can see we have a
[02:53] value just below getting updated let me
[02:55] go and bump the size a little bit so if
[02:57] I scroll here you can see that value is
[02:59] getting updated right if I click this

### Minute 3

[03:00] check boox again we have state getting
[03:02] updated right so we have UI
[03:04] automatically updating state right let's
[03:06] type in this input field hello Maro is
[03:10] awesome and if I blur or hit enter we're
[03:13] going to get the text field value I want
[03:15] you to hold onto that key idea while we
[03:17] move through this so what else can we do
[03:19] with marimo we have reactive data
[03:21] visualization right so we have this plot
[03:23] here it's a simple data frame with some
[03:25] random data right now it's a scatter
[03:26] plot if we want to we can change its
[03:28] form we want to see a line chart perfect
[03:31] if we want to see the bar version we can
[03:32] go ahead and do that as well nice and
[03:35] clean nice and simple so you can already
[03:37] kind of see this being useful for data
[03:39] exploration right if we scroll down we
[03:41] do have conditional output and control
[03:43] flow if I hit this checkbox of course
[03:46] based on a bing we can render different
[03:48] content right if we check that off it'll
[03:50] change turn it on it'll change again if
[03:52] we drag and drop a CSV file we can
[03:55] automatically get a breakdown of the
[03:57] data and so this basically just
[03:58] converted a hand's data frame and gave

### Minute 4

[04:01] us a really really clean layout of a
[04:04] bunch of fields right you can see here
[04:05] all the columns we can do some sorting
[04:07] let's descend on location let's Ascend
[04:10] on age right so you can see this mock
[04:13] user data set getting broken down right
[04:15] and then we have some Advanced UI
[04:16] components right we have classic uh
[04:19] accordion we have nested slider in here
[04:21] and then we have a data frame display
[04:23] okay we have things like tabs we have
[04:25] forms images videos layouts and fullon
[04:29] interactive data Exploration with just a
[04:32] few lines of code so this is incredible
[04:35] what we're going to do now is hop out of
[04:36] user mode so I like to call this user
[04:38] mode and then if we hit command dot
[04:41] we'll hop into Builder mode or
[04:43] engineering mode right so basically
[04:45] these notebooks are now showing the code
[04:47] surrounding them so we have all of our
[04:49] Imports here you can see we have all the
[04:51] markdown getting displayed in these
[04:53] sections and then we can see what
[04:54] exactly these components look like right
[04:56] so super clean Super declarative if
[04:59] you've used Swift UI or any framework

### Minute 5

[05:01] where you define your elements in line
[05:03] you'll be very familiar and you'll be
[05:05] very accustomed to how marimo creates
[05:07] components right so we have slider
[05:08] checkbox input field and then we're just
[05:10] rendering them in a vstack right and if
[05:12] we want to we can just switch this right
[05:14] now hstack command enter and all of a
[05:17] sudden we're floating left to right and
[05:19] we just you know really quickly updated
[05:21] the UI of our elements so I'll revert
[05:23] that back and we can do the same thing
[05:26] in developer mode right I'm checking
[05:27] this I'm changing this I'm typing you
[05:30] know test input input value hitting
[05:33] enter and you can see that all gets
[05:35] updated there if you want to we can hop
[05:36] in here and do something kind of fun we
[05:39] can paste this and say
[05:41] slider. Val and multiply it by the text
[05:45] input value and of course this is going
[05:47] to render that value multiple times
[05:51] right so let's go ahead and do something
[05:52] else let's change text input to like
[05:53] just an emoji or something right so if
[05:55] we do something like this place a star
[05:57] here rerender we can now change this

### Minute 6

[06:01] value and reactively one of the
[06:03] highlights of Maro is that this is fully
[06:05] reactive right so as the slider goes up
[06:07] our stars go up and down so let's talk
[06:08] about how we can use this wonderful
[06:11] reusable very visual interactive
[06:14] notebook to get an edge in the age of AI
[06:17] let's look at a concrete use case of
[06:19] using this tool for prompt engineering
[06:22] for prompt management and ultimately to
[06:25] build your own prompt Library
[06:28] [Music]
[06:30] all right so if we hop back to the
[06:32] readme and copy this paste this and run
[06:35] it you can see here that we have a ad
[06:39] hoc prompt notebook and again command
[06:42] dot we're now in user mode right so
[06:44] before we were in kind of deep
[06:46] engineering mode you can see all the
[06:47] code you can see all the details you can
[06:49] quickly tweak and modify you hit command
[06:51] Dot and now you're just focus in on
[06:54] consuming the tool right consuming the
[06:57] use case and you can imagine this is
[06:59] super useful for yourself looking back

### Minute 7

[07:01] at products for you and I on the channel
[07:03] sharing ideas sharing tools but also for
[07:06] other Engineers on your team and for
[07:08] your product managers and your product
[07:09] team so you can see here we have a
[07:11] couple input fields we have prompt we
[07:13] have temperature we have a model and if
[07:15] we click the model drop down you can see
[07:17] we have all the state-of-the-art models
[07:18] at our disposal and then we can hit run
[07:21] on all models so let's just do a test
[07:23] prompt we'll just say ping we'll run on
[07:25] son 3.5 and we'll hit submit so you can
[07:27] see two new blocks have appeared we have
[07:29] the form values which are just the
[07:31] values of our form from above and we
[07:34] also have the prompt output so let's go
[07:36] ahead and run something else we'll say
[07:37] count to 10 Z then Implement python then
[07:41] in typescript okay and then we'll just
[07:43] hit submit so just running another
[07:45] random prompt here on Sonic 3.5 you can
[07:47] see they got kicked off and we got a
[07:49] nice response there we have markdown we
[07:51] have code and this is just a simple
[07:53] reusable ad hoc prompt tool again if we
[07:57] just hit command dot we can switch into
[07:59] to engineering mode and we can see

### Minute 8

[08:01] exactly how this works so we have
[08:02] Imports we're pulling in our models
[08:04] we're creating a map between the name
[08:06] and the value of our model we have our
[08:09] inputs so you can see here you know
[08:10] we're literally just creating m.i. text
[08:13] area m.i. slider drop down and then we
[08:18] have a checkbox and so remember I said
[08:20] in the beginning you know one checkbox
[08:22] is going to run this prompt against
[08:24] every single one of our models so you
[08:25] know what while we're looking at this we
[08:27] can go ahead and just kick this off so
[08:28] I'll say run on models and let's make it
[08:31] do something more interesting right
[08:32] let's say uh create a pros and cons of
[08:36] typescript versus python explain when to
[08:39] use both and then we'll hit submit here
[08:41] so that's just going to be kicking off
[08:43] in the background and you can see here
[08:45] we're taking Maro components and we're
[08:48] throwing them in a form you know that's
[08:50] how we got our text rendered that's how
[08:52] we got our temp our model and our run
[08:54] all right so really kind of simple
[08:56] declarative UI uh it's easy to reason
[08:58] about it's easy to consume and think

### Minute 9

[09:00] about you can see here we just have ad
[09:02] hoc prompt and then we just in text we
[09:05] place our four components we then run
[09:08] this batch to kind of insert our data
[09:12] into the MD and then we call form on
[09:14] this so theform is what creates the
[09:16] submit button we can then click that and
[09:18] get our submitted output right we can
[09:20] see our form values just as before and
[09:23] this is a simple you know looping
[09:24] through our form and just grabbing the
[09:26] values based on the key and then we use
[09:28] the mo ui. component and then we just
[09:31] throw that inside of a markdown block
[09:33] right so that's how we get that if we
[09:35] scroll down here you can see this is our
[09:37] loader for our single prompt execution
[09:39] takes the form value form prompt and the
[09:42] form temperature if we're running the 01
[09:45] or Gemini prompts the temperature just
[09:47] gets set to one inside of this llm
[09:49] module prompt with temperature function
[09:52] so if we scroll down some more you can
[09:53] see we have our multimodel prompt
[09:57] completed we have a H1 you can see we
[09:59] have a nice clean table right model ID

### Minute 10

[10:03] and then the output we have the Sonet
[10:05] 3.5 answer to our pros and cons table
[10:09] comparing typescript and python we also
[10:11] have our 01 mini 01 preview you know you
[10:14] can already kind of tell that the
[10:15] reasoning model outputs are much richer
[10:19] and then we have gpg 40 latest o mini
[10:22] Gemini 1.5 and Flash and if we scroll
[10:26] down to see what that looks like it's
[10:27] really really simple right we're taking
[10:29] our our list of objects placing that in
[10:32] the table and then we're just throwing
[10:33] that in a vstack since I'm not running
[10:35] any computations in the cell it just
[10:37] reruns no problem all the data in the
[10:40] previous cells that it's used inside of
[10:42] this cell uh doesn't need to change or
[10:44] update right so this is really really
[10:46] powerful I hope you can see the value in
[10:48] this we're in engineering mode we can
[10:49] come in here we can add models we can
[10:52] update our list we can add new UI items
[10:56] very very quickly if we haven't clicked
[10:58] submit you know our our form won't have

### Minute 11

[11:00] any values to display so this block just
[11:02] won't show up same thing with the values
[11:04] down here and in just two cells we're
[11:07] able to build a multi-model execution
[11:10] prompt that runs the same prompt against
[11:12] several models in just eight cells or so
[11:15] we've replaced a ton of tools right you
[11:18] you you've probably seen or use a tool
[11:20] that does basically just this right it's
[11:22] a simple chat GPT replacement with a
[11:25] couple extra nice features and and
[11:28] tweaks right so this is just a minimal
[11:30] example of how you can build a simple
[11:32] reusable prompt notebook that you can
[11:35] hop into run prompts test your prompts
[11:37] against different models and just kind
[11:39] of get an idea for prompts and easily
[11:41] see and read the output right if you
[11:43] want to we can uncheck we can fire off a
[11:45] mini and then we can just get that
[11:47] response right so if we hit submit all
[11:49] of our reactive cells that are dependent
[11:52] on the form are now recomputing and
[11:55] giving us a concise result right so you
[11:57] can see there the 01 mini is giving us a
[11:59] really really great breakdown of when to

### Minute 12

[12:00] use typescript versus python so before
[12:03] we move onto the prompt Library I want
[12:05] to call out another incredible Maro
[12:07] feature inside of the display user mode
[12:10] we can come over to this drop down and
[12:14] display as a grid and as slides great
[12:17] engineering really comes down to two
[12:19] things build great software and then
[12:21] communicate the great software that
[12:23] you've built this tool allows you to do
[12:25] both of those things so let's switch
[12:27] over to grid mode here and as you can
[12:30] imagine we can now drag and drop the
[12:33] cells that we've been building up right
[12:35] so we now have this cell here let's just
[12:37] say I wanted this View and I wanted I
[12:40] want my prompt output view right I just
[12:42] want to keep it really simple here when
[12:44] I'm in this mode widen this a little bit
[12:48] okay so let's just go ahead and run
[12:50] another prompt right so let's just drop
[12:52] down to 40 and let's just rerun you can
[12:55] see we got the loading State and now
[12:57] we're just looking at these two cells
[12:59] left to right super concise super simple

### Minute 13

[13:03] it's rendering our prompts and we can
[13:04] pull in any cell that we want for
[13:07] instance if we wanted to we can pull in
[13:08] our form values component and move that
[13:11] over here make this a little wider so we
[13:13] can see everything that's actually
[13:14] getting computed from this and again
[13:17] it's all reactive so if I you know
[13:19] maximize this if I switch to 1.5 Pro
[13:23] resubmit both of these items because
[13:25] they Depend and have state referenced in
[13:28] this original
[13:29] cell all of those States will get
[13:32] updated right so now we have our new
[13:33] model temperature so on and so forth
[13:35] Maro notebooks are incredible right we
[13:37] have rapid prototyping we have reactive
[13:40] notebooks we have data visualization
[13:43] which we haven't tapped into too much
[13:45] yet and we have easy interactivity let's
[13:48] go ahead and keep pushing you know this
[13:50] is just another fantastic way to view
[13:53] the work you've done there's also a mode
[13:54] where you can run it in slides for o
[13:57] latus let's make it super specific and

### Minute 14

[14:00] then we can hit submit and then in our
[14:02] you know future items here you know
[14:04] while this is loading it's going to run
[14:06] in this slide mode really interesting
[14:08] way to kind of view manage and update
[14:11] your code so let's go ahead and switch
[14:13] back to Vertical view so that you have a
[14:14] good idea of how this works go ahead and
[14:17] hit the like hit the sub and let's hop
[14:19] into how we can use Maro Next Generation
[14:21] python notebooks to build a reusable
[14:24] prompt
[14:28] Library so let's dive into our third
[14:30] notebook I'm going to copy this UV run
[14:32] command and this is going to kick off
[14:34] our prompt Library notebook right away
[14:37] I'm going to collapse all the code and
[14:38] we're just going to talk about this from
[14:39] a high level we don't need to see all
[14:42] the nitty-gritty details we're reviewing
[14:44] the product we're reviewing the tool and
[14:46] we're just talking high level so you can
[14:48] see here we have a similar UI have a
[14:50] nice H1 header we have a form with a
[14:53] submit button and here we can select an
[14:55] llm so let's go ahead and just select um
[14:57] let's go and use o1 Mini and now we're
[14:59] going to select a prompt so you can see

### Minute 15

[15:01] here I have four prompts three of these
[15:04] you'll recognize from the previous 01
[15:06] reasoning model video we're going to use
[15:08] the bullet knowledge compression prompt
[15:10] and hit submit so we've now locked in
[15:13] our prompt if I hit click to show you
[15:15] can see we can view this prompt right
[15:18] here and if we want to we can go ahead
[15:20] and change our prompt hit submit again
[15:23] and you can see we've now selected that
[15:25] other prompt right so this is a YouTube
[15:27] video Chapter prompt that automatically
[15:30] generates YouTube chapters based on
[15:32] timestamps and SEO keywords let's go
[15:35] ahead and hop back let's keep this
[15:36] simple for this example here's the
[15:38] amazing part that makes this prompt
[15:40] library and that makes Maro notebooks
[15:43] really powerful we have this block that
[15:45] we want to update you want to reuse your
[15:47] prompts right you don't want to spend a
[15:49] bunch of time and then throw your prompt
[15:51] away there's massive value in reusing
[15:53] your prompts and most importantly adding
[15:56] variables to your prompts so you can see
[15:58] here we have a variable content and this

### Minute 16

[16:01] Maro notebook takes that content and
[16:03] finds this pattern it takes the variable
[16:06] within it and creates a text area so now
[16:09] we can fill in this text area here and
[16:11] what I'll do here is I'll pull I'll pull
[16:13] the legendary how to succeed in Mr be
[16:16] production PDF this PDF went viral a
[16:19] couple weeks ago I think there are some
[16:21] seriously valuable nuggets of
[16:22] information in here so let's go ahead
[16:24] and just grab a piece of content one of
[16:27] my favorite sections was where is a
[16:29] critical components yeah this is so
[16:30] relatable in engineering so I'm going to
[16:33] copy this and what I'm going to do is
[16:35] just paste this inside of our prompt
[16:37] variable and I'll hit prompt so we have
[16:40] another cell that just got kicked off
[16:42] now that we have a value and something
[16:44] really cool is going to happen here 01
[16:45] mini is churning and now it has a result
[16:48] for us it followed the prompt perfectly
[16:51] by creating a list of ideas with a theme
[16:54] and then some bullet points underneath
[16:56] we can click to show the context filled
[16:59] prompts which has our variable filled in

### Minute 17

[17:02] and replaced with this Dynamic text area
[17:05] I hope you can see where this is going
[17:07] right and I hope you can see how
[17:08] valuable this is in the age of
[17:10] generative AI let me just go ahead let's
[17:12] do a refresh here let's restart reset
[17:14] the kernel and let's go back into user
[17:16] mode and let's just run that over again
[17:18] we're going to select the prompt we want
[17:20] to select a model hit submit we want to
[17:22] pass in the context and prompt okay so
[17:25] in literally no time right and four
[17:28] clicks
[17:29] I have reused a it's a fairly simple
[17:32] prompt but this could be much much more
[17:34] complex right in our previous video we
[17:36] looked at an AI coding meta review
[17:38] prompt if we look at that prompt you can
[17:40] see we have two variables here right so
[17:42] this is an AI coding prompt check out
[17:44] the previous video to see more details
[17:45] on this but we'll pass in our code files
[17:48] and the diff of our code and then we're
[17:50] going to get a full comprehensive code
[17:53] review right so this prompt can be
[17:55] easily and quickly reused using Mar
[17:58] notebooks there are a ton of ways to

### Minute 18

[18:00] push this further but I want to share
[18:02] with you how I'm starting to build out
[18:04] and organize my prompts inside of a
[18:07] reusable prototyp notebook marot is also
[18:12] really incredible because it's a great
[18:13] tool we can use on the channel to kind
[18:16] of share and show ideas in a more visual
[18:18] datar Rich way but if we hop into the
[18:21] code here if we hop into engineering
[18:22] mode you can see we have Imports you can
[18:25] see I have this method that is pulling
[18:26] in my map prompt library and you know we
[18:30] can just dial into this if we want if I
[18:32] just hit enter here and run this you can
[18:34] see it's a simple map between the file
[18:38] and the prompt that's inside of the file
[18:40] if we open up our editor we can just
[18:43] crack that open and you can see
[18:45] underneath prompt Library I just have
[18:47] four prompts here we can click into that
[18:49] and you can see the you know AI coding
[18:51] meta review you can see the bullet
[18:53] knowledge compressor and the other
[18:55] prompts are here as well right so we
[18:56] just have a simple python function
[18:58] that's pulling that in and creating this

### Minute 19

[19:00] dictionary for us right it's just fully
[19:02] reactive super easy to just dive in see
[19:04] what the code is doing see what it looks
[19:06] like I'm building all of our models here
[19:08] creating a map we have some simple CSS
[19:10] styles that I use for the prompts and
[19:12] then we have our user interface for our
[19:14] primary controls you can see here MMD
[19:16] we're using batch to pass in these
[19:19] values and then we're using form to turn
[19:21] it into a form so that we can utilize
[19:24] these items after they're submitted
[19:26] specifically throughout the rest of our
[19:28] cells let's go ahead and run our haacker
[19:30] newes sentiment analysis uh we'll use 01
[19:33] mini this is a heavier prompt so now we
[19:36] have a vertical stack with just a simple
[19:39] H1 header right that's just our selected
[19:41] prompt header and then we have this
[19:42] accordion right so this is really cool
[19:44] click to show and then it maps to
[19:45] another component so we'll click to show
[19:47] and then you can see there it's just
[19:48] showing the prompt that we selected
[19:50] right so this is our Hacker News
[19:51] sentiment analysis prompt we can go
[19:53] ahead and close that and then here we
[19:55] have the text area right so we're doing
[19:57] some dynamic work here to find every

### Minute 20

[20:00] item inside the prompt between these
[20:03] delimeters right so we have this you
[20:04] know left curly right curly and then we
[20:07] use that to dynamically create text area
[20:09] components you can imagine us pushing
[20:12] this further maybe you want some PDF
[20:14] components maybe you want a file
[20:17] selector where you pull in all the files
[20:19] just a kind of hint hint at where this
[20:22] prompt framework is going and then you
[20:25] can of course run the prompt so when the
[20:28] prompt runs it comes down here we have a
[20:30] couple variable Stoppers so you know if
[20:33] we don't have any array items or if the
[20:35] button hasn't been pressed just do
[20:36] nothing right that's what this stop does
[20:38] this is really important in this
[20:40] reactive environment down here we
[20:42] actually have the run so let's go ahead
[20:43] and just kick this off let's quick hop
[20:44] on Hacker News let's find a post this
[20:47] one looks interesting so I'm just going
[20:48] to go ahead hop into this copy the ID go
[20:52] to hn. algolia paste in the ID copy
[20:57] these items just like before four
[20:58] instead of going to the CLI and creating

### Minute 21

[21:00] a file we're just going to paste it all
[21:02] right here and something that would be
[21:04] really great to add to this would be to
[21:06] create a simple token counter or at
[21:08] least a word counter for now I'm just
[21:10] going to open up a cursor hit paste and
[21:12] you can see here I have about 8,000
[21:14] tokens that's fine I'll go ahead and hit
[21:16] prompt down at the bottom here you can
[21:17] see our prompt is now spinning this is
[21:19] what's running right now right so we're
[21:20] running the 01 model you can see we got
[21:23] the model dropped down from our form and
[21:25] then we're passing that in along with
[21:26] our context fill prompt and into our
[21:29] python method this is just a classic llm
[21:31] prompt function and there's our results
[21:34] right so this is our hacker new
[21:36] sentiment analysis if we hop into user
[21:39] mode we can see this in a clean format
[21:42] we got both the markdown and the Json
[21:46] version with negative sentiment analysis
[21:48] of this Hacker News Post a Nuance View
[21:51] and then a positive view so this is
[21:54] awesome you know don't worry about
[21:55] what's in the content too much again
[21:56] check out the previous video to see
[21:59] what exactly we did there with The

### Minute 22

[22:00] Hacker News sentiment analysis prompt
[22:02] this is a much much faster way to to use
[22:05] and consume your prompts in the age of
[22:08] large language models and in the age of
[22:10] generative AI the most important thing
[22:12] we can do as Engineers is increase our
[22:14] ability to rapidly prototype and iterate
[22:17] products and tools and also increase our
[22:21] ability to rapidly prototype with large
[22:24] language models prompt engineering
[22:26] although originally a complete meme joke
[22:29] is probably one of the most serious
[22:32] professions there are now and as
[22:34] Engineers we have a massive Advantage
[22:36] because we can utilize tools like Maro
[22:39] to build out these incredible reusable
[22:41] notebooks that allow us to manipulate
[22:44] information faster than anyone don't let
[22:46] anyone confuse you you and I and every
[22:48] engineer we are the kings of knowledge
[22:51] work the ability to use tools like this
[22:54] to manipulate data to build out prompts
[22:56] to build out prompt Frameworks and
[22:58] prompt libraries like this means that

### Minute 23

[23:00] you can control and manipulate
[23:02] information faster than anyone I wanted
[23:05] to share this with you the link for this
[23:06] code base is going to be in the
[23:08] description I highly recommend you check
[23:10] this out there's a ton of value here in
[23:13] getting started with Maro notebooks for
[23:16] agentic engineering but also just for
[23:19] you know standard software engineering
[23:21] where you're Building Products you're
[23:23] testing out ideas and again you're
[23:26] sharing ideas there are two m of pieces
[23:28] to software engineering there's building
[23:31] products and then there's sharing the
[23:33] value that the product has notebooks
[23:36] like Maro and Jupiter notebooks help
[23:39] communicate the value that has been
[23:41] created the massive Advantage I see here
[23:43] with Maro is that it allows you to think
[23:46] about things in an interactive user
[23:49] focused way again I know I've been a
[23:51] broken record about this but the command
[23:53] dot switching from product Focus from
[23:57] high level from user focused to the

### Minute 24

[24:00] engineering level is just a to die for
[24:03] feature that I absolutely love to see in
[24:06] a tool like this so again you know
[24:08] command dot we're switching between
[24:10] engineering and product mode in no time
[24:13] one of the really important things about
[24:14] these notebooks is that it's air quotes
[24:17] just python so you know if we hop over
[24:21] to our prompt Library notebook and
[24:23] collapse everything you can see here
[24:26] that it's just a bunch of appell decor
[24:28] ators with some really fancy graph State
[24:32] Management happening and you can see
[24:34] here right we have that cell where we're
[24:36] building out our models at the top and
[24:39] if we go into developer mode in the UI
[24:42] you know that's exactly what's happening
[24:44] here right so line one is our LM Sonet
[24:47] and if we search that you can see that
[24:49] that is that cell exactly right so you
[24:51] know exactly what this means it means
[24:53] that you can easily commit and modify
[24:55] these files right so we can you know
[24:57] commit these files push them easily

### Minute 25

[25:00] manage them and understand them this is
[25:01] a massive advantage over jupyter
[25:03] notebooks because jupyter notebooks they
[25:05] store all of the output but it also
[25:07] enables us to very importantly use AI to
[25:11] write this for us in fact most of what
[25:13] you're seeing here I generated using AER
[25:16] and using cursor you can imagine you
[25:19] open up AER you add the file to the
[25:22] context and then you just start
[25:24] prompting right so you can say ask how
[25:26] can I add another sell so you can get a
[25:29] nice breakdown there we don't need to go
[25:31] into this we have other videos on that
[25:32] and more coming in the future great
[25:35] engineering is all about rapidly
[25:37] building valuable software and
[25:39] communicating that value to others marmo
[25:42] is a fantastic tool that helps you do
[25:43] that and I had to bring this to you and
[25:45] I had to share this with you I have not
[25:47] been excited about a non-generative AI
[25:50] tool since duck database came out and
[25:53] this is a tool that is going to change
[25:54] the game for you if you give it a good
[25:56] shot and if you understand how valuable
[25:59] it can be to have a reactive notebook

### Minute 26

[26:01] that can help you rapidly prototype your
[26:03] tools and products in the age of
[26:05] generative AI you need every Edge you
[26:08] can get and this is a massive one the
[26:10] idea to take this and create your own
[26:13] prompt Library I think is very novel
[26:15] very interesting very cool because you
[26:17] can come in here switch to Dev mode and
[26:20] just start hacking away on exactly how
[26:22] you want to organize your prompt
[26:24] framework this is just the beginning of
[26:26] this I'm going to be sharing more on my
[26:28] personal prompt library and how I'm
[26:30] organizing my prompts to help give you
[26:32] ideas on how you can do the same thanks
[26:35] so much for watching if you enjoyed the
[26:36] video drop a like drop a comment and
[26:38] I'll see you in the next one