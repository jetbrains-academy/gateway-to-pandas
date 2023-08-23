import numpy as np
import pandas as pd
import jinja2


def highlight_max(s, props=''):
    return np.where(s == np.nanmax(s.values), props, '')


def models_styler(df):
    models = (df[['Model name', 'Year', 'Parameters', 'Training tokens']]
              .sort_values(by='Year'))
    models.set_index(['Model name', 'Year'], inplace=True)
    styler = (models.style.format(precision=2, decimal=".").
              apply(highlight_max, props='font-weight:bold', axis=0))
    return styler


def year_stats_styler(df):
    year_stats = df.groupby('Year').agg(
        num_of_models=('Model name', 'count'),
        parameters_mean=('Parameters', 'mean'),
        tokens_mean=('Training tokens', 'mean'),
    )
    styler = (year_stats.style.format(precision=2, decimal=".")
              .relabel_index(['Number of models',
                              'Mean of parameters', 'Mean of tokens'], axis=1))
    return styler


if __name__ == '__main__':
    df = pd.read_csv('../Intro to LLMs/LLMs_metadata.csv')

    # Template handling
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
    template = env.get_template('report_template.html')
    html = template.render(models=models_styler(df).to_html(),
                           year_stats=year_stats_styler(df).to_html())

    # Write the HTML file
    with open('report.html', 'w') as f:
        f.write(html)
