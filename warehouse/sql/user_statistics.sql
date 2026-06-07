CREATE OR REPLACE VIEW analytics.user_statistics AS
SELECT
    label,
    COUNT(*) AS total_samples,
    AVG(feature_1) AS avg_feature_1,
    AVG(feature_2) AS avg_feature_2,
    AVG(feature_3) AS avg_feature_3
FROM raw.keystroke_raw
GROUP BY label;

SELECT *
FROM analytics.user_statistics
LIMIT 10;