It's quite plausible to suggest that the majority of Python-based reporting commences with Pandas. 
The ease of establishing Pandas DataFrames from various data sources such as databases, Excel or csv files, or 
json responses from web APIs is phenomenal. 

Once the raw data is captured in a DataFrame, a few lines of code suffice to clean the data and partition it 
into a comprehensible format for reporting. In this task our focus will be on exploiting the inherent facilities 
provided by Pandas for reports in HTML format.

## Report template
Creating an HTML report with pandas is quite straightforward.
However, for enhanced functionality beyond simply converting a DataFrame into 
a bare HTML table, it is advisable to use a combination of 
Pandas and a template engine like Jinja.
 
So firstly, we created a file called [report_template.html](report_template.html), 
where we have some predefined styles and general structure of the report with
stubs instead of actual tables.

## Table visualization
Now goes the most impressive part, demonstrating visualization of 
tabular data using the [Styler class](https://pandas.pydata.org/docs/user_guide/style.html).

After processing the data within a pandas.DataFrame, you should carry out any 
styling and display customisation. Be aware that if you make further changes 
to the DataFrame, the Styler will not be dynamically updated. 

The `DataFrame.style` attribute essentially returns a `Styler` object. 
This object contains a `_repr_html_` method, which enables it to be automatically rendered 
in a Jupyter Notebook.
Although the Styler can be utilized with large datasets, 
its primary design focus in on smaller datasets. 
Currently, you have the ability to output to these formats:
 * HTML
 * LaTeX
 * String (which enables the use of CSV)
 * Excel
 * (JSON is currently unimplemented)

This way you can use the full power of the pandas and Python to create nice reports on your data. 
For example, you can easily bold the maximums in a row or column, or even set a color gradient 
depending on the values in the table.

## Task
In this task we have implemented an example of creating from DataFrame 
a table of LLMs in HTML format. You need to create the second table similarly in 
the `year_stats_styler(df)` function:
 * group original DataFrame by `Year` column
 * aggregate group elements to calculate the number of models and mean values of parameters and training tokens by year
 * create and return proper `styler`

If everything is implemented correctly, 
then `task.py` will create a nice HTML report file [report.html](report.html) 
in the current directory.
