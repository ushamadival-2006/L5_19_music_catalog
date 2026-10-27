# Lab 5: Static Code Analysis — Issue Report

| No. | Tool | Issue | Fix Applied |
|---|---|---|---|
| 1 | Pylint | Mutable default argument in `add_song()` | Replaced `playlist=[]` with `playlist=None` and initialized the list inside the function. |
| 2 | Bandit | Possible SQL injection through string-formatted SQL | Replaced string formatting with parameterized SQL queries. |
| 3 | Bandit | Unsafe deserialization using `pickle.loads()` | Replaced pickle serialization with JSON serialization and deserialization. |
| 4 | Pylint | Missing module and function docstrings | Added documentation strings. |
| 5 | Pylint | Function names did not follow snake_case | Renamed functions and updated their calls. |
| 6 | Pylint | Bare exception handling | Caught `sqlite3.Error` explicitly. |
| 7 | Flake8 | Long lines, ambiguous variable name and multiple statements per line | Reformatted the code and used descriptive variable names. |
| 8 | Bandit | B311: use of `random.choice()` | Reviewed the finding. Cryptographic randomness is unnecessary for ordinary music selection; the warning is documented as not security-sensitive for this use case. |

## Verification

- Original Pylint score: 4.57/10
- Updated Pylint score: 10.00/10
- Bandit: One low-severity B311 finding remains, documented above.
- Flake8: No reported violations after the changes.
- Program execution: Verified successfully with the expected output.
