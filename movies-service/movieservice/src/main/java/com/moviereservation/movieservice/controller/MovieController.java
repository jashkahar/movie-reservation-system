package com.moviereservation.movieservice.controller;

import com.moviereservation.movieservice.entity.Movie;
import com.moviereservation.movieservice.service.MovieServicesAPI;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/movies")
public class MovieController {
    private final MovieServicesAPI movieService;

    public MovieController(MovieServicesAPI movieService) {
        this.movieService = movieService;
    }

    @GetMapping
    public List<Movie> getAllOrSearchMovies(
            @RequestParam(required = false) String genre,
            @RequestParam(required = false) String language,
            @RequestParam(required = false) String keyword,
            @RequestParam(required = false) Boolean nowshowing) {
        if (genre == null && language == null && keyword == null && nowshowing == null) {
            return movieService.getAllMovies();
        } else {
            return movieService.searchMovies(genre, language, keyword, nowshowing);
        }
    }

    @PostMapping
    public Movie addMovie(@RequestBody Movie movie) {
        return movieService.addMovie(movie);
    }
}
