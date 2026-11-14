# Dockerized Microservices Playground with Nginx API Gateway

A local, containerized microservices lab built with Docker Compose. Three independent services (User, Order, and Product) are exposed through a single Nginx API Gateway, with Docker bridge networking and request-rate limiting on the Product API.

## Lab details

| Item | Value |
|---|---|
| Platform | Windows + Ubuntu on WSL 2 |
| Container runtime | Docker Desktop |
| Orchestration | Docker Compose |
| API Gateway | Nginx (nginx:alpine) |
| User Service | Python 3.9 + Flask |
| Order Service | Node.js 18 + Express |
| Product Service | Node.js 18 + Express |
| Network | User-defined Docker bridge network (lab-net) |
| Exercise type | Local, self-directed hands-on lab |
| Completion | Core stack deployed; final rate-limit and failure-isolation evidence pending |

## 1. Objective

Build and run a small microservices environment locally, route client requests through one API Gateway, understand service-to-service discovery on a Docker network, and configure basic request-rate limiting.

## 2. Architecture

~~~mermaid
flowchart TB
    Client["Client / curl"] -->|HTTP :8080| Gateway["Nginx API Gateway"]
    Gateway -->|/api/users| User["User Service - Flask :5000"]
    Gateway -->|/api/orders| Order["Order Service - Express :5000"]
    Gateway -->|/api/products| Product["Product Service - Express :5000"]
    User --- Network["Docker bridge network: lab-net"]
    Order --- Network
    Product --- Network
    Gateway --- Network
~~~

The client sends requests to the host on port 8080. Nginx routes each API path to the corresponding service by its Docker Compose service name. Containers communicate over the shared bridge network using their internal port 5000; the Product Service is intentionally not published directly to the host.

## 3. Repository contents

~~~text
01-docker-microservices-api-gateway/
├── README.md
├── docker-compose.yml
├── gateway/
│   └── nginx.conf
├── user-service/
│   ├── app.py
│   └── Dockerfile
├── order-service/
│   ├── server.js
│   └── Dockerfile
├── product-service/
│   ├── server.js
│   └── Dockerfile
└── Screenshots/
~~~

## 4. API routes

| Gateway route | Upstream service | Expected response |
|---|---|---|
| GET /api/users/1 | user-service:5000/users/1 | User ID, name, and membership |
| GET /api/orders | order-service:5000/orders | Sample order list |
| GET /api/products | product-service:5000/products | Sample product list |

## 5. Run the lab

From this project directory:

~~~bash
docker compose config
docker compose up -d --build
docker compose ps
~~~

Test the APIs:

~~~bash
curl -i http://localhost:8080/api/users/1
curl -i http://localhost:8080/api/orders
curl -i http://localhost:8080/api/products
~~~

Expected successful responses use HTTP 200 and return JSON.

Stop, start, and remove the stack:

~~~bash
docker compose stop
docker compose start
docker compose down
~~~

Use **docker compose down** when finished to stop and remove the containers and Compose network. It does not delete the project source files.

## 6. Nginx routing and rate limiting

Nginx forwards the three gateway paths to their matching upstream services. The Product API uses the following rate-limit policy:

- Shared zone: product_limit (10 MB)
- Sustained rate: 5 requests per second per client IP
- Burst allowance: 2 requests
- nodelay: excess requests within the burst are not queued

Nginx's default limit-request rejection status is HTTP 503. The actual response mix depends on request timing and should be captured during verification.

Run a quick request burst:

~~~bash
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "Request $i: HTTP %{http_code}\n" \
    http://localhost:8080/api/products
done
~~~

Expected behavior: accepted requests return 200; requests rejected by the configured limit return 503. If every request returns 200, check the active Nginx configuration and run the burst again.

## 7. Verification record

| Check | Result |
|---|---|
| Docker Compose stack | Four containers observed running: gateway and three services |
| User API through gateway | JSON response received |
| Order API through gateway | JSON response received |
| Product API through gateway | Route corrected and confirmed working |
| Failure-isolation test | Not recorded in the available test evidence |
| Rate-limit status-code test | Configuration added; final 200/503 output not yet recorded |

Only the checks listed as observed should be treated as verified. Add sanitized terminal screenshots to the Screenshots directory after capturing the final tests.

## 8. Security and operational considerations

- Keep all services on the private Compose bridge network; publish only the gateway port when a host-accessible entry point is sufficient.
- The User and Order host-port mappings (5001 and 5002) are retained for direct local testing in this exercise. Remove these mappings for a gateway-only deployment.
- The sample APIs do not implement authentication, authorization, TLS termination, persistent storage, or production-grade health checks.
- Rate limiting is a protective control, not a substitute for authentication, input validation, monitoring, or upstream capacity planning.
- Do not expose this development stack directly to the public internet.

## 9. Key takeaways

- Docker Compose can define and run a multi-container application from one configuration.
- Containers on a shared user-defined bridge network can discover each other by service name.
- An API Gateway provides a single client-facing entry point and centralizes routing controls.
- Independent services can be restarted and operated separately.
- Nginx can apply request-rate limits at the gateway layer.

## 10. Possible improvements

- Add health checks and readiness-aware startup behavior.
- Remove direct host port mappings from backend services.
- Add structured logging, request IDs, and centralized log collection.
- Add API authentication and HTTPS.
- Add automated integration tests and capture verified rate-limit and failure-isolation evidence.
