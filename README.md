# Sentiment analysis

Perform sentiment analysis on english text using django web app running on docker.

We created a pipeline where the local git repository is mounted on docker using volume.
- DockerFile containes all the environment requirement for the project
- DockerCompose mount the volume (The volume contains all the folder such as django, and model)

For the python part, we started the project by a phase of preprocessing where the text was tokenized, filtered to remove words that not contain important information (stopwords)and stem the words to tighten the dictionnary. Then we vetorized our sentences by creating a sparse matrix.



## To run the project
``
docker-compose up
``
Then type in the browser
``http://localhost:8000/``

For now the model is not trained yet.

