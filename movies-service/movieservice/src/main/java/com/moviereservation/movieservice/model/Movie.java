package com.moviereservation.movieservice.model;

import javax.persistence.Column;
import javax.persistence.Entity;

@Entity
public class Movie {

    @Column(nullable = false)
    private boolean nowshowing = false;

    public boolean isNowshowing() {
        return nowshowing;
    }

    public void setNowshowing(boolean nowshowing) {
        this.nowshowing = nowshowing;
    }
}
