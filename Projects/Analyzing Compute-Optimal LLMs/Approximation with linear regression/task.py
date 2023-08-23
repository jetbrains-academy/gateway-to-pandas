import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression


def annotate_models(ax, colors, df, models):
    rows_to_annotate = df.loc[df['Model name'].isin(models)]
    x_shift_multiplier = 1.1
    for index, row in rows_to_annotate.iterrows():
        ax.annotate(row['Model name'], (row['Training tokens'] * x_shift_multiplier, row['Parameters']))
        # Set color of some specific points
        colors[index] = 'orange'


def create_ax():
    # Create a figure and a set of subplots
    fig, ax = plt.subplots()

    # Set labels and grid
    ax.set_xlabel('Training tokens, billions')
    ax.set_ylabel('Parameters, billions')
    ax.grid(True)

    ax.set_xscale('log')
    ax.set_yscale('log')
    return ax


def lin_reg_fit(df):
    # create linear regression model
    model = LinearRegression()

    # reshape and log the data
    X = np.log(df['Training tokens'].values.reshape(-1, 1))
    y = np.log(df['Parameters'].values.reshape(-1, 1))

    # fit the model
    model.fit(X, y)

    # print coef and intercept
    print('Coefficients:', model.coef_)
    print('Intercept:', model.intercept_)

    return model


if __name__ == '__main__':
    df = pd.read_csv('../Intro to LLMs/LLMs_metadata.csv')

    colors = ['blue'] * len(df)
    ax = create_ax()
    models = ["GPT-2", "T5", "BERT", "GPT-3", "Chinchilla", "GPT-4"]
    annotate_models(ax, colors, df, models)

    # Plot 'Size' and 'Training tokens' on a log-scale plot
    ax.scatter(df['Training tokens'], df['Parameters'], c=colors)

    lin_reg = lin_reg_fit(df)
    X = np.log(df['Training tokens'].values.reshape(-1, 1))
    y_pred = lin_reg.predict(X)
    x_y_df = (pd.DataFrame({'x': np.exp(X).reshape(-1), 'y': np.exp(y_pred).reshape(-1)})
              .sort_values(by='x'))
    plt.plot(x_y_df['x'], x_y_df['y'], linestyle='dashed')

    fig = ax.get_figure()
    fig.savefig('lin_reg_plot.svg')
    plt.show()
