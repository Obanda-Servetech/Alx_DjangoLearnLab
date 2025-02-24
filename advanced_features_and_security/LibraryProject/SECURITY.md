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
