package com.moviereservation.movieservice.service;

import com.moviereservation.movieservice.entity.Movie;
import com.moviereservation.movieservice.repository.MovieRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MovieServicesAPI {
    private final MovieRepository movieRepository;

    public MovieServicesAPI(MovieRepository movieRepository) {
        this.movieRepository = movieRepository;
    }

    public List<Movie> getAllMovies() {
        return movieRepository.findAll();
    }

    public Movie addMovie(Movie movie) {
        return movieRepository.save(movie);
    }
}

