package com.moviereservation.movieservice.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.moviereservation.movieservice.entity.Movie;

public interface MovieRepository extends JpaRepository<Movie, Long> {
}
