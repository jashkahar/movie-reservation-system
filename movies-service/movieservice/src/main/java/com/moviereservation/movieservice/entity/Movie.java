package com.moviereservation.movieservice.entity;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Data
public class Movie {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;
    private String description;
    private String genre;
    private String director;
    private int duration;
    private String language;
    private String posterUrl;
}
