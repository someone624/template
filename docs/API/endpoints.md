# API Endpoints

This document lists most available endpoints for the **Project Name** API.

---

## User Management

### 1. **GET `/users`**
Retrieve a list of all users.

**Query Parameters:**
- `page` (optional): Page number for pagination.
- `limit` (optional): Number of users per page.

**Example Request:**
```http
GET /v1/users?page=1&limit=10
Authorization: Bearer <your-access-token>
```

**Example Response:**
```json
{
  "status": 200,
  "message": "Users retrieved successfully",
  "data": [
    { "id": 1, "name": "Alice" },
    { "id": 2, "name": "Bob" }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5
  }
}
```

---

### 2. **POST `/users`**
Create a new user

**Required Body Parameters**
- `name` (string): The name of the user.
- `email` (string): The email address of the user.

**Example Request**
```http
POST /v1/users
Content-Type: application/json
Authorization: Bearer <your-access-token>

{
  "name": "Charlie",
  "email": "charlie@example.com"
}
```

**Example Respnse:**
```json
{
  "status": 201,
  "message": "User created successfully",
  "data": {
    "id": 3,
    "name": "Charlie",
    "email": "charlie@example.com"
  }
}
```

---

## Product Management

### **GET `/products`**
Retrieves a list of all products
### **POST `/products`**
Creates a new product

---

## Analytics

### **GET `/analytics/overview`**
Gets data of key analytics
### **GET `/analytics/sales`**
Gets sales data

---

#### List of all endpoints
- GET `/users`
- POST `/users`
- GET `/products`
- POST `/products`
- GET `/analytics/overview`
- GET `analytics/sales`

Additional Endpoints:
- GET `/users/{id}`       - Gets user by ID
- DELETE `/users/{id}`    - Deletes a user
- GET `/orders`           - Gets a list of all orders
- GET `/orders/{id}`      - Gets data about a specific order
- POST `/orders`          - Makes a new order

## Notes
- Include the `Authorization` header with every request.
- Refer to the [Authentication Guide](authorization.md) for token details.
