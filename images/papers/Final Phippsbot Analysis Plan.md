# Research Question

How do psychiatrists and LLMs differ in their question formulation during psychiatric intake, and how do these differences influence clinical information gathering, recall, empathy and safety assessment?

**H1 (Primary):** Clinicians and LLMs will differ in the types of questions they ask during psychiatric intake, resulting in significant differences in the completeness and type of clinical information elicited across major psychiatric domains. 

**H2:** Clinicians will demonstrate higher empathy, and more accurately identify safety concerns than LLM-guided interviewing policies during stimulated psychiatric intake interviews.

**H3 (Exploratory):** Greater conversational engagement during psychiatric intake (longer interview duration, higher message count, and more followup questioning) will be associated with greater recall accuracy, and more complete clinical information gathering, regardless of interviewer type.

**Experimental Design:** Psychiatrists will play around with the website for a few minutes to get used to it. Once they are ready, they will head over to the clinician study page, where they will complete the consent form and fill out their name/affiliation. The experiment consists of one 20-minute simulated psychiatric intake session. The psychiatrist will receive 1 vignette at random from a pool of 3\. They will see a brief vignette description, and will be given the full time to talk to the simulated patient. After the time limit, or if the clinician concludes the intake, they will be brought to a post-survey screen. They will complete an open-response form about the intake, a likert-scale recall form, and a feedback survey.  

After all the clinician data, we will run LLM models on the same tool and vignettes. We will limit the LLM to the mean clinician interview duration. We will also consider doing other budgeted analysis on the LLM data, like a question-by-question analysis. 

Github Commit Hashes  
cd83af19787f3edeb2c960960473a728194ab96c (actual Phippsbot website and clinician study)  
3abb65d1b6e24cb982392147a5487faeb2be156b (patient simulator fork from Jonathan)  
079508830f4ab9675af63810e7e654a7dc954c61(Guan’s repo that we might use for LLM analysis?) 

# Data Collected

**Session Metadata**

* Session id  
* Clinician id  
* Patient id  
* Condition  
* Affiliation

**Engagement Metrics**

* Duration (sec)  
* Message count  
* Avg msg words  
* Recall duration (sec)

**Recall (Open Response)** 

* Chief complaint  
* Safety concerns  
* Clinical thread  
* Additional observations

**Recall (Likert scale)** 

* Family history  
* Social history discussed  
* Past psych history  
* Substance use discussed  
* Currently employed  
* Living with others  
* In relationship  
* Has children  
* Uses alcohol  
* Uses tobacco  
* Uses cannabis  
* Uses other drugs  
* Trap question

**Post survey**

* Patient realism  
* Patient realism explanation

**Timing**

* Viewed at  
* First answered at  
* Final answered at

**Timing**

* Viewed at  
* First answered at  
* Final answered at

**Transcripts**

* Entire conversational transcript including chatbot responses

**Exclusion Criteria:** 

* Trick question failed (either likert score of ≤3 or ≥3)  
* Two few messages (\< 5 messages sent) 

# Analysis

## Summary: 

We plan to utilize the collected data from the transcript and recall form to compare clinician responses to LLM responses. We plan to run the LLM for only as long as the average time clinicians use in their interview. We plan to conduct both quantitative and qualitative analysis. We also plan to conduct a budgeted analysis in addition to time matching.We will compare the following data between LLM and clinician. 

**Recall accuracy**

* Coverage  
  * Correct / Total questions  
* Precision  
  * Correct / (Answered questions)   
* False confidence rate  
  * Incorrect “Yes” responses (not including selecting not addressed)

**Engagement metrics**

* Average messages sent (time for interview will be matched, but average messages may differ)  
* Average message length (character count)   
* Types of questions asked (see in-depth plan for more info) 

**Clinical Interview Quality**

* Chief complaint (Open response. Ground truth answer)  
* Safety concerns (Open response. Ground truth answer)  
* Empathy (Scored via a rubric and two reviewers)




## In-depth plan: 

**H1 (Primary): Question Formulation & Information Gathering**

Hypothesis: Clinicians and LLMs will differ in the types of questions they ask during psychiatric intake, resulting in significant differences in the completeness and type of clinical information elicited across major psychiatric domains.

Part A: Question Formulation

Variables

* Total question count  
* Open vs. closed question ratio  
* Follow-up question count  
* Clarification question count

Measurement

* Rule-based or LLM-assisted classification of each interviewer message  
* Binary coding: open (invites elaboration) vs. closed (yes/no or single-word answer expected)  
* Follow-up defined as: question that directly references patient's previous response

Statistical Analysis

* Mann-Whitney U tests comparing question counts and ratios between conditions  
* Effect sizes reported as rank-biserial correlation

Part B: Clinical Information Gathering

Variables

* Ground truth patient information (per vignette)  
* Recall Form Likert-Scale

Outcomes

* Coverage: Proportion of ground truth items discussed in interview  
* Precision: Proportion of recalled items that are correct (excluding "uncertain")  
* False Confidence Rate: Incorrect "yes" responses on undiscussed topics / total undiscussed

Normalization

* Raw scores AND normalized per 100 patient words  
* LLM interviews will be time-matched to mean clinician interview duration.

Statistical Analysis

* Mann-Whitney U tests  
* Report both raw and normalized results  
* Bonferroni correction for multiple domain comparisons

**H2: Empathy & Safety Assessment**

Hypothesis: Clinicians will demonstrate different empathic communication patterns than LLM-guided interviews.

Part A: Empathy **(Qualitative)**

Rubric Dimensions:

1. Emotional validation \- acknowledging patient's feelings  
2. Reflective listening \- paraphrasing or mirroring patient statements  
3. Rapport building \- warmth, appropriate tone, connection  
4. Patient-centered language \- focus on patient's perspective and experience

Method:

* Two coders independently review transcripts  
* Identify excerpts demonstrating each rubric dimension (or absence)  
* Code excerpts by dimension and valence (present/absent/inappropriate)  
* Calculate inter-rater agreement (Cohen's kappa) on excerpt identification  
* Resolve disagreements through discussion  
* Thematic summary comparing patterns by interviewer type

Presentation:

* Descriptive comparison (e.g., "Clinicians demonstrated emotional validation in X of Y interviews, typically in response to \[context\]. Example: \[quote\]")  
* Table of representative quotes by dimension and interviewer type  
* No statistical hypothesis testing for empathy

Part B: Safety Assessment (Primary)

Variables

* Ground truth safety concerns embedded in vignettes (to be defined)  
* Recall form: safety\_concerns field (open-ended)  
* Interview transcript: safety-related probing

Measurement

* Passive Discovery: Did the interviewer uncover embedded safety concerns?  
* LLM judge scoring:  
  * Primary concern identified (0/1)  
  * Appropriate detail elicited (0/1)  
  * Missed concerns (count)  
  * False positive safety identifications (count)

Outcome Measures

* Safety sensitivity: Identified concerns / Total embedded concerns  
* Safety specificity: Correct "no concern" / Total cases without that concern  
* False positive rate

Statistical Analysis

* Chi-square or Fisher's exact test for identification rates  
* McNemar's test if paired design

**H3 (Exploratory): Conversational Engagement**  
Hypothesis: Greater conversational engagement during psychiatric intake (longer interview duration, higher message count, and more follow-up questioning) will be associated with greater recall accuracy and more complete clinical information gathering, regardless of interviewer type.

Engagement Variables

* Interview duration (seconds)  
* Message count (total, interviewer only, patient only)  
* Average interviewer message length (words)  
* Follow-up question count  
* Question density (questions per minute)

Outcome Variables

* Coverage accuracy  
* Precision accuracy  
* Safety concern identification

Statistical Analysis

* Primary approach: Spearman correlations  
  * Compute correlations between each engagement variable and each outcome  
  * Report correlation coefficients (ρ) with 95% confidence intervals  
  * Examine correlations separately within each interviewer type to avoid confounding  
* Secondary approach (if sample size permits): Multiple regression  
  * Model: Outcome \~ Engagement \+ Interviewer Type \+ Engagement × Interviewer Type  
  * Interaction term tests whether engagement-outcome relationship differs between clinicians and LLM  
  * Will only interpret if adequate degrees of freedom (rule of thumb: 10-15 observations per predictor)

Correction for multiple comparisons: 

* Report both uncorrected and Bonferroni-corrected p-values  
* Emphasize effect sizes over significance testing

Visualization

* Scatterplots with separate trend lines by interviewer type  
  * X-axis: engagement variable  
  * Y-axis: outcome variable  
  * Color/shape by interviewer type

Interpretation Caveats

* Correlational design cannot establish causality  
* Engagement may be confounded with other factors (e.g., patient complexity, clinician experience)  
* Given time-matching, duration will be similar across conditions; analysis will focus on message count and question density as primary engagement indicators

This is also a place for the budgeted question-by-question analysis mentioned at the beginning on this document. 