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
    public List<Movie> getAllMovies() {
        return movieService.getAllMovies();
    }

    @PostMapping
    public Movie addMovie(@RequestBody Movie movie) {
        return movieService.addMovie(movie);
    }
}
