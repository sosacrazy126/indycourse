# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=dabeidyv5dg
- **Duration:** 31:26
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 5521
- **Transcript Generated:** 2025-03-30 23:48:29

## Transcript


### Minute 0

[00:00] what's up Engineers Indie Dev Dan here
[00:03] there is zero debate in the tech
[00:06] ecosystem you and I and almost every
[00:09] Builder knows that all code will soon be
[00:13] written by AI coding agents a natural
[00:16] next question is then how can we design
[00:20] our code bases to be optimal for our AI
[00:23] coding tools if our AI coding agents are
[00:26] going to be operating our code bases we
[00:29] should be designing our code bases to be
[00:31] token efficient it doesn't matter if
[00:33] you're using cursor Zed claw code AER or
[00:37] wind surf these tools will all change
[00:40] and evolve some will die some will
[00:43] Thrive what matters is how you architect
[00:47] systems of context that can be easily
[00:50] understood and operated by your AI
[00:53] coding tools always keep in mind the big
[00:57] three context model prompt so in this

### Minute 1

[01:02] video we're going to explore the
[01:04] question what is the optimal codebase
[01:07] architecture for AI coding and AI agents
[01:11] why is this important it's important
[01:13] because if you manage your context you
[01:16] manage your results in the generator of
[01:19] AI age this is the name of the game if
[01:22] you manage your context you will manage
[01:25] your results let's break down the key
[01:27] questions we're going to answer what is
[01:29] the optimal code based architecture for
[01:31] AI coding what is the optimal codebase
[01:33] architecture for building AI agents and
[01:36] then lastly and most importantly does it
[01:39] matter at all as AI coding tools
[01:42] progress as new agentic tools like Claud
[01:45] code emerge we have to zoom out and
[01:48] answer the question does it matter at
[01:51] all great Engineers always stop to ask
[01:54] if the problem they're trying to solve
[01:56] is worth solving at all does it matter

### Minute 2

[02:00] what our code-based architecture looks
[02:01] like if these three questions interest
[02:03] you stick around and let's start with a
[02:06] popular yet misused codebase
[02:09] architecture this is the atomic
[02:11] composable architecture there are many
[02:14] names for all the structures we're going
[02:15] to look at I'm using generic versions of
[02:18] these names what does this codebase
[02:19] architecture look like it looks like
[02:22] this we have atoms that are composed
[02:24] into molecules that are then composed
[02:27] into organisms for each one of our
[02:29] architectures we're going to break down
[02:31] pros and cons so what are some pros of
[02:33] this it's very very reusable right the
[02:35] entire architecture is basically
[02:37] reusable pieces reuse is off the charts
[02:40] this is fantastic this is going to be in
[02:42] contrast to some of the architectures
[02:44] we're going to look at that have really
[02:45] low reuse there's a very very clear
[02:47] separation of concerns as long as you
[02:50] have a brief description for your atoms
[02:52] molecules and organisms it will be very
[02:54] easy for your ating tools to understand
[02:57] this architecture by the way you know
[02:59] Adams molecules organisms these can be

### Minute 3

[03:01] named other things this is the atomic
[03:04] design framework popularized by Brad
[03:07] Frost it was originally adopted for
[03:09] front-end code bases for composing UI
[03:12] components but it's really been adopted
[03:15] throughout the engineering stack and all
[03:17] types of code bases and it's because
[03:19] just like in nature there are often
[03:21] smaller pieces that create larger pieces
[03:23] right you have atoms that make molecules
[03:26] and molecules make organisms as you'll
[03:28] see in this video you can also extend
[03:30] this even further with membranes and
[03:33] ecosystems if you want to go above the
[03:35] organism level you can really create as
[03:37] many levels of abstraction as you need
[03:40] another super super important part about
[03:42] this architecture is that it's very easy
[03:45] to test let me show you exactly what I
[03:47] mean in a previous video we worked on
[03:49] pocket pick this is an mCP server built
[03:52] to help you store and retrieve
[03:54] information quickly if I run uh asza
[03:57] tree get ignore on the Source directory

### Minute 4

[04:00] you can see a clean atomic structure
[04:03] here if we just isolate on modules we
[04:06] have a single layer of abstraction right
[04:08] we have one composable layer modules and
[04:11] to be super super clear our modules are
[04:14] just our atoms okay and then we only
[04:16] have one higher level we have the server
[04:19] right our mCP server that then consumes
[04:22] our modules okay so we just have one
[04:24] level of atomic units inside of our
[04:26] modules you can divide these up into
[04:28] additional director if you want but the
[04:30] key here is that these are all atoms
[04:33] right these are all small pieces that
[04:35] make big pieces okay and in this case we
[04:38] only have one big piece that's our mCP
[04:40] server I'll link the video where we
[04:42] build this in a single prompt with claw
[04:45] code in the description that video
[04:47] absolutely popped off what we get here
[04:50] is a clean architecture for writing
[04:52] tests right and this is probably the
[04:55] biggest advantage of the atomic
[04:57] architecture you can build fine grain

### Minute 5

[05:00] functionality and then isolate them in
[05:02] tests right so we can quickly just run
[05:05] you know UV run P test and we can see
[05:07] all of our functionality validated 38
[05:10] tests ran this is a well tested you know
[05:13] well oiled compact code base thanks to
[05:16] the atomic structure and thanks to the
[05:18] small pieces you know if you're in your
[05:20] AI coding tools you can quickly come in
[05:22] here add the context and just start
[05:24] working all right so that's the atomic
[05:26] composable architecture it's a very
[05:28] simple pattern for AI tools to
[05:30] it also scales well because you can just
[05:31] keep adding atoms molecules and
[05:33] organisms what are the cons everything
[05:35] we do as engineers and Builders has
[05:39] trade-offs what are the cons of the
[05:40] atomic structure this suffers from
[05:42] something I call the new feature
[05:44] modification chain problem so what does
[05:46] that mean it's a bunch of words gobbled
[05:48] together it basically means when you're
[05:51] modifying an organism or you're adding a
[05:53] new organism or you know a new higher
[05:55] level composition and you want to change
[05:57] something in the lower level you now now
[05:59] need to go back and change everything

### Minute 6

[06:02] that's using the lower level atom right
[06:05] and this can be really really annoying
[06:07] as you start building up more and more
[06:08] molecules and organisms and if you have
[06:11] even higher levels of abstraction like
[06:13] membranes or ecosystems this can be
[06:15] really really annoying to work with
[06:18] right because now I want to make it one
[06:20] change to insert now I need to back test
[06:23] everything else right every higher level
[06:25] composition so you know this is the main
[06:27] con right in addition to that it
[06:29] requires discipline to maintain your
[06:32] proper composable chain an annoying
[06:35] thing for your AI coding tools is that
[06:37] like I mentioned if you need to make one
[06:39] change to insert or even one change to
[06:42] you know a molecule you then need to
[06:44] update everything that uses it right so
[06:47] every higher level layer must be updated
[06:51] and that means that your AI coding tools
[06:53] will need to have even more context in
[06:56] its context window okay so this is the
[06:58] atomic composable architecture as you

### Minute 7

[07:00] can see here there are pros and cons to
[07:03] the structure let's move on the layered
[07:05] architecture is the most popular widely
[07:08] known widely established pattern okay
[07:12] you basically just have arbitrary layers
[07:14] right arbitrary directories and they are
[07:17] a logical collection of files so you
[07:20] know typical one might be interface
[07:21] layer um you know your API endpoints
[07:24] your data models your business logic and
[07:27] then like utilities right there a very
[07:29] kind of typical structure um we can you
[07:31] know just quickly open up literally any
[07:34] code base and you can find that right if
[07:36] we look at the postgress code base you
[07:38] hit Source you can see this architecture
[07:41] uh everywhere right it's it's just the
[07:43] simplest architecture it's Dynamic it
[07:45] allows you to scale really well you can
[07:47] see we have a bunch of folders that
[07:49] contain specific functionality right we
[07:51] can see the same thing in the reddis
[07:53] code base redus is interesting because
[07:55] it is a relatively flat architecture
[07:57] with a bunch of header and C files but

### Minute 8

[08:00] nonetheless this is a classic layered
[08:02] architecture just to Breeze through this
[08:04] one uh there's a clear separation of
[08:06] concerns it's easy to understand the
[08:08] responsibilities and boundaries of every
[08:10] directory uh cons here is uh basically
[08:15] you you have to import across these
[08:18] layers your AI coding tools must operate
[08:20] across API modules Services utils right
[08:24] they have to operate across everything
[08:27] this is the tradeoff that you make when
[08:28] you build when you use this architecture
[08:30] right and it's important to note that
[08:32] this is likely the most popular
[08:34] architecture right the most popular
[08:35] architecture is us having to import a
[08:38] bunch of stuff into the context window
[08:40] so I think this is a really important
[08:42] thing to keep an eye on is the layered
[08:44] architecture the best for AI coding
[08:46] tools I doubt that so that's a lay
[08:48] architecture you know the pros here is
[08:50] that you can really operate quickly and
[08:53] add new functionality right if you think
[08:55] about what this architecture means in
[08:57] terms of how businesses oper operate and

### Minute 9

[09:00] how Dev shops operate you really want to
[09:02] be able to add and modify things quickly
[09:04] right that's kind of the core here and
[09:07] usually you know there is some type of
[09:09] layered um Atomic architecture embedded
[09:12] inside of the layered architecture for
[09:14] instance your utils is usually the
[09:16] bottom level right your utils are if we
[09:19] back up here your atoms right that's
[09:22] kind of where it all breaks down though
[09:23] right because after that you could have
[09:25] Imports cutting across all types of of
[09:29] modules right and it's it's not clear
[09:31] you know looking at a code base like for
[09:33] instance if we you know hop back to the
[09:36] um postgress database and when we click
[09:38] Source it's not clear at all who's
[09:40] importing who and what the rules are
[09:43] there right this is the layered
[09:45] architecture super popular I'm not
[09:47] saying this architecture is bad it's
[09:48] here for a reason um it allows us to
[09:50] scale and move and build without
[09:52] thinking too much right you need a new
[09:54] API jump into the API layer you need a
[09:57] new model jump into the models Direct so
[09:59] on and so forth right again the biggest

### Minute 10

[10:01] con here is that your AI really has to
[10:04] look across every one of these
[10:05] directories right Cloud code cursor
[10:08] agent mode you have to look across all
[10:10] of these files and of course that's
[10:12] going to chew up tokens so let's move on
[10:15] to a super exciting architecture I've
[10:17] talked to several principal AI coding
[10:19] members about the vertical slice
[10:21] architecture it's come up over and over
[10:23] and over you know to give it away I
[10:25] think the vertical slice architecture is
[10:27] the optimal architecture for AI coding
[10:30] tools and for agentic coding tools let
[10:32] me explain why let's just take a look at
[10:34] this okay you're going to get it right
[10:36] away it's very very simple to understand
[10:40] why this could be optimal for AI coding
[10:42] tools everything is a slice okay we have
[10:46] a features directory that contains a
[10:49] directories which contain all of the
[10:52] functionality for a specific feature
[10:54] inside your product inside your
[10:56] application so we have the users feature
[10:59] slice and it contains API model service

### Minute 11

[11:03] we have the images feature and it
[11:05] contains you know API model and FFM Peg
[11:08] just to kind of make it clear you don't
[11:10] need the same file structure although
[11:11] this will definitely help your AI coding
[11:13] tools if you have you know similar api.
[11:16] py across all your features and then we
[11:18] have the messaging feature at the bottom
[11:20] right so you can see here how this can
[11:21] be super super clean Super concise for a
[11:25] coding tools okay all you do is import
[11:29] this entire directory you context Prime
[11:32] with this single directory and We're Off
[11:35] to the Races right you can even do a
[11:37] couple features if you're working on two
[11:39] features at once right so I hope you can
[11:40] see why this is a very very interesting
[11:44] codebase architecture to pay attention
[11:45] to Pros um things are organized by
[11:49] feature rather than some arbitrary
[11:51] technical layer okay and and you know
[11:53] the arbitrary layer is some logical
[11:55] layer right it's there for a reason but
[11:57] by organizing into a feature Fe it's a
[11:59] lot easier to collect everything you

### Minute 12

[12:01] need into a collection of context a
[12:04] beautiful thing you can do here this is
[12:06] all one prompt context priming so when
[12:09] you're sending up your AI coding tools
[12:11] it's just a single shot to get this
[12:12] working okay and I can show this off
[12:14] here uh very very quickly if we open up
[12:17] cursor and let's go into uh the single
[12:20] file agents code base I have this new
[12:22] directory here codebase architectures if
[12:25] we open up a terminal CD into this
[12:27] codebase architecture vertical slice so
[12:30] you know this is what vertical slice
[12:31] looks like we have our features and then
[12:33] we have you know projects tasks users if
[12:35] we do AER D- noit and if we just do
[12:38] slash add features slash users slash we
[12:44] just set up all the code based context
[12:46] we need right and this is it we're done
[12:49] so you know ask uh what does this do and
[12:54] you know We're Off to the Races our AI
[12:55] coding assistant is primed it's good to
[12:58] go right
[12:59] um we can do the exact same thing if we

### Minute 13

[13:01] want to boot up Cloud code we can CD
[13:04] codebase architectures vertical open up
[13:07] Claud and then we can do our classic
[13:09] context priming read and then same thing
[13:12] right features tasks slst star that
[13:14] means everything and now you're going to
[13:16] see Claude read just these files and
[13:20] there it is we got that nice new
[13:22] parallel subtask read it read all those
[13:25] in parallel four tools love to see that
[13:27] and you know now we're good to go okay
[13:30] we saved a crap ton of tokens we saved a
[13:32] crap ton of time we have a simple
[13:35] context priming prompt you know of
[13:37] course we' probably want to throw in the
[13:38] read me in there right and and read me
[13:42] like this but we're good to go here
[13:44] right and you know something important I
[13:45] want to call out is that the tool only
[13:48] matters so much right it's about the
[13:50] patterns it's about the techniques it's
[13:52] about you
[13:53] know not not not to sound too gimmicky
[13:56] but it's about principled AI coding okay
[13:58] these principles and patterns that you

### Minute 14

[14:00] know we discuss on the channel and
[14:02] inside the principal AI coding course
[14:04] they allow you to operate on any tool
[14:07] any model any codebase over time and I
[14:10] want you to win just today I want you to
[14:12] win tomorrow and the day after we can
[14:14] open up another tool okay let's open up
[14:17] uh agent mode in cursor and we're just
[14:19] going to say read this okay uh /ar fire
[14:23] that off and look at that four files
[14:25] right there it's reading all of them
[14:27] cursor agent also picking up on the read
[14:29] there's a model file there's a service
[14:31] file there's the app.py file you can see
[14:33] the read tools and that's it right it's
[14:37] ready to go okay we can Now operate on
[14:39] this feature doesn't matter what tool
[14:41] you're using it only matters that it has
[14:44] these capabilities right we've context
[14:46] primed cursor agent mode Cloud code and
[14:50] AER all of these a coding tools are now
[14:53] good to go they're ready for you to
[14:55] build and operate with that specific
[14:58] chunk of of context right with that

### Minute 15

[15:00] vertical slice of context okay so this
[15:04] is why vertical slice architecture is so
[15:06] important we get one prompt context
[15:08] priming or one/ add command moving on
[15:11] here with the pros it minimizes cross
[15:13] cutting concern as the gears R turning
[15:15] in your mind um you know any engineer
[15:17] that's worked with this code based
[15:19] architecture or you know maybe you're
[15:20] just thinking through the trade-offs of
[15:22] this the fact that it minimizes
[15:23] crosscutting concerns is also a massive
[15:26] massive downside Okay so uh you know we
[15:29] also have feature Centric value Centric
[15:32] structure right which is fantastic you
[15:34] always want to be thinking from the
[15:35] perspective of your users of your
[15:37] customers not of your code base right a
[15:41] lot of good Pros here we of course you
[15:43] know can't get too high on our own
[15:45] Supply we're software Engineers we have
[15:47] to have balance takes what are the cons
[15:50] here this uh structure has terrible
[15:53] terrible code duplication a reason for
[15:56] that is because what you don't want to
[15:58] do is build out the util SL shared right

### Minute 16

[16:01] you don't want that utilities folder
[16:03] where you share functionality you
[16:05] actually want to to not do that sharing
[16:07] cross cutting code here is a massive
[16:10] mistake it's a blunder it's an
[16:12] anti-pattern when you're using the
[16:13] vertical slice architecture why is that
[16:17] it's because you want all of the
[16:19] functionality isolated right as soon as
[16:21] you start building out that utils you're
[16:24] going to have it across multiple
[16:25] features and now all of a sudden your
[16:27] utils files is going to grow gr larger
[16:29] and larger and then when you update a
[16:31] util function you need to update it
[16:33] across multiple features and now you're
[16:35] losing that vertical slice architecture
[16:38] right literally defeats the point of
[16:39] this architecture for these reasons
[16:41] these are all roughly the same thing
[16:43] they you know kind of all talking about
[16:44] the same side effect code reuse here is
[16:46] terrible I would say probably newer and
[16:48] mid-level Engineers are going to have a
[16:50] really hard time with this architecture
[16:52] because you will duplicate code you're
[16:54] going to have that same API code here
[16:56] here and here you're going to have
[16:58] similar similar model scaffolding over

### Minute 17

[17:00] and over and over so this is great uh
[17:03] but as you can see you know once again
[17:05] tradeoffs are everywhere vertical siiz
[17:07] architecture is something I'm going to
[17:09] be playing with a lot more this idea of
[17:12] isolating everything in a single context
[17:16] package and a single chunk is very very
[17:19] very powerful for AI coding tools moving
[17:23] on Pipeline architecture so we have to
[17:25] give a shout out to the pipeline
[17:27] architecture you know functional
[17:29] programmers the true
[17:31] programmers they love this architecture
[17:33] right um I don't think this is super uh
[17:36] powerful or important for AI coding
[17:38] tools but nonetheless it's not a bad
[17:41] architecture so I want to cover this one
[17:42] because it's important for any data
[17:44] engineer you know working on data
[17:46] pipelines any ml Ops Engineers you know
[17:49] this is a very very common architecture
[17:51] you have your pipeline you have shared
[17:53] utilities and then you have steps right
[17:55] and your steps are composed into your
[17:57] pipelines and then you run your
[17:59] pipelines right anyone fine-tuning

### Minute 18

[18:01] training or building llms from ground up
[18:04] they have some type of pipeline like
[18:06] architecture so you know Pros uh great
[18:09] for sequential processing llms love
[18:12] types and clear paths right they love
[18:14] patterns so this is a great architecture
[18:17] for communicating your steps and your
[18:18] stages will always link together the
[18:21] appropriate types and data structures
[18:23] and or save them to that you know third
[18:26] party database structure and of course
[18:28] language model AI coding tools they love
[18:30] that they love the patterns they love
[18:31] the types it makes it easy for them to
[18:33] see and understand what they should do
[18:35] where they should do it it's easy to you
[18:37] know play with these steps you can
[18:39] reorder these very quickly parallel
[18:41] processing is a massive Pro for pipeline
[18:43] architectures so cons not ideal for
[18:46] basically anything else that's not
[18:48] pipeline driven uh and I'm just going to
[18:50] kind of Breeze through these other ones
[18:52] the big problem here is that it's
[18:53] nonsensical for most codebase structures
[18:55] not you know very few of us probably
[18:58] less than 10% Engineers are building out

### Minute 19

[19:00] any type of pipeline architecture and
[19:01] then you know State Management can be
[19:03] challenging so these are just four you
[19:05] know there are many other architectures
[19:07] but I think these are the four most
[19:08] important most common structures to hit
[19:10] on for thinking about Building
[19:12] architecture for AI systems okay so for
[19:14] AI coding we looked at the atomic
[19:16] composable we looked at layered pipeline
[19:19] we looked at vertical slice okay these
[19:20] are all great options I am heavily
[19:23] leaning toward vertical and atomic for
[19:26] building out code bases that are
[19:27] optimized for AI coding there are of
[19:30] course as we mentioned tradeoffs in each
[19:33] one of these architectures as we turn
[19:35] our attention to AI agents um you know
[19:38] it is an interesting question and it's a
[19:41] question that a lot of us are asking
[19:42] more uh what about the optimal
[19:44] architecture for building AI agents
[19:47] three codebase structures stand out to
[19:48] me Atomic composable vertical slice and
[19:52] single file agents we covered single
[19:55] file agents on the channel what I want
[19:57] to do here is briefly walk through why I

### Minute 20

[20:00] think these three structures are great
[20:03] if you're thinking about building out um
[20:06] AI agents and it doesn't matter if you
[20:07] want to throw a framework on top of
[20:09] these if you're using mCP if you like
[20:11] anthropic agents or openi agents or
[20:13] Gemini agents that doesn't matter this
[20:16] is all just structural these structures
[20:18] work with every provider okay so let me
[20:21] just highlight a couple things here if
[20:23] we hop into the single file agents code
[20:25] base and look at example agent
[20:27] architecture let me show you what an
[20:29] agent architecture could look like for
[20:31] the atomic composable architecture you
[20:33] can see that similar structure I'm using
[20:35] the names you know as defined in the
[20:39] atomic structure we have atoms molecules
[20:41] organisms and then membranes so let's
[20:43] start from the top so the membrane is
[20:45] your main file right and so you know
[20:48] this is what we'll use to actually kick
[20:50] off this agent it has a main down here
[20:54] so you know we can pass in args this is
[20:56] also where if you wanted to you would
[20:58] build out you know um mCP right so you

### Minute 21

[21:01] could do something like this mCP agent
[21:03] and now you have a command line
[21:05] interface and an mCP interface okay so
[21:09] the membrane is quite literally you know
[21:10] the API layer okay it defines all the
[21:14] ways you can interact with the system
[21:17] right with your Atomic system and then
[21:19] you know moving into the the actual you
[21:22] know content um we have the organism
[21:25] right and the organism here using our
[21:28] file agent example is our file agent
[21:31] right so the file agent then composes
[21:33] whatever it needs to from the molecules
[21:36] it would compose the file reader file
[21:38] writer and then those files would
[21:42] compose the file tools right so you can
[21:46] see how this works top to bottom right
[21:48] the membrane is our access layer the
[21:50] organism is our actual file agent the
[21:53] molecule is the components that make up
[21:56] the file agent and then lastly that
[21:58] atoms are the like lowest level units

### Minute 22

[22:01] that we can test we can run on their own
[22:04] you can see the insert file here it's
[22:06] just a function right it's a single
[22:07] function isolated easily testable easily
[22:10] composable okay so this is what an AI
[22:13] agent design could look like inside of
[22:15] the atomic structure this directory by
[22:17] the way is not runnable don't try to hop
[22:18] in here and run this I am exploring the
[22:20] space here we're just looking at
[22:22] different potential architectures so
[22:24] that's the atomic structure for AI
[22:26] agents I think another great option is
[22:28] going to be the vertical slice
[22:30] architecture for the same reasons we
[22:32] mentioned right you can imagine you have
[22:35] um your features or slice into agents
[22:38] okay so you know if we hop back to the
[22:41] vertical slice architecture instead of
[22:44] you know features here for a typical
[22:47] product application when you're building
[22:49] out agents you can look at agents as the
[22:52] individual features right and this is
[22:54] really fantastic because everything
[22:56] under your agent is all the contexts you
[22:58] need need to get started we can open up

### Minute 23

[23:00] AER and then also go into vertical and
[23:03] then we can boot up AER D- no get/ add
[23:06] features SL blog agent and you can see
[23:08] that exact same pattern our agent is now
[23:11] good to go there's nothing else we need
[23:14] to do here it has all the tools it needs
[23:16] to operate the blog agent it has all the
[23:18] context has the you know the manager
[23:21] every tool and it has that top level
[23:23] blog agent okay so this is why vertical
[23:25] slice is really important I think it's
[23:27] going to be great for build AI agents
[23:29] because you can version them very
[23:31] quickly right say I want to create
[23:32] another version of the blog agent I can
[23:34] just copy this entire
[23:36] thing and you know update to whatever
[23:39] blog agent V2 just like below right we
[23:41] have file agent file agent V2 and then
[23:44] maybe you want to change the llm
[23:45] provider you know you can doore Gemini
[23:47] whatever you want to do here right so
[23:49] when we're thinking about building
[23:51] agents and architectures for agents uh
[23:54] the vertical slice architecture
[23:55] definitely stands out to me and so the
[23:58] last architecture single file agents

### Minute 24

[24:00] this is something that we've explored in
[24:01] previous video I also think this is a
[24:03] massive Contender if we scroll down here
[24:06] you know in the single file agents
[24:08] codebase you can see that exactly right
[24:10] we have tons of single file agents if we
[24:14] click into one of these where's the
[24:16] latest one there it is file editor Sony
[24:18] 37 you know if we click into this we
[24:21] have everything in a single file right
[24:22] 700 lines in other code bases a 700 line
[24:25] file is an anti- pattern okay but in
[24:28] this structure right in the single file
[24:30] agents codebase architecture this is
[24:33] just a completely self-contained one
[24:36] file context agent you can imagine the
[24:39] pros of this right uh it's it's as
[24:42] simple as this right you you know hop up
[24:45] to the top directory you file reference
[24:48] and then you open up CLA you say read
[24:51] this right and and you don't even have
[24:53] to do this right you can just start
[24:55] prompting right open up Claud and you
[24:57] just you know you start prompting change
[24:59] the blah blah to the ble B okay whatever

### Minute 25

[25:03] you want to do here this is an important
[25:05] architecture for building agents um I'm
[25:07] going to keep leaning on single file
[25:09] agents the fact that you have one file
[25:13] to allow your AI coding assistant to
[25:15] quickly update your agent I think is a
[25:18] you know massive win and just to
[25:21] explicitly mention it these are the two
[25:23] big themes we're focus on on the channel
[25:25] AI coding agentic coding and of course
[25:28] AI agent so you know here are optimal
[25:31] architectures you can use for building
[25:32] AI agents if you haven't checked out the
[25:35] single file agents codebase definitely
[25:37] check it out link is going to be in the
[25:38] description for you it's all about
[25:40] understanding agent architecture it's
[25:43] all about understanding code bases to do
[25:45] and to build with our new generative AI
[25:48] technology AI coding tools and AI agents
[25:51] so full circle does this matter at all
[25:55] right cool we looked at a bunch of
[25:57] architectures we you know we we we can
[25:59] see the advantage of them uh does it

### Minute 26

[26:02] really matter uh I have kind of two
[26:04] answers here right now in the short and
[26:06] medium term yes I think absolutely good
[26:10] code based architecture means easier
[26:12] context management for us and our AI
[26:15] tools later and the more time that goes
[26:17] on I think you can more easily argue
[26:20] that as llms and geni evolves the
[26:23] codebase structure that you're working
[26:24] with matters a lot less but you know I
[26:27] think you can see here from just these
[26:29] few simple examples on you know small
[26:32] and you know really full on code bases
[26:35] um context management matters if you
[26:38] manage your context you manage your
[26:41] results so you know precise context
[26:44] management still matters AI needs clear
[26:47] Pathways right llms to be specific or
[26:49] llms or AI coding tools they need clear
[26:52] Pathways to you know not just one file
[26:55] but collections of files right colle C
[26:58] of information we all know you know clog

### Minute 27

[27:00] code Klein a lot of these tools they
[27:03] chew up tokens and they chew them up
[27:07] just looking for stuff right they're not
[27:09] even doing work they're not even
[27:11] creating value and it's the poor
[27:14] organization of our code base right not
[27:16] to just harp on it but you know the
[27:19] layered architecture really forces our a
[27:22] coding tools to just read everything
[27:24] right look through all of it it's we
[27:26] know we're looking for an API file
[27:27] somewhere
[27:28] let's look through one of these 20 files
[27:31] in our API right um you know this is
[27:34] where the atomic structure and you know
[27:37] most notably the vertical slice
[27:40] structure the vertical slice
[27:41] architecture really stand out if you can
[27:44] build this codebase structure you will
[27:47] save a ton of tokens right and I think
[27:50] you can see why you know that's
[27:51] important when you organize your code
[27:52] base you make it easy to save time
[27:54] tokens and that means money right well
[27:57] structured code is cost effective okay

### Minute 28

[28:00] the balance is really key here so you
[28:01] know most of us are still operating
[28:03] we're building for human readability um
[28:06] it's time to flip that Trend okay I am
[28:08] flipping that Trend I want you to join
[28:10] me I want you to get ahead of the curve
[28:12] AI will be writing most code moving
[28:14] forward right our AI tools AI coding
[28:17] assistants agentic coding tools they'll
[28:19] be writing most of code that means we
[28:20] need to start thinking about our code
[28:23] bases from their perspective how can we
[28:25] best organize things to be simple to
[28:28] both manage context but also just to
[28:30] hand off the entire process to our AI
[28:33] tooling right this is why AI readability
[28:35] is now greater than or equal to human
[28:38] readability the goal here is to help
[28:41] both engineers and your AI tools to
[28:44] navigate your code bases efficiently and
[28:47] effectively I have an announcement for
[28:48] all principled AI coding members I'm
[28:51] going to be releasing a state of AI
[28:54] coding essay at the end of March this is
[28:57] going to help you understand the current

### Minute 29

[29:00] landscape of AI coding and agentic
[29:02] coding I'm going to share the tools I'm
[29:05] adding I'm going to share the tools I'm
[29:07] removing we're going to discuss what's
[29:09] next we're going to break down the tier
[29:11] list of where you should be as an
[29:14] engineer and where you can be as an
[29:17] engineer I'm going to break it all down
[29:19] into one comprehensive document one
[29:21] comprehensive essay this will give you
[29:23] an inside perspective on AI coding
[29:26] agenta coding and the big trends I'm
[29:29] seeing that I'm preparing for that I'm
[29:31] betting on with my money and time I'm
[29:33] going to share all those ideas and more
[29:35] with you in the state of AI coding for
[29:38] q1 2025 that's going to be exclusive for
[29:42] principled AI coding members that have
[29:43] completed the course if you're not
[29:46] already a part of principled AI coding I
[29:49] highly recommend you check out this
[29:51] course especially if you made it this
[29:52] far into the video you clearly have some
[29:54] chops you're clearly an engineer that's
[29:57] interested in great design and great
[29:59] architecture do not miss out on the AI

### Minute 30

[30:03] coding train we're quickly moving from
[30:06] AI coding to agentic coding which is the
[30:08] next level of AI coding this is the new
[30:12] standard if you haven't caught on this
[30:13] already this is the way code is being
[30:17] written most code as we discussed will
[30:19] be written by AI coding tools 2025 is
[30:23] the last year to get on this train
[30:27] before you deprecate your career before
[30:29] you deprecate your engineering abilities
[30:31] over eight lessons we break down core
[30:34] principles like the big three right
[30:37] context model prompt that's going to
[30:40] help you win in the generative AI age as
[30:43] an engineer okay we go from beginner to
[30:45] intermediate to Advanced um we have
[30:48] great reviews from real Engineers
[30:50] operating in the space hop in here check
[30:53] this out link is going to be in the
[30:55] description for you for all my existing
[30:57] principal AI Co members stay tuned for

### Minute 31

[31:00] the state of AI coding breakdown coming
[31:04] at the end of March I'm packing a ton of
[31:07] value into this is going to help you
[31:09] make decisions and stay ahead of the
[31:11] generative AI wave you know were to find
[31:14] me every single Monday like comment
[31:18] subscribe and I'll see you in the next
[31:20] one stay focused and keep building