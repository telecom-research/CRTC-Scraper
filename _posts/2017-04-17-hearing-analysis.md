---
layout: post
title: CRTC Hearing Text Analysis
---

This is a brief summary of the text analysis performed on a series of transcripts published by the CRTC between April 11 and April 28, 2016.

The purpose of this post is twofold: 

- describe how to read the Jupyter Notebook
- highlight key findings of the analysis

### How to Read the Jupyter Notebook

[Jupyter Notebook](http://jupyter.org/) is an interactive web-based tool that combines live code, data visualizations, and rich text and media. The notebooks provide researchers with an agile programming environment that supports reproducible research and the ability to have code, visualization and analysis in one accessible platform. The interactive Jupyter Notebooks are easily shared with others via GitHub, but they can also be downloaded as static PDF or HTML files.

`You can read a Jupyter Notebook even if you can’t read code; in fact, this is one reason why they exist.`

All of the code blocks in a Jupyter Notebook are found in outlined grey boxes, with a numeric identifier beside it that looks like this: `In [6]`. Sometimes the code will have words that appear in different colours, with different formatting (usually bold/italics). Without worrying too much about the colours right now, the only thing you need to know about the code blocks is that any text that appears with a `#` in front of it is known as a `comment`. Comments are generally used to describe the code, but sometimes a `#` is used to ‘turn off’ the code so it doesn’t run. See two examples below:

{% highlight python %}

# checks to see how many records we have
print(len(file))

{% endhighlight %}

{% highlight python %}

# working on a regex to split text by speaker. This code is still in development.
#diced = re.split('(\d+(\s)\w+[A-Z](\s|.\s)\w+[A-Z]:\s)', joined)

{% endhighlight %}

Text describing the code and showing the results of the code is found everywhere **but** the grey boxes. This is the text to pay the most attention to. The text that shows the results of the code is in what I can only describe as a typewriter style font (like Courier), while the text that describes the code is not. In the photo below, the text on the top shows the result of the code, while the text on the bottom is descriptive text.

![Notebook Text Difference](/assets/images/notebookTextDifference.png){:class="img-responsive"}

