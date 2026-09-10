from client import DPLLSatSolver

def main():
    print("=== Testing DPLL SAT Solver ===")
    solver = DPLLSatSolver()
    
    # Formula: (x1 or x2) and (-x1 or x2) and (x1 or -x2)
    clauses = [[1, 2], [-1, 2], [1, -2]]
    assignment = solver.solve(clauses)
    print(f"CNF Clauses: {clauses}")
    print(f"Satisfying Assignment: {assignment}")
    assert assignment is not None
    assert assignment[1] is True and assignment[2] is True

    # Unsatisfiable formula: (x1) and (-x1)
    unsat = solver.solve([[1], [-1]])
    print(f"Unsatisfiable Check: {unsat}")
    assert unsat is None
    print("=== DPLL SAT Verification Complete ===")

if __name__ == "__main__":
    main()
