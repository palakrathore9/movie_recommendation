import pandas as pd
from django.core.management.base import BaseCommand
from movies.models import Movie
from sentence_transformers import SentenceTransformer

class Command(BaseCommand):
    help = 'Load movie data from a CSV URL and generate embeddings'

    def handle(self, *args, **kwargs):
        # Specify the URL of the CSV file
        url = "https://raw.githubusercontent.com/datum-oracle/netflix-movie-titles/main/titles.csv"

        # Read the CSV file from the URL
        df = pd.read_csv(url)

        # Initialize the pre-trained model from Hugging Face
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        # Loop through each row in the DataFrame and save the data to the database
        for _, row in df.iterrows():
            combined_features = f"{row['title']} {row['description']} {row['genres']}"
            embedding = model.encode(combined_features).tolist()  # Generate embeddings

            # Create and save the Movie object
            movie, created = Movie.objects.get_or_create(
                title=row['title'],
                description=row['description'],
                genres=row['genres'],
                defaults={'embedding': embedding}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Movie '{movie.title}' loaded successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"Movie '{movie.title}' already exists"))

        self.stdout.write(self.style.SUCCESS('All movies have been loaded and embeddings generated'))

