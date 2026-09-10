from client import DPLLSatSolver
import json

def handle_request(req):
    solver = DPLLSatSolver()
    action = req.get("action")
    if action == "solve":
        clauses = req.get("clauses", [])
        res = solver.solve(clauses)
        return {"status": "ok", "satisfiable": res is not None, "assignment": res}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "solve", "clauses": [[1, 2], [-1, 2]]})))
