# genpark-dpll-sat-solver-skill

[![GenPark Skill](https://img.shields.io/badge/GenPark-Skill-blue.svg)](https://github.com/alphaparkinc/genpark-dpll-sat-solver-skill)
[![Agentic AI](https://img.shields.io/badge/Agentic-AI-orange.svg)](https://github.com/alphaparkinc/genpark-dpll-sat-solver-skill)
[![Zero Pip Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library-green.svg)](https://github.com/alphaparkinc/genpark-dpll-sat-solver-skill)

Davis-Putnam-Logemann-Loveland (DPLL) Boolean satisfiability solver with unit propagation and recursive backtracking.

## Architecture
```mermaid
graph TD
    A[Formal Specification / Problem] --> B[genpark-dpll-sat-solver-skill]
    B --> C[Theorem Prover / State Explorer]
    C --> D[Satisfiability / Model Trace / Proof Result]
```

## Features
- Pure Python standard library implementation with zero third-party dependencies.
- Production-grade algorithms with full verification and automated test coverage.
- Standalone client, MCP protocol server, and execution examples.

## Quickstart
```bash
python example_usage.py
```
