# 🧩 Brute-force Login — Concise Report

### 🎯 Objective

Test if the login form is susceptible to brute-force to obtain a high-privilege account.

---

### Steps

<img width="1439" height="896" alt="Capture d’écran 2025-09-23 à 19 44 36" src="https://github.com/user-attachments/assets/86059069-fba7-4eb3-90ea-2db63c682b1f" />


1. **Target:** login form; username `admin`.
2. **SQLi checks:** simple payloads (e.g. `1' OR '1'='1`) — **no success**.
3. **Wordlist:** common passwords prepared (e.g. `password`, `123456`, `shadow`, …).
4. **Attack:** Burp Suite **Sniper** mode against the `password` parameter.
   <img width="1428" height="778" alt="Capture d’écran 2025-09-23 à 19 49 35" src="https://github.com/user-attachments/assets/82f74b6c-dce3-47c7-a0b4-8ef0c4015494" />

6. **Result:** During the Burp Suite sniper attack, each password attempt produced a slightly different server response:
- Failed attempts: longer response with an error message
- Successful attempt (shadow): shorter response, redirect, or different headers.
The shorter response indicated the correct password, confirming that shadow was valid for the admin account.
   Example POST:

   ```
   POST /login
   username=admin&password=shadow
   ```
<img width="1286" height="772" alt="Capture d’écran 2025-09-23 à 20 27 52" src="https://github.com/user-attachments/assets/f0f00c77-6f6d-455e-93d0-d5f3cd291fcc" />

---

### Conclusion

The authentication endpoint is vulnerable to credential-guessing: `shadow` from the wordlist granted administrative access.

---

### Quick Remediation

* Implement rate limiting and progressive backoff.
* Account lockout after repeated failures.
* Enforce MFA for privileged accounts.
* Add CAPTCHA / adaptive challenges on login.
* Monitor/auth logs and alert on abnormal attempts.
* Strengthen password policy (complexity, rotation).
