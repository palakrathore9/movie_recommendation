from django.shortcuts import render
from .forms import MovieSearchForm
from .models import Movie
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def search_movies(request):
    form = MovieSearchForm()
    results = None

    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            query_embedding = model.encode(query).tolist()

            movies = Movie.objects.all()
            embeddings = np.array([movie.embedding for movie in movies])
            similarities = cosine_similarity([query_embedding], embeddings)
            movies_with_similarity = zip(movies, similarities[0])
            results = sorted(movies_with_similarity, key=lambda x: x[1], reverse=True)[:10]

    return render(request, 'movies/search.html', {'form': form, 'results': results})
