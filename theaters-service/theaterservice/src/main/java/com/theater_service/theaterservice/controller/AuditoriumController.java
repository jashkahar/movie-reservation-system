package com.theater_service.theaterservice.controller;

import com.theater_service.theaterservice.entity.Auditorium;
import com.theater_service.theaterservice.service.AuditoriumService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;

import java.util.List;

@RestController
@RequestMapping("/auditoriums")
public class AuditoriumController {
    @Autowired
    private AuditoriumService auditoriumService;

    @GetMapping
    public List<Auditorium> getAllAuditoriums() {
        return auditoriumService.getAllAuditoriums();
    }

    @GetMapping("/{id}")
    public Auditorium getAuditoriumById(@PathVariable Long id) {
        return auditoriumService.getAuditoriumById(id);
    }

    @GetMapping("/theater/{theaterId}")
    public List<Auditorium> getAuditoriumsByTheaterId(@PathVariable Long theaterId) {
        return auditoriumService.getAuditoriumsByTheaterId(theaterId);
    }

    @PostMapping(consumes = "application/json")
    public Auditorium addAuditorium(@RequestBody Auditorium auditorium) {
        return auditoriumService.addAuditorium(auditorium);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> deleteAuditorium(@PathVariable Long id) {
        auditoriumService.deleteAuditorium(id);
        return ResponseEntity.ok().build();
    }
}