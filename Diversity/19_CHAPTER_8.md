# CHAPTER 8

CHAPTER 8
=========

Diversity and Prediction
========================

THE CROWD OF MODELS
===================

*Prediction is very hard, especially about the future*. —YOGI BERRA

IN this chapter, we will apply the predictive model framework to explain the wisdom of crowds. The analysis culminates in two theorems: *The Diversity Prediction Theorem* and *The Crowds Beat Averages Law*. The first states that a crowd’s collective accuracy equals the average individual accuracy minus their collective predictive diversity.[1](9781400830282_epub_nts_r1.htm#c08-ftn1) So for predictive tasks, the answer to the question, “how much does diversity matter?” is “just as much as ability.” No less. No more. The second states that the accuracy of the crowd’s prediction cannot be worse than the average accuracy of its members. Thus, the crowd necessarily predicts more accurately than its average member. So, groups are, on average, above average. Furthermore, the amount by which the crowd outpredicts its average member increases as the crowd becomes more diverse.

In this chapter, we also see how crowds of people using diverse interpretations can predict more accurately than models based on independent signals would suggest. Though convenient, an assumption of independence may understate the predictive ability of small crowds. We also see that it overstates the ability of large crowds. In addition to looking at crowds alone, we’ll compare the performance of crowds to that of experts. We will learn conditions under which we would expect the crowd to predict more accurately and conditions under which we would not. We even consider crowds of experts—what we call the *crowd of models*. These crowds may predict best of all. Finally, we show how incentives can improve the accuracy of collective predictions, thus making the case for information markets.

We will restrict our discussion in this chapter to crowds of people, though we could also include examples of other species— ants, crows, and bison—as well as examples of machines and algorithms. The bison example provides a hint of how other species exploit diversity. Bison take different routes across a mountain range. Each bison leaves a trail. Two trails, in fact. A continuous foot trail and a discrete trail that we ignore. More heavily traveled routes become more beaten down and encode the collective wisdom of the bison. The collective trails over time become efficient.[2](9781400830282_epub_nts_r1.htm#c08-ftn2) Norman Johnson has constructed models that demonstrate this phenomenon.

Covering this substantial terrain requires moving back and forth between several types of models. This may prove challenging for many readers. The analysis includes quite a few mathematical calculations. Though no one calculation takes much effort (the hardest require squaring the difference of two numbers), we make a lot of them. The payoff at the end proves worth this effort. We get the theorems. These theorems are not political statements, but mathematical truths. To understand those theorems we must roll up our sleeves and work through a few simple formulas.

Before we begin, keep in mind that we will implicitly limit attention to challenging predictive tasks and intelligent predictors. Any easy predictive task (which will be warmer on January 8, 2006, at noon: International Falls, Minnesota, or San Diego, California?) requires neither a crowd nor an expert. Similarly, if the individual predictors do not know much of anything, the crowd may not predict well. If we ask ten thousand first graders to guess the weight of a fully loaded Boeing 747 (about fourty tons), we should expect their average guess to be well off the mark. Some might guess as low as one hundred pounds. Some might guess as high as a billion billion tons. You cannot make a silk purse out of a crowd of sows’ ears.

TABLE 8.1: The screenplay attribute to movie quality mapping

![](images/9781400830282_199-1.png)

THE WISE CROWD FROM SCREENING SUCCESS
-------------------------------------

To lay a foundation for the remainder of the chapter, let’s return to Screening Success (discussed in [chapter 4](9781400830282_epub_c08_r1.htm)) and consider Ray, Marilyn, and Deborah as a crowd. We find this crowd to be wise indeed. In a few pages, we will show why crowds must be wiser than the people in them and why this particular crowd does so well. For the moment though, let’s revel in the mystery of their wisdom.

Recall that the task in Screening Success was to predict whether a given screenplay would produce a profitable movie. Ray, one of our predictors, considered the amount of sexual content. Another predictor, Marilyn, considered the level of violence. These were their interpretations of the screenplays. Our third predictor, Deborah, used a much more complicated interpretation that relied on balancing the amount of sexual content and violence. We’ll revisit her predictive model as well as Ray and Marilyn’s in the next paragraph. [Table 8.1](#c08tab1) presents the mapping from screenplay attributes to whether the movie would be profitable (i.e., good, denoted by G) or unprofitable (i.e., bad, denoted by B).

Remember that Ray predicts that those screenplays with moderate or high levels of sexual content will be good and that others will be bad; Marilyn predicts that those screenplays with moderate or high levels of violence will be good; and Deborah predicts that those screenplays that are balanced will be good. Their predictive models can be written in tabular form as shown in [tables 8.2](#c08tab2), [8.3](#c08tab3), and [8.4](#c08tab4).

TABLE 8.2: Ray’s predictive model

![](images/9781400830282_200-1.png)

TABLE 8.3: Marilyn’s predictive model

![](images/9781400830282_200-2.png)

TABLE 8.4: Deborah’s predictive model

![](images/9781400830282_200-3.png)

TABLE 8.5: Ray and Marilyn’s agreement set

![](images/9781400830282_201-1.png)

To capture how these three predict as a crowd making a prediction, we assume that they vote based on their predictions. As each person predicts either a good or a bad outcome, we cannot have any ties. If Ray and Marilyn agree that a screenplay is either good or bad, they leave Deborah with no say in the matter. Given our assumptions, Ray and Marilyn make the same predictions on screenplays that have relatively low sexual content and violence (these fall in the four upper left boxes) and on screenplays that have relatively high sexual content and violence (these fall in the four lower right boxes). Call this their *agreement set* (see [table 8.5](#c08tab5)). Extra terminology helps us keep track of what’s what.

Inside their agreement set, Ray and Marilyn have total say. Deborah is irrelevant. Outside of this agreement set, Deborah becomes all-powerful. Political scientists call her pivotal—her prediction determines the crowd’s prediction. Looking at [table 8.5](#c08tab5), we see that Ray and Marilyn make different predictions for eight of the boxes—the boxes not in their agreement set. Filling in Deborah’s predictions in those eight cases gives the predictions from the crowd shown in [table 8.6](#c08tab6).

This table should look familiar. It is the original table that maps from attributes to outcomes. The crowd predicts accurately every time. Amazing? Yes. But given that my parents are named Ray and Marilyn and my older sister is named Deb, shouldn’t we have expected something like this? Clearly this example was carefully crafted, but for a purpose. The example shows how diverse predictive models can aggregate in ways far more subtle and sublime than the putting together of distinct pieces described by Aristotle. The Law of Large Numbers cannot get you to 100 percent, and neither can canceling errors.

TABLE 8.6: The crowd’s predictions

![](images/9781400830282_202-1.png)

To make sense of how the crowd can be 100 percent accurate, we need to compare this example to the sweater example in the Gravity of Truth Model (from [chapter 7](9781400830282_epub_c07_r1.htm)). In both examples, each individual predicts correctly three-fourths of the time. However, in the sweater example, the crowd predicted correctly only 84 percent of the time. What accounts for this difference? In the sweater example, we assumed independent individual signals: One person’s reaction to the wool was independent of another’s. We made no such assumption in Screening Success. The predictions in Screening Success must not be independent. They must be better than independent somehow. And they are. In those cases that Ray predicts incorrectly, Marilyn predicts correctly more than three-fourths of the time. Thus, she purposefully, as opposed to randomly, cancels out his errors. (That’s true of my parents as well.) This reduces the probability that the crowd makes an error. Statisticians call this *negative correlation*. As will become clear, the wisdom of crowds resides partly in the presence of negative correlation or the lack of positive correlation.

To show negative correlation mathematically, we need that when Ray predicts correctly, Marilyn is *less* likely to predict correctly, as this implies that when Ray predicts incorrectly, Marilyn is more likely to predict correctly. So she cancels out his mistakes. To do this, let’s first write down the screenplays that Ray predicts correctly, and then highlight those screenplays among them that Marilyn also predicts correctly (see [table 8.7](#c08tab7)).

TABLE 8.7: Correct predictions by Ray

![](images/9781400830282_203-1.png)

The table shows that Ray predicts correctly in twelve of sixteen cases. Marilyn predicts correctly in just eight of those twelve cases, or ![](images/9781400830282_203-2.png) of the time. If her probability of predicting correctly had been independent of Ray’s probability, then she would predict correctly ![](images/9781400830282_203-3.png) of the time, or in nine of the cases. Eight is less than nine; therefore Marilyn predicts correctly less often than would be the case if her predictions were independent of Ray’s. Thus, put in the formal language of statistics: the correctness of their predictions is negatively correlated.[3](9781400830282_epub_nts_r1.htm#c08-ftn3)

As I have already admitted, this example is contrived. However, it reveals a deeper truth. Ray and Marilyn’s negatively correlated predictions provide the key insight. Notice that they look at different attributes of the same perspective. Earlier, we called these *projection interpretations*. Ray and Marilyn’s projection interpretations do not contain any of the same attributes, so let’s get precise and call them *nonoverlapping projection interpretations.[4](9781400830282_epub_nts_r1.htm#c08-ftn4)* In yes-or-no, good-or-bad predictive tasks such as the one considered here, nonoverlapping projection interpretations *always* create negatively correlated predictions.[5](9781400830282_epub_nts_r1.htm#c08-ftn5)

**The Projection Property:** *If two people base their predictive models on different variables from the same perspective (formally, if they use nonoverlapping projection interpretations) then the correctness of their predictions is negatively correlated for binary predictions*.

Understanding the Projection Property requires careful thought. It says that if two people look at different attributes of the same perspective (that is, different dimensions), and if the task is to predict success or failure, or any other binary outcome such as good or bad, or yes or no, then when one person is correct, the other person is less likely to be correct. Thus, they’re better at collectively predicting than they’d be if they got independent signals.

At first, this result might seem hard to believe, or at least unintuitive. Yet it has a simple explanation that goes as follows: We know that it must be possible for two people to make predictions so that when one is right, the other is more likely to be wrong. The obvious way to do this would be to make diverse predictions. How better to make diverse predictions than to look at different attributes?

The projection property implies that crowds containing people who look at diverse attributes will be wise. Unfortunately, this insight cannot be leveraged as much as we might hope. The dimensionality of the perspective defines the number of nonoverlapping projection interpretations. A perspective that creates a five-dimensional representation of an event or situation can support at most five nonoverlapping projection interpretations. A perspective that creates ten dimensions can support at most ten nonoverlapping projection interpretations.

To avoid positive correlation as the number of people in the crowd becomes larger, people must either use cluster interpretations or they must base their interpretations on different perspectives. Deborah’s interpretation is an example of the former. Though based on the same perspective, it is not a projection interpretation. Many papers, in fact, even seminal papers in political science and economics, assume infinite numbers of people getting independent signals (believe it or not, using infinity makes the math easier). If these signals come from predictive models, that assumption just doesn’t have logical foundations. Constructing cluster interpretations that lead to independent signals is possible, but such examples are contrived. It’s convenient, but so would be self-toasting bread. In writing good models, we shouldn’t confuse convenient assumptions with good ones. By assuming independent signals, these scholars assume more diversity than may exist.[6](9781400830282_epub_nts_r1.htm#c08-ftn6)

TABLE 8.8: Predictions of the Rudy G. Bee

![](images/9781400830282_205-1.png)

THE DIVERSITY PREDICTION THEOREM
--------------------------------

Now that we’ve worked through an example, we’re ready to turn to the more general theorems that reveal the importance of diverse predictive models among the members of a crowd. Versions of these theorems can be found in computer science, statistics, and econometrics.[7](9781400830282_epub_nts_r1.htm#c08-ftn7) To describe these theorems, we’ll need two measures. The first captures how much a collection of predictive models differs. The other captures how accurate the models are. Both are based on the same accuracy measure: *squared errors*. In statistics, errors are squared so that negative errors and positive errors do not cancel one another out. If errors were added, a person who was equally likely to overestimate or underestimate an amount on average would make no errors (—5 + 5 = 0). If we first square the errors, then the negative and positive errors do not cancel ((—5)2 + 52 = 25 + 25 = 50). To build the logic of the theorem, we first construct an example. Suppose that Micheala and Juliana have developed models to predict where three students—Maggie, Cole, and Brody—will place in an upcoming spelling bee at Rudy Giuliani Elementary. [Table 8.8](#c08tab8) shows their individual predictions, their average prediction, and the actual outcome from the bee.

We first compute the squared errors of Micheala and Juliana’s predictions. Michaela picks Maggie to take sixth place and she takes sixth, an error of zero. She picks Cole to take third and he takes fifth, an error of two. And she picks Brody to take fifth, but he takes first place, an error of four. Squaring these three errors gives zero, four, and sixteen. The sum of the her errors equals twenty.

**Micheala’s Individual Error:** (6 − 6)2 + (3 − 5)2 + (5 − 1)2 =0 + 4 + 16 = 20

We next make the same calculation for Juliana. She misses Maggie’s placement by four, she misses Cole’s by two, and gets Brody’s place exactly right. Squaring these errors gives sixteen, four, and zero, for a total squared error of twenty.

**Juliana’s Individual Error:** (10 − 6)2 + (7 − 5)2 + (1 − 1)2 =16 + 4 + 0 = 20

The sum of each of their squared errors equals twenty, so their average sum of squared errors also equals twenty. We call this the *average individual error*. Here that’s easy because their errors are the same.

**Average Individual Error:** *Average of the individual squared errors*

![](images/9781400830282_206-1.png)

We next compute the error of their *collective prediction:* the average of their individual predictions. They collectively predict that Maggie will take eighth place. She takes sixth, for an error of two. Their collective prediction for Cole, fifth place, is correct, and their prediction for Brody is off by two. Squaring these errors gives four, zero, and four, for a total of eight. We call this their *collective error*.

**Collective Error:** *Squared error of the collective prediction*

(8 − 6)2 + (5 − 5)2 + (3 − 1)2 = 4 + 0 + 4 = 8

Notice that their collective prediction is more accurate than either of their individual predictions. The explanation for this can be found in the diversity of their predictions. When one of them predicts too high, the other predicts too low and their mistakes, while not canceling entirely, become less severe. To make this relationship between the diversity of their predictions and the accuracy of their collective prediction more formal, we calculate how much their predictions differ. We do this by calculating Juliana’s squared distance from their collective prediction and Micheala’s squared distance from their collective prediction. We then average these two numbers. Statisticians call this the *variance* of their predictions. We will call it the *prediction diversity*.

We first compute Micheala’s squared distance from the collective prediction. The collective prediction for Maggie is eighth place. Micheala predicts sixth place for a difference of two. The collective prediction for Cole is fifth place, and she predicts third place for a difference of two. Finally, the collective prediction for Brody is third place, and she predicts fifth, a difference also equal to two. The squares of these differences are four, four, and four, which sum to twelve.

**Micheala’s Squared Distance from the Average:**  
(6 − 8)2 + (3 − 5)2 + (5 − 3)2 = 4 + 4 + 4 = 12

As there are only two predictors in this example, Juliana’s distance from the average in each case must be the same as Michaela’s. That calculation can be made as follows:

**Juliana’s Squared Distance from the Average:**  
(10 − 8)2 + (7 − 5)2 + (1 − 3)2 = 4 + 4 + 4 = 12

The *prediction diversity* equals the average of these two distances; in this case, it equals twelve.

**Prediction Diversity:** *Average squared distance from the individual predictions to the collective prediction*.

![](images/9781400830282_207-1.png)

Notice the relationship between the collective error (8), the average individual error (20), and the prediction diversity (12): *Collective error equals average error minus diversity*. This equality is not an artifact of our example. It is always true. And, even better, it holds for any number of predictors, not just two predictors as in our example. Thus, we call this the *Diversity Prediction Theorem*.

**The Diversity Prediction Theorem:** *Given a crowd of predictive models*

![](images/9781400830282_208-1.png)

We have to be careful not to over- or understate what this theorem means. It doesn’t say that you don’t want all accurate people. If individual people predict perfectly, they cannot be diverse. (If average individual error equals zero, then diversity must also equal zero.) Notice also that prediction diversity equals the *average* squared distance from the collective prediction, so adding someone who predicts differently need not increase overall prediction diversity. Prediction diversity increases only if the additional person’s predictions differ by more, on average, than those of other people. This implies a limit to the amount of predictive diversity we can have. If a collection of people has an average individual error of one thousand, then their prediction diversity cannot exceed one thousand. Any more diversity and the collective error would become negative, an impossibility.

Fine, we’ve got some caveats. But they just reveal some of the theorem’s subtleties. What’s important is that we keep in mind the core insight: individual ability (the first term on the right-hand side) and collective diversity (the second term) contribute *equally* to collective predictive ability. *Being different is as important as being good*. Increasing prediction diversity by a unit results in the same reduction in collective error as does increasing average ability by a unit.

Contrasting the Diversity Trumps Ability Theorem with the Diversity Prediction Theorem reveals important differences. In making a prediction, a group of randomly selected predictors might or might not predict more accurately than a group of the best predictors. Randomly selected predictors will be more diverse, to be sure, but they will also be less accurate. The two effects work in opposite directions. So, we cannot expect that a random intelligent group will predict more accurately than the group of the best. Yet, that stronger claim holds in the problem-solving context. The reason why is that poor performers fail to drag down problem-solving teams. If we bring Larry, a social scientist, into our cheese-making business, his lack of relevant tools won’t hurt our cheese making. We just ignore him. He may cause delay or frustration, but if he has only bad ideas—peppermint cheese— those ideas won’t be adopted. However, if we’re predicting how much cheese to make, we won’t know that he doesn’t know and his prediction gets averaged along with everyone else’s. And he could make the crowd less wise.

An implication of the theorem is that a diverse crowd always predicts more accurately than the average of the individuals. This runs counter to our intuition. We can call this the Crowd Beats the Average Law.

**The Crowd Beats the Average Law:** *Given any collection of diverse predictive models, the collective prediction is more accurate than the average individual predictions*

*Collective Prediction Error < Average Individual Error*

The Crowd Beats the Average Law follows from the Diversity Prediction Theorem. The Diversity Prediction Theorem says that collective error = average individual error − prediction diversity. Prediction diversity has to be positive if the predictions differ. Therefore, the collective error must be smaller than the average individual error. There’s no deep math going on. But the insight is powerful nonetheless.

We now have a logic for the wisdom of crowds. In an ideal world, these formal claims would replace pithy statements such as “two heads are better than one,” but they may not be catchy enough. We can try though. We might replace the Diversity Prediction Theorem with “the wisdom of a crowd is equal parts ability and diversity” and the Crowd Beats the Average Law with “the crowd predicts better than the people in it.” Not memorable, but accurate.

*A Crowd of Draft Experts*
--------------------------

To cement our understanding of the logic, let’s consider some real data. Die-hard theorists prefer constructed examples because they are neater and cleaner. But sometimes even a theorist cannot help but peek out the window. So if we’re going to look at data, we might as well look at something important: football draft selections. [Table 8.9](#c08tab9) shows predictions for the top dozen picks in the 2005 NFL draft from seven prognosticators. The players are listed in the order that they were selected. Each predictor provides a ranking of the draftees. We use the NFL draft because it has clean, integer-valued data, because it can be seen as a ramped-up version of our earlier example that involved Juliana and Michaela, and because these experts’ predictions came from detailed analyses. They don’t call them draft experts for nothing. These people, er men, devote long days and nights evaluating team needs, player skills, and a host of other factors.

If we look at their predictions, we see that they differ in their accuracy. The table reveals that some do far better than others. The last column, by the way, shows the crowd’s prediction.[8](9781400830282_epub_nts_r1.htm#c08-ftn8) Here the crowd is just the collection of all seven predictors.

These data show the Crowd Beats the Average Law in full force. The average of the individual errors equals 137.3. The collective error, shown in the last column, equals about one-fourth of that, 34.4. In this example, the crowd predicts more accurately even than its most accurate member even though the Crowd Beats the Average Law makes no such claim.[9](9781400830282_epub_nts_r1.htm#c08-ftn9) The example also shows the power of diversity. These predictors are so diverse that they collectively predict well.

Even more amazing, note that this comparison between the crowd and its most accurate member is unfair. In selecting the best person after the fact, we stack the deck against the crowd. No one, other than perhaps Clark Judge himself, would have predicted Judge (despite his name) to be more accurate than the others. In the future, Judge may not be the best predictor. To take another example with higher stakes, successful investment funds differ from year to year. If at the beginning of the year, we could pick the fund that would do best at the year’s end, investing would be fun and easy. But we cannot, so we diversify. By going with the crowd, we take on less risk. We should go with the expert only if we know that person to be far more accurate than the others and the others to make similar predictions.

TABLE 8.9: Experts’ predictions of 2005 NFL draft

![](images/9781400830282_211-1.png)

*Points and Ranges*
-------------------

Up until now, we have focused on the difference between the predictions and the outcomes. In many instances, we may want to know best- and worst-case scenarios. We want to know the range of possibilities. In building a stock portfolio, an investor may care about the range of possible prices. How high might the stock price go? How low might it go? In predicting a potential political uprising, a policy analyst may care less about having an accurate point prediction than about knowing worst- and best-case scenarios. We can look at the best and worst predictions and the actual outcomes (see [table 8.10](#c08tab10)). In every case, the outcome falls within the range of predictions.

TABLE 8.10: Range of predictions of 2005 NFL draft

![](images/9781400830282_212-1.png)

Amazing? No, not given the diversity of the predictions.

THE MADNESS OF CROWDS
---------------------

Up to now, we have not discussed communication among crowd members. If people can share predictions, then they might become less diverse. To paraphrase Socrates, it’s much easier to go with the flow, and people often change their predictions to match those of others. And, rather than seeing wisdom emerge, we might see madness—we might see speculators buying tulips at crazy prices. We can use the Diversity Prediction Theorem to explain the madness of crowds. When we think of a crowd being mad, we think of a collection of people all taking an action that in retrospect doesn’t make sense. The madness of crowds led people to drink the green Kool Aid. The madness of crowds leads people to burn cars and sometimes even houses after sporting events. The madness of crowds explains stock market bubbles and stock market crashes.[10](9781400830282_epub_nts_r1.htm#c08-ftn10)

![](images/9781400830282_213-1.png)

Figure 8.1 Asch’s Lines

For a crowd to be mad, its members must systematically make the same bad decision. If people make these decisions in the heat of the moment—such as when burning a couch—we can chalk it up to the human tendency to join in, a topic we will return to in the epilogue. If though, people have time to construct what they believe to be reasonable predictive models, then we can often blame a lack of diversity. The Diversity Prediction Theorem implies that a crowd can make egregious errors only if the crowd members lack both accuracy and diversity.

Thus, the theorem shows the double-edged sword of deliberation. If people communicate with one another, if they share information and criticize one another’s models, they can increase the accuracy of their models. However, they can also reduce their diversity. And it has been shown time and again that people often choose to abandon accurate predictive models in favor of inaccurate models. In a classic experiment, Solomon Asch asked people to compare the lengths of several lines. Each was given pictures with a reference line and three other lines marked A, B, and C.[11](9781400830282_epub_nts_r1.htm#c08-ftn11) [Figure 8.1](#c8fig1) provides an approximation of Asch’s pictures.

Subjects were assembled together in a room and sequentially asked which lines were longer than the reference line, which lines were the same length as the reference line, and so on. The first subjects to answer were planted by Asch. They purposefully gave wrong answers. Asch found that others follow the majority— giving wrong answers—about one-third of the time. Given that people abandon their stated beliefs on the lengths of lines, we can hardly be surprised that they would abandon their beliefs in their predictions about the stock market, housing prices, or winning number combinations in the lottery.

More than just conformity leads to the madness of crowds. Often, in a group setting, people move too far in the direction of the majority opinion. So, if on average people think that prices are going to rise, then the group may work itself into a frenzy and begin to believe that because most people think prices are going up, prices are going to rise substantially.

DIVERSITY’S FREE LUNCH
----------------------

To make the next step in our analysis of why and how crowds can be wise, we can build from an earlier insight that diverse interpretations lead to diverse predictive models. In Screening Success we saw how diverse interpretations lead to negatively correlated predictions using the Projection Property. This told us how crowds can sometimes be far wiser than we might expect.

To make this connection more explicit, we next analyze a class of examples in which people use diverse projection interpretations. In these examples, all of the interpretations rely on a common perspective. We then analyze an example in which the crowd members base their interpretations on different perspectives. We see that, in some cases, interpretations based on diverse perspectives can make a predictive task easier than it would be using predictive models that rely on interpretations based on either perspective alone. We have some magic after all. That magic results from diverse perspectives.

*Different Parts of the Same Vision*
------------------------------------

If asked to make an important prediction such as who will win an election, whether an economy will grow, or the likelihood of armed conflict, we have to include many variables or attributes to make an accurate prediction. We’ve got to keep lots of variables in our heads. We might try a single-variable model, but they rarely work. A while back Thomas Friedman noticed that no two countries with McDonald’s restaurants had ever gone to war. The Golden Arches Theory held up until 1999, when NATO began dropping bombs on Serbia.[12](9781400830282_epub_nts_r1.htm#c08-ftn12) Basing foreign policy on the location of fast-food restaurants wouldn’t be a bright idea.

However, people just aren’t that willing to spend hours developing sophisticated models with lots of variables. We’re more likely to use simple, one- or two-variable models. We might think, for instance, that the economy improved and so the incumbent president is likely to be reelected. Or we might think that the incumbent president failed to pass a major policy initiative and so he’s likely to lose. Each of these models makes sense. Each looks at only a single variable.

To see how these simple models aggregate to be collectively accurate, or at least reasonably so, imagine that we want to predict the annual sales for a hot dog stand on the Jersey shore. Assume for the moment that sales can be written as a linear function of a set of ten attributes (in statistics these would be called variables). These attributes include things such as the average summer temperature, the amount of rainfall, the price of gas, the level of construction on the roads, and possibly even the price of beef. (We’re assuming the hot dogs contain beef—a leap of faith in some cases.)

Next, let’s gather a crowd of people and ask each person in it to predict the change in sales from the previous summer. Each member of our crowd would probably consider some subset of these attributes in making her prediction. Let’s suppose that these crowd members randomly choose attributes. In this way, the crowd may or may not include all *N* attributes.[13](9781400830282_epub_nts_r1.htm#c08-ftn13) For convenience, let’s assume each person in the crowd uses a linear regression model. A linear regression model predicts an outcome as a constant added to each relevant variable multiplied by a coefficient. A regression model that predicts sales based on temperature might look as follows:

*Sales* = 0.3 + 1.2 *temperature*

In this example, sales will be a linear function of these ten attributes. To keep the model as simple as possible, we will assume that the coefficient of each of these variables equals one. We further assume that each attribute takes a value between minus one and one making expected change in sales equal to zero. If we denote the attributes by *a* 1 to *a* 10, then we get the following formula for the change in total sales:

*S* = a1 + a2 + … a10

We next assume that each person in the crowd makes a prediction based on the three attributes that she chooses randomly. When running a regression with sparse data, coefficient estimates are approximations. Therefore, a crowd member who looks at attributes one, four, and eight may have the following model:

**Individual** *i* **’s Predictive Model:** *Si* = 1.1a1 + 1.08a4 +.991a8

By summing up the predictions of a crowd of models and averaging their predictions, we get that the crowd’s predictive model looks something like the following:

**The Crowd’s Predictive Model:** *SC* = .32*a* 1 + .42*a* 2 + .28*a* 3 + .37a4 + .36a5 + .35a6 + .33a7 + .38a8 + .29a9 + .34a10

The crowd’s predictive model includes all of the attributes, but its coefficients are far from accurate. This lack of accuracy is not just due to the individuals’ errors in approximation, though these exist. The larger cause is that, on average, only 30 percent of the crowd members consider each variable. Therefore, when the predictions are averaged, even if the estimates of the coefficients by each crowd member were correct, the collective prediction understates the effects of each attribute. The averaging dampens each person’s predictive model.

This example reveals two features of predictions by diverse crowds: the *Coverage Property* and the *Crude Approximation Property*.

**The Coverage Property:** *A crowd’s predictive model includes the effects of any attribute or combination of attributes included by any member of the crowd’s predictive model*.

**The Crude Approximation Property:** *A crowd’s predictive model crudely approximates the effect of any attribute or combination of attributes on outcomes*.

These two properties combine to ensure that the crowd will make good predictions on average, but indicate that expecting perfect accuracy may be asking too much. Because the crowd includes lots of variables, it won’t be caught by surprise if some subset of the variables takes on unexpected values. So, even though the crowd’s coefficients only approximate the actual values, most of the time the crowd won’t make enormous mistakes. In our hot dog model, it might be that only a couple of people take road construction into account. If major construction takes place, those people will make low estimates and they’ll dampen the crowd’s estimate, making it more accurate.

This formal investigation lacks the sexiness of real-world examples of crowds that predict the weight of a steer within a pound or the number of jellybeans in a jar within one or two. But we should not expect such outcomes every time. Our analysis suggests that diverse crowds predict pretty well, not that they will be freakishly accurate in all cases. Sometimes though, the crowd will get lucky. They’ll be incredibly accurate. Let’s see how that can happen. Let’s put some magic back in the bottle before this all becomes too clinical and statistical.

*Magic in the Bottle*
---------------------

Our example of the hot dog stand limited the amount of diversity by assuming that everyone chose from the same set of variables. In our formal language, they all used interpretations derived from the same perspective. Yet we have no reason to think that people would do this in all cases. And if people don’t, then we can have some magic. In our next example, both the Coverage Property and the Crude Approximation Property hold, but in more interesting ways.

TABLE 8.11: Energy as a function of compounds present

![](images/9781400830282_218-1.png)

We’ll rely on a rather complicated function that gives the energy produced by a chemical reaction based on the presence or absence of three compounds. Each of these three chemical compounds, *A, B,* and C, can be assigned a value of one if it is present and zero if it is not present. The function mapping compounds to outcomes looks as follows:

**Energy Produced:** *E* = 2 *A* + *B* + *C* − 2 *AB* − 2 *AC* − 2*BC* + 4 *ABC*

It’s functions like this that give math a bad reputation. But just as beauty is in the eye of the beholder, so is ugliness. So we must hang in there; we’ll turn this into a swan in just a page. To apply this ugly-looking function, we just plug in the values of *A, B*, and *C*. Fortunately, these variables take only two values, 0 and 1. So, if *A* = 0, *B* = 1, and *C* = 1, the value of the function equals *B* + *C* − 2BC, which equals 0(1 + 1 − 2).

We consider here a crowd of two children, Orrie and Cooper, with deep interests in scientific phenomena. We assume that they have no idea how complicated this function is. They’re just trying to predict outcomes. Orrie’s predictive model considers only the presence of the first compound A. To determine his prediction of total energy, we need first to determine total energy for each combination of compounds (see [table 8.11](#c08tab11)).

TABLE 8.12: Energy versus predicted energy

![](images/9781400830282_219-1.png)

In the cases where *A* is present, the average energy produced equals 1.5. In the cases in which *A* is not present, the average energy produced equals 0.5. Orrie’s predictive model, therefore, would be as follows:

**Orrie’s Predictive Model:** *EO* = 0.5 + *A*

This looks nothing like the original function. But then again, Orrie’s just a kid.

The second member of the crowd, Cooper, relies on a different perspective. He’s known for his unique way of looking at things. Rather than consider the chemical compounds alone, he looks at the combinations of compounds present. He then uses an interpretation that considers only whether the number of compounds included is even or odd. Based on this construction, his predictive model looks as follows:

**Cooper’s Predictive Model:** *EC* = 0.5 *if A* + *B* + *C is even and EC* = 1.5 *otherwise*

Again, this appears to have no resemblance to the ugly formula they’re trying to predict. Orrie and Cooper’s joint prediction equals the average of their two predictions. Our expectations here should be pretty low. [Table 8.12](#c08tab12) shows their average prediction and the actual energy level for each combination of compounds.

Incredibly, Orrie and Cooper predict four of the eight cases perfectly and miss by only one-half on the other four. This occurs despite the simplicity of their models and the complicated underlying function that they are trying to predict. How does this happen? Here the crowd seems far wiser than either member.

Their amazing accuracy can be explained by the diversity of their perspectives. Orrie’s considers the compounds present. Cooper’s considers combinations of compounds.[14](9781400830282_epub_nts_r1.htm#c08-ftn14) We see the magic of diverse perspectives when we translate Cooper’s predictive model into Orrie’s *A, B, C* perspective. It looks like a swan.

**Cooper’s Predictive Model:** *EC* = 0.5 + A+ *B* + *C* − 2 *AB* − 2 *AC* − 2 *BC* + 4 *ABC*

Checking this takes a little effort, but any odd number of compounds gives a value of 1.5 and any even number gives a value of 0.5. Despite how complicated this formula looks, Cooper is not doing anything sophisticated. He’s just counting the number of compounds and determining whether it is even or odd. Yet when written in the other perspective, his model appears complicated and it eerily approximates the true function. If we average this with Orrie’s predictive model, we get the Crowd’s Predictive Model:

**Crowd’s Predictive Model:** *E* = 0.5 + *A* + 0.5*B* + 0.5C − *AB* —*AC* − *BC* + 2 *ABC*

As in our example of hot dog sales on the Jersey shore, here again, the coefficients are crude approximations of the real values. But these crude approximations allow the crowd to predict with amazing accuracy.[15](9781400830282_epub_nts_r1.htm#c08-ftn15)

What we have just seen is that the crowd’s predictive model can be complicated if it combines two simple predictive models based on diverse perspectives. This reinforces a point that we made in the chapter on perspectives. What is easy to represent (i.e., linear) in one perspective may be complicated to write in another perspective. So, crowds of unsophisticated people might be able to predict a complicated function if they use interpretations based on diverse perspectives.

We will next see that predictive models based on clumping interpretations can play a similar role. These also can capture interactions between variables. Recall Deborah’s predictive model from Screening Success. To turn the example from Screening Success into a mathematical function, we need only represent the sex and violence attributes that range from none to high with the numbers 0 to 3. We then let *S* and *V* denote these values for a particular screenplay. If we assign an outcome value of 1 to a profitable screenplay and a value of 0 to an unprofitable one, then (with quite a bit of effort) we can write Deborah’s predictive model as follows:[16](9781400830282_epub_nts_r1.htm#c08-ftn16)

**Deborah’s Predictive Model:***V* = ![](images/9781400830282_221-1.png) (3S2 *V* + 3SV2 − S2 V2 − 9SV— S2 − V2 + 3S + 3V)

This equation is hideous. And that’s the point. Predictive models based on clumping interpretations include interaction terms. By definition, clumping combines variables. For this reason, good clumping interpretations may be difficult to explain. Emerson was right: to be different often is to be misunderstood.

This potential for diverse perspectives (such as Cooper’s) and clumping interpretations (such as Deborah’s) to include interactive effects suggests a nearly magical property of diverse predictors: simple, diverse models can be sophisticated. To contrast this with the No Free Lunch Theorem, which states that no heuristic is better than any other across all problems, let’s call this the *Crowd’s Possibly Free Lunch Theorem*.

**The Crowd’s Possibly Free Lunch Theorem:** *Clumping interpretations and interpretations based on diverse perspectives result in predictive models that include interactive effects. A crowd of these predictive models can sometimes predict a complicated function*.

We will call this the possibly free lunch because we have no guarantee that these interaction terms will be the appropriate ones, and, by the crude approximation property, we know that the crowd’s model’s coefficients of these interaction terms err as well. Even so, there remains the possibility, as was true in the last example and in Screening Success, that the sublime is possible.

GROUPS VERSUS EXPERTS
---------------------

We have seen how crowds can make accurate predictions, but often the relevant comparison is between a crowd and an expert. We talk about this more later in the book. Who should decide—a diverse group or a lone expert? Should Warner Brothers hire someone to predict DVD sales of a movie or should they just have forty people in the firm make off-the-cuff predictions? Should the government hire an office of people to predict the budget surplus or deficit or should they just create a prediction market on the Web?

Our analysis up to now has given us some insight into the tradeoff between the crowd and the expert. The crowd’s predictive model will include lots of attributes and possibly even interactions among these attributes, but the coefficients that it places on them will be crude. Relatively speaking, the expert’s model will be more elaborate than any member of the crowd’s individual model but starker than the crowd’s collective model. Though the expert will include fewer variables and fewer interaction terms, we can assume that the expert’s estimates of the coefficients will be more accurate.

To deepen our understanding, we begin by investigating when the expert’s predictive model is more accurate than the crowd’s. This will always be true if the expert’s interpretation refines each crowd member’s interpretation. When this happens, we say the expert *dominates the crowd*.

*An expert* **dominates the crowd** *if any set in any member of the crowd’s interpretation contains a set in the expert’s interpretation*.

This condition implies that the expert’s model contains any attribute or interaction among attributes that a member of the crowd includes in his predictive model. Or, in less technical language, the expert parses reality more finely on every attribute than does any member of the crowd.

TABLE 8.13: Suebee’s interpretation and predictions

![](images/9781400830282_223-1.png)

The next claim states that an expert who dominates the crowd predicts more accurately, on average, than the crowd.

**The Dominance of Experts:** *The predictive model of an expert who dominates the crowd is more accurate (has a smaller squared error) than the crowd’s predictive model*.

The logic of this claim is easy to comprehend. Within any set in her interpretation, the expert minimizes the squared error. The crowd’s sets lump together sets of the expert, so the crowd can, on average, do no better than make the same prediction as the expert. Often, the crowd will fail to do that. Thus, the expert must predict more accurately on average.[17](9781400830282_epub_nts_r1.htm#c08-ftn17)

Now we hit on a subtle point. Even though the dominant expert does better on average, the expert won’t be more accurate in every case. Moreover, we can find patterns in those cases when the crowd predicts more accurately.

Let’s imagine a bowling tournament with fifteen participants whose last names conveniently begin with the letters *A* through *O*. Each person has an average bowling score somewhere between one hundred ten and two hundred fifty. In this example, the higher the letter that begins the person’s name, the higher that person’s average. We compare the ability of an expert, Susan, who goes by the funkier name of Suebee, against that of a crowd consisting of a certain Larry, Moe, and Curly. We will set this up so that Suebee dominates this crowd of stooges. Suebee partitions the participants into five sets of size three (see [table 8.13](#c08tab13)).

TABLE 8.14: Larry’s interpretation and predictions

![](images/9781400830282_224-1.png)

TABLE 8.15: Moe’s interpretation and predictions

![](images/9781400830282_224-2.png)

Larry’s interpretation creates three sets (see [table 8.14](#c08tab14)). He lumps together Suebee’s sets number two, three, and four.

Similarly, Moe lumps together Suebee’s sets number one and two, and number four and five. He considers Suebee’s set three separately (see [table 8.15](#c08tab15)).

Finally, Curly lumps all five of Suebee’s sets into one set. Thus, Curly predicts that everyone will bowl a one hundred and eighty game. One could do worse. At least he’s got the average correct.

Notice that each set in Larry’s, Moe’s, and Curly’s interpretations contains a set in Suebee’s. Thus, Suebee dominates the stooges, as we had desired. This does not mean that Suebee is always more accurate. [Table 8.16](#c08tab16) shows the predictions of Suebee and the crowd for each of the fifteen possible bowlers, as well as the more accurate predictor. The horizontal lines delineate the sets in Suebee’s interpretation.

Even though Suebee dominates the crowd, she predicts more accurately than the crowd in only ten of the fifteen cases. The crowd predicts better in two of the fifteen cases, and in three of the cases, the stooges and Suebee make equally accurate predictions. Thus, even a dominant expert can be less accurate than a crowd of stooges. The possibility that a not-so-wise crowd can predict more accurately than a dominant expert should lead us to be suspicious of collections of anecdotes of wise crowds. We can always find cases where crowds did better than experts. The ease with which one can accumulate anecdotes (especially with the Internet) explains why social scientists place such emphasis on systematic evidence.

TABLE 8.16: Suebee versus Larry, Moe, and Curly

![](images/9781400830282_225-1.png)

Let’s return to the example. A careful look at the table reveals a pattern to when the stooges predict more accurately than Suebee. The stooges predict more accurately only when the outcome lies between Suebee’s prediction and the average outcome. For example, the stooges predict bowler *F*’s score to be 165 when his actual score is 160, whereas Suebee predicts a score of 150. The stooges’ prediction lies halfway between the mean score of 180 and Suebee’s prediction of 150. This bias toward the mean occurs because of the stooges’ crude interpretations.

*A Crowd of Projection Interpretations against an Expert*
---------------------------------------------------------

Our analysis of Suebee and the stooges shows how even crowds of moderately accurate models can hold their own against much more sophisticated experts. Clearly though, allowing the expert to dominate the crowd stacks the deck in favor of the expert. So, we now put the crowd on more equal footing with the expert. We do this by extending our previous example of predicting hot dog sales on the Jersey shore, by systematically varying the ability of the expert and crowd members and making some comparisons.

We start by assuming that our expert constructs a predictive model based on *E* of the ten attributes. The bigger is *E,* the more sophisticated the expert. If *E* = 6 and if the expert considers the first six attributes, then the expert’s predictive model could be as follows:

![](images/9781400830282_226-1.png)

In contrast, we assume that each person in the crowd constructs a predictive model based on *C* randomly chosen attributes. We make sure that *C < E;* otherwise, the members of our crowd are more expert than the expert. We can then run experiments varying *C* and *E*. The bigger *C,* the wiser the crowd. The bigger *C* relative to *E,* the more likely the crowd is more accurate.

[Tables 8.17](#c08tab17) and [8.18](#c08tab18) compare the crowd against an expert. In [table 8.17](#c08tab17), *C* varies while *E* remains fixed at eight. In [table 8.18](#c08tab18), *E* varies while *C* is held constant at four.[18](9781400830282_epub_nts_r1.htm#c08-ftn18)

These two tables show what we expect. The more sophisticated the people in the crowd, the better the crowd predicts. And the more sophisticated the expert, the better the expert predicts.

TABLE 8.17: The informed expert versus crowds of varying ability (E = 8)

![](images/9781400830282_227-1.png)

TABLE 8.18: The informed expert versus crowds of varying ability (E = 8)

![](images/9781400830282_227-2.png)

*The Overfitting Paradox*
-------------------------

These examples beg an intriguing question: why doesn’t the expert just include more attributes in her model? The expert could then have coverage over the attributes. If the expert also made precise calculations of the effects of each attribute and combination of attributes, then she would predict more accurately than any crowd because of the crudeness of the crowd’s predictive model.

Would that this were possible. Unfortunately, this logic suffers from three flaws, and as a result, we always need crowds. First, it assumes that the expert writes down her model and performs a careful regression. Otherwise, all of the usual arguments about cognitive constraints and biases might cause her to predict even less accurately if she took in too much information. Second, it fails to take into account the possibly free lunch. It could be that the crowd members’ models rely on multiple perspectives and clumping interpretations. If so, the expert may not be able to construct a model as sophisticated as the crowd’s. This possibility exists, but it is probably not one on which someone advocating the use of crowds would want to hang his hat. The free lunch is possible, but we have no reason to think it always exists.

Third, and most important, the logic assumes that sufficient data exist and that the expert has access to them. In practice, the expert may not be able to construct a sophisticated model with lots of attributes. Without sufficient data, if the expert considered all of the attributes, she would overfit her predictive model.

Overfitting means that the predictive model uses too many variables relative to the amount of data *and* tries to estimate the coefficients for those attributes precisely. Doing so runs the risk of getting inaccurate estimates. An example helps us see what we mean by overfitting.

Suppose that a consulting company hires an expert, Magda, fresh from a top MBA program. The company assigns her the crucial task of predicting the number of waffles to make for the company breakfast. This company consists of a group of slothful partners who demand that their young associates work long hours and stay in great shape. The true model of how many waffles *W* that need to be made is as follows:

*Waffle Reality: W* = 4 *P* + 2 *A* + *F*

where *P* denotes the number of partners, *A* is the number of associates, and *F* equals the number of waffles dropped on the floor.

Our interest here is in overfitting, so we don’t want to give Magda much information on which to base her model. So we assume that Magda has only two data points from which to construct her predictive model: the April breakfast and the March breakfast. At the April breakfast, ten partners and twenty associates attended and no waffles fell on the floor. If we do the math, we learn that eighty waffles were made.[19](9781400830282_epub_nts_r1.htm#c08-ftn19) At the March breakfast, fifteen partners and fifteen associates attended and fifteen pancakes fell on the floor. This requires 105 waffles. Let’s assume that Magda’s predictive model includes the number of partners and the number of associates, but not the possibility of waffles falling to the floor. It therefore takes the following form.

*Magda’s Predictive Model: W* = β*P* + α*A*

With a little effort, we can show that Magda’s predictive model can be written *W* = 6 *P* + *A.[20](9781400830282_epub_nts_r1.htm#c08-ftn20)* If we plug in the numbers, we see that her model perfectly fits the existing data. However, it fails as a predictive model because she has overfit the data. The true coefficients are not anywhere close to six and one.

Next, we construct a model for a crowd. Our crowd contains only two people: Josh and Anna. Josh’s model takes into account the number of partners, and Anna’s takes into account the number of associates. Using the same data, we get the following predictive models:[21](9781400830282_epub_nts_r1.htm#c08-ftn21)

*Josh’s Predictive Model: W* = 7.4 *P*

*Anna’s Predictive Model: W* = 5.3 *A*

If we average these two models, we get the crowd’s predictive model

*The Crowd’s Predictive Model: W* = 3.7*P* + 2.65 *A*

The crowd’s predictive model more closely approximates the true function: 4 *P* +2 A+ *F*. Most of the time it will be far more accurate than Magda’s.[22](9781400830282_epub_nts_r1.htm#c08-ftn22)

What went wrong with Magda’s estimate? In including both partners and associates together, Magda underestimates how much the associates eat. This occurs because at the first breakfast, more associates than partners attend, but fewer waffles fall on the floor. Therefore, she cannot but infer that associates do not eat many waffles.

This example speaks to a larger issue. Some econometricians believe that models with more than a few variables are dubious, precisely because of this problem.[23](9781400830282_epub_nts_r1.htm#c08-ftn23) Models with only a handful of variables suffer no such problems. Yet we can add up those simple models and in doing so create a larger model. That aggregate model will not suffer from overfitting. And it may be a better predictor. However, it will be only a crude approximation.

Why don’t experts average over multiple models? One answer is that often the expert’s goals go beyond just prediction. They also want to explain the effects of attributes. An expert might want to know the effect of education on income as well as predict income levels as accurately as possible. A second answer is that they do, and they have done so for a long time. The idea of combining forecasts became popular among economists in the 1970s.[24](9781400830282_epub_nts_r1.htm#c08-ftn24) As computer power has increased, the combining of multiple models has become a well-established approach to making predictions. These *ensemble methods,* as they are called, often prove more accurate than any of the models within them.[25](9781400830282_epub_nts_r1.htm#c08-ftn25) We know that the average of models must be better than the average model by the Crowd Beats the Average Law, but we cannot be certain it beats the best, though often it does.

Ensemble methods need not assume equal weighting of the models, though equal weighting is a good benchmark. One approach used to improve on equal weighting relies on Bayesian statistics. This approach, Bayesian Model Averaging, averages across possible models but chooses weights based on the likelihood that each model is correct given the data.[26](9781400830282_epub_nts_r1.htm#c08-ftn26) Unlike with crowds of people, crowds of statistical models can get only so big (at least at the moment). Computation takes too much time if more than twenty or so models are combined. Bayesian model averaging is not the only way to weight the models. Another popular approach, bootstrap aggregation, or bagging, adds weight to models that catch the errors of the other models.[27](9781400830282_epub_nts_r1.htm#c08-ftn27) As we see next, weighting models by accuracy has advantages, and, as we also see, markets create incentives for this to happen.

INCENTIVES: POLLS VERSUS INFORMATION MARKETS
--------------------------------------------

Polls weight everyone’s predictions equally, even the bad ones. A better method would be to weight models according to their accuracy. Information markets can place more weight on some models than on others.[28](9781400830282_epub_nts_r1.htm#c08-ftn28) In an information market, people bet money. Those people who believe their predictive models to be accurate can place larger bets and those who are unsure can bet less. Incentives drive out the less accurate predictors. Markets also reduce incentives for people to make different predictions. If some other intelligent person thinks that the stock price is below what you think, then you should probably lower your prediction. In fact, if there exists common knowledge of both rationality and optimizing behavior, then all predictions should be the same.[29](9781400830282_epub_nts_r1.htm#c08-ftn29)

Let’s assume that our information market includes many participants and that participants can place bets of different sizes. Let’s also assume that the more accurate a person’s model, the larger her bet. In other words, people know when their models are accurate. In some contexts, this can be a strong assumption.[30](9781400830282_epub_nts_r1.htm#c08-ftn30)If the size of the bet and predictive accuracy are positively correlated, information markets would seem to have an advantage over equally weighted voting, but that’s not necessarily true. We can see why using the Diversity Prediction Theorem. Under the assumption that more accurate predictions get more weight, the average accuracy of the predictions increases. However, the diversity of the predictions may decrease. The answer as to whether the information market produces a more accurate prediction than a poll (an averaging of all of the model) hinges on whether the increase in average ability outweighs the decrease in diversity.

Think back to our comparison of crowds versus experts. We can consider the expert to be a crowd that places all of its weight on its best predictor. In many instances, the expert fails to predict as accurately as the crowd because loss of diversity more than offsets the gain in accuracy. Placing all weight on a single predictor is an extreme case, as is giving all equal weight. Information markets lie between these two extremes. Does this mean that they predict better? The answer depends on the weighting. One condition that often ensures the gain in accuracy exceeds the loss in diversity is that highly inaccurate predictors drop out of the information market. We call this the *Fools Rush Out* condition.

TABLE 8.19: Poll, expert, and information markets, 2005 NFL draft

![](images/9781400830282_232-1.png)

**Fools Rush Out:** *People with highly inaccurate predictive models answer poll questions but do not wager money in information markets*.

If the most inaccurate models leave, the gain in accuracy can be substantial. Though some diversity is lost, that loss will be offset by the accuracy gain.[31](9781400830282_epub_nts_r1.htm#c08-ftn31) To see this in an example, let’s return to our NFL draft data. Let’s assume that the two least accurate predictors lack the confidence to enter the information market. They rush out of our information market. We consider two weighting schemes after we have dropped these least accurate predictors. In the *equal weighting* scenario, the remaining predictors all place equal sized bets. In the *weighted bets* scenario, the predictors place bets proportional to their rank. The best predictor gets a weight of five, the second best a weight of four, and so on, with the worst predictor assigned a weight of one. [Table 8.19](#c08tab19) shows the squared errors from poll (the crowd’s prediction), the best individual predictor, Clark Judge (whom we call the expert for the purposes of this analysis), and the information markets’ predictions under the two scenarios.

The best expert, Clark Judge, fares worst overall and the weighted bets scenario performs best. Interestingly, the poll of all seven predictors does better than the poll of the best five. This example shows that even though dropping the worst predictors put more weight on more accurate models, it can reduce diversity and collective performance. We have to be careful not to read too much into this one example, but it vividly reinforces that ability and diversity merit equal weight.

*The Double Power of Incentives*
--------------------------------

Information markets create incentives for less confident people to stay out, and for confident people to bet more. Both incentives can improve aggregate predictions as long as they are not too powerful. Otherwise, only the single most accurate predictor bets. Thus, we should include incentives but only in moderation. Tempering incentives may be difficult for some economists. Economists love incentives the way that botanists love plants. (And rightly so.) Incentives are powerful forces. They give information markets huge advantages over polls. They’re why free markets work. But we must keep them in check to maintain some diversity. We want to toss out some of the bad models but not all of them.

Incentives also operate in a deeper, more subtle way that we have yet to discuss. In many information markets, payoffs depend not only on being correct but also on the probability that other people are correct. If you are the only person who bets on a particular horse to win a race, your payoff is much larger than if a majority of people bet on that horse. This negative correlation between winnings and the number of people making the winning prediction occurs because the markets have to be balanced: the amount paid out must equal the amount bet. (At the horse races, only a percentage of the money bid is paid back, but the logic still applies.) So if one person predicts correctly, she gets all the money. If a thousand people predict correctly, they must split the money one thousand ways.

This the-larger-the-upset-the-bigger-the payoff feature of many markets creates an incentive to construct diverse predictive models. Suppose that you could construct a model that predicts correctly when most other people are wrong. That model would generate large payoffs on average because when it predicted correctly, the winnings would be split only a few ways. Thus, markets create two incentive effects that polls lack: *an incentive to be correct and an incentive to be diverse*. Both effects improve collective predictive ability. By predicting correctly, a person makes money. By predicting diversely, a person makes even more money.

All this talk of money is a bit crass. Money is only one coin of the realm. Prediction markets can also pay out in reputations. Consider our NFL draft experts. One reason that their predictions differed as much as they did may well have been because of the incentives for diversity. These predictors compete in a market for our attention. So each prognosticator has incentives to make predictions that run counter to the consensus.

THE CROWD OF MODELS
-------------------

A summary of this chapter might read like this: for a crowd to be wise its members must be individually smart or collectively diverse. Ideally, they would be both. And sometimes, when their members’ models rely on diverse interpretations, crowds can even enjoy a free lunch. Simple, diverse predictive models can form sophisticated crowd-level predictions. These crowds can perform better than experts, provided their increased coverage more than makes up for the crudeness of their estimates. This surely happens when one of the attributes or variables considered by the crowd and ignored by the expert takes on an unexpected value. And if instead of polling the crowd, we create an information market so that people can place bets of various sizes, we can make the crowd even more accurate. Market incentives can drive out the least accurate predictors and place more weight on the more accurate ones, so long as the accurate predictors know that they are accurate. Both of those effects would seem to lead to greater crowd accuracy, but we can take that logic too far. If only the best predictors remain or get most of the weight, we end up with a single expert who may not be better than the crowd. Finally, if people know that an information market will be used, they have incentives to be diverse as well as accurate. This further improves the performance of the crowd.

All of this leads to the conclusion that ideally we would have a *crowd of models* competing in a market. The best predictions should come from collections of diverse models. These models should parse reality differently. They should rely on interpretations based on diverse perspectives that look at different attributes in the same perspective, or interpretations that slice up the same perspective into different clumps. If so, each model will be accurate, and the collection of models will be diverse. This combination of accuracy and diversity makes for a wise crowd.

The recipe for creating a crowd of models might look as follows: create incentives for a collection of people with diverse (and relevant) identities, experience, and training, and add in a few wild cards. Training in chemistry may be less relevant than training in sociology or psychology if predicting which of five marketing plans to pursue, but adding a chemist guarantees some diversity. Then create incentives for those people to construct models— not necessarily mathematical or empirical models, but coherent predictive models. Do not train them in how to think about the problem; that would destroy their diversity. Finally, create an entry barrier, so that only those who think that they can make a reasonable prediction join the crowd. The crowd need not be large. It could contain only seven or eight people. With smaller crowds, such as management teams, juries, hiring committees, boards of directors, and the like, making efforts to ensure that people use diverse models may be even more important. With a larger crowd some diversity is almost sure to be present. Eighty-seven people are not likely all to think alike, but eight might.

Individuals can also amass their own crowds of models. Some of the best investors on Wall Street do exactly this. In fact, the legendary Charlie Munger, who, along with Warren Buffett, made Berkshire Hathaway investors billions of dollars, bases his investment decisions on what he calls a lattice of mental models: a collection of logically coherent diverse models that combine to help him make accurate forecasts. His crowd of models, we can only surmise, is an intelligent, diverse bunch.
