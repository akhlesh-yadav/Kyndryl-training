Authentication Flow Diagram

1. ASCII Visual Architectural Diagram

+---------------+              1. Request Login              +-----------------+
|               |  ----------------------------------------> |                 |
|               |                                            |                 |
|     USER      |              8. Access Granted             |   APPLICATION   |
|   (Client)    | <----------------------------------------- |    (Service)    |
|               |                                            |                 |
+---------------+                                            +-----------------+
  |           ^                                                |             ^
  |           |                                                |             |
  | 3. Auth   | 4. Auth                                        | 5. Exchange | 6. Issue
  | Credentials | Code                                         | Code +      | Tokens
  | & MFA     | Redirect                                       | Client      | (ID & Access
  v           |                                                | Secret      |  Tokens)
+--------------------------------------------------------------v-------------+ |
|                                                                            | |
|                           IDENTITY PROVIDER (IdP)                          | |
|                           (e.g., Auth0, Azure AD)                          |<+
|                                                                            |
+----------------------------------------------------------------------------+


2. Mermaid Sequence Diagram

sequenceDiagram
    autonumber
    actor User as User / Client
    participant App as Application
    participant IdP as Identity Provider

    User->>App: 1. Request Login / Access Resource
    App-->>User: 2. Redirect to IdP Login Page
    User->>IdP: 3. Submit Credentials / Authenticate
    IdP-->>User: 4. Issue Authorization Code (Redirect to App)
    User->>App: 5. Pass Auth Code to Application
    App->>IdP: 6. POST Auth Code + Client Secret
    IdP-->>App: 7. Validate & Return Access/ID Tokens
    App-->>User: 8. Establish Session & Grant Access


3. High-Level Flow Chart

flowchart TD
    A[User] -->|1. Clicks Login| B[Application]
    B -->|2. Redirects to Login| C[Identity Provider]
    C -->|3. Prompts for Credentials| A
    A -->|4. Inputs Username/Password| C
    C -->|5. Returns Auth Code| B
    B -->|6. Requests Token with Auth Code| C
    C -->|7. Issues Access & ID Tokens| B
    B -->|8. Grants Access| A
