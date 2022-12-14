# Sentiment analysis

Perform sentiment analysis on english text using django web app running on docker.

We created a pipeline where the local git repository is mounted on docker using volume.
- DockerFile containes all the environment requirement for the project
- DockerCompose mount the volume (The volume contains all the folder such as django, and model)

For the python part, we started the project by a phase of preprocessing where the text was tokenized, filtered to remove words that not containing important information (stopwords) and stem the words to tighten the dictionnary. Then we vetorized our sentences by creating a sparse matrix.



## To run the project
``
docker-compose up
``
Then type in the browser
``http://localhost:8000/``

We have tried one classifier so far, which is the Multinomial Naive Bayes Classifier. It has yielded an accuracy score of 85% on our testing set. We plan on furthering our search for a better classifier. But for now, we will use this model to make sure our pipeline is well deployed. 

