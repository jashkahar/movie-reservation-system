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

    public List<Movie> searchMovies(String genre, String language, String keyword, Boolean nowshowing) {
        if (genre != null) {
            return movieRepository.findByGenre(genre);
        } else if (language != null) {
            return movieRepository.findByLanguage(language);
        } else if (keyword != null) {
            return movieRepository.findByTitleContaining(keyword);
        } else if (nowshowing != null) {
            return movieRepository.findByNowshowing(nowshowing);
        } else {
            return movieRepository.findAll();
        }
    }

    public List<Movie> getNowShowingMovies() {
        return movieRepository.findByNowshowing(true);
    }

}
