import os.path
import pathlib

import matplotlib as mpl
# This has to happen before pyplot is imported to avoid needing an X server to draw the graphs.
# pylint: disable=wrong-import-position
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from decksite.data import competition, deck
from shared import configuration
from shared.pd_exception import DoesNotExistException

def cmc(deck_id):
    path = determine_path(str(deck_id) + '-cmc.png')
    if os.path.exists(path):
        return path
    d = deck.load_deck(deck_id)
    costs = {}
    for ci in d.maindeck:
        c = ci.get('card')
        if c.is_land():
            continue
        if c.mana_cost is None:
            cost = '0'
        elif next((s for s in c.mana_cost if '{X}' in s), None) is not None:
            cost = 'X'
        else:
            cost = int(float(c.cmc))
            if cost >= 7:
                cost = '7+'
            cost = str(cost)
        costs[cost] = ci.get('n') + costs.get(cost, 0)
    return image(path, costs)

def image(path, costs):
    ys = ['0', '1', '2', '3', '4', '5', '6', '7+', 'X']
    xs = [costs.get(k, 0) for k in ys]
    sns.set_style('white')
    sns.set(font='Concourse C3', font_scale=3)
    g = sns.barplot(ys, xs, palette=['#cccccc'] * len(ys))
    g.axes.yaxis.set_ticklabels([])
    rects = g.patches
    sns.set(font='Concourse C3', font_scale=2)
    for rect, label in zip(rects, xs):
        if label == 0:
            continue
        height = rect.get_height()
        g.text(rect.get_x() + rect.get_width()/2, height + 0.5, label, ha='center', va='bottom')
    g.margins(y=0, x=0)
    sns.despine(left=True, bottom=True)
    g.get_figure().savefig(path, transparent=True, pad_inches=0, bbox_inches='tight')
    plt.clf() # Clear all data from matplotlib so it does not persist across requests.
    return path

def archetypes_sparkline(competition_id):
    path = determine_path(str(competition_id) + '-archetypes-sparkline.png')
    if os.path.exists(path):
        return path
    c = competition.load_competition(competition_id)
    return sparkline(path, c.base_archetypes_data().values())

def sparkline(path, values, figsize=(2, 0.16)):
    values = list(values)
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    for v in ax.spines.values():
        v.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.bar(range(len(values)), values, 1/1.1, align='edge', color='#cccccc')
    plt.margins(y=0, x=0)
    fig.savefig(path, transparent=True, pad_inches=0, bbox_inches='tight')
    plt.clf()
    return path

def determine_path(name):
    pathlib.Path(configuration.get('charts_dir')).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(configuration.get('charts_dir')):
        raise DoesNotExistException('Cannot store graph images because {dir} does not exist.'.format(dir=configuration.get('charts_dir')))
    return os.path.join(configuration.get('charts_dir'), name)
