# Movie Recommendations
A recommender system is one that seeks to predict the "rating" or "preference" a user would give to an item. 

## Methods



### Cosine Similarity [Notebook](./notebooks/Recommending%20movies%20using%20Cosine%20similarity.ipynb)

Since the one-hot representation of movies is too sparse, we can create a dense representation using Principal Component Analysis. On this dense representation, we can recommend similar movies using cosine similarity metric.

### Truncated SVD [Notebook](./notebooks/Recommending%20movies%20using%20Truncated%20SVD.ipynb)

In this method, we create representations of both, movies and users by considering the top-n factors from their Singular Value Decompositions. Next, using the (movie, user) representaion pairs we can train a regression model to predict the corresponding rating value.

### Restricted Boltzmann Machines [Notebook](./notebooks/Recommending%20movies%20using%20Restricted%20Boltzmann%20Machines.ipynb)

The Restricted Boltzmann Machine (RBM) is a special type of artificial neural network. Here, the RBM is trained using the  Contrastive Divergence loss function to estimate the distribution of ratings given the movie ratings of a user.

### SVD Matrix Factorisation [Notebook](./notebooks/Recommending%20movies%20using%20SVD%20Matrix%20Factorisation.ipynb)

This method involves embedding movies in a vector space by using a stochastic estimation of Matrix Factorisation. The movie embedding can be considered a representation of the movie features and we can make recommendations using a similarity metric.


### Probabilistic Matrix Factorization [Repository](https://github.com/saurabhmathur96/variational-collaborative-filtering)

A Bayesian approach to factorizing the Ratings matrix using Variational Inference. As a result, each rating prediction is a Gaussian with its variance representing uncertainty.


## Miscellaneous

- Movie Sentiment : Analysing a movie review's text to determine whether it is positive or negative. [Find the repository here](https://github.com/saurabhmathur96/movie-sentiment).

- Anime Finder : A cosine similarity based anime recommendation engine along with a web-based interface. [Find the repository here](https://github.com/saurabhmathur96/Anime-Finder).

- Book Recommendations : An experiment using the Truncated SVD method to recommend books. [Find the notebook  here](http://nbviewer.jupyter.org/github/saurabhmathur96/jupyter-notebooks/blob/master/Book%20Recommendation.ipynb).
