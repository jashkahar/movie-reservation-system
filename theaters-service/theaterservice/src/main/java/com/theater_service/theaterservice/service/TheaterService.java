package com.theater_service.theaterservice.service;

import com.theater_service.theaterservice.entity.Theater;
import com.theater_service.theaterservice.repository.TheaterRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TheaterService {
    @Autowired
    private TheaterRepository theaterRepository;

    public List<Theater> getAllTheaters() {
        return theaterRepository.findAll();
    }

    public Theater getTheaterById(Long id) {
        return theaterRepository.findById(id).orElse(null);
    }

    public Theater addTheater(Theater theater) {
        return theaterRepository.save(theater);
    }

    public void deleteTheater(Long id) {
        theaterRepository.deleteById(id);
    }
}
