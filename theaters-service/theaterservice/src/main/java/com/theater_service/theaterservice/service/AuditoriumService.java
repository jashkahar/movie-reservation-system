package com.theater_service.theaterservice.service;

import com.theater_service.theaterservice.entity.Auditorium;
import com.theater_service.theaterservice.repository.AuditoriumRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AuditoriumService {
    @Autowired
    private AuditoriumRepository auditoriumRepository;

    public List<Auditorium> getAllAuditoriums() {
        return auditoriumRepository.findAll();
    }

    public Auditorium getAuditoriumById(Long id) {
        return auditoriumRepository.findById(id).orElse(null);
    }

    public List<Auditorium> getAuditoriumsByTheaterId(Long theaterId) {
        return auditoriumRepository.findByTheaterId(theaterId);
    }

    public Auditorium addAuditorium(Auditorium auditorium) {
        return auditoriumRepository.save(auditorium);
    }

    public void deleteAuditorium(Long id) {
        auditoriumRepository.deleteById(id);
    }
}
