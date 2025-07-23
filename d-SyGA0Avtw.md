# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=d-SyGA0Avtw
- **Duration:** 32:19
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 5618
- **Transcript Generated:** 2025-03-30 23:48:33

## Transcript


### Minute 0

[00:01] what's up Engineers Indy Dev Dan here I
[00:05] have a special video for you today this
[00:07] is a Hands-On nobs AI coding Dev log
[00:12] using CLA code and the model context
[00:16] protocol I have never adopted a tool
[00:19] faster than I've adopted Cloud code
[00:22] there is nothing more important going on
[00:26] right now for True software engineering
[00:29] and in the Gen AI age then CLA code and
[00:33] mCP in this video I'll show why that's
[00:37] true so we're going to boot up claw code
[00:40] but we're not going to prematurely jump
[00:42] in here and start firing off prompts
[00:45] iteratively that's the old 2024 way to
[00:49] do things first thing we need to do is
[00:52] gather all the context and information
[00:55] we need to run claw code in its true
[00:58] agentic form to do this we're going to

### Minute 1

[01:01] use a tool called repo mix repo mix
[01:04] allows us to read entire code bases and
[01:08] collapse them into a single file that we
[01:11] can use as context for our AI tooling
[01:14] for CLA code AI coding tools llms they
[01:18] love patterns they love pre-existing
[01:21] information so that's what we're going
[01:23] to do here we're going to clone the
[01:25] model context protocol servers GitHub
[01:28] repository and then we're going to look
[01:31] at a specific example that we can pull
[01:33] from so we're going to look at git here
[01:35] and so we're going to CD into the git
[01:38] directory and you know we can see
[01:40] there's the structure we can run LS and
[01:42] tree to kind of understand the high Lev
[01:44] structure and then we can run repo mix
[01:47] so repo mix allows us to take this code
[01:49] base and collapse it into a single file
[01:53] you can see we have 30k tokens there and
[01:55] now we're just going to move this into
[01:57] our code base right so I'm going to get
[01:59] the

### Minute 2

[02:00] path to our current
[02:01] codebase run that and then move this
[02:05] into the um AI doc directory you may
[02:09] have seen this throughout some of the
[02:11] code bases that I work on maybe you have
[02:12] your own pattern for this um this is
[02:15] super important for just organizing
[02:17] information that your AI tooling can
[02:19] reference all right so there's that we
[02:22] now have the uh mCP server for git and
[02:28] now we can use this is a you know key
[02:31] guiding example a key guiding structure
[02:34] for our new tool that we're building our
[02:37] new mCP server that we're going to build
[02:39] in this video called pocket pick so
[02:42] there's that now we're going to do
[02:44] something super super important we're
[02:46] going to create a spec we're going to
[02:49] create a plan so before we dive into
[02:53] what this plan is all about um I'm
[02:55] curious what you think comment down
[02:57] below let me know what you think is a
[02:59] more important release model context

### Minute 3

[03:01] protocol or CLA code I feel like these
[03:04] are two massively game-changing tools
[03:07] let me know which tool you're using the
[03:09] most are you fully on board with CLA
[03:11] code and are you fully on board with mCP
[03:15] servers I've been holding off trying to
[03:18] wait to you know understand the
[03:21] landscape of the model context protocol
[03:24] there are of course risks associated
[03:27] with committing to a technology like
[03:29] this but I think and ropic is doing it
[03:31] in such a way that it makes sense it's
[03:34] open source it's public anyone can build
[03:36] these this is turning out to be the
[03:38] standard for building AI agents for
[03:41] building AI tools as you'll see in this
[03:44] video you can quickly build your own mCP
[03:47] servers so what are we building and what
[03:50] is the spec right what is the spec
[03:52] prompt what is this what is this plan
[03:53] that we're building so we are building
[03:55] pocket pick this is your personal
[03:57] knowledge base for reusability

### Minute 4

[04:00] of ideas patterns and code Snippets this
[04:04] is something that we started building
[04:05] out in lesson 8 of principled AI coding
[04:08] and what we're going to do here in this
[04:10] video is use CLA code in its true
[04:13] agentic coding form to build out a full
[04:17] version of this built completely on mCP
[04:21] so this is something different I've been
[04:23] waiting to pull the trigger on this
[04:24] we're going to build this tool as an mCP
[04:28] server first so there will be no other
[04:30] way to interact with this tool other
[04:32] than mCP I think this is going to be the
[04:35] direction things will go as mCP grows
[04:38] and develops so pocket pick is all about
[04:41] quickly being able to save and then
[04:44] reference ideas patterns and code
[04:46] stimits for your engineering work we're
[04:49] setting up the project structure so
[04:51] quite literally the directory structure
[04:54] of this new tool just above you can see
[04:56] the simple pocket pick SQL light table
[04:59] structure

### Minute 5

[05:00] um I love when I can boil down data
[05:02] structures to just the essentials we
[05:04] have ID created text and tags right this
[05:08] is all we need to create a great first
[05:11] version of our personal knowledge base
[05:13] of our pocket piics and so you know you
[05:16] might be asking why are we building out
[05:18] this plan why aren't we just starting to
[05:20] prompt right cuz I can guarantee you
[05:23] that if you're writing prompts
[05:24] iteratively you are not doing as much as
[05:28] you can and you're not scaling in your
[05:30] impact as much as you could be and in
[05:32] this video you'll see exactly what I
[05:34] mean I'm creating that classic
[05:36] implementation notes section this is
[05:38] where you just basically write ad hoc
[05:40] information it's where you work through
[05:42] things it's kind of the catchall section
[05:44] we're doing some API based design here a
[05:48] great way to communicate information to
[05:50] your AI coding tools is to create the
[05:53] interface in which you would use to
[05:55] operate with it so what we're doing here
[05:56] is creating a CLI based API design right
[05:59] and and this will very clearly

### Minute 6

[06:01] communicate to our AI coding assistant
[06:02] what we want the API to look like you
[06:04] can see here I'm using cursor tab as
[06:06] well to help me you know quickly create
[06:09] this spec prompt I think the tech
[06:12] ecosystem has a massive problem in
[06:15] thinking that there are best tools right
[06:18] and thinking you know uh what's the best
[06:21] tool what's the best a coding tool I can
[06:23] use is it cursor is it CLA code is it
[06:25] AER Devon what's the best tool right I
[06:27] just want to use the best tool I think
[06:29] this is a very limiting mindset because
[06:31] it forces you to always think in
[06:33] competition right it forces you to think
[06:35] in Winner Takes all the world is not
[06:38] Winner Takes all at least not our world
[06:41] right we don't have to pick one we can
[06:42] pick multiple the real question we
[06:44] should ask is what combination of tools
[06:48] gives me the best results in the least
[06:51] amount of time with the fewest
[06:53] trade-offs right we're Engineers our
[06:56] work is all about tradeoffs right we're
[06:58] balancing tradeoffs

### Minute 7

[07:00] it doesn't matter what AI technology
[07:02] you're using there will always be a
[07:04] tradeoff the best Engineers know when to
[07:08] make the right
[07:10] tradeoffs so I think in ANS not ores I
[07:13] use you know claw code I use cursor tab
[07:18] I use AER right there there's a time in
[07:20] place for all these tools and you know
[07:22] just to like you know address the
[07:24] elephant in the room that is CLA code um
[07:27] this tool does change things like I
[07:29] mentioned you know um in combination
[07:32] with mCP this tool is a must have for
[07:36] engineers uh moving
[07:38] forward specifically some powerful mCP
[07:42] host and you know your own personal set
[07:45] of mCP servers this is just going to be
[07:48] the way things are moving this this this
[07:51] information set this tool set has caught
[07:54] fire we'll talk about AER and Cloud code
[07:57] more in the future

### Minute 8

[08:00] I'm continuing to build out the project
[08:02] structure and as you can see here we're
[08:04] using information dense keywords we're
[08:06] using the mirror keyword if you've taken
[08:08] principal AI coding you know exactly how
[08:10] powerful that is and what this means
[08:12] this is really cool so I'm basically
[08:14] treating every file inside of our
[08:17] project structure as a prompt right so
[08:21] you can communicate additional
[08:23] information um by using some simple
[08:26] nesting structure like this right so you
[08:29] can see here I'm adding a new pantic
[08:30] type in the data types file I'm
[08:32] detailing that we want that default
[08:34] database path and then here we're going
[08:36] to use one of my favorite patterns dot
[08:38] dot dot this is one of my all-time
[08:40] favorite information Den keywords dot
[08:42] dot dot tells your a coning assistant
[08:46] continue right keep going with the
[08:48] pattern right fill in the blanks feel
[08:50] free to pause the video there um this is
[08:52] something we talk about uh in principal
[08:54] a coding but just by typing that dot dot
[08:56] dot there our AI coding assistant knows
[08:59] to create the other pantic types filling

### Minute 9

[09:01] in some more implementation notes here
[09:03] you know nothing super crazy nothing
[09:05] super new happening here and we're just
[09:07] working through everything that we want
[09:09] done here right so we're referencing our
[09:12] documentation uh we're saying that we
[09:14] want all of our tags to be
[09:16] lowercase and now we're looking at the
[09:19] mCP git server we want to see the
[09:22] dependencies it has right I want to make
[09:23] sure that I'm covering the dependencies
[09:25] we also want pie test we're going to
[09:27] need this for closed loop self
[09:29] validation and of course SQL light 3
[09:32] this is built in so I'm going to make
[09:33] sure that I mention that okay and I'm
[09:37] telling the you know I'm I'm telling
[09:39] Cloud code um how to run things right
[09:44] and so just adding some more
[09:45] implementation notes Here I definitely
[09:48] could have ADD added some of these
[09:49] inside of the uh project structure um
[09:52] but it's important to not overthink
[09:55] things too much you just want to have
[09:57] the information visible to your AI

### Minute 10

[10:00] coding tool right keep things simple now
[10:02] we're doing something really really
[10:03] important again principal AI coding
[10:05] members know why this is so important um
[10:08] we're closing the loop here by telling
[10:10] our language model how to validate
[10:13] itself so we're working through here we
[10:15] almost have a final version we're going
[10:17] to make one tweak to our plan and and
[10:20] you know you you may be like holy crap
[10:22] you haven't done anything yet you know
[10:24] we spent 10 minutes writing this plan um
[10:26] that's right we have and you're going to
[10:29] see why and how powerful it is in just a
[10:31] moment here and so as I was working
[10:33] through this I realized that I don't
[10:35] think I had enough information to
[10:37] complete the work needed for the find
[10:40] command and now that I'm playing this
[10:42] back I'm actually I actually completely
[10:45] uh write this incorrectly so I'm using
[10:48] Pocket ad instead of pocket find so you
[10:51] know there's just a glaring mistake
[10:53] there we'll see if our AI coding
[10:54] assistant picks up on my mistake or
[10:56] automatically corrects it for me so
[10:59] there we go now we're back in CLA code

### Minute 11

[11:01] and now it's time to fire off CLA code
[11:05] so we now have our plan now it's time to
[11:09] watch our upfront investment pay off so
[11:12] I'm going to Prime Cloud code this is a
[11:15] really important kind of new paradigm
[11:16] I'm saying read these files then
[11:20] implement the plan right so you can
[11:23] see as per request it's reading those
[11:26] files and then it's going to read you
[11:28] know there go reading the project at
[11:30] taml right it's understanding the entire
[11:33] uh project structure and now it's going
[11:34] to read the plan right so there it goes
[11:37] now it wants to start working so you
[11:40] know if you've used Cloud code you know
[11:42] what's going to happen next we're going
[11:43] to turn on YOLO mode I don't want it to
[11:45] ask for permission all the time I wanted
[11:47] to get the work done in the most agentic
[11:51] fashion possible so here we go this is
[11:54] the incredible part like subscribe
[11:57] comment if you know what's going going
[11:59] to happen next year right so we wrote

### Minute 12

[12:01] out this comprehensive plan and look at
[12:03] what's happening look at what's
[12:05] happening on the
[12:06] left files content um code it's getting
[12:12] generated right we wrote the plan we
[12:16] outlined the directory structure we used
[12:19] idks to communicate a lot of information
[12:22] and check this out add got created F got
[12:26] created list tags got created list got
[12:28] created removed just got generated right
[12:31] this is a different way of engineering
[12:34] this is the next phase in AI coding
[12:38] we're moving from AI coding to a gentic
[12:41] coding great planning is now great
[12:46] prompting okay this is a paradigm shift
[12:50] in how code gets
[12:52] created our AI coding assistant
[12:56] understands what we want because we
[12:57] spent The Upfront investment right these

### Minute 13

[13:00] are not oneoff ad hoc prompts right
[13:03] Claud Cod doesn't need to read write
[13:05] read right read right we gave it a big
[13:09] picture as if our product manager or
[13:12] lead engineer uh you know wrote up a
[13:14] very very powerful comprehensive you
[13:16] know ticket or plan for you to build
[13:19] something right that's the way to think
[13:21] about writing great spec prompts so you
[13:24] can see here
[13:25] dependencies right uh it's all getting
[13:28] added here and now it knows we're
[13:30] operating in UV it's asking to install
[13:33] we say yes of
[13:35] course and things are happening right
[13:38] things are just happening um I actually
[13:42] enter in the wrong command here but it
[13:43] doesn't end up uh mattering too much and
[13:46] there we go uh tests right tests are
[13:48] getting generated and you know it's all
[13:52] just
[13:53] happening you know it's it's just we set
[13:56] things up we invested and now our
[13:58] tooling is doing the work for us okay so

### Minute 14

[14:00] Claude is suggesting the wrong command
[14:03] so I'm just going to remind it I'm
[14:04] saying UV runp test remember I'm kind of
[14:07] triggering it to run a needle in the
[14:09] Hast stack uh test against the plan
[14:12] right because I did mention that
[14:14] expensively in the implementation notes
[14:17] I said use UV runp test so something I
[14:20] noticed here it's running test that's
[14:21] great it's self validating it's awesome
[14:23] but I notied we're missing a ton of
[14:26] tests right we only have test ad and
[14:28] test test a knit we need full test
[14:31] coverage I don't want to know that part
[14:34] of the codebase works I want to know
[14:35] that all of it works I'm just running a
[14:38] follow-up prompt and you can see here in
[14:40] the functionality test uh we are just
[14:42] missing test it only has a knit and test
[14:44] ad so um I mentioned that to clog code
[14:47] and now it's going to blaze through all
[14:49] the missing tests right clog code is
[14:51] fantastic this is one of the best
[14:53] agentic coding tools uh to date a tool
[14:57] like this a tool that's powerful forces
[14:59] you to rethink how you're building it

### Minute 15

[15:02] forces you to consider that this is a
[15:05] paradigm shift that this is a new way of
[15:08] engineering and it is it is I have
[15:11] access to three clawed you know API
[15:13] tokens across different teams and I can
[15:16] tell you I've spent hundreds of dollars
[15:18] on cloud code already that number is
[15:21] only going to go up when we talk about
[15:23] trade-offs when we talk about AER versus
[15:25] Cloud code and Cloud code versus really
[15:28] anything this tool is going to cost you
[15:32] this thing is a token gobbler I know
[15:35] some Engineers have talked about Klein
[15:37] and other agentic tools you know chune
[15:39] through tokens Cloud code is no
[15:42] different everything must come through
[15:44] the context window okay so this is
[15:46] fantastic we just ran that help command
[15:49] and you can see everything looks like it
[15:51] passed properly plug code is reporting
[15:53] success if we run/ cost you can see
[15:56] exactly what I'm talking about there
[15:58] that session
[15:59] right those three and really one prompt

### Minute 16

[16:02] cost $2 to run okay so this is not cheap
[16:06] technology right we are talking when
[16:08] you're writing these big powerful spec
[16:10] prompts we are talking dollars per
[16:12] prompt right and this is nowhere near
[16:16] the largest spec prompt I've created
[16:18] okay so you can imagine as you scale
[16:19] this up as you hand off more of your
[16:21] work as you create these more powerful
[16:23] precise packages for your AI tooling
[16:26] those costs these numbers go up right
[16:29] right and I do want to quickly mention
[16:31] this is something we talk about in
[16:32] Lesson Four of principal AI coding you
[16:35] want to be spending money to save
[16:39] time you know as long as the costs are
[16:42] worth it I absolutely recommend using
[16:45] tool like this using other tools that
[16:46] let you scale up your computer right now
[16:49] we're doing the review process okay so
[16:51] we're reviewing we're validating we're
[16:53] making sure that um you know no matter
[16:56] how great these tools get it's always
[16:58] going to just take a pass through the
[16:59] code to make sure it looks good so

### Minute 17

[17:01] that's what I'm doing right now we
[17:02] walking through our brand new pocket
[17:03] pick mCP server functionality so it all
[17:06] looks good and what I'm going to do now
[17:08] is just understand how much impact I
[17:10] just had so I'm going to remove the lock
[17:14] file stage these current files and then
[17:16] run uh get diff head stat so you can see
[17:19] there 1,600 lines 1,600 lines of code
[17:23] created from a I think we have a 100
[17:27] line uh prompt right about 1,000 tokens
[17:31] okay so you know just looking at it from
[17:33] a point blank perspective I just 16 xed
[17:38] my impact right I multiplied what I
[17:40] could do by 16x not considering any
[17:43] complications not considering any of the
[17:45] time it takes to actually write the code
[17:47] that's just on a
[17:49] perline basis okay really it's more like
[17:52] a 30 or 40 or 50x because it takes time
[17:56] to think through and test all this code
[17:59] right and we just packaged it we created

### Minute 18

[18:02] a great package we created a great plan
[18:04] and what did we do we handed it off to
[18:07] our AI tooling we handed it off to our
[18:10] AI coding assistant we gave it to Claude
[18:13] code the new agentic coder on the Block
[18:16] and we said here's a great comprehensive
[18:19] plan build this for us okay so um I hope
[18:23] you can see why that's so valuable if
[18:25] you kind of get it if you understand
[18:26] where things are going hit like hit
[18:28] subscribe join the journey as we dig
[18:32] into using these tools and getting
[18:34] massive value out of these tools for
[18:36] your engineering work for your career
[18:38] and for your projects as mentioned in
[18:41] principal ad coding soon there will be
[18:43] nowhere else to go AI coding tools are
[18:47] taking over Engineers using these tools
[18:50] as you can see here they're doing more
[18:53] than ever thought possible before an
[18:56] engineer even writing iterative prompts
[18:59] over and over and over they're not

### Minute 19

[19:01] coding like this right they're not
[19:03] generating as much as they could be okay
[19:06] so this is really important so what are
[19:08] we doing now so now we're actually
[19:10] running our mCP server right so we just
[19:12] created a brand new pocket pick codebase
[19:15] as a mCP First Tool so now we're going
[19:19] to test it all
[19:22] right now we're fing up Claud you can
[19:24] see there no tools right no mCP tools
[19:27] and now we're going to take this Command
[19:30] right Claude mCP add Pocket pick and you
[19:33] know I'm adding some documentation here
[19:35] for uh snippet
[19:37] reuse and and we're going to fire that
[19:39] off so again looks like everything's
[19:41] working well that was successfully added
[19:44] I'm going to add some more documentation
[19:46] here again just for reuse I don't like
[19:47] to constantly be looking this stuff up
[19:50] so I always add these to my readme or
[19:52] you know some type of
[19:54] documentation so Claude mCP list is
[19:57] going to show uh the mCP servers I
[19:59] noticed that uh there's a bug here

### Minute 20

[20:01] sometimes you have to run Claude mCP
[20:03] list twice to get the true list so
[20:06] that's what I've done you can see the
[20:08] second time pocket pick actually lists
[20:11] so there it is when I run claw you can
[20:12] see pocket pick exists as an mCP server
[20:16] if we go full screen we can get this
[20:17] nice beautiful view of claw code and now
[20:21] I'm saying you know list all the tools
[20:24] and so you know there's an issue here
[20:26] Cloud code running Sonic 3 7 it's not
[20:29] perfect so I'm going to be more precise
[20:31] here with my prompt I'm going to say um
[20:34] list pocket pick
[20:36] tools and you know just trying to be a
[20:38] little bit more precise with my prompt
[20:41] and there it is so we can see all the
[20:43] capabilities we have access to Via this
[20:45] new pocket pick mCP server that we had
[20:48] Cloud code uh you know quite literally
[20:51] one shot for us I think it was one shot
[20:52] in you know maybe uh two or three small
[20:55] follow-up prompts and so now we're
[20:57] running our first Command right so
[20:58] pocket list and we have an error okay so

### Minute 21

[21:02] this is something that's going to happen
[21:03] we're we're we're expecting our large
[21:05] scale agentic coding tools to get us 90
[21:08] 95 99% of the way there so I'm literally
[21:11] just going to take that error and write
[21:13] a follow-up prompt inside of clog code
[21:16] detailing where the issue is right at
[21:19] this point in the video at this point
[21:22] Claude understands this codebase better
[21:25] than I do right I I haven't even seen
[21:28] half the files in this code base right
[21:30] speaking of tradeoffs when you use
[21:32] agentic coding tools like this you will
[21:35] naturally understand less of what is
[21:38] getting built right in more high stakes
[21:40] production products I am spending a lot
[21:43] more time on the review process so that
[21:46] change got implemented I'm now running
[21:49] um the same Command right list all
[21:51] pocket picks there it is and now we have
[21:54] the correct response no items found so
[21:57] our pocket pick database is empty as you
[21:59] saw there Claude giving us some key

### Minute 22

[22:01] information and now what we need to do
[22:03] is add some content to our pocket pick
[22:06] database pocket pick helps us keep track
[22:08] of ideas patterns and code Snippets I'm
[22:11] sure you've run into this issue a
[22:12] million times where you have a code
[22:15] snippet you have some piece of code that
[22:17] you refer to over and over and over
[22:19] again for me I refer to you know these
[22:21] model documentation all the time right
[22:23] but there are you know many other things
[22:25] that uh you might want to refer to for
[22:27] instance you might want to save how to
[22:29] run the claw 3.7 thinking tokens right
[22:34] you might want to save specific you know
[22:35] a or startup commands you might want to
[22:37] save um you know some documentation or
[22:40] quote that you liked or an idea that you
[22:42] liked right there's tons of examples of
[22:44] things that you might want to save right
[22:46] so I'm doing something really cool here
[22:48] um this is an mCP First Tool so I'm
[22:51] saying use PB paste and add a new pocket
[22:53] pick item with these
[22:56] tags so this is really cool so
[22:59] you can see there's the paste and

### Minute 23

[23:00] there's the Pocket ad command with the
[23:03] text with the tags the tool is alive we
[23:08] have built this thing right and in we've
[23:11] built it in fractions of the time that
[23:14] it would have taken if we did this by
[23:16] hand or even with iterative a coding
[23:19] prompts okay so I mean I mean you know
[23:23] you can you can literally go back and
[23:24] count if you want um you know we ran
[23:28] Maybe six prompts and one prompt did 90%
[23:31] of the work right uh thanks to our spec
[23:33] so just testing out functionality here
[23:35] you can see I just ran pocket git with
[23:37] that exact ID and got that you know
[23:39] correct
[23:42] item and now we're just continuing to
[23:44] look through I want to add additional
[23:46] pocket picks right I want to add
[23:48] additional items into my pocket pick
[23:50] database to work with so I'm going to
[23:52] the open AI model page just going to do
[23:54] a quick Copy and you know kind of run
[23:57] that same thing right so I'm saying PB

### Minute 24

[24:00] paste uh ppck ad so I'm using it you
[24:03] know on the Fly uh information T keyword
[24:07] that I literally just made up out of
[24:08] nowhere ppck add and then uh some tags
[24:12] right and I actually just I should have
[24:13] prefixed that with tags but Cloud code
[24:15] is going to get it here it understands
[24:18] uh how to write this and there you go uh
[24:20] there's that new Pocket ad command you
[24:22] can see item successfully added with
[24:24] those tags so it did you know understand
[24:27] the proper tagging
[24:29] and now we're going to run clear to
[24:31] reset everything I don't want Cloud Cod
[24:33] having the context of what just happened
[24:36] I want that fresh session and there we
[24:38] go so I'm running um pocket list tags so
[24:41] now you can see all the tags that
[24:43] currently exist in the pocket pick SQL
[24:46] light database and so now we're going to
[24:49] run pocket pick find 03 mini and I'm
[24:53] going to look for it in substring mode I
[24:55] really should have chosen a different
[24:56] mode there because substring is the
[24:57] default but you can see there it found
[24:59] that pocket pick item and now we're

### Minute 25

[25:01] going to run uh list tools again so
[25:03] we're want to see all the tools
[25:04] available so just letting claw work
[25:07] through whatever it needs to run to show
[25:09] me the available tools there it is so
[25:11] I'm going to run pocket backup so I want
[25:13] to back up the database and so you can
[25:15] see there I just ran LS through Claude
[25:18] this is a kind of cool way to run
[25:19] commands you can just type you know
[25:21] Point Blank uh bash commands shell
[25:23] commands and now I'm saying back up the
[25:25] database using absolute path so you know
[25:28] back up to this current directory and
[25:30] then I'm going to run LS again write in
[25:31] claw code and you can see there's the
[25:34] result we now have that backed up
[25:36] database so that works great and opening
[25:39] up a new terminal tab here I'm going to
[25:41] move to that directory I just want to
[25:43] just doing validation right I want to
[25:44] make sure that things are actually
[25:47] working as expected opening up a cursor
[25:49] instance here using a nice extension
[25:53] here that lets me view into SQ light
[25:55] databases and as you would expect we
[25:57] have our two rows
[25:59] so again we're just validating right a

### Minute 26

[26:01] lot of what we're going to do now in the
[26:02] AG of generative AI with these powerful
[26:04] AI coding tools is just curate validate
[26:08] review double check triple check and
[26:11] tweak right so what we're going to do
[26:13] now is add an additional mCP tool as you
[26:15] can see Cloud code by itself is
[26:17] incredibly powerful Cloud code is even
[26:19] more powerful when you add a tool but
[26:21] when you start stacking these mCP
[26:24] servers together you get something truly
[26:26] extraordinary so that's what we're going
[26:27] to do here we're going to add fetch to
[26:30] make it easier to put together these
[26:31] pocket pick items so again I'm adding
[26:35] documentation right I highly recommend
[26:37] you you don't just copy this stuff and
[26:39] fire once like make it reusable right
[26:42] make it easy for yourself to keep
[26:43] winning make it easy for yourself to
[26:45] move fast so creating that command there
[26:48] and then I'm going to you know end this
[26:50] session move back to Cloud code kill
[26:52] this session you can see there that was
[26:54] a 13 C session not cheap for the little
[26:57] work that we did
[26:59] um but there we go right so added that

### Minute 27

[27:00] server validated it with mCP list and
[27:03] now we can click off claw with a brand
[27:05] new mCP server connected right so now we
[27:07] have the ability to make web requests
[27:10] I'm going to the Gemini docs and you can
[27:12] guess what I'm going to do here right
[27:13] copy the URL
[27:16] fetch Gemini web page then I'm saying
[27:19] then add Pocket pick item then of course
[27:22] I'll specify tags so we're going to say
[27:24] llm models Gemini and Flash so whenever
[27:26] I want to look up this pocket pick item
[27:29] I can just search for llm models gemini
[27:32] or Flash
[27:33] right so there it is uh we need to give
[27:37] YOLO mode access to uh scrape this
[27:40] entire page over and over so that's what
[27:43] we're doing we're you know we're letting
[27:45] Cloud code operate in its highest
[27:48] efficiency mode right which is Yolo mode
[27:50] it's just agentic right um it did make a
[27:52] mistake here I want all the content it's
[27:54] doing some trimming um this is one of
[27:56] the Annoying Parts about some of these
[27:58] models they try to uh uh you know reduce

### Minute 28

[28:01] context sometimes so you have to be
[28:04] explicit every once in a
[28:06] while and there we go so we saw that
[28:09] that new Gemini pocket pick item got
[28:11] added fantastic so now I can run lists
[28:15] again information T keyword there ppck
[28:19] tags and there we go so uh there are all
[28:23] of my tags now we're going to go ahead
[28:26] and and find
[28:28] all of my items I want to look for all
[28:31] my llm
[28:32] tags and then create a markdown file
[28:35] with all the models right so there we go
[28:37] so we're going to run that first command
[28:38] you can see that that was wrong that was
[28:40] the wrong command so immediately Cloud
[28:42] code pivoted to the pocket list command
[28:45] versus the pocket find pocket find is
[28:47] for looking up texts and pocket list is
[28:51] for searching via tags I probably could
[28:54] have improved the naming there but as
[28:56] you can see here we're working through
[28:58] it making progress there's that llm

### Minute 29

[29:01] models file that all looks great and now
[29:04] I'm just going to do some more you know
[29:06] ad hoc testing you've seen me do this in
[29:08] a couple previous videos you know create
[29:10] the AML and Json version I'm just kind
[29:12] of playing with Cloud code here and uh
[29:15] you know validating some functionality
[29:16] so you know this tool these tools are
[29:21] incredibly powerful okay it's important
[29:24] to stay up to date it's important to
[29:26] understand what you can do with these
[29:27] tools on the channel I try to share you
[29:29] know as much as I can with the time that
[29:31] I do have I try to share with you these
[29:33] kind of key AI coding ideas and
[29:35] principles and patterns but you know in
[29:37] every video we only really scratch the
[29:39] surface of what we can do I highly
[29:42] highly recommend you check out principle
[29:44] a coding if you haven't already um this
[29:46] is my take on how to transition from the
[29:49] old ways of engineering to the new way
[29:52] where we code and build faster than ever
[29:55] with AI coding tools like AER cursor and
[29:59] now Claude code right and whatever is

### Minute 30

[30:01] coming next in the course we focus on
[30:04] principles not tools we focus on
[30:06] principles not models we know that
[30:10] models will continue to evolve we know
[30:12] that tools will just keep changing but
[30:16] you know what matters and I'm really
[30:18] proud of this the fact that you know
[30:20] with every passing day with every
[30:22] release principled ad coding is still
[30:25] relevant in fact it's it's it's even
[30:28] more relevant than it was when it was
[30:30] launched okay so I highly recommend you
[30:32] check it out um um I'm I'm packing in
[30:36] bonuses after bonuses inside the tool
[30:38] I'm going to be releasing a state of AI
[30:42] coding a long form essay detailing tools
[30:46] I'm using the models I'm using I'm going
[30:49] to break down where the industry is at
[30:51] where the industry is going so again
[30:53] that's going to be available exclusively
[30:55] for principled ad coding members that
[30:58] have taken principal AI coding to

### Minute 31

[31:00] completion so I highly recommend you
[31:02] check that out I put a lot of Blood
[31:04] Sweat and prompts into principal AI
[31:07] coding it's going to help you move fast
[31:09] it's going to help you remain and be
[31:12] relevant and truly Thrive with these air
[31:15] coding tools as you saw here in this
[31:17] video um it's all about adaptability
[31:20] it's all about patterns that you can
[31:23] reuse across code bases across time and
[31:27] the best best way to form these patterns
[31:29] is with concrete
[31:32] principles so definitely check that out
[31:34] Link's going to be in the description
[31:36] for you um this codebase pocket pick is
[31:38] also going to be available for you if I
[31:40] have time I will create a full um you
[31:43] know piie hosted version of this so we
[31:45] can just run uvx on this but this is
[31:48] cloud code this is um you know a a just
[31:53] a glimpse of a coding with these tools
[31:57] like I mentioned I only spent $2 here I

### Minute 32

[32:00] spend hundreds across the week shipping
[32:04] more code than ever if you enjoyed this
[32:06] video if you want to stay up toate hit
[32:09] the like hit the Subscribe join the
[32:11] journey thank you so much for watching
[32:14] stay focused and keep building