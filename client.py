class DPLLSatSolver:
    """
    DPLL (Davis-Putnam-Logemann-Loveland) SAT Solver.
    Determines satisfiability of propositional logic formulas in CNF.
    """
    def solve(self, cnf_clauses):
        assignment = {}
        return self._dpll(cnf_clauses, assignment)

    def _dpll(self, clauses, assignment):
        simplified = []
        for clause in clauses:
            clause_true = False
            new_clause = []
            for lit in clause:
                var = abs(lit)
                val = assignment.get(var)
                if val is not None:
                    if (lit > 0 and val) or (lit < 0 and not val):
                        clause_true = True
                        break
                else:
                    new_clause.append(lit)
            if not clause_true:
                if len(new_clause) == 0:
                    return None
                simplified.append(new_clause)

        if not simplified:
            return assignment

        # Unit propagation
        for clause in simplified:
            if len(clause) == 1:
                unit_lit = clause[0]
                var = abs(unit_lit)
                val = (unit_lit > 0)
                new_assign = dict(assignment)
                new_assign[var] = val
                return self._dpll(clauses, new_assign)

        all_vars = sorted(list({abs(l) for cl in simplified for l in cl}))
        branch_var = all_vars[0]

        for val in [True, False]:
            new_assign = dict(assignment)
            new_assign[branch_var] = val
            res = self._dpll(clauses, new_assign)
            if res is not None:
                return res

        return None
