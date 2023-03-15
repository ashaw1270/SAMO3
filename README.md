# SAMO3

This is a deep-learning neural network written in Python using the Keras library that predicts if a set of data comes from group of black or white people.

## Implementation

The neural network consists of an input layer of 2 neurons with a sigmoid activation, one hidden layer of 128 neurons also with a sigmoid activation, and an output layer of 2 neurons (black or white) with a softmax activation. The model compiles with an Adam optimizer and a binary cross-entropy loss function.

## Data

The data is split up into four .csv files. Each file is either data for training or testing and x (input) or y (output).
The data for the x values consists of two categories: average household income at age 35 and incarceration rate, each being that of
a certain "tract", as defined by the US Census, separated by the data from all black residents and all white residents, ignoring people of other or multiple races.
There are 88,570 data tuples for training and 10,000 data tuples for testing.
The data was taken from the opportunityatlas.org data set which can be found at https://opportunityinsights.org/data/?geographic_level=0&topic=0&paper_id=1652#resource-listing.

## Results

The learning model was able to predict whether a set of data came from a group of black or white people with 88% accuracy.
