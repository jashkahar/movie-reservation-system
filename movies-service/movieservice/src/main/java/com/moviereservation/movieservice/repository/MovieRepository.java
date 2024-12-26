package com.moviereservation.movieservice.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.moviereservation.movieservice.entity.Movie;

public interface MovieRepository extends JpaRepository<Movie, Long> {
    List<Movie> findByGenre(String genre);

    List<Movie> findByLanguage(String language);

    List<Movie> findByTitleContaining(String keyword);

    List<Movie> findByNowshowing(boolean nowshowing);
}
