package com.theater_service.theaterservice.repository;

import com.theater_service.theaterservice.entity.Seat;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface SeatRepository extends JpaRepository<Seat, Long> {
    List<Seat> findByAuditoriumId(Long auditoriumId);

}
