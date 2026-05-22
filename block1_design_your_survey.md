# Design your survey: Things to bear in mind during the design phase

By Ted Barker

## Purpose

This block teaches you to design surveys that produce trustworthy data. You'll learn to design, test, and defend your survey before launch—from sampling decisions through question design, cognitive load management, stakeholder governance, and testing protocols.

Format: 80-minute taught session with integrated Activity 1 (research questions & methods matching)

## Learning Objectives

By the end of this block, researchers will be able to:

1. **Select appropriate sampling strategies** and calculate required sample sizes for their research objectives (including oversampling and statistical power considerations)

2. **Write clear, unbiased survey questions** that minimize measurement error and respondent confusion

3. **Apply the fatigue hierarchy** to reduce cognitive load, prevent dropout, and maintain data quality throughout the survey

4. **Defend survey scope** against stakeholder additions using evidence-based trade-offs between data quality and question volume

5. **Conduct effective pre-launch testing** through cognitive interviews and technical pilots that catch problems before fieldwork

## Session Flow (80 min)

| Section | Duration | Focus |
|---------|----------|-------|
| 1. Sampling | 5-10 min | Probabilistic sampling, oversampling, power calculations |
| 2. Question Construction | 10 min | Writing clear, unbiased questions |
| 3. Fatigue Hierarchy | 20 min | Cognitive load management, six strategies |
| 4. Methods + Activity 1 | 20 min | Research designs, methods matching exercise |
| 5. Governance | 10 min | Managing stakeholder question creep |
| 6. Pilot Test | 5 min | Cognitive testing and technical pilots |

---

## 1. Sampling (5-10 min)

**Core Principle:** You need probabilistic sampling to generalize your findings to the full population. Without it, your analysis can't tell you anything beyond your specific respondents.

### Three Sampling Approaches

**Random Sampling**  
Every member of the population has an equal chance of selection. Simple, unbiased, but may undersample small segments.

**Stratified Sampling**  
Population divided into subgroups (strata), then random sampling within each stratum. Ensures representation across key segments (e.g., by product type, tenure, geography).

**Oversampling**  
Deliberately sample more from underrepresented groups to enable separate analysis. 

*Example:* HVCs represent 8% of the Wise user base. Proportional sampling of n=400 gives you only 32 HVC responses—too few to analyze separately or detect meaningful differences. Oversample HVCs to reach n=100+, then decide whether to weight back for population-level estimates.

Oversampling increases cost and complexity but enables segment-level insights that would otherwise be invisible.

### Two Power Calculations (Both Required)

**1. Sample Size Power**  
How many responses do you need to detect a real effect?

**Rule:** 80% confidence, 5% margin of error  
**Reference:** Cochran (1977)  
**Calculator:** [SurveyMonkey Sample Size Calculator](https://www.surveymonkey.com/mp/sample-size-calculator/)

*Worked example:* Population of 50,000 users → need n=381 for 5% margin of error at 95% confidence level

**2. Statistical Power**  
Is your sample size large enough for the analyses you plan to run?

Different analyses have different requirements:
- **Correlation:** n ≥ 30 (minimum); n ≥ 100 (recommended)
- **Regression:** n ≥ 50 + 8×(number of predictors)
- **Chi-square:** At least 5 expected observations per cell
- **T-test:** n ≥ 30 per group (minimum); n ≥ 50 per group (recommended)

**Rule:** Plan your statistical analyses first, then calculate required sample size. 80% power is the minimum (Cohen, 1988).

**Calculator:** [G*Power](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower) (free statistical power analysis software)

### Segmentation as a Moderator

**Question to the room:** If you want to determine what different user groups exist in your population, how would you determine the sample size you need?

**Answer:** Segmentation acts as a moderator (a variable that changes the relationship between other variables) of both sample size and statistical power requirements.

- If you plan to run separate analyses per segment (e.g., compare HVCs vs non-HVCs), each segment needs to meet minimum power requirements independently
- If you're grouping respondents by shared patterns (cluster analysis) or using statistics to find hidden segments in your data (latent class analysis), you need larger overall samples (n ≥ 200 minimum; n ≥ 500 recommended)
- Plan for the smallest expected segment size—that's your constraint

**Practical implication:** A study targeting 400 total responses with 4 expected segments means ~100 per segment. Check whether your planned analyses work at n=100. If not, increase total sample or simplify analyses.

Before launching:
- Define your target population precisely
- Calculate sample size power for your margin of error
- Calculate statistical power for your planned analyses  
- Account for segmentation if analyzing subgroups separately
- If using oversampling, document the rationale and weighting plan

---

## 2. Question Construction (10 min)

Start with your research question, not the survey. Your objective informs structure, language, and what data you get at the end.

### The BRUSO Model (Open Textbook BC)

Every questionnaire item should be:
- **Brief:** Short, scannable questions
- **Relevant:** Directly serves your research objective  
- **Unambiguous:** Only one interpretation possible
- **Specific:** Concrete rather than abstract
- **Objective:** No leading language

### What To Do

**Question Design**
- **Use closed-ended questions.** Surveys generate quantitative data through closed-ended questions. Use a small number of open-ended questions for qualitative colour. If your survey tilts heavily toward open-ended, consider interviews instead. *(Nielsen Norman Group)*
- **Ask about recent, specific behaviour rather than predictions or averages.** "How many times did you use this product in the past 7 days?" beats "How often do you currently use this product in an average week?" Include "approximately" and allow ranges rather than exact numbers. Note: the time window should reflect the lived experiences of your target users. If you're surveying users who only visit the product every 14 days, a 7-day window may capture zero interactions, making a 30-day window more appropriate. *(Nielsen Norman Group)*
- **End with one broad open-ended question.** Many respondents arrive with specific feedback already in mind. Give them a place to put it.

**Response Scales**
- **Choose unipolar or bipolar scales based on what you're measuring.** Unipolar scales measure intensity of one attribute (e.g., "Not at all satisfied" to "Extremely satisfied"). Bipolar scales measure between two opposing attributes (e.g., "Very difficult" to "Very easy"). Use unipolar when measuring presence/absence of a quality. Use bipolar when measuring trade-offs or opposites. *(Pew Research Center)*
- **Include a neutral midpoint for attitude questions, exclude it for behaviour or factual questions.** When measuring opinions or satisfaction, a neutral option captures genuine ambivalence and prevents forced choices. When measuring behaviour or facts, there's no true neutral—either something happened or it didn't. *(AAPOR)*
- **Use verbal labels on response scales.** Respondents find numeric labels harder to understand than verbal labels. *(Purdue University)*
- **Keep scales consistent throughout.** For surveys with multiple rating questions, consistent scales improve respondent experience and produce cleaner data. *(GLG)*
- **Maintain equal visual spacing between response options.** Reinforces equal distance between options, reduces bias, aligns visual midpoint with conceptual midpoint. *(Imperial College London)*
- **Maintain equal mental spacing between response options.** Respondents perceive modifiers like "slightly," "somewhat," "very," and "extremely" as having unequal psychological distances. Choose verbal labels that feel evenly spaced in intensity. Avoid scales like "Not at all / A tiny bit / Somewhat / An enormous amount" where the jump between options varies wildly. Test with pilot respondents to confirm the labels feel evenly distributed. PUT IN A GRAPH OF MODIFIER INTENSITY. LOOK IN FOLDER FOR THE HTML FILE *(Survey methodology research on modifier perception)*
- **Consider best-worst scaling when rating scales won't work.** If respondents struggle to differentiate between similar options, or if you need to measure relative importance rather than absolute ratings, best-worst scaling forces trade-offs. Present small sets of items and ask respondents to pick the most and least important. This produces clearer preference hierarchies than Likert scales. *(Qualtrics)*
- **Provide escape options when appropriate.** Include "I don't know," "Not applicable," or "Other" options when a question might not apply to all respondents or when they may genuinely lack the information to answer. This prevents forced responses that introduce noise into your data. Don't overuse these—every question should be relevant to most respondents—but they're essential when asking about specific experiences or knowledge that may vary. *(AAPOR)*

**Question Sequencing**
- **Place sensitive and demographic questions late.** Respondents feel more comfortable sharing this information later in the survey. *(Imperial College London)*
- **Pilot test every survey.** Use cognitive interviews, focus groups, or small opt-in samples to refine questions before production. *(Pew Research Center)*
- **If tracking change over time, keep wording identical.** To measure true shifts in attitudes or behaviours, question wording, framing, and context must remain consistent across waves. *(AAPOR)*

### What To Avoid

**Question Structure Issues**
- **Double-barrelled questions.** Ask for two things in one question = confusion and inaccuracy. The word "and" is the tell. Split into two questions. *(SurveySparrow)*
- **Leading questions.** Phrasing that pushes respondents toward a certain answer. Example: "We are committed to a 5-star experience—how would you rate us?" produces biased data that confirms your own assumptions. *(Qualtrics)*
- **Questions respondents can't actually answer.** People can't reliably predict their own behaviour or recall distant averages. If you're measuring behaviour, observe it. If you need qualitative depth, interview. *(Nielsen Norman Group)*
- **Jargon.** If respondents can't understand your questions, you introduce bad data. Pilot with your target audience to strip out jargon. *(Nielsen Norman Group)*

**Response Format Issues**
- **Agree/disagree formats.** Avoid them. Rating agreement to statements is cognitively demanding, increases measurement error, and reduces respondent effort. Use question-specific scales instead. For example, ask "How satisfied are you with X?" with a satisfaction scale rather than "I am satisfied with X" with an agree/disagree scale. *(Imperial College London)*
- **Ranking tasks when rating will do.** Comparative judgments (ranking) are harder than absolute judgments (rating). Use ratings unless ranking is essential. *(Purdue University)*

**Survey Scope Issues**
- **Unnecessary demographics.** Ask yourself: will you actually use it? Could you source it another way? Every question costs cognitive load.
- **Over-length surveys.** Only ask about things essential to your research questions. If you don't absolutely need it, leave it out. *(Nielsen Norman Group)*

**Order Effects**
- **Ordering questions that prime or anchor later responses.** Early information limits or influences subsequent answers. If closed-ended questions on a topic precede an open-ended question on the same topic, respondents will echo concepts from earlier questions. *(Pew Research Center, Qualtrics)*

Every unclear question, every double-barrelled item, every unnecessary demographic burns trust and degrades data quality. Write questions respondents can answer accurately, with minimal effort.

---

## 3. Fatigue Hierarchy (20 min)

Completion rates look fine, but halfway through, people stop reading and start clicking. You get data that looks real but isn't. The driver isn't length—it's cognitive load.

### The Fatigue Hierarchy (High to Low Load)

| Question Type | Cognitive Load | Fatigue Impact |
|--------------|----------------|----------------|
| **Open-ended (detailed)** | Very High | Severe |
| **Open-ended (short)** | High | High |
| **Ranking tasks** | High | High |
| **Matrix/grid questions** | Medium-High | High |
| **Multiple choice (select all)** | Medium | Moderate |
| **Likert scale (agree/disagree)** | Low | Minimal |
| **Single choice (3-5 options)** | Low | Minimal |

**Implication:** High-load question types earn their place or get cut. Every grid, every ranking task, every open-ended question is a withdrawal from your respondent's attention budget.

### Six Strategies to Reduce Cognitive Fatigue

#### 1. Cut question load, especially loops

**The problem:** Looped blocks are the worst offender. The survey doesn't get longer in time—it gets longer in effort. Same cognitive cost, repeated.

**The evidence:** A Walr study (UK sample, n=1,000) found "don't know" responses rose **50% by loop 3**, with engagement dropping around 20% in later iterations. *(Research Live)*

**The fix:** Cut loops entirely, or run them once only. If you must loop, limit to 2 iterations maximum.

#### 2. Front-load important questions

**The problem:** People are sharpest at the start. Attention degrades as the survey progresses.

**The fix:** Important questions first, when attention is highest. Demographics and simple ratings at the end. *(Lensym)*

#### 3. Skip logic is not optional

**The problem:** Redundant questions damage motivation. Every question that doesn't apply to a respondent is a small trust withdrawal.

**The fix:** Use skip logic so respondents only see questions relevant to them. Audit for duplicate or unnecessary questions. *(Kantar)*

#### 4. Randomize option order in multi-select blocks

**The problem:** People gravitate to options that appear first (primacy bias). If your list always starts with "Easy access to money," that option gets picked more often just because it's at the top.

**The fix:** Randomize the order for each respondent so they see options in different positions, but keep the order consistent within their own survey. Stops early-option bias and straightlining (giving the same answer to every question without reading).

**Exception:** Don't randomize scales (like "Strongly Disagree" to "Strongly Agree"). For scales, reverse the direction on some questions—flip "Agree" and "Disagree" ends to catch people who pick the same position every time without reading (straightlining detection).

#### 5. Back-to-back multi-selects compound fatigue

**The problem:** Matrix grids are the worst version of this, but consecutive "select all that apply" lists hit the same problem. Scanning 10+ abstract options and making comparative judgments, repeatedly, is where straightlining starts.

**The fix:** Break them up with lower-load questions (single-choice, Likert), or cut the weakest one.

**Decision rule:** One grid/multi-select is fine. Two is pushing it. Three means your design has a problem.

#### 6. Fatigue is load, not length

**The problem:** Survey length gets blamed, but cognitive cost is the real driver. A 25-minute survey can hit 80% completion. A 5-minute survey can stall at 40%.

**The fix:** Manage perceived value, not just time. A clear intro explaining **why the study matters** raises completion rates. Respondents who understand why they're answering work harder at it. *(PMC)*

**Progress indicators help:** Make progress visible and achievable—completion feels less burdensome when people can see how far they've come.

### The Fatigue-Prevention Checklist

Before launching, verify:

- [ ] No grid exceeds 5-7 rows (think similarly for "check all that apply" questions)
- [ ] High cognitive load questions are spread throughout, not clustered
- [ ] Branching logic: Every question is relevant to the respondent seeing it
- [ ] Open-ended questions are limited (ideally 1-2 maximum)
- [ ] If possible, progress is visible and feels achievable
- [ ] Mobile experience is tested and optimized
- [ ] Cognitive testing: Pilot respondents reported acceptable fatigue levels
- [ ] Time estimate is accurate and communicated upfront

A 25-minute survey that respects cognitive load will outperform a 5-minute survey that doesn't. Design for the cognitive budget, not the clock.

---

## 4. Methods + Activity 1 (25 min)

**Core Principle:** The method you choose determines your sample size, what biases threaten validity, and what conclusions you can defend. Within-subjects vs. between-subjects isn't an implementation detail—it's a strategic choice.

### Within-Subjects vs. Between-Subjects Design

**Within-Subjects (Repeated Measures)**

Every respondent sees every condition. The same person evaluates Concept A and Concept B.

*Advantages:* Requires fewer participants and increases the chance of discovering a true difference among conditions. Because individual variation is controlled, the design has higher statistical power with a smaller sample. *(Nielsen Norman Group)*

*Core pitfall:* **Carryover and order effects.** Seeing Concept A changes how a respondent evaluates Concept B. Two forms:
- **Contrast effects:** B looks worse because A set a high anchor
- **Assimilation effects:** B looks better because the respondent is now primed to the category

Studies over decades have shown question order affects responses in surveys about everything from presidential campaigns to employee opinions. *(Qualtrics)*

*Mitigation:* Counterbalance (show conditions in different orders to different respondents) or randomize the order each respondent sees conditions. This distributes carryover effects across the sample rather than systematically biasing one direction. It does not eliminate them; it neutralizes them statistically.

*Other pitfalls:* Demand characteristics increase in within-subjects designs. Respondents who see multiple conditions are more likely to infer the study's purpose and adjust their answers to appear consistent or cooperative.

*When to use:* Tasks where individual differences would create noise you can't afford to sample out (small B2B samples, niche populations). Also appropriate when the stimulus is abstract enough that seeing multiple versions is realistic (e.g., comparing two pricing structures, not two product designs that look obviously similar).

**Between-Subjects**

Different respondents see different conditions. Group A sees Concept 1. Group B sees Concept 2.

*Advantages:* Each participant experiences only one condition. No carryover. Responses are independent. *(Statistics By Jim)*

*Core pitfall:* **Sample size.** This design needs more participants to reach the same statistical power as within-subjects designs. For concept tests with 3+ conditions, sample requirements grow quickly. A test with 4 concepts at 200 respondents per cell requires 800 completes. *(Statistics By Jim)*

*Other pitfalls:* Group equivalence depends on proper randomization at recruitment. Any systematic difference between groups confounds the result. Pre-screening variables must be balanced across cells.

*When to use:* Concept tests where seeing multiple stimuli would bias evaluation—messaging tests, pricing tests, design alternatives where the question is "which would you choose if you only ever saw this one option."

**Mixed Designs**

One variable is between-subjects, another is within-subjects. In practice: segment is between-subjects (SMB vs. enterprise); concept version is within-subjects (respondents in each segment evaluate all feature descriptions). Useful when you need both cross-group comparisons and within-person preference data. *(Scribbr)*

### Complete vs. Incomplete Block Designs

**Complete Block Design**

Every respondent sees every stimulus. Works when the stimulus set is small (2-4 items) and fatigue isn't a concern.

**Balanced Incomplete Block Design (BIBD)**

An advanced design for large stimulus sets. Not every respondent sees every concept, but the design ensures every pair of concepts appears together the same number of times across respondents. This maintains statistical efficiency while preventing respondent fatigue. *(VSNi)*

*Where BIBDs appear:* Large-scale educational assessments (NAEP) use BIBDs to distribute item banks across test booklets. The same logic applies to concept tests with large stimulus sets: if you have 12 product concepts, no respondent realistically evaluates all 12 without severe fatigue. Assign each respondent 3-4 concepts, engineered so all pairwise comparisons are represented across the full sample. *(ResearchGate)*

*Critical constraint:* BIBDs require strict mathematical parameters. Design errors break the balance and invalidate cross-stimulus comparisons. Use statistical software (R's ibd package, SAS PROC FACTEX) rather than constructing manually.

*Pitfall:* Because of its efficiency-increasing potential, it can be attractive when resources are limited. But incorrect use, including improper application of the name, has led to chains of erroneous interpretations in published research. Know what you're implementing before claiming it. *(ScienceDirect)*

### Randomization (Two Levels)

**Within-Question Randomization (Response Option Order)**

*The problem:* The SurveyMonkey Research team ran an experiment with 400 respondents about workplace pet peeves. Half saw randomized answer options, half didn't. Results differed significantly. Without randomization, choices appearing above the midpoint were more likely to be picked, producing biased data. *(SurveyMonkey)*

*The mechanisms:* **Primacy bias** (tendency to select options appearing first in self-administered surveys) and **recency bias** (tendency to select options appearing last in interviewer-administered surveys). *(AAPOR)*

*Exception:* Don't randomize ordinal response categories (e.g., excellent, good, only fair, poor). These scales convey important information about order and should be presented sequentially. *(Pew Research Center)*

**Question Order Randomization**

*Example:* When pollsters ask "What is the most important problem facing the nation?" the answer becomes the focus for the next question: "Do you approve of the way [name] is handling his job as president?" People judge the president primarily on whichever issue they just named. *(SurveyMonkey)*

*Mitigation options:*
1. Randomize question order across respondents
2. Use block randomization (question groups shuffled but within-group logic preserved)
3. A/B test different sequences before full launch

*Pew's recommendation:* Open-ended questions on national problems or opinions about leaders should appear near the beginning. If closed-ended questions related to the topic are placed before an open-ended question, respondents are much more likely to mention concepts raised in those earlier questions. *(Wisc)*

*Impact scale:* One RCT found question order led to a 23.7% difference in patient-reported outcomes rated as essential when appearing last vs. first. Order isn't a minor design detail—it materially changes which items "win." *(NIH)*

---

### Activity 1: Matching Methods to Research Questions

**Format:** FigJam exercise. For each research question type below, groups identify: (1) appropriate survey method/design, (2) key pitfalls/challenges, (3) when to use vs. avoid.

#### Concept Tests / Evaluations

*Core decision:* Between-subjects vs. within-subjects. If respondents evaluate multiple concepts, you're in within-subjects territory and carryover is the primary threat. If each respondent sees only one concept, you need larger samples but cleaner independent evaluations.

*Best practice:* Combine qualitative and quantitative research. Qualitative research before and after quantitative concept testing allows you to design better concepts and derive better insights from the quantitative analysis. *(Relevant Insights)*

#### Perception

*What it is:* How a concept is understood and interpreted (not whether people like it).

*Best design:* Between-subjects. Each respondent exposed to one version. Measures spontaneous comprehension, associations, and framing. Within-subjects risks the first concept contaminating interpretation of the second.

*Pitfall:* Respondents tell you what they think they understood rather than what they actually understood. Verbal comprehension questions ("What does this mean to you?") are more valid than prompted agreement scales for perception work.

#### Persona Development

*What it is:* Identifying segments by shared attitudes, behaviours, motivations, and needs to build research-based archetypes.

*Best design:* Within-subjects for attitudinal batteries (same person answers all attitudinal items, enabling clustering). Segment assignment is then the output, not the input. *(SurveyMonkey)*

*Pitfall:* Long attitudinal batteries produce fatigue, which compresses variance and makes segmentation solutions weaker. For cluster analysis or LCA to work, you need genuine variance in responses; a fatigued respondent giving 4/5 to every item is noise.

#### Feature Set Hierarchy / Prioritisation

*What it is:* Which features matter most to which users.

*Best design:* MaxDiff (Best-Worst Scaling), structured as an incomplete block design. Respondents see subsets of features and choose the most and least important. This forces trade-offs and eliminates the "everything is important" bias of rating scales. *(Polling.com)*

*Why BIBD matters here:* With 10+ features, no respondent evaluates all pairs; the design ensures every feature appears the same number of times and every pair appears together the same number of times across respondents.

*Pitfall:* MaxDiff requires a reasonable sample size and careful design to generate a reliable preference list. Low sample sizes break the balance and produce unstable utilities (preference scores). *(arXiv)*

#### Pricing (Willingness to Pay)

*What it is:* How much different segments will pay, and for which feature combinations.

*Best design:* Conjoint analysis (choice-based conjoint, CBC) or Van Westendorp Price Sensitivity Meter depending on whether you need feature-price trade-offs or a simpler acceptable price range.

*Conjoint:* Quantifies how customers trade off features and price, producing part-worth utilities (preference scores showing how much each feature matters), willingness to pay, and market simulators. Use choice-based designs with realistic attributes, levels, and a "none" option. *(Umbrex)*

*Common workflow:* Use MaxDiff to shortlist features, then run conjoint to refine how those features combine in actual choice scenarios. *(Polling.com)*

*Pitfall:* Stated willingness to pay ≠ actual willingness to pay. Hypothetical bias (people overstate what they'd pay in surveys vs. real purchases) inflates WTP estimates. Conjoint produces relative WTP (trade-off value), not absolute price predictions. Always triangulate with behavioural data before committing to price points.

#### Attitudinal

*What it is:* Measuring beliefs, opinions, and feelings toward a product, brand, or concept.

*Best design:* Within-subjects for established attitudinal batteries (rating a single concept across multiple dimensions). Between-subjects when comparing brand/concept evaluations where seeing multiple stimuli would contaminate associations.

*Pitfall:* Agree/disagree formats inflate agreement (acquiescence bias). Use construct-specific scales ("How clearly does this explain the benefit?" from Very clearly to Not at all clearly) rather than generic Likert agreement. *(Imperial College London)*

*Question quality matters:* Since attitudinal research deals with self-reported data, craft neutral, unbiased questions. Leading questions skew results and distort user attitudes. *(Nielsen Norman Group)*

#### Behavioral

*What it is:* Measuring what people do or have done, not what they think.

*Best design:* Within-subjects for behavioural frequency questions about a single product or category. Behaviour is less susceptible to carryover than attitudes because it's factual.

*Pitfall:* Surveys can't measure behaviour; they measure self-reported behaviour. These diverge in predictable ways. If you're looking to learn something behavioural, there's likely a method better suited to your needs. Asking it in a survey is, at best, inefficient and, at worst, will produce unreliable or misleading data. *(Nielsen Norman Group)*

*When behaviour must be measured by survey:* Ask about specific, recent, bounded time windows. "How many times did you make an international payment in the past 30 days?" not "How often do you typically make international payments?" The former is anchored; the latter invites respondents to construct a fictional average.

#### Hybrid: Qual at Scale

*What it is:* Research that captures rich qualitative data from large samples by combining survey structure with unmoderated media capture and computational analysis. The goal is depth and context at a sample size pure qual can't reach.

*Beyond text:* Tools like dscout allow researchers to capture participants completing tasks, reacting to concepts, or interacting with prototypes in their natural context, without a moderator present. A rating scale tells you a concept scores 6.2 out of 10. A 90-second video shows you exactly where a participant paused, what confused them, and what they said in the moment. *(dscout, ATLAS.ti)*

*NLP and text mining:* Open-text survey responses are one entry point, but audio and video capture give richer raw material. Automated speech recognition (ASR) converts recordings to text in minutes. Once transcribed, NLP pipelines can process the corpus for themes, sentiment, and patterns at scale. *(PMC, AWS ML Blog)*

*The workflow:*
1. Participants record audio/video responses (via dscout or equivalent)
2. ASR produces transcripts
3. NLP processes transcript corpus for themes, sentiment, patterns
4. Human analysts add context, nuance, and the "why" behind what the model flags

*Accuracy caveats:* ASR performance degrades with accents, overlapping speakers, and low audio quality. A noisy transcript produces noisy themes. Quality of audio capture matters as much as quality of analysis downstream. *(medRxiv)*

The choice between within-subjects and between-subjects determines sample requirements, validity threats, and what you can conclude. Block designs and randomization aren't technical details—they're decisions that shape whether your data is defensible or confounded.

---

## 5. Governance (10 min)

**Core Principle:** Every stakeholder who asks "can we just add one more question?" is making a trade. They rarely frame it that way. Your job is to make the trade explicit, with evidence.

### Survey length changes response quality

Respondents who stay in long surveys give you tired data. This is the argument most researchers reach for last but should reach for first.

**The evidence:**
- An additional hour of survey time increases the probability that a respondent skips a question by **10 to 64%**
- The total monetary value of aggregated response categories declines as the survey goes on, with an extra hour lowering reported food expenditure values by **25%**
- Similar effect sizes were found in phone surveys where respondents were already familiar with the questions, suggesting **cognitive burden is a key driver**

*(Jeong et al., 2023, Journal of Development Economics, NBER Working Paper 30439)*

**The implication:** The respondents who stay aren't giving you good data; they're giving you tired data.

### Satisficing: The Hidden Data Quality Problem

When respondents become cognitively overloaded they stop optimizing their answers and start **satisficing**. Krosnick's (1991) theory categorizes satisficing into weak and strong forms, and identifies four response strategies:

1. Saying "don't know" when they do know
2. **Agreeing by default** (acquiescence: saying yes to statements they actually disagree with)
3. **Response order effects** (settling for the first plausible option)
4. **Nondifferentiation in rating scales** (straightlining)

Straightlining is the most visible symptom: the pattern of giving the exact same answer to all questions in a grid is more common towards the end than the beginning of a questionnaire. *(NCBI, ResearchGate)*

**The result:** Data that looks complete but is analytically useless. A dataset of 500 respondents where 30% straightlined the last battery is not a dataset of 500; it's a dataset of 350 with 150 rows of noise that you can't easily identify or remove.

### Drop-Off is Concentrated Early, Not Spread Evenly

Analysis of **100,000 SurveyMonkey surveys** found that the sharpest increase in drop-off rate occurs with each additional question **up to 15 questions**. If a respondent is willing to answer 15 questions, drop-off rates for each incremental question up to 35 questions are lower than for the first 15. *(SurveyMonkey)*

**Practical implication:** The first few stakeholder additions carry the highest abandonment risk. Adding questions 8, 9, and 10 is more dangerous to completion than adding questions 30, 31, and 32.

### The Trade-Off to Put in Front of Stakeholders

Frame it as a choice between two things they both claim to want: **more questions or better answers to the questions already there**.

The evidence shows they cannot have both without a cost. A stakeholder adding five questions to a 15-minute survey isn't getting five questions' worth of insight; they're getting five questions' worth of fatigued, potentially satisficed responses, applied across their questions and yours.

### Practical Tools for the Defense

**1. Estimate the time cost before the conversation**

Most survey platforms report median completion time. Add questions, rerun the estimate, show the before and after. A 12-minute survey becoming 18 minutes is a number stakeholders respond to better than abstract quality concerns.

**2. Use the question audit question**

"What decision will this question inform, and what would you do differently if the answer were X versus Y?"

If you don't absolutely need the information, leave it out. Ask yourself whether you will use the demographic information, and whether there is another way to capture it. *(Nielsen Norman Group)*

Questions that can't answer the audit question don't belong in the survey regardless of what a stakeholder wants.

**3. Offer an alternative route**

If a stakeholder's question is genuinely important but adds unacceptable length, the answer is:
- A separate, shorter survey
- A follow-up qualitative session with a subset
- A passive data source

Some research questions are better answered using qualitative interviews, focus groups, or secondary data analysis. These methods can also serve as useful precursors to survey research. Giving stakeholders a viable alternative makes the "no" easier to accept. *(WSU)*

The conversation isn't "we can't add more questions." It's "adding questions degrades the answers to the questions already there, including yours." Make the trade explicit. Use the evidence. Offer alternatives.

---

## 6. Pilot Test (5 min)

**Core Principle:** Pretesting is required before launch. Conducting a pilot test with a small group of participants identifies unclear or misleading questions before they contaminate your full dataset. *(Pew Research Center, Omniconvert)*

### Two Types of Testing (Both Required)

#### Cognitive Testing

**What it is:** 5-7 respondents thinking aloud as they complete the survey. This is **non-negotiable**. Cognitive testing before launch catches ambiguity before it contaminates the full dataset.

**What you're listening for:**
- Confusion on question wording
- Questions being interpreted differently than intended
- Response options that don't fit how people actually think
- Anything that makes someone pause, re-read, or guess

**Scaling with complexity:** What scales with survey complexity is the formality. A 5-minute pulse check and a 40-question segmentation study have different requirements. The checklist documents where flexibility exists and where it doesn't.

**When to do this:** Before anything else. Cognitive testing is the first gate, not the last.

#### Test Run

**What it is:** Full technical check. Especially important for longer, complex surveys.

**What to verify:**
- Embedded data populating correctly
- Skip logic routing as intended
- Survey displays correctly on mobile
- Completion time matches your estimate
- No broken questions or dead ends

**Who runs it:**
1. Run it yourself
2. Get 2-3 colleagues to run it too
3. Send to 2-5% of your sample as a last check

Cognitive testing finds the questions respondents can't answer. Technical testing finds the mechanics that break. Both are required. Skipping either means launching blind.


---

## Key References

### Sampling & Statistical Power

Cochran, W. G. (1977). *Sampling techniques* (3rd ed.). John Wiley & Sons.

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

Lohr, S. L. (2019). *Sampling: Design and analysis* (3rd ed.). CRC Press.

Kish, L. (1965). *Survey sampling*. John Wiley & Sons.

Kalton, G., & Anderson, D. W. (1986). Sampling rare populations. *Journal of the Royal Statistical Society: Series A (General)*, 149(1), 65–82.

Faul, F., Erdfelder, E., Lang, A. G., & Buchner, A. (2007). G*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. *Behavior Research Methods*, 39(2), 175–191.

Hair, J. F., Black, W. C., Babin, B. J., & Anderson, R. E. (2019). *Multivariate data analysis* (8th ed.). Cengage Learning. [For segmentation analysis sample size requirements]

### Question Construction & Survey Design

Dillman, D. A., Smyth, J. D., & Christian, L. M. (2014). *Internet, phone, mail, and mixed-mode surveys: The tailored design method* (4th ed.). John Wiley & Sons.

Krosnick, J. A. (2018). Questionnaire design. In D. L. Vannette & J. A. Krosnick (Eds.), *The Palgrave handbook of survey research* (pp. 439–455). Palgrave Macmillan.

Tourangeau, R., Rips, L. J., & Rasinski, K. (2000). *The psychology of survey response*. Cambridge University Press.

Vannette, D. L., & Krosnick, J. A. (Eds.). (2018). *The Palgrave handbook of survey research*. Palgrave Macmillan.

**Industry & Practitioner Resources:**

Pew Research Center. (2023). *Writing survey questions*. https://www.pewresearch.org/methods/u-s-surveys/writing-survey-questions/

Nielsen Norman Group. (2023). Writing good survey questions: 10 best practices. https://www.nngroup.com/articles/survey-best-practices/

American Association for Public Opinion Research (AAPOR). *Best practices for survey research*. https://www.aapor.org/Standards-Ethics/Best-Practices.aspx

Imperial College London. *Best practice in questionnaire design*. https://www.imperial.ac.uk/media/imperial-college/administration-and-support-services/staff-development/public/questionnaire-design.pdf

Vannette, D. L. (Ed.). *Handbook of question design*. Qualtrics XM Institute / Purdue University. https://www.purdue.edu/research/research-ethics/docs/QuestionnaireDesign_Qualtrics.pdf

GLG. *Survey design best practices*. https://glg.it/

SurveySparrow. *Survey question mistakes and best practices*. https://surveysparrow.com/

### Cognitive Fatigue & Survey Experience

Krosnick, J. A. (1991). Response strategies for coping with the cognitive demands of attitude measures in surveys. *Applied Cognitive Psychology*, 5(3), 213–236.

Galesic, M., & Bosnjak, M. (2009). Effects of questionnaire length on participation and indicators of response quality in a web survey. *Public Opinion Quarterly*, 73(2), 349–360.

Revilla, M., & Ochoa, C. (2017). Ideal and maximum length for a web survey. *International Journal of Market Research*, 59(5), 557–565.

Deutskens, E., de Ruyter, K., Wetzels, M., & Oosterveld, P. (2004). Response rate and response quality of internet-based surveys: An experimental study. *Marketing Letters*, 15(1), 21–36.

**Industry & Practitioner Resources:**

Walr. (2023). Survey fatigue research. *Research Live*. https://www.research-live.com/

Lensym. *Best practices in survey question sequencing*. https://www.lensym.com/

Kantar. *Skip logic and survey quality*. https://www.kantar.com/

National Center for Biotechnology Information (PMC). *Survey completion and cognitive load*. https://www.ncbi.nlm.nih.gov/pmc/

### Research Design Methods

Charness, G., Gneezy, U., & Kuhn, M. A. (2012). Experimental methods: Between-subject and within-subject design. *Journal of Economic Behavior & Organization*, 81(1), 1–8.

Greenwald, A. G. (1976). Within-subjects designs: To use or not to use? *Psychological Bulletin*, 83(2), 314–320.

Keppel, G., & Wickens, T. D. (2004). *Design and analysis: A researcher's handbook* (4th ed.). Pearson.

Cochran, W. G., & Cox, G. M. (1957). *Experimental designs* (2nd ed.). John Wiley & Sons. [Balanced incomplete block designs]

**Industry & Practitioner Resources:**

Scribbr. *Mixed factorial design*. https://www.scribbr.com/

Statistics By Jim. *Between-subjects vs. within-subjects designs*. https://statisticsbyjim.com/

VSNi. *Balanced Incomplete Block Designs*. https://www.vsni.co.uk/

ResearchGate. *Incomplete block designs in survey research*. https://www.researchgate.net/

University of Wisconsin. *Question order effects*. https://www.wisc.edu/

National Institutes of Health (NIH). *Question order RCT in patient outcomes*. https://www.nih.gov/

PMC / BMC Medical Research Methodology. *Question order effects in surveys*. https://www.ncbi.nlm.nih.gov/pmc/

### Concept Testing & Advanced Methods

Relevant Insights. *Concept testing for UX researchers*. https://relevantinsights.com/

Polling.com. *MaxDiff vs. Conjoint analysis*. https://blog.polling.com/

Umbrex. *Conjoint analysis and willingness to pay*. https://umbrex.com/

arXiv. *MaxDiff reliability and sample size requirements*. https://arxiv.org/

### Qualitative at Scale & NLP

dscout. *Unmoderated video research at scale*. https://dscout.com/

ATLAS.ti. *Qualitative data analysis with multimedia*. https://atlasti.com/

European Journal of Cardiovascular Nursing / Oxford Academic. (2024). Transcription in qualitative research. https://academic.oup.com/

PMC / NCBI. *Intelligent speech recognition for qualitative research*. https://www.ncbi.nlm.nih.gov/pmc/

AWS Machine Learning Blog. *Speech-to-text NLP pipeline at scale*. https://aws.amazon.com/blogs/machine-learning/

medRxiv. *ASR accuracy in multi-speaker qualitative settings*. https://www.medrxiv.org/

JMIR / PMC. *NLP augmenting qualitative analysis*. https://www.ncbi.nlm.nih.gov/pmc/

### Survey Governance & Stakeholder Management

Jeong, D., Aggarwal, S., Robinson, J., Kumar, N., Spears, D., & Spinellis, N. (2023). Exhaustive or exhausting? Evidence on respondent fatigue in long surveys. *Journal of Development Economics*, 161, 103010. Also available as NBER Working Paper 30439.

Krosnick, J. A. (1991). Response strategies for coping with the cognitive demands of attitude measures in surveys. *Applied Cognitive Psychology*, 5(3), 213–236.

Roberts, C., Vandenplas, C., & Stähli, M. E. (2019). Evaluating the impact of response burden on data quality in the European Social Survey. *Journal of Survey Statistics and Methodology*, 7(4), 573–595.

**Industry & Practitioner Resources:**

SurveyMonkey. *Survey length and drop-off analysis (100,000 surveys)*. https://www.surveymonkey.com/

Washington State University. *Survey best practices*. https://surveys.wsu.edu/

NCBI / PMC. *Satisficing and response quality*. https://www.ncbi.nlm.nih.gov/pmc/

ResearchGate. *Straightlining and survey fatigue*. https://www.researchgate.net/

### Pilot Testing & Pretesting

Presser, S., Rothgeb, J. M., Couper, M. P., Lessler, J. T., Martin, E., Martin, J., & Singer, E. (Eds.). (2004). *Methods for testing and evaluating survey questionnaires*. John Wiley & Sons.

Willis, G. B. (2005). *Cognitive interviewing: A tool for improving questionnaire design*. SAGE Publications.

Beatty, P. C., & Willis, G. B. (2007). Research synthesis: The practice of cognitive interviewing. *Public Opinion Quarterly*, 71(2), 287–311.

**Industry & Practitioner Resources:**

Pew Research Center. *Pretesting survey questions*. https://www.pewresearch.org/

Omniconvert. *Survey pilot testing best practices*. https://www.omniconvert.com/

---

## Facilitation Notes

**Tone:** Practical and applied. This isn't survey methodology theory—it's "here's what you do on Monday."

**Pacing:** 
- Sampling is brief overview—go deeper in optional quant programme
- Fatigue hierarchy is the anchor section (25 min)—use real Wise examples
- Activity 1 in FigJam allows hands-on application
- Governance section addresses real pain point: stakeholder additions

**Dependencies:** This block feeds directly into the afternoon exercise (building best/worst surveys). The principles taught here are what groups will apply (or deliberately violate).

**Delivery:** Light lecture + FigJam activities. Deck provides framework, activities drive learning.

**Leave-behind:** The pre-launch checklist is the durable artifact. Everything else scaffolds understanding of why each checklist item matters.
