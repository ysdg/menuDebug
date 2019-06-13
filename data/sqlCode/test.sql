-- select * from information_schema.columns WHERE table_schema = 'public' and table_name = 'test_try';
-- INSERT INTO test_try(time) values(LOCALTIMESTAMP);
-- DELETE FROM test_try where time_sec = null OR time_year = null;
-- DELETE FROM test_try where id = 1;
-- UPDATE test_try SET time_sec = 0 where time_year = null;
-- COMMENT ON TABLE test_try is 'just a try';
-- ALTER TABLE test_try ADD COLUMN endline int;
-- SELECT LOCALTIMESTAMP;
-- SELECT *, ROW_NUMBER() OVER(ORDER BY time) FROM test_try;
SELECT * FROM test_try