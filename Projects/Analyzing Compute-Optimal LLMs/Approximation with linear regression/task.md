In this task, your objective is to plot an approximate trendline illustrating the ratio between 
the number of training tokens and the size of the LLM, using data sourced from various academic research papers.

### Task
Look at the code in [task.py](task.py) and implement the function `lin_reg_fit(df)`. 
Keep in mind that our linear regression training is based on the logarithms of the initial values. 
Following the model training, we will plot the initial values and model predictions on a logarithmic scale. 
