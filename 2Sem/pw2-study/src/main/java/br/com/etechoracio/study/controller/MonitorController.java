package br.com.etechoracio.study.controller;

import br.com.etechoracio.study.entity.Disciplina;
import br.com.etechoracio.study.entity.Monitor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

public class MonitorController {
    @PostMapping("/cadastrar")
    public ResponseEntity<Monitor> cadastrarMonitor(@RequestBody Monitor monitor){
        var novaMonitor = service.cadastrarDisciplina(disciplina);
        return ResponseEntity.status(HttpStatus.CREATED).body(novaDisciplina);
    }
}
