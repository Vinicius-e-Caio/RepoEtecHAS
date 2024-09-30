package com.etechas.pw_study.controller;

import com.etechas.pw_study.entity.Disciplina;
import com.etechas.pw_study.service.DisciplinaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/disciplinas")
public class DisciplinaController {
    @Autowired
    private DisciplinaService service;
    @GetMapping
    public List<Disciplina> listar(){
        return service.listar();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Disciplina> buscarPorId(@PathVariable Long id) {
        var existe = service.buscarPorId(id);
        if (existe.isPresent()) {
            return ResponseEntity.ok(existe.get());
        }
        else {
            return ResponseEntity.notFound().build();
        }
        /*return service.buscarPorId(id)
                .map(d-> ResponseEntity.ok(d))
                .orElse(ResponseEntity.notFound().build());*/
    }
    @PostMapping
    public void cadastrar(@RequestBody Disciplina disciplina){
        service.cadastrarDisciplina(disciplina);
    }
}
