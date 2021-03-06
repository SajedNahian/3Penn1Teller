# 3Penn1Teller
## Sajed Nahian, Jeffrey Wu, Qian Zhou, Bo Lu

## Description of data set(s)
* [Cannabis Price by State](https://github.com/frankbi/price-of-weed/tree/master/data) :
From a github repo kindly created by some dude who had time to research this. However, these prices are a few years out of date, so we do have to keep that in mind.
* [Median Household Income by State](https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_income) :
Info from a Wikipedia article.
* These two datasets are related because cannabis prices vary between the states and correlations can be drawn between the median income of the state and the prices of cannabis in that state. Once again, we do need to be wary because the cannabis price dataset is a few years out of date. We believe this is significant to us, because legalization of cannabis is starting to spread to numerous states in America.

## How We Aim to Make This Data Alive
* Show a map of the United States with each state shaded a different color of green depending on the ratio of the median household income to the cannabis price within the state
* Users can hover over states to get specific information about each state such as cost of cannabis within that state for the different qualities of cannabis, the median household income within that state, and the exact ratio of household income to cannabis price ratio
* This data will allow users to explore potential correlation between economic status compared with the cannabis market.
## D3 Feature Utilization
* enter() cannabis price and income
    * Perhaps give option to vary year???
* Displays more information when mouseover happens
### Similar Galleries
* [Choropeth](https://observablehq.com/@d3/choropleth) We also aim to display a color-coded map of the United States. This gallery also may contain related information should we wish to explore the problem further.
* [Topojson US Map](http://bl.ocks.org/mapsam/6083585) Nice user interaction.
## Sketch-up of Envisioned Visualization
![Mockup](https://i.imgur.com/SQcenBK.png)

## LAUNCH CODES:
* $python3 -m venv (name of virtual environment)
* $ . (name of virtual environment)/bin/activate
* $pip3 install wheel
* $pip3 install flask
* $python3 app.py
* Go to the link given in terminal. [Or Click Here](http://127.0.0.1:5000/)

## *Disclaimer: Kids, don't do drugs.*
