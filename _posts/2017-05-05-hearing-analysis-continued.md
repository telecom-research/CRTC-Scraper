---
layout: post
title: CRTC Hearing Text Analysis, Continued
---

This is a continuation of the text analysis performed on a series of transcripts published by the CRTC between April 11 and April 28, 2016.

This analysis will look at the following words: 

- broadband
- fibre
- service
- digital literacy

### Key Findings of the Analysis

#### BROADBAND

The word `broadband` and its variations appear with the greatest frequency in the transcript dated April 11, 2015.

![Frequency of the word ‘broadband’](./assets/images/broadbandFrequency.png){:class="img-responsive"}

Here is a KWIC concordance from April 11, 2015 that shows its use. [View the complete file](https://github.com/telecom-research/crtc-scraper/blob/master/_code/notebooks/outputs/April11_broadband_concord.txt).

![Concordance for ‘broadband’](./assets/images/broadbandConcordance.png){:class="img-responsive"}

After removing stopwords and lemmatizing the text, `broadband` occurs a total of `1143` times across all of the transcripts.

Here is a list of the most significant collocated words appearing with `broadband` using the Log-likelihood ratio.

The word most significantly collocated with `broadband` is `national`, followed by `strategy` and `access`. It is extremely important to note here that **words will appear twice** in the following list. As the ngrams can appear both before and after the word, care must be taken to identify duplicate occurrences in the list below and then combine the totals. Therefore, the list below is a sample. Please refer to [this file](https://github.com/telecom-research/crtc-scraper/blob/master/_code/notebooks/outputs/broadband_collocate_Log.csv) for the complete list, and calculate accordingly. 

![Log Likelihood Collocates with broadband](./assets/images/broadbandCollocatesLL.png){:class="img-responsive"}

#### FIBRE

The word `fibre` and its variations appear with the greatest frequency in the transcript dated April 20, 2015.

![Frequency of the word ‘fibre’](./assets/images/fibreFrequency.png){:class="img-responsive"}

`Fibre` is by far the most common of these occurrences, with ‘fibres’ occurring only four times in total throughout all of the transcripts. Here is a KWIC concordance from April 20, 2015 that shows its use. [View the complete file](https://github.com/telecom-research/crtc-scraper/blob/master/_code/notebooks/outputs/April20_fibre_concord.txt).

![Concordance for ‘fibre’](./assets/images/fibreConcordance.png){:class="img-responsive"}

After removing stopwords and lemmatizing the text, `fibre` occurs a total of `476` times across all of the transcripts.

Here is a list of the most significant collocated words appearing with `fibre` using the Log-likelihood ratio.

The word most significantly collocated with `fibre` is `optic`, followed by `premise` and `build`. The list below is a sample. Please refer to [this file](https://github.com/telecom-research/crtc-scraper/blob/master/_code/notebooks/outputs/fibre_collocate_Log.csv) for the complete list, and calculate accordingly. 

![Log Likelihood Collocates with fibre](./assets/images/fibreCollocatesLL.png){:class="img-responsive"}

#### SERVICE

The word `service` and its variations appear with the greatest frequency in the transcript dated April 18, 2015.

![Frequency of the word ‘service’](./assets/images/serviceFrequency.png){:class="img-responsive"}

`Service` is the more common of these occurrences, though ‘services’ occurs many times throughout the transcripts as well. Here is a KWIC concordance from April 18, 2015 that shows the use of `service`. [View the complete file](https://github.com/telecom-research/crtc-scraper/blob/master/_code/notebooks/outputs/April18_service_concord.txt).

![Concordance for ‘service’](./assets/images/serviceConcordance.png){:class="img-responsive"}

Here is another concordance from April 18 showing the use of `services`. [View the complete file](https://github.com/telecom-research/crtc-scraper/blob/master/_code/notebooks/outputs/April18_services_concord.txt).

![Concordance for ‘services’](./assets/images/servicesConcordance.png){:class="img-responsive"}

The differences in usage between `service`, which looks as if it primarily occurs in the phrase `service providers`, and `services`, which occurs in a variety of contexts, might make a case against lemmatization.

Regardless, after removing stopwords and lemmatizing the text, `service` occurs a total of `2435` times across all of the transcripts.

Here is a list of the most significant collocated words appearing with `service` using the Log-likelihood ratio.

The word most significantly collocated with `service` is `provider`, followed by `basic` and `telecommunication`. The list below is a sample. Please refer to [this file](https://github.com/telecom-research/crtc-scraper/blob/master/_code/notebooks/outputs/service_collocate_Log.csv) for the complete list, and calculate accordingly. 

![Log Likelihood Collocates with service](./assets/images/serviceCollocatesLL.png){:class="img-responsive"}

#### DIGITAL LITERACY

Counting the frequency of two words requires a slightly different approach. This is accomplished by counting the `bigrams` rather than individual words. The bigram `digital literacy` occurs a total of `100` times across all of the transcripts.

![Frequency of 'digital literacy’](./assets/images/digital-literacyFrequency.png){:class="img-responsive"}

Counting the frequency of the bigram in each individual transcript takes a little more work. Since the text processing has reduced the transcripts to a comma-separated list of individual words, we will first count the frequency of the words as they appear separately in the transcripts. The highest separate frequency of `digital` and `literacy` occurs on April 21.

![Frequency of 'digital' and 'literacy’](./assets/images/digital-literacyFrequency1.png){:class="img-responsive"}

Counting the frequency of the bigrams for April 21 yields `45` occurrences of `digital literacy` as a word pair.

![Frequency of 'digital literacy’ on April 21](./assets/images/digital-literacyFrequency2.png){:class="img-responsive"} 

Counting the frequency of the bigrams for April 28 yields `10` occurrences of `digital literacy` as a word pair.

![Frequency of 'digital literacy’ on April 28](./assets/images/digital-literacyFrequency3.png){:class="img-responsive"} 

And finally, here is a sample of the concordance for `digital literacy` from April 21. It's important to note that concordances can only be generated for an individual word. Since there are fewer instances of `literacy` than `digital`, the concordance was generated for `literacy` alone. That's why there are a few results that don't include `digital`. [View the complete file](https://github.com/telecom-research/crtc-scraper/blob/master/_code/notebooks/outputs/April21_literacy_concord.txt).

![Concordance for ‘digital literacy’](./assets/images/digital-literacyConcordance.png){:class="img-responsive"}
