# Cheatsheet pour les injections SQL inspirée de PayloadAllTheThings

## Payloads de version

### MSSQL
    SELECT @@version
    
### MYSQL
    SELECT version()
    
### OracleSQL
    SELECT user FROM dual UNION SELECT * FROM v$version

### PostgreSQL
    SELECT version()
    
### SQLite
    select sqlite_version();
    
### Cassandra 
