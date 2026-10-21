# Endpoint Architecture Sketch

Client (Browser / Requests)
        |
        |  GET /api/v1/users/42?include_profile=true
        v
+-------------------------------------------------------------+
| FastAPI Local App                                           |
|                                                             |
| 1. Route Handler: @app.get("/api/v1/users/{user_id}")       |
| 2. Parameter Parsing: user_id: int, include_profile: bool    |
| 3. Execution: Fetch record / validate bounds                |
| 4. Error Handling: Return 404 JSON if not found             |
+-------------------------------------------------------------+
        |
        | HTTP 200 OK (Content-Type: application/json)
        v
{ "status": "success", "data": { ... } }