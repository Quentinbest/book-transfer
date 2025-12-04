# CHAPTER 4

CHAPTER 4
=========

Predictive Models
=================

JUDGING BOOKS BY THEIR COVERS
=============================

*Red cars go fast*.—ORRIE PAGE (at age three)

RESTAURANTS in Japan often advertise their fare by featuring plastic versions of their menu items in their windows. When American tourists visit Japan, they often shy away from these restaurants. These tourists predict—incorrectly, it turns out—that these restaurants cannot be good. After all, even Waffle House is too sophisticated to have plastic sausages and waffles in the window. These tourists are using interpretations to gauge a future event: they’re making predictions. Whereas an interpretation categorizes the set of possibilities, a predictive model describes what we think will happen in some context in light of our interpretations. We categorize a cloud as a “rain cloud” and correctly predict rain. We categorize lightning as “heat lightning” 1and correctly predict that we’ll remain dry. But, like those tourists in Tokyo, our predictive models can also lead us astray. Nearly every restaurant in Japan features plastic food; in fact, it’s so popular that there’s even a street in Tokyo called Kappabashi-dori jammed full of stores where you can buy plastic food and other essentials of the Japanese culinary experience.

We use predictive models when we vote, when we buy houses, when we select partners for life or business, and when we invest money for retirement. In each of these instances, we make predictions about the future based on our interpretations of the world. We do not know how events will transpire, whether the market will go up or down, whether learning Russian is a good career move, or whether a particular candidate will make a competent president. We make our predictions and take our chances.

To make a prediction or to infer a causal relationship, we first interpret the situation. To extend an earlier example, when we look into the sky and try to predict the likelihood of rain, we interpret the current weather: the temperature, wind speed, cloud formation, time of day, and the color of the sky. We take a slice of reality that, based on our experience, is relevant to the weather. We then predict a likelihood of rain based on our knowledge and experience. Interpretations influence predictions but they do not determine them. Two people with the same interpretation can make diverse predictions because their experiences or intuitions point them toward different inferences.

Over time we improve and refine our predictive models. We may have economic incentives to do so, or we may just desire deeper understandings. Whether capitalist or Buddhist, we want to know how things work. This constant honing and refinement of models need not lead to convergence of interpretations across different people. We’re only likely to converge if presented with abundant data. We learn the causal relationships between fire and heat and ice and cold because fire is always hot and ice is always cold. The less noisy the environment, the more easily we can draw causal inferences. If ice were cold only 51 percent of the time, we might disagree about whether or not it is cold, just as we debate global warming.

Though lots of noise hinders our ability to predict, adding a little noise has an unexpected effect. It reinforces our beliefs in our models. This has practical consequences. If we want to teach a behavior, a bit of randomness can be helpful. For example, to teach a dog to sit, you should not always give her a treat as reward. Most of the time you should, but every once in a while you should withhold it. In doing so, you make the dog think, “I’m sitting, why am I not getting a treat? What is going on here? Didn’t he say sit?” This helps her brain make even stronger connections between my command/plea to sit and her response. This may seem like wholly academic research, but it’s not. The variable reward schedule is taught in most dog training classes.

Whether we learn them in noisy or clean environments, each of us carries around a set of predictive models in our heads. In what follows, we assume these predictions to be as accurate as possible given the interpretation and available information. Yet this may not always be the case. The theory of evolution has been supported by a century of empirical work. Nevertheless, many people do not believe it. Some government programs, such as Head Start, which most evidence suggests are successful, still have detractors.[1](9781400830282_epub_nts_r1.htm#c04-ftn1)

Evolution and Head Start remain controversial because of their dimensionality and complexity. When the connections from policies and actions to outcomes become complicated, even experts do not understand them entirely. Therefore, we simplify. We use interpretations. Even experts do. If these interpretations differ, they lead to predictions that differ. Different predictions prove beneficial. Before we show why, we need to understand its sources in more detail.

PREDICTIVE MODELS
-----------------

Models take many forms. A survey of the vast modeling literature reveals systems dynamics models, regression models, game theory models, factor analysis models, and agent-based models. Models simplify the world. In fact, you’re soaking in a model right now. But rather than soften your hands, models interpret reality and then produce outputs. These outputs often take the form of predictions. Here we restrict our attention to these *predictive models*.

A **predictive model** *is an interpretation together with a prediction for each set or category created by the interpretation*.

Just to help keep all of these frameworks and concepts clear, let’s think of how predictive models differ from heuristics. A predictive model tells us what we think will happen: “It looks like rain.” A heuristic tells us what to do: “It’s raining, let’s run for cover”—or what not to do: “We get just as wet by running, so let’s walk.” Predictive models are thoughts. Heuristics are actions.

Predictive models based on crude interpretations can be powerful. In *Blink,* Malcolm Gladwell describes how experts learn to look at just a few features and make expert predictions. Gladwell is describing predictive models based on simple interpretations.[2](9781400830282_epub_nts_r1.htm#c04-ftn2) Gladwell loads his book with examples, including the story of an expert who instantly recognized a multimillion-dollar sculpture as fake even though scientific analysis had found otherwise, and one of an expert who can accurately predict whether a married couple will stay together by looking at a few dimensions of their relationships. Gladwell’s book popularizes ideas that get a more formal treatment in the work of Gerd Gigerenzer and Peter Todd.[3](9781400830282_epub_nts_r1.htm#c04-ftn3) Using our framework of predictive models, we can make sense of how these brief appraisals can be accurate and also why there may exist environments where even the best “blinker” won’t be accurate.

As Gladwell’s examples suggest, we should not think of predictive models as applying just to important events such as stock market price changes or the causes of diseases. We apply predictive models almost every time we think. And our predictive models rely on interpretations. A popular predictive model for when a television show has reached its peak relies on categorizing episodes by features of the script. “Jumping the shark” (a reference to Fonzie jumping over a shark on water skis that signified the long decline of *Happy Days)* occurs for many reasons. It could be an event—a wedding, birth, or death—or it could be when the show brings on a special guest star (Nancy Reagan showing up on *Diff’rent Strokes).[4](9781400830282_epub_nts_r1.htm#c04-ftn4)* In predicting whether a show has jumped the shark, people may rely on diverse models. Some people believe that *American Idol* jumped the shark with William Hung (a singer with no pitch). Others believe that it occurred when Paul Anka appeared as a guest star.

To provide some formalism for predictive models, I construct an example called Screening Success. It’s only a little less fun than jumping the shark, but it’s much easier to understand. I lean heavily on this example, considering it again in the next part of the book when aggregating predictive models.

TABLE 4.1: The sex and violence interpretation

![](images/9781400830282_94-1.png)

SCREENING SUCCESS
-----------------

To see how crude predictive models work, let’s consider a context in which quick appraisals are the norm: evaluating movie scripts. In Los Angeles, a shockingly high percentage of the waiters, surfers, valets, mall employees, and even lawyers, doctors, and professors write screenplays. Many of these screenplays get only cursory reads by low-level studio employees (who themselves write screenplays on the side). A few screenplays get passed up the chain, but most get dragged across the computer screen and dumped into the trashcan.

In our example, we consider two employees of a movie production company, Ray and Marilyn, who have the task of reading screenplays. We can assume that they have been assigned the task of accepting only those scripts that will produce profits. Every submitted screenplay can be objectively assigned levels of sex (S) and violence (V). These levels can be classified into one of four categories: none, low, moderate, or high. (See [table 4.1](#c04tab1).) A complete perspective on the set of all movies would contain more dimensions than these two. So this encoding is an interpretation.

To make this example as simple as possible, we assume a deterministic mapping from these characteristics to whether a screenplay is good (G) (i.e., can be the basis for a profitable film) or is bad (B) (i.e., should be dragged into the can). Leave aside the idea that evaluating film scripts on the criteria of sex and violence would have deprived us of some great movies. Models require simplifying reality. [table 4.2](#c04tab2) shows the mapping into profits.

TABLE 4.2: The screenplay attribute to movie quality mapping

![](images/9781400830282_95-1.png)

![](images/9781400830282_95-2.png)

Figure 4.1 Projection onto Sexual Content

Given this construction, if someone knew this map and kept track of the levels of sex and violence, she could perfectly predict whether or not the screenplay is good or bad. We’re assuming that Ray and Marilyn don’t do this. Each of them lacks the ability (or time, or inclination) to look at both attributes. In keeping with gender stereotypes, we assume that Ray keeps track of the level of sex ([Figure 4.1](#c04fig1)) and Marilyn keeps an eye on the violence ([Figure 4.2](#c04fig2)). (We would classify both of these as projection interpretations.)

To turn these interpretations into predictive models, we need only attach a prediction to each set in the interpretation. For example, assume that Ray reads a screenplay with no sex. Provided Ray has lots of experience reading screenplays (a point we take up shortly), he knows that three times out of four (or 75 percent of the time) the movie will turn out unprofitable. He similarly learns that screenplays with low levels of sex also turn out to be bad 75 percent of the time, but that movies with moderate and high levels of sex turn out to be good 75 percent of the time.

![](images/9781400830282_96-1.png)

Figure 4.2 Projection onto Violence

TABLE 4.3: Ray’s predictive model

![](images/9781400830282_96-2.png)

He’s not always right, but he’s not paid always to be right. He’s making a quick appraisal. He’s blinking. We can summarize Ray’s predictions in [table 4.3](#c04tab3). This table describes his predictive model. In the first column, we show the level of sex in the films. In the second column, we show what realizations Ray would see. Of those films with no sexual content, three will be Bs and one will be G. The good one will be a film with no sexual content and moderate violence.

Similarly, we can characterize Marilyn’s predictive model in [table 4.4](#c04tab4).

A moment’s observation shows that Marilyn will also be correct 75 percent of the time. Note though that she and Ray do not make the same predictions. When evaluating a screenplay with no sex and lots of violence, Ray would predict a flop whereas Marilyn would predict a success. In this instance, Ray would predict correctly and Marilyn wouldn’t. If we average across all cases, it’s equally likely that she’d be correct and he wouldn’t.

TABLE 4.4: Marilyn’s predictive model

![](images/9781400830282_97-1.png)

TABLE 4.5: Deborah’s interpretation

![](images/9781400830282_97-2.png)

In addition to Ray and Marilyn, we now add a third screenplay evaluator, Deborah. She uses a clumping interpretation, creating sets that allow for variation in both attributes within the same category. Whereas a projection interpretation divides the square into rows or columns, a clumping interpretation divides it into boxes of various shapes.

To construct the correct frame for this interpretation, think of Deborah as someone fueled by large quantities of Diet Coke who wears funky glasses and has serious attitude. Deborah’s interpretation clumps screenplays into three sets: dull, extreme, or balanced. Deborah classifies screenplays with low and moderate levels of both sex and violence as dull, screenplays with low or moderate levels of either sex or violence and either a high level or none of the other as balanced, and screenplays with neither a low nor a moderate level of either sex or violence as extreme (see [table 4.5](#c04tab5)).

Assuming that she has lots of experience and makes the more likely prediction for each set in her interpretation, Deborah’s model predicts that balanced screenplays will be good and that all others will be bad. Her predictive model looks as shown in [table 4.6](#c04tab6).

TABLE 4.6: Deborah’s predictive model

![](images/9781400830282_98-1.png)

Relative to Ray and Marilyn’s models, Deborah’s seems strange. And yet by examining all the cases (which takes a little effort), we can see that she also predicts correctly 75 percent of the time. She’s just as accurate as they are. Given their equal proficiency at predicting, Ray, Marilyn, and Deborah would all feel comfortable holding onto their own predictive models. Even under pressure to make good predictions, people need not converge on a common predictive model. *Selective pressure, or what could be called survival of the fittest, need not imply convergence to a single predictive model*. Diversity can persist in a competitive environment. Several predictive models can be close to equally accurate. Each of twenty pundits can analyze an election differently yet compellingly. Was it Ohio evangelicals that swung the 2004 election for Bush or was it the new exurbanites? A case can be made either way. As we will see in [part II](9781400830282_epub_p01_r1.htm), when we aggregate these predictive models, this diversity proves beneficial.

THEORY-BASED MODELS
-------------------

Our discussion so far has assumed that our screenplay readers make the correct predictions that they have learned from experience. But even in the absence of experience, we may still have to make predictions based on theories. On their first days of work, for instance, Marilyn and Ray would have had to rely on these experience-free theories. These theories could be no better than random or they could be accurate if underpinned by sound logic. Ray might have theorized that screenplays with low and moderate levels of sex would do well and come up with the predictive model shown in [table 4.7](#c04tab7).

TABLE 4.7: Ray’s theory-based predictive model

![](images/9781400830282_99-1.png)

This model predicts correctly a mere 50 percent of the time. Ray could do equally well flipping a coin and he’d no longer have to suffer through all that terrible dialogue.

This simple example makes an important point: an interpretation that represents the objects or events meaningfully is by itself not enough. An interpretation may capture dimensions or attributes that reveal underlying causality or correlation, but unless that interpretation is combined with an accurate predictive model, possibly one informed by experience, it may not prove useful.

Thus, we can distinguish between the maximal accuracy of a predictive model given an interpretation and the accuracy of a given model. The maximally accurate predictions from an interpretation are those that would be made if the person knew the true probability distribution over outcomes (something we get closer to with experience). As we saw, the accuracy of a particular theory need not achieve this maximum. In addition, maximal accuracy given an interpretation may not be high in some contexts. If so, then it would be impossible to make quick assessments that were highly accurate.

In other words, sometimes we can blink and sometimes we cannot. Suppose we begin with a common perspective that we use to construct projection interpretations and predictive models. We then have at our disposal one predictive model for each dimension. It may be that none of those predictive models works well. If so, blinking—making a quick evaluation based on a single attribute—won’t be effective. Good blinking requires the existence of a dimension that makes the task easy. As Gladwell describes in *Blink,* evidence of nastiness is a good predictor of the likelihood a marriage will end in divorce. If our interpretation considers only that single dimension—does a couple make nasty, diminishing comments about each other—it’ll allow us to predict pretty well.

But no such dimension may exist for a given predictive task. To take an obvious case, suppose that we want to predict whether a stock price of a company will increase or decrease. If we looked at any one attribute of that company—price—earnings ratio, sales growth, change in stock price over the past year, or the like— we could not predict much better than randomly whether the price would go up or down. The reason no single dimension is of much predictive value rests on a logic of markets. If a simple way to predict rising stock prices existed, someone would find it and raise the price of the undervalued stocks. For this simple reason, people who successfully invest in the stock market use sophisticated predictive models, and we can’t “blink” stock prices.

The bulk of the evidence shows that most people, even experts, are less accurate than regression models based on data. The book *Moneyball* popularized this stylized fact by showing how Billy Beane ran regressions and then ran circles around other baseball executives.[5](9781400830282_epub_nts_r1.htm#c04-ftn5) The *Moneyball* example is not an outlier. More than two hundred studies conducted over the past seventy years demonstrate that simple linear regression models outperform experts in forecasting the future.[6](9781400830282_epub_nts_r1.htm#c04-ftn6) We should not view these findings as puzzling. Experts are people, too, and they suffer from biases just like the rest of us.

In a decade-long study, Philip Tetlock found that experts could not very accurately predict outcomes of complex economic and political processes. He further found that those experts who relied on fixed ideological interpretations, so-called hedgehogs, performed worse than those who were willing to be flexible. Overall, most experts proved to be more confident than they should have been.[7](9781400830282_epub_nts_r1.htm#c04-ftn7) Almost everyone suffers from overconfidence. It comes with being human. Most of us feel we’re above average in most things. And echoing earlier results, he finds experts worse than regressing.

We shouldn’t be too sanguine about Tetlock’s findings. We must remember that even experts’ heads can hold only so much information. In making predictions, experts rely on a few dimensions at most. They omit variables that matter, and they sometimes include variables that do not. Hence, when the inference task becomes difficult, even the experts must throw up their hands and their predictions may not be much better than tosses at a dartboard.

The fact that experts are not as accurate as regression models begs the question of why we use experts at all. Why don’t we just use regression models? We do. Experts do. Successful investors, forecasters, and odds makers do not just get a feel for what is likely to happen using mystical powers, they gather data. They run regressions. These regressions are still based on variables chosen by people—what we call interpretations. The human element is not absent. These interpretations leave out some variables and include others. Given the diversity of possible interpretations, we have lots of diverse experts. And, as we will see, that’s beneficial.

CONCLUDING THOUGHTS
-------------------

At this point, a brief summary helps us keep track of the various concepts that we’ve covered in the past two chapters. If we want to predict something, we have to have some way of representing those entities whose outcomes we are predicting. Perspectives would give us a full and complete representation, but in most cases people don’t use perspectives. We use interpretations— categorizations—based on perspectives. Given these interpretations, we then make predictions based on our experiences or on a theory. We call these predictions, together with the interpretations, a predictive model. Thus, predictive models map the sets (or categories) in our interpretations onto outcomes. Any interpretation has a maximally accurate model, but we have no reason to believe that people use this model. After all, we’re human.

Being human, we differ in the interpretations we choose. And as we saw in Screening Success, we therefore differ in our predictive models. Ray thinks the screenplay is good. Marilyn thinks it is not. Sometimes crude predictive models work well. Sometimes they don’t. If we confront a complicated predictive task, predictive models based on crude interpretations will be inaccurate most of the time. As we see in the next part of the book, even when individual predictions may not be accurate, collections of diverse inaccurate predictions can be.
