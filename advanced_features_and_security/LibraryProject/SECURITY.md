# Django Security Best Practices

## 1. Secure Settings
- `DEBUG = False` in production
- XSS, Clickjacking, and MIME type sniffing protection enabled
- CSRF and session cookies secured with HTTPS

## 2. CSRF Protection
- `{% csrf_token %}` added to all forms

## 3. Safe Data Handling
- Django ORM used for queries
- User input validated and sanitized

## 4. Content Security Policy (CSP)
- `django-csp` middleware enabled
- Restricts loading of scripts and styles from external sources

# Security Configuration for LibraryProject

## HTTPS Enforcement
- All HTTP requests are redirected to HTTPS (`SECURE_SSL_REDIRECT = True`).
- HTTP Strict Transport Security (HSTS) is enabled for 1 year (`SECURE_HSTS_SECONDS = 31536000`).

## Secure Cookies
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` ensure that cookies are transmitted only over HTTPS.

## Security Headers
- `X_FRAME_OPTIONS = "DENY"` prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` protects against MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True` enables built-in browser XSS protection.

## Deployment
- HTTPS enabled via Let’s Encrypt SSL on Nginx.
- All non-HTTPS traffic is permanently redirected.
