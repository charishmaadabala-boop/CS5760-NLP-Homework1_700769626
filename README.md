# CS5760-NLP-Homework1_700769626
Homework 1 for CS5760 – Natural Language Processing
CS5760 – Natural Language Processing
Homework 1
Student Name: CHARISHMA ADABALA
Student ID: 700769626
Course: CS5760 – Natural Language Processing
Semester: Spring 2026
University: University of Central Missouri

Question 1: Regular Expressions
1.U.S. ZIP Codes
\b\d{5}(?:[- ]\d{4})?\b

2.Words not starting with a capital letter
\b(?![A-Z])[a-zA-Z]+(?:['-][a-zA-Z]+)*\b

3.Numbers with optional sign, commas, decimals, scientific notation
[+-]?\d{1,3}(?:,\d{3})*(?:.\d+)?(?:[eE][+-]?\d+)?

4.Email spelling variants
(?i)e(?:-|–|\s)?mail

5.Repeated 'go' with optional punctuation
\bgo+\b[!.,?]?

6.Lines ending with question mark and closing quotes/brackets
?\s*[)"’]]\s$

Question 2: Byte Pair Encoding (BPE)
2.1 Manual BPE
Corpus with end-of-word marker (_):

low_ low_ low_ low_ low_
lowest_ lowest_
newer_ newer_ newer_ newer_ newer_ newer_
wider_ wider_ wider_
new_ new_

Initial vocabulary: {l, o, w, e, s, t, n, r, i, d, _}

Step 1: Merge (e, r) → er
Step 2: Merge (er, ) → er
Step 3: Merge (n, e) → ne

2.2 Mini-BPE Learner
Implemented in bpe.py.
Example segmentations:

new → n e w_
newer → ne w er_
lowest → low est_
newestest → ne w est est_
Subword tokenization solves the OOV problem by breaking unseen words into known subwords. Some learned subwords align with real morphemes such as er_ and est_.

2.3 BPE on a Paragraph
Frequent merges: th, ing_, ion_, ed_, re_
Longest subwords: information_, processing_, tokenization_, understanding_, classification_

Reflection: BPE learns stems and suffixes effectively, reducing vocabulary size while handling rare words, though some splits may not be linguistically intuitive.

Question 3: Bayes Rule Applied to Text
P(c): Prior probability of a class.
P(d|c): Likelihood of a document given a class.
P(c|d): Posterior probability of a class given a document.
The denominator P(d) is ignored because it is constant across classes and does not affect comparisons.

Question 4: Add-1 Smoothing
Vocabulary size = 20, total negative tokens = 14.

Denominator = 14 + 20 = 34

P(predictable|−) = (2 + 1) / 34 = 3/34
P(fun|−) = (0 + 1) / 34 = 1/34

Question 5: Tokenization
5.1 Naïve vs Manual
Naïve tokenization fails to separate punctuation and contractions, while manual tokenization correctly handles clitics and punctuation.

5.2 spaCy Comparison
spaCy produces similar tokens but uses Unicode-aware splits such as ca + n’t.

5.3 Multiword Expressions
New York City
Machine learning
As well as
These should be single tokens due to non-compositional meaning.

5.4 Reflection
Tokenization is challenging due to punctuation, contractions, and MWEs. While English is simpler than morphologically rich languages, tokenization errors still affect NLP performance.
