Movie Recommender Project
This Django-based project allows users to search for movies using semantic queries. It leverages a pre-trained model from Hugging Face to generate embeddings and uses ChromaDB for vector storage, enabling effective movie recommendations based on user input.

Setup Instructions

Clone the Repository:
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender

Install Dependencies:
pip install -r requirements.txt

Apply Migrations:
python manage.py migrate

Load Movie Data and Generate Embeddings:
python manage.py load_movie_data

Run the Development Server:
python manage.py runserver

Visit http://127.0.0.1:8000/ to use the application.
