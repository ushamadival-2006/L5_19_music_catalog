# Lab 5: Static Code Analysis — Reflection

**1. What is static code analysis?**

Static code analysis examines source code without executing it to identify potential bugs, security risks and style violations.

**2. How do Pylint, Bandit and Flake8 differ?**

Pylint checks code quality and programming practices. Bandit identifies potentially insecure coding patterns. Flake8 checks Python style and common code issues.

**3. What issues were found and fixed?**

The analysis identified a mutable default argument, SQL query construction using string formatting, unsafe pickle deserialization, missing docstrings, inconsistent function naming, broad exception handling and formatting violations.

**4. How did static analysis improve the program?**

The program became more readable and maintainable, SQL queries became safer, and unsafe deserialization was replaced with JSON. The Pylint score improved from 4.57/10 to 10.00/10, and Flake8 reported no remaining violations. Bandit retained one low-severity warning concerning non-cryptographic random selection, which was reviewed in context.
