-- Script to convert the database, table, and field to UTF8 (utf8mb4)

-- Convert database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert table and field to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN name TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
