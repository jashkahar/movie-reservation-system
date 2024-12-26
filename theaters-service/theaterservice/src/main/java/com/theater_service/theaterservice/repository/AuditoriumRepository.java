package com.theater_service.theaterservice.repository;

import com.theater_service.theaterservice.entity.Auditorium;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AuditoriumRepository extends JpaRepository<Auditorium, Long> {
    List<Auditorium> findByTheaterId(Long theaterId);
}
