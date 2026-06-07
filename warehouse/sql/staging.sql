CREATE OR REPLACE VIEW staging.stg_keystrokes AS
SELECT *
FROM raw.keystroke_raw;

SELECT COUNT(*)
FROM staging.stg_keystrokes;