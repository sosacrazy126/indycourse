# YouTube Video Transcript

## Metadata

- **Title:** Unknown Title
- **Author:** Unknown Author
- **Channel URL:** N/A
- **Video URL:** https://www.youtube.com/watch?v=pytSbBRoFw8
- **Duration:** 19:10
- **Views:** N/A
- **Published:** N/A
- **Word Count:** 3303
- **Transcript Generated:** 2025-03-30 23:48:54

## Transcript


### Minute 0

[00:00] what's up Engineers welcome back Indy
[00:02] Dev Dan here the generative AI ecosystem
[00:05] continues to move at a light speed Pace
[00:08] although the releases haven't been that
[00:11] exciting open AI has continued to
[00:13] release every single day I'm really
[00:15] excited for them to round out with a
[00:17] huge final model hopefully a gbt 5 some
[00:20] type of Next Generation model at the end
[00:22] of the week my favorite Announcement by
[00:24] far has been the 01 and chat gbt Pro I'm
[00:27] looking forward to having the 01 model
[00:30] available in the API alongside open AI
[00:33] there's been a massive release by
[00:35] Microsoft the 54 14 billion parameter
[00:38] model is absolutely groundbreaking this
[00:40] thing is performing at GPT 40 plus
[00:43] levels and it's Ultra Ultra tiny we're
[00:46] going to look at this model side by side
[00:48] Gemini 2 another Fantastic Model I'm
[00:52] really excited for this model to fully
[00:54] roll out so that we can get access to
[00:56] every single input and output format
[00:58] available last but not least we have

### Minute 1

[01:00] llama 3.3 this model has been great to
[01:03] work with another model on the level of
[01:06] GPT 40 with all of these releases I
[01:08] thought it would be a good time to take
[01:10] a step back and share my large language
[01:13] model use case framework I've been using
[01:15] this framework to move quickly in
[01:18] degenerative AI age and filter through
[01:20] all of these new model releases and all
[01:22] of these new tool releases I want to
[01:25] share it with you here to help you break
[01:26] down the types of prompts you're writing
[01:28] and the AI tooling that complements the
[01:31] generative AI work that you're doing
[01:33] we're going to walk through examples
[01:34] using Gemini flash llama 3.3 and the new
[01:40] 54 so what does this framework look like
[01:43] this framework is a simple mental model
[01:45] that I use for categorizing large
[01:47] language model use cases so what are
[01:49] these use cases and how do they help you
[01:52] and the generative AI age let's break
[01:54] them down we have expansion compression
[01:57] conversion Seeker action and reasoning

### Minute 2

[02:02] just by seeing these categories alone
[02:04] I'm sure the wheels are starting to turn
[02:06] in your mind so let's break down these
[02:07] categories one by one expansion prompts
[02:10] are what you use to generate content
[02:12] learn new things get explanations and
[02:15] generate new ideas this is one of the
[02:18] most common categories of prompts
[02:21] compression prompts are the opposite of
[02:23] expansion prompts instead of writing a
[02:25] little bit of content and getting a lot
[02:27] of output compression prompts take
[02:29] information they take blog posts
[02:31] research large swads of information and
[02:34] they dtill it down for you the most
[02:36] common use case here is of course
[02:38] summarization conversion prompts change
[02:41] the format of information from one
[02:43] format to another you can think text to
[02:46] SQL you can think typescript to python
[02:49] you can think French to German
[02:51] conversion prompts take information in
[02:53] one format and convert it to another the
[02:56] core information is still there but
[02:58] these prompts transfer that information
[02:59] information between different formats we

### Minute 3

[03:02] have Seeker prompts Seeker prompts are
[03:04] used to find information this is what
[03:07] gets run at the end of your rag pipeline
[03:10] we then have action prompts these are of
[03:12] course our tool calling prompts that
[03:14] execute commands that have concrete side
[03:16] effects and then of course last but not
[03:18] least we have reasoning prompts these
[03:20] provide judgments conclusions insights
[03:22] and ultimately they help Drive action
[03:25] they help Drive decision- making so
[03:27] let's explore each category in a little
[03:28] bit of detail and run a couple prompts
[03:30] to kind of show off how each category is
[03:33] different so that you can easily
[03:34] categorize your work your prompts and
[03:37] the tooling you need to support each one
[03:39] of these types of prompts okay so before
[03:41] we move on let's talk about who cares
[03:44] why is this framework important why you
[03:45] need to categorize at all can we just
[03:47] write random prompts organizing
[03:49] generative AI work into categories will
[03:51] help you speed up and simplify your gen
[03:54] AI work how will they do that mental
[03:56] Frameworks create better and faster
[03:58] decision-making one type of prompt only

### Minute 4

[04:00] needs certain tooling only needs certain
[04:03] syntax only needs certain prompt
[04:05] structures it also simplifies your
[04:07] prompt engineering by classifying
[04:09] generative AI problems into one of these
[04:11] six categories you simplify the process
[04:14] of writing prompts and selecting the
[04:15] right AI tooling you also find that
[04:17] these categories are a great way to
[04:19] create reusable benchmarks for the
[04:21] problems that you're solving the way
[04:23] you'll Benchmark a expansion prompt is
[04:26] much different from the way you'll
[04:27] Benchmark a Seeker prompt okay and then
[04:30] last but not least this framework is
[04:32] really fantastic for guiding agentic
[04:34] design when I'm thinking about building
[04:36] agents and agentic workflows the chain
[04:38] of the prompt categories can help guide
[04:41] and simplify the shape and structure of
[04:44] your AI agent as we're pushing toward
[04:46] the north star of this channel which is
[04:48] to build living software that works for
[04:51] us while we sleep we need to be putting
[04:53] together these larger AI agents and
[04:55] agentic workflows with chains of prompts
[04:59] and work flows of these prompt

### Minute 5

[05:01] categories and having concrete
[05:03] categories makes it easier to design and
[05:05] build the structure of your AI agents if
[05:07] the ideas interest you and you want to
[05:09] accelerate your generative AI
[05:10] engineering with this simple framework
[05:13] let's go ahead and dive into this hit
[05:14] the like hit the sub join the journey
[05:16] prompt engineering AI coding AI agents
[05:19] this is the bread and butter of this
[05:20] channel this is all we're focused on
[05:23] this is the most important technology
[05:24] this is the best tool for most
[05:28] jobs so let's start with the expansion
[05:30] prompt so this is where you're taking
[05:32] small inputs and converting them into
[05:34] large outputs you're literally expanding
[05:36] your input text into something larger
[05:39] the obvious Ed cases here are content
[05:40] generation explanation learning ideation
[05:43] storywriting code gen documentation so
[05:46] here's an example prompt we have the
[05:47] Gemini 2.0 flash model here llama 3.3
[05:50] and of course the new 54 here's a simple
[05:53] prompt right write the intro to a blog
[05:55] post about Ai and its impact on software
[05:58] if we just click you 2.0 here Gemini is

### Minute 6

[06:01] going to take this prompt and generate a
[06:03] response for it so you can see here it's
[06:05] generating a couple options for us we're
[06:07] taking a little bit of information right
[06:09] a query a question a request and it's
[06:12] being expanded out into something larger
[06:15] right so this is say an entire category
[06:17] an entire class of prompts that you
[06:20] likely have and will write so you can
[06:22] see here we're getting a couple
[06:23] different options from Gemini that's
[06:24] cool let's run llama 3.3 that ran really
[06:28] quickly I'm using fireworks as LL 3.3
[06:30] provider this is a great 70 billion
[06:32] parameter model you can see we got a
[06:34] nice response here we got a title and a
[06:36] nice block of content and then of course
[06:39] we can run 54 54 is running locally on
[06:42] my device I love that this is running on
[06:44] my device has incredible intelligence
[06:47] for a 14 billion parameter model but you
[06:49] can see we have a really nice response
[06:50] here from fi this is a proper expansion
[06:53] prompt you have a little bit of
[06:55] information you have a query and you
[06:57] want to blow it out into something
[06:58] larger these are one of the most common

### Minute 7

[07:01] categories of prompts next we have
[07:03] compression prompts so compression
[07:05] prompts are the opposite of expansion
[07:08] prompts this is where you're taking
[07:09] large inputs and compressing it down
[07:12] into small outputs you're distilling
[07:14] you're summarizing you're Gathering key
[07:16] points you're extracting key information
[07:19] You're Building summaries for meetings
[07:21] let's look at a simple prompt here this
[07:23] is information from the Gemini 2.0 Flash
[07:26] release and we can of course use Gemini
[07:28] 2.0 Flash to summarize its release this
[07:31] model is insanely fast I'm really
[07:33] excited for everything that's being
[07:35] announced around the Gemini 2.0 series
[07:38] the multimodal input and output is
[07:40] making this model truly unique you can
[07:42] see there we compressed the information
[07:45] inside of this prompt to get a concise
[07:48] result we can also use llama 3.3 here to
[07:51] execute our compression prompt and of
[07:52] course 54 14 billion parameters it can
[07:55] definitely do this job you can see there
[07:57] we also have three bullet points from 54

### Minute 8

[08:00] so compression prompts are a great way
[08:02] to condense information right I use this
[08:04] one all the time there's so much
[08:06] information out there compression
[08:07] prompts allow us to learn faster they
[08:10] allow us to compress information and
[08:13] these are essential for compressing
[08:15] large amounts of information for AI
[08:17] agents and for agentic workflows so
[08:20] moving on we have conversion prompts so
[08:22] this is where we take an input format
[08:24] and we want the response to be in a
[08:26] different format so you can think you
[08:28] know text to code text to SQL language
[08:31] translation format conversion you know
[08:34] Json to XML uh style conversions this is
[08:38] a really powerful category for prompts
[08:42] you can see how they're distinct from
[08:44] compression and you can see how they're
[08:46] distinct from expansion so here's a
[08:49] classic scenario where we have an SQL
[08:52] table and we want to convert a natural
[08:54] language query into an SQL statement we
[08:56] can pass this to any model and it's
[08:58] going to give us a really nice concise

### Minute 9

[09:00] result here right we want to show all
[09:02] customers and their total spending in
[09:04] the last s days we pass in the table as
[09:07] a variable for the prompt and then of
[09:09] course uh you know llama flash fi um
[09:14] this is a very very solved problem for
[09:16] language models language models are
[09:18] great at converting formats because they
[09:21] know and have internalized the language
[09:23] of many many formats these are
[09:26] conversion prompts let's move on Seeker
[09:28] prompts are very very valuable many
[09:31] businesses are built around the secret
[09:34] prompt this is where we're querying
[09:36] information and we're extracting data
[09:39] this slightly overlaps with the
[09:41] compression prompt the big difference
[09:43] here is that we're pulling specific
[09:46] information with the Seeker prompts so
[09:48] you think of things like codebase
[09:50] question answering right you can think
[09:52] of things like support keyway Bots right
[09:55] information extraction document search
[09:57] when you're running OCR or parsing

### Minute 10

[10:00] information out of documents pattern
[10:02] recognition and knowledge retrieval the
[10:05] secret prompt is all about pulling
[10:06] important information for your specific
[10:09] use cases so a prompt will look
[10:11] something like this right this is a
[10:12] really simple example we have this sales
[10:15] report and we want to know what's the
[10:17] best performing product in Q3 right so
[10:19] we're looking for a specific piece of
[10:22] information this differs from
[10:23] compression because we're not taking
[10:25] information and changing the format of
[10:27] it into a smaller form what we're doing
[10:29] is looking for a key piece of
[10:32] information that's embedded inside a
[10:34] document right there's one version of
[10:36] this answer that we're looking for not
[10:38] multiple so you can see here the answer
[10:40] here is product B right we have 95k
[10:43] sales let's go ahead and see if llama
[10:44] 3.3 gets the answer right here perfect
[10:47] 95k sales you can see llama 3.3 working
[10:50] through the answer here and of course 54
[10:53] great model 14 billion parameters once
[10:55] again it's going to get the answer right
[10:57] here product B at the higher sales

### Minute 11

[11:00] figure and that quarter Q3 so these are
[11:02] Seeker prompts right you have
[11:04] information and you want to extract
[11:06] specific data Seer prompts are very
[11:09] valuable and you can see how by looking
[11:11] at the Seeker prompt you would use
[11:13] completely different AI tooling between
[11:15] Seeker prompts versus conversion prompts
[11:18] impression and expansion prompts right
[11:20] so let's move on to our action prompts
[11:23] these are really simple action prompts
[11:25] execute real commands so the most
[11:28] fundamental form of this of course is
[11:30] tool calls most llms have some type of
[11:33] tool calling mechanism we can kind of
[11:35] mock this functionality by writing this
[11:37] prompt generate get commands obviously
[11:39] this is not actually going to execute
[11:41] these commands but you get the idea
[11:43] action prompts have a concrete side
[11:45] effect this is where our prompts and our
[11:47] large language models start acting in
[11:50] the real world these are powerful
[11:52] distinct prompts that really allow llms
[11:55] to take control over things in the real
[11:58] world world and have larger effects

### Minute 12

[12:01] outside of different types of text
[12:03] generation and manipulation okay so we
[12:05] have you know Gemini 2.0 flash here
[12:07] giving us a great answer there 3.3 will
[12:10] spit out effectively the same thing and
[12:12] 54 of course will also do the same thing
[12:15] okay get check out get add get commit
[12:18] get push so these are action prompts you
[12:20] can summarize this category roughly as
[12:22] text to Tool or text to action it
[12:25] doesn't always need to be in the form of
[12:27] a tool call you can manually set that
[12:30] flow up yourself for instance if you
[12:32] execute Json and parse you know function
[12:35] calls or parse functionality that will
[12:37] then get executed by code that's also an
[12:40] action prompt and finally we have the
[12:42] most powerful type of prompt the
[12:45] reasoning prompt these are becoming a
[12:47] lot more popular right now because this
[12:49] is the prompt that is going to make
[12:51] decisions for you right so this is where
[12:53] we're taking complex sets of inputs
[12:55] we're taking State we're taking you know
[12:57] the current kind of application State
[12:59] we're taking variables and we're letting

### Minute 13

[13:01] our language models make judgments give
[13:04] us insights and make fullon decisions
[13:07] based on our complex inputs okay so use
[13:10] cases here are decision- making planning
[13:12] problem solving risk assessment Trend
[13:14] analysis recommendation systems threat
[13:17] analysis these all fit under reasoning
[13:20] prompts so for example we have this
[13:22] prompt where we're looking for an
[13:24] opinion right we're looking for judgment
[13:26] on three different approaches for
[13:28] implementing user authentication in our
[13:31] web app Custom jwt's Classic o and then
[13:34] Firebase off these models are going to
[13:36] inform us they're going to give us
[13:38] insights into a decision that that we
[13:41] might want to make there is some overlap
[13:43] here with expansion prompts but you can
[13:46] see how this is completely distinct
[13:47] because we could use this reasoning
[13:49] prompt to inform a chain of prompts
[13:53] right so we're getting a great long
[13:54] breakdown here from Gemini flash we can
[13:57] run the exact same thing in llama
[13:59] it's giving us a breakdown of you know

### Minute 14

[14:01] when to use each you can see llama 3.3
[14:04] breaking down a nice concise answer for
[14:06] us it's giving us information it's
[14:08] making a judgment call and giving us a
[14:11] recommendation of a best option okay so
[14:14] you can see how this is again completely
[14:16] distinct from the other five categories
[14:18] we're not expanding information here
[14:20] we're not compressing it we're not
[14:22] converting it we're not firing an action
[14:23] we're not seeking any information we're
[14:25] looking for an opinion we're looking for
[14:27] insight we're looking for information to
[14:29] guide a decision right we can run this
[14:31] on 54 as well and we'll get a similar
[14:35] breakdown fantastic so you can see our
[14:37] 54 response came back here you know this
[14:40] gave me the exact same quality of answer
[14:42] and it and this model ran on device
[14:45] really loving this if we changed the
[14:47] inputs gave us some more information
[14:49] about our team or our current Tech stack
[14:52] it very likely would have changed the
[14:54] Judgment Insight or decision that this
[14:56] reasoning prompt would have returned for
[14:58] us the these are the six categories

### Minute 15

[15:01] categorizing your llm use case
[15:03] immediately Narrows Down The Prompt
[15:04] engineering approach and tooling needed
[15:07] if you're writing a Seeker prompt you
[15:09] might need a rag pipeline if you're
[15:10] writing a reasoning prompt you need
[15:13] information to help Drive the decision
[15:16] if you're just doing Simple expansion or
[15:18] compression just paste in the
[15:19] information and then let it expand into
[15:21] more details or compress into the key
[15:23] bullet points or content that you're
[15:25] looking for this is a big takeaway um
[15:27] categorizing has helped me a ton and I
[15:30] think it can help you which is why I'm
[15:31] sharing it with you here today so chain
[15:34] categories to guide AI agents and
[15:36] agentic workflows I think when you're
[15:38] designing agentic workflows and AI
[15:40] agents you can break things down into
[15:42] individual prompts in sequence for
[15:44] instance you might have a Seeker look
[15:46] for specific information based on
[15:48] information from your database then it
[15:51] might reason over that information in
[15:53] your database say you might want to uh
[15:55] pitch an upsell to a specific user in
[15:58] specific scenarios and you want to have

### Minute 16

[16:00] your llm do that you would seek then you
[16:02] might do reasoning and then you would
[16:05] act right then you would actually fire
[16:06] off an action prompt to call a specific
[16:09] tool categorizing llm use cases is a
[16:12] great way to build and design your AI
[16:14] agents and agentic workflows you can
[16:16] reuse tooling for each category each
[16:19] category has a distinct success metric
[16:21] patterns tooling benchmarks prompt
[16:24] structures so on and so forth right this
[16:26] makes it easy to reuse tooling and
[16:29] benchmarks for prompts that fit in the
[16:31] same category okay the power of this llm
[16:34] use case framework lies in its
[16:36] Simplicity every large langage model
[16:38] will likely fit into one or two at most
[16:40] of these categories they each have their
[16:42] own distinct patterns prompt structures
[16:44] success metrics and tooling Associated
[16:48] which will make your gener of AI
[16:49] engineering more systematic and
[16:51] efficient ultimately leading to speed
[16:54] and easier decision- making so just to
[16:56] summarize one more time the six categor
[16:59] for the most common large language

### Minute 17

[17:01] modeled use cases you have expansion
[17:03] compression conversion Seeker action and
[17:07] reasoning right expansion prompts are
[17:10] expanding content expanding text you
[17:13] have compression prompts where you're
[17:14] distilling summarizing pulling key
[17:17] information from a larger body of
[17:20] information you have conversion where
[17:21] you're transferring between formats
[17:23] Seeker prompts where you're looking for
[17:25] specific information inside of a larger
[17:28] body of data we have action prompts
[17:31] where we can execute workflows and
[17:34] commands that themselves can run entire
[17:37] chains of prompts agents and agentic
[17:40] workflows and then of course we have the
[17:41] reasoning prompts reasoning prompts are
[17:44] especially powerful and especially
[17:45] unique they help you actually make
[17:48] decisions and when you put this in an AI
[17:50] agent or an agentic workflow they guide
[17:53] the flow of your tool this is where
[17:56] everything is going tool calling is is
[17:59] still I think super super underutilized

### Minute 18

[18:02] in developer workflows in AI agents in
[18:05] general this is something we're going to
[18:06] be spending a lot of time on in the
[18:08] channel actually using all these
[18:11] categories of prompts to put together
[18:13] concrete reasoning machines AI agents
[18:17] that solve specific problems really well
[18:19] on their own thanks to these categories
[18:21] I have developed you know entire Suites
[18:23] of patterns benchmarks and AI tooling
[18:27] that specialize in each one of the
[18:29] categories so let me know what you think
[18:32] about these six categories do you find
[18:34] this grouping useful do you see
[18:36] completely different categories am I
[18:37] missing one drop a comment down below
[18:40] let me know what you think of my
[18:41] categorization here so that's it for
[18:43] this one I wanted to share this with you
[18:44] to give you an idea of how you can move
[18:47] faster with all of these incredible
[18:49] releases coming out from open AI
[18:51] Microsoft Gemini llama Google none of
[18:54] this matters if we can't categorize and
[18:57] use and build with this stuff I'm ultra

### Minute 19

[19:00] excited for the releases coming up I
[19:01] hope you are too if you're not
[19:03] subscribed to the channel hit the like
[19:04] hit the sub and I'll see you in the next
[19:07] one