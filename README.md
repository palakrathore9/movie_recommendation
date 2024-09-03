# Movie Recommender Project

This Django-based project allows users to search for movies using semantic queries. It leverages a pre-trained model from Hugging Face to generate embeddings and uses ChromaDB for vector storage, enabling effective movie recommendations based on user input.

## Setup Instructions

1.**Clone the Repository:**
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
 ```

2.**Install Dependencies:**

  ```bash
  pip install -r requirements.txt
 ```

3.**Apply Migrations:**

 ```bash
 python manage.py migrate
  ```

4.**Load Movie Data and Generate Embeddings:**

  ```bash
  python manage.py load_movie_data
   ```
    
5.**Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000/ to use the application.

