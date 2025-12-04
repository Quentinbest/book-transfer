# CHAPTER 9

CHAPTER 9
=========

Diverse Preferences
===================

WHY TAPAS
=========

*Do not do unto others as you would they should do unto you. Their tastes may not be the same*.

—GEORGE BERNARD SHAW, “Maxims for Revolutionists: The Golden Rule”

WE all differ in what we prefer. Some of us like old Craftsman houses. Some of us like modern houses with open floor plans. Some of us enjoy Latin jazz. Some of us prefer heavy metal. Some of us like spicy cooked food. Some of us are vegetarian. That’s fine. That’s the reason for tapas restaurants. Little plates, lots of different stuff. As has often been said, there’s no accounting for taste.[1](9781400830282_epub_nts_r1.htm#c09-ftn1) (Less often said is the equally true claim that there’s no taste for accounting.) Though we cannot account for taste, we can model it. And in this chapter, that’s what we do.

We need to model tastes, or what we call diverse preferences, because they create problems—huge problems. If we value different ends, we may not agree on what good solutions are or what outcomes to predict. This potential for disagreement may create incentives to misrepresent how we feel. We may try to manipulate processes and agenda, creating distrust and dislike. Thus, much of the good created by a diverse toolbox might be undone by diverse values. Of course, we needn’t care about diverse preference so much if the same people who have diverse toolboxes don’t also have diverse preferences, but often they do.

To understand the severity of problems caused by diverse values, we need to see the root causes of the problems. We need frameworks and models. So, we build them. In this chapter, we learn the basics. In the next, we apply them. This treatment of preference theory is by no means complete nor is it traditional. Entire books from multiple disciplines are devoted to preferences and preference theory.[2](9781400830282_epub_nts_r1.htm#c09-ftn2) Most books present preference theory with an abundance of notation complicating the connection to the real world. We err in the other direction, forgoing variables whenever possible. This treatment is not traditional because it emphasizes the distinction between *fundamental preferences* (preferences about outcomes) and *instrumental preferences* (preferences about how we get what we want). Preferences about outcomes—fish tacos, healthy knees, or economic growth—are fundamental. Preferences about actions or policies—diets, stretching exercises, or tax policies— are instrumental. Actions are not ends in themselves; they are not outcomes, but they are the means to those outcomes.

Diverse fundamental preferences need not imply diverse instrumental preferences and vice versa. This finding has implications for how we think about preference diversity. People who have different fundamental preferences might be said to have different *values*. People who have different instrumental preferences but the same fundamental preferences have the same values but different *beliefs about how the world works*. In either case, people disagree over what policy or action to choose, but only in the first case does preference diversity create a problem. In the latter case, it can prove useful.

We highlight this distinction because diverse instrumental preferences derive from diverse predictive models. And it’s easy to confuse the two types of diversity. So even if we don’t like accounting, we have to do some. This linking of diverse predictive models to diverse perspectives offers a hint of the complexity to come. The frameworks—perspectives, heuristics, interpretations, predictive models, and preferences—can all be connected, and in many cases, diversity in one domain begets diversity in another.

PREFERENCE ORDERINGS AND UTILITY FUNCTIONS
------------------------------------------

To describe preferences, we first note that they are distinct from choices. Preferences describe how much we value or desire things. Choices are what we select. Our preferences guide our choices, and our choices reveal (partially) our preferences. When we meet someone new, we try to infer something about that person’s preferences by his choices. What clothes does he wear? What car does he drive? What does he order for lunch? You can even use your own choices as information about your preferences. In looking at a closet filled with black shirts, you might suddenly realize that you like black, or that you like Johnny Cash.

As is standard, we assume a set of alternatives about which people have preferences. These may be locations, product designs, public policies, or political candidates. They could be *outcomes* or they could be *actions* or *policies.[3](9781400830282_epub_nts_r1.htm#c09-ftn3)* That difference proves important. It is the basis for the distinction between fundamental and instrumental preferences.

The most basic way to think about preferences is to conceive of them as imposing an ordering over a set of actions, policies, or outcomes. For ease of presentation, I refer to these as the *set of alternatives. A preference relation* describes an ordering of alternatives, >. The statement *A > B* means that alternative *A* is preferred to alternative B. If, for example, Joe is asked his preferences among a burrito, a taco, and an enchilada, and if he most prefers the burrito and least prefers the taco, then his preferences can be written as follows:

*burrito > enchilada > taco*

He might also be indifferent between two outcomes. He could like burritos and tacos equally well. If so, he is indifferent between burritos and tacos, and his preferences would be written

*burrito ![](images/9781400830282_241-1.png) taco*

Preferences are typically assumed to be *rational*. The term *rational* has a formal definition. It means *complete* and *transitive. Preferences are complete if they compare any two alternatives.*

*Preferences are* **complete** *if given any two alternatives, A and B, either A > B, B > A, or A ![](images/9781400830282_242-1.png) B*.

We might think that everyone’s preferences satisfy completeness, that everyone can compare any two alternatives. Yet it is not a vacuous assumption because people often have conflicting or deep feelings about some pairs of outcomes. They either cannot or would be reluctant to make decisions among them. If someone asks you which of your parents or children you prefer, you might find the question impossible to answer.

Preferences are *transitive* if they do not admit cycles. A person with transitive preferences cannot prefer papers to rocks, rocks to scissors, and scissors to papers.

*Preferences are* **transitive** *if they do not admit cycles; for example, if apples are preferred to bananas and bananas are preferred to pears, then apples are preferred to pears*.

The condition that preferences are transitive may also seem as though it states an obvious condition in technical language. At the individual level, it does. If Ravi prefers ice cream to yogurt and prefers yogurt to tofu, then he must prefer ice cream to tofu. For individuals, transitivity usually holds. When an individual must choose from among outcomes, she is not likely to have a preference cycle unless she is not thinking clearly. In comparing alternative plans for which gift to buy her mother (an action) in order to make her happy (an outcome), Laura might think that her mother would prefer a necklace to flowers (it lasts longer), flowers to garden tools (flowers are prettier), and garden tools to a necklace (they’re more practical). This would be a preference cycle over actions, but one that should go away if Laura thought more carefully.

Though preference cycles may be rare within an individual, they are common within collections of people. In [chapter 10](9781400830282_epub_c10_r1.htm), we analyze the aggregation of diverse preferences, we see that it is possible for a group of people to violate transitivity, to have cycles, even though none of the individuals themselves do. A collection of rational people may prefer tofu to ice cream, even though they prefer ice cream to yogurt and yogurt to tofu.

*Preferences are* **rational** *if they are complete and transitive*.

An assumption of rational preferences seems reasonable. Completeness and transitivity are mild assumptions, but they severely restrict the amount of preference diversity that can exist. To see this, we work within a restricted framework that rules out indifference, that is, we do not allow people to be indifferent between two alternatives.

In what follows, we consider preferences about five possible actions with respect to a man’s facial hair: *a goatee, muttonchops, a mustache, a full beard,* and *a Van Dyke beard*. These could also be thought of as outcomes, but we want to think of these as actions that create an outcome called attractiveness. Preferences about attractiveness would surely satisfy *monotonicity*. People prefer to be more attractive. A rational preference relation without the possibility of indifference creates a complete ordering, a ranking, over the alternatives from best to worst. One such ranking would be the following:

*full beard > goatee > Van Dyke > mustache > muttonchops*

We can calculate the total number of such orderings as follows. Any of the five facial hair styles can be ranked first, leaving four that can be ranked second, three that can be ranked third, two that can be ranked fourth, and one that can be ranked last, or be least preferred. The total number of such orderings equals 5 \* 4 \* 3 \* 2 \* 1, or 120. If we up this to twenty alternatives, we get more then two million, billion orderings; that’s why we’re considering only five alternatives.

We can compare our 120 rational orderings to the number of possible irrational preference relations. Notice that we say relations and not orderings. The word *ordering* makes no sense when preferences are irrational. Irrational preferences do not necessarily order all of the alternatives. We first relax the transitivity assumption. This implies that for each pair of alternatives, a person still must have a preference, but it places no restriction on cycles.

![](images/9781400830282_244-1.png)

To compute the number of preference relations that are not transitive, we begin with these ten pairs of facial hairstyles. For each pair, one of the two must be chosen. That creates two times two times two… (ten times), or two to the tenth power, possible preference relations. Two to the tenth power equals 1,024. Almost ten nontransitive preference relations exist for each of the 120 rational preference orderings. Most of these preference relations contain cycles (904 of them, to be precise.) Here is one: mustache is preferred to muttonchops which are preferred to the Van Dyke, but the Van Dyke is preferred to the mustache.

Were we also to allow preferences to violate completeness, we would get an even larger number of possible preference relations. Now for each pair of alternatives, in addition to either being preferred, it could also be that the alternatives are noncomparable. This creates three possibilities for each pair of alternatives. With five alternatives (and, therefore, ten pairs of alternatives) the number of preference relations that violate both transitivity and completeness equals three (not two) raised to the tenth power, 59,049, or nearly five hundred times as many as the number of rational preference orderings.[4](9781400830282_epub_nts_r1.htm#c09-ftn4)

These calculations demonstrate the many ways to be rational. They also show the many, many more ways to be irrational. They have implications when we study preference aggregation. Collections of people need not have transitive or complete preferences. The billions of preference orderings that an individual might have over a set of twenty alternatives are a mere drop in the bucket compared to the number of irrational preference relations that a collection of people might have.

SPATIAL PREFERENCES
-------------------

Up to now, the alternatives were arbitrary, so we had no reason to attach any significance to preferring *A* to *B* or *B* to A. But suppose that we construct a *perspective* of these alternatives. Sometimes creating a perspective is easy. If we were to analyze how much people enjoy work, play, and sleep, we might describe an outcome as a vector *(work, play, sleep)* where the three variables denote the time spent working, playing, and sleeping, respectively. Decompositions like this into separate dimensions are a common approach in economics and political science.

Other times, representing alternatives in a perspective becomes complicated. Consider someone’s preferences for food. Listing the particular food items, such as nachos, sushi, and pretzels, would be cumbersome. We could create *dimensions* that characterize food items based on ingredients. In the Ben and Jerry’s example, this worked great. The number and size of chunks characterized the pints of ice cream. These two dimensions allowed Ben and Jerry to make a *spatial* representation of the various pints. However, this won’t always work. Many of the items at Taco Bell contain the same ingredients in the same proportions. A taco salad is just a taco in a new arrangement.

But let’s suppose that we can map the alternatives to a single-dimensional perspective. We can then distinguish between three types of preferences along that dimension. In defining each type, we take the other dimensions as fixed and ask what happens to preferences as we vary the level on one dimension. The first type of preference applies to those dimensions for which more is better.

*Preferences are* **increasing** *if more is always preferred to less*.

Preferences about money are usually assumed to be increasing. More money is better. Preferences are also increasing about health, gas mileage, and computer speed.

The second type of preferences apply to things that people do not like, such as pollution or noise, for which less is better.

*Preferences are* **decreasing** *if less is always preferred to more*.

Preferences about pollution are decreasing, as are preferences about the amount of time spent doing our taxes.

For most things, including sleep, salmon, and software, more is not always better and neither is less. We like more up to a point, and then we like less. Consider the size of an ice cream cone. One scoop is nice. Two are better. Three may be a bit much. And four borders on outrageous (unless you happen to be fourteen years old). We call such preferences *single-peaked* because graphical representations of our happiness, or what economists call utility, have a single peak. We call the amount that provides the highest utility the *ideal point.[5](9781400830282_epub_nts_r1.htm#c09-ftn5)*

*Preferences are* **single-peaked** *if there exists an* **ideal point**. *If the current amount is less than the ideal point, more is preferred. If the current amount is more than the ideal point, less is preferred.*

The powerful implicit assumption in the spatial formulation is that the dimensions used to define the alternatives, as defined by the *perspective,* capture those attributes of the alternatives that drive preferences. Otherwise, the assumptions of increasing, decreasing, or single-peaked preferences do not make sense. Think back to the masticity-based perspective on ice cream. Masticity was a measure of how long it took to chew a spoonful of ice cream. Most people would not have increasing, decreasing, or single-peaked preferences about masticity. This discussion reiterates a point made at length earlier: making sense of the world, in this case making sense of preferences, requires a good perspective.

![](images/9781400830282_247-1.png)

Figure 9.1 The Space of Sno-Cone Colors

![](images/9781400830282_247-2.png)

Figure 9.2 An Ideal Sno-Cone

*Raspberry and Bubble Gum Sno-Cones*
------------------------------------

Spatial representations of the set of alternatives, combined with assumptions that structure preferences, limit the number of possible preference orderings. To see this, consider preferences about the color for raspberry sno-cones. First some background for those unfortunately not in the know about raspberries and sno-cones. In the wild, raspberries can be black, red, and even yellowish orange. Raspberry-flavored sno-cones vary in color as well. In some regions of the United States, you will find dark red raspberry sno-cones. In others, you will find that they are light blue. Had we the time and energy, we might even make a map of the country coloring some states red and other states blue depending on the more common color of their raspberry sno-cones. (Maps of red and blue states are important to political scientists.)

Here we consider preferences within Ohio, a blue state, at least for raspberry sno-cones. We represent the range of possible blue colors on a line with light blue (denoted by L) on the left, and royal blue, denoted by R, on the right (see [Figure 9.1](#c9fig1)).

Each Ohioan has an *ideal point,* a color that she most prefers. A person with an ideal point *L* (resp R) has a decreasing (increasing) preference, and a person with an ideal point in the interior has a single-peaked preference. In what follows, distance to the ideal point determines preference: the closer a color lies to a person’s ideal color, the more the person prefers that color. Though not necessary, this assumption simplifies the presentation. [Figure 9.2](#c9fig2) shows a person’s ideal point at X.

![](images/9781400830282_248-1.png)

Figure 9.3 Five Alternative Sno-Cones

![](images/9781400830282_248-2.png)

Figure 9.4 Brenda’s Preferences

We now explore the implications of our three assumptions: (i) that the alternatives can be placed on a single line, (ii) that people have ideal points, and (iii) that preferences about alternatives are determined by the distance of the alternatives from the ideal point.

To see the restrictiveness of these assumptions, let’s consider the task of assigning a color to bubblegum sno-cones. Bubblegum sno-cones could be any color. We won’t use all of the colors—just the familiar ROYGB (red, orange, yellow, green, and blue) arranged along the spectrum. To make the comparison exact, we place these five colors on a line (see [Figure 9.3](#c9fig3)).

Suppose that Brenda most prefers the color orange. Her ideal point could be right at O; it could lie between *R* (red) and *O* or it could lie between *O* and *Y* (yellow). Let’s suppose that her most preferred color lies between *O* and Y. For the purposes of this example, we assume that the colors are evenly spaced on the line and that Brenda’s preferences about colors depend on the distance from the color to her ideal point. If we look at [Figure 9.4](#c9fig4), we see that she must then prefer yellow (Y) to red (R), and she must also prefer red to green (G) and green to blue (B).

Thus, once we place her ideal point on the line, we uniquely define her preferences and limit preference diversity. We can calculate how many possible preference orderings can exist if we represent preferences on a single line. As before, we rule out ties. If a person most prefers red, she must like orange second best, then yellow, then green, and then blue. A person who most prefers blue must have preferences that go in the opposite order. Someone who most prefers orange could like yellow next best (as in our example above) or could like red next best. Either way, once we know her second favorite color, we know her full preferences. Therefore, two preference orderings have orange as the favorite color. The exact same logic applies to preferences that rank green or yellow first.[6](9781400830282_epub_nts_r1.htm#c09-ftn6)

Adding up all of these possibilities: only one preference ordering each for red and blue being ranked first, and two each for the other three colors, makes a total of only eight possible spatial preference orderings. If we relax the equal spacing assumption, then with a little effort we can see that only fifteen possible orderings exist. Either number is small when compared to the 120 possible rational orderings, the 1,024 intransitive relations, and the 59,049 relations that are neither complete nor transitive.

Thus, we see that assuming single-dimensional preferences reduces the number of possible preference relations—just as does imposing completeness and transitivity. If we increase the dimensionality of the perspective—say, moving from a line to a square— we allow for more preference orderings. The higher dimensional the perspective needed to make sense of preferences, the more diverse rational preferences can be. We might ask if we can always represent preferences spatially. We can, but we might have to make the number of dimensions large. It may even have to equal the number of alternatives.

*Getting More Serious*
----------------------

We may disagree about what we believe to be pressing problems. Some of us believe it to be poverty, others believe it to be environmental sustainability, and still others believe it to be international stability. No one believes it to be selecting a type of beard or the color for a sno-cone. What we learn from fun examples, though, also applies to more serious contexts.[7](9781400830282_epub_nts_r1.htm#c09-ftn7) And we can think of the one dimension as representing an ideological spectrum from left to right. In fact, the sno-cone model provides a logical foundation for much of how we think about political ideologies. When we describe senators or congressional representatives as liberal, conservative, or moderate, we are placing them on a line.

These one-dimensional ideologies can be thought of as an interpretation. We can use this interpretation to construct a model to predict how representatives will vote on a bill. That crude predictive model works well. If we add a second ideological dimension, then we can do even better.[8](9781400830282_epub_nts_r1.htm#c09-ftn8)

INSTRUMENTAL PREFERENCES
------------------------

Now that we have seen two basic preference frameworks— one based on orderings and one based on spatial representations— we turn to the distinction between fundamental and instrumental preferences, which is a big reason we’re studying this in the first place. This distinction can be alternatively described as the distinction between preferences about ends and preferences about means. A person’s preference about ends might be to live a long life and to minimize his chances of getting cancer and heart disease. His preferences about means may be to eat a low-fat diet that includes lots of fruits and vegetables.

We focus here on how interpretations and predictive models influence our instrumental preferences but not our fundamental preferences. Two people can have the same values, the same fundamental preferences, but have different instrumental preferences. To show this, we’ll construct an example that includes government policies and the outcomes that those policies produce. Disconnecting ends and means is meaningful only so long as the mapping from policy choices to outcomes is difficult to infer, that is, if the mapping from policies to outcomes creates a rugged landscape. For nonrugged landscapes, even crude interpretations lead to correct predictions.[9](9781400830282_epub_nts_r1.htm#c09-ftn9)

We’ll assume that everyone has the same preferences about outcomes. This assumption is not as strong as it seems. Sure, people disagree about abortion and the right to own guns. But our preferences agree more than we think. Try to think of any politician who doesn’t claim to want a better educational system, less crime, more growth, less inequality, greater international security, cheaper health care, and enhancing sustainability. Now try to think of any two politicians who agree on how to achieve those outcomes.[10](9781400830282_epub_nts_r1.htm#c09-ftn10) One politician may claim that markets generate greater efficiency than bureaucracies and that we should have vouchers for education. Another may claim that markets benefit the wealthy at the expense of the poor and that we should not create vouchers. This political posturing on policies continues year after year, decade after decade because the policy problems remain difficult. If confronted with simple problems, voters would learn the correct policy and demand that politicians adopt it. But policy problems are rarely simple. To predict the likely outcomes of proposed policies, we rely on predictive models.

*We Reduce Crime by…*
---------------------

To see the linkage between interpretations, predictive models, and instrumental preferences as well as the disconnect between instrumental and fundamental preferences, consider policies for crime reduction. Assume that crime-fighting policies have a fiscal and a social dimension. On the fiscal dimension, each policy can be left (L), moderate (M), or right (R). The same is true for the social dimension. We distinguish the social dimension by using lowercase letters, *l, m,* and *r*.

Policies either increase crime, reduce crime, or have no effect. The policy space and the mapping from policies to outcomes look as shown in [table 9.1](#c09tab1).

So, for example, the policy *Lm* reduces crime, and the policy *Rm* increases crime. Now, let’s imagine two politicians, Arun and Rebecca, running for office. Each interprets the policy space differently. Arun sees only the social dimension of a policy. He looks at the columns. This interpretation resembles Marilyn’s interpretation in Screening Success. Given this interpretation, Arun’s predictive model looks as shown in [table 9.2](#c09tab2).

TABLE 9.1:   
A policy mapping

![](images/9781400830282_9.1.png)

TABLE 9.2: Arun’s predictive model

![](images/9781400830282_9.2.png)

TABLE 9.3:  
Rebecca’s predictive model

![](images/9781400830282_9.3.png)

Arun predicts that socially liberal policies have on balance no effect, that socially moderate policies increase crime, and that socially conservative policies reduce crime. Rebecca looks only at the fiscal dimension of a policy. She predicts that fiscally liberal policies (L to her) reduce crime, that fiscally moderate policies have no effect, and that fiscally conservative policies increase crime (see [table 9.3](#c09tab3)).

Suppose that Arun and Rebecca compare two policies: one that is moderate on both dimensions (*Mm)* and one that is conservative on both (*Rr)*. Rebecca predicts that the latter policy, which she interprets as conservative, will increase crime and that the first policy, which she interprets as moderate, will have no effect. Arun predicts that the conservative policy will reduce crime and that the moderate one will increase it.

In this example, Arun and Rebecca have identical preferences about outcomes—they both want reductions in crime—but their diverse predictive models lead them to have opposing policy preferences. Arun prefers the conservative policy, and Rebecca prefers the more moderate one. This example, more than any other in this chapter, reveals the interplay between preferences and tool boxes. Think back to the landscape metaphor where high elevations represent better solutions. Arun and Rebecca don’t agree on which end is up in policy space even though they want the same outcome.

LINKING PREFERENCES AND TOOLBOXES
---------------------------------

We have just seen how diverse interpretations can result in diverse instrumental preferences. The causality can also go in the other direction. Diverse preferences, in this case fundamental ones, can result in differences in interpretations. How a politician interprets a welfare policy depends on his preferences. How a businessperson interprets a strategic plan or a potential product launch depends on her preferences. College applicants who want to study drama look at schools differently than do physics applicants: In considering a school such as Carnegie Mellon University, which is strong in both disciplines, students interested in drama ignore the computer facilities and laboratory spaces, attributes that budding physicists find of utmost importance.

Our brains are not large enough to keep track of everything we need to know. We look at what is important to us. When what we look at is large, metaphorically, when it has many parts and dimensions, we abandon perspectives for interpretations. We can have a perspective on a route between ten cities. But we cannot have a perspective on the design for the car we drive between those cities. As a result, for most problems, the dimensions we include depend on what we value. The link between what we prefer and what we notice is so obvious that it requires little elaboration.

How we experience events or draw aesthetic pleasure from them is a function of our knowledge of what we see and experience. The dimensions that we see and experience are partly choice-driven, though not entirely so. Politicians, and some might say the media, exploit our susceptibility to manipulate how we think. But they are not alone in doing so. Writers, performers, film makers, in fact all artists, manipulate and focus our attentions to create certain understandings. Advertisers do the same thing. How else to explain our worries about gingivitis?

A related connection can be made between preferences and cognitive tools generally. The tools that people choose to acquire are those that help them achieve their preferences. People who have different preferences likely acquire different tools. People who love good food often learn tools that enable them to become excellent cooks. People who love to hike may cognitively represent regions of the country based on the number and types of trails they have. This powerful, widespread influence cast by preferences on perspectives, interpretations, and tools suggests the centrality of preferences in any discussion of diversity and its influences.
