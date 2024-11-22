# Authentication

This document explains how to authenticate with the **Project Name** API. The API uses **OAuth 2.0 Bearer Tokens** for secure access.

---

## Steps to Authenticate

### 1. Register Your Application
Register your application to obtain a `client_id` and `client_secret`.

- Visit: [Developer Portal](https://api.example.com/developer-portal)
- Fill out the registration form.
- Retrieve your credentials.

---

### 2. Request an Access Token
Use the ```/auth/token``` endpoint to obtain an access token.

#### Endpoint:
```http
POST /auth/token
```

**Required Body Parameters:**
- ```client_id``` (string): Your client ID.
- ```client_secret``` (string): Your client secret.
- ```grant_type``` (string): Set to client_credentials.

**Example Request**
```http
POST /auth/token
Content-Type: application/json

{
  "client_id": "your-client-id",
  "client_secret": "your-client-secret",
  "grant_type": "client_credentials"
}
```

**Example Response**
```json
{
  "access_token": "eyJhbGc...dXJsIiw",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

---

## Using the Access Token
Include the ```access_token``` in the ```Authorization``` header for all requests.

**Example Request**
```http
GET /v1/users
Authorization: Bearer eyJhbGc...dXJsIiw
```

---

## Refreshing Tokens
Tokens expire after 1 hour. Use the ```/auth/refresh``` endpoint to get a new access token.

**Endpoint**
```http
POST /auth/refresh
```

**Required Body Parameters:**
- ```refresh_token``` (string): Your refresh token.

**Example Request**
```http
POST /auth/refresh
Content-Type: application/json

{
  "refresh_token": "your-refresh-token"
}
```

**Example Response**
```json
{
  "access_token": "new-access-token",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

---

## Common Errors
- Check the [Trobbleshooting](../troubleshooting.md) file for errors
