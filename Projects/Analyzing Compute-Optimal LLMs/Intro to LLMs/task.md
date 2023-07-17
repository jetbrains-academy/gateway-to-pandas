# Introduction
A Large Language Model (LLM) is an artificial intelligence model that has been trained on a significant amount of text data. 
It uses machine learning algorithms to generate human-like text based on the input it's given. 
Because it's trained on a very large dataset, it can generate highly diverse responses and can answer a wide range of prompts. 
It can also incorporate a lot of knowledge about the world, including facts, logic, reasoning abilities, 
and even some level of "understanding" of emotions and human experiences.

For example, GPT-3, developed by OpenAI, is a large language model with 175 billion machine learning parameters. 
It is capable of tasks such as translation, question-answering, and even generating creative content like 
poems or short stories, often with surprising accuracy and coherence.
However, it's important to remember that even large language models do not truly understand the text in the way humans do. 
They analyze the statistical patterns in the data they were trained on and generate responses based on those patterns.

Over recent years, the emphasis in language modelling has shifted towards enhancing performance by augmenting 
the quantity of parameters in transformer-based models. This methodology has culminated in remarkable outcomes and 
state-of-the-art performance across many natural language processing tasks.

# Project description
In this project we aim to analyse connection between two primary elements determine the computational cost of 
training transformers in LLMs: its size, i.e. number of model parameters, and number of training tokens.

We are using approach from the Google DeepMind 
publication ["An empirical analysis of compute-optimal large language model training"](https://www.deepmind.com/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training).

The rising costs associated with training large-scale models necessitate a thorough evaluation 
of the most effective training configuration, ensuring resources aren't wasted.

# Dataset collection
Current generations of large language models predominantly allocate increased computational resources 
towards augmenting the parameter count, while the training data volume generally remains static, 
approximately around 300 billion tokens. 
In this task we aim to analyze the optimal balance between enlarging model size and 
augmenting training data volume given the availability of computational resources, 
based on the information from research papers. 

Principal discovery from the Google DeepMind's publication above suggests 
that current large language models are disproportionately large in relation to their computational budget, 
indicating that they are not trained on sufficient data. In fact, their findings show that, for the computed FLOPs 
used to train a model like Gopher, a model 4x smaller trained on 4x more data would have been a more optimal choice.

So we have prepared for you table with the following columns:
 * Paper link — URL of the research paper, which is information source about the characteristics of the model, 
usually publication on arXiv
 * Paper title 
 * Year — year of publication 
 * Model name — common notation for certain large language model
 * Parameters — number of model parameters (in billions), which is size of model in essence
 * Training tokens — number training tokens (in billions)
