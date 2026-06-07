CREATE OR REPLACE VIEW analytics.user_typing_metrics AS
SELECT
    AVG(feature_1) AS avg_feature_1,
    AVG(feature_2) AS avg_feature_2,
    AVG(feature_3) AS avg_feature_3,
    AVG(feature_4) AS avg_feature_4,
    AVG(feature_5) AS avg_feature_5,
    AVG(feature_6) AS avg_feature_6,
    AVG(feature_7) AS avg_feature_7,
    AVG(feature_8) AS avg_feature_8,
    AVG(feature_9) AS avg_feature_9,
    AVG(feature_10) AS avg_feature_10,
    COUNT(*) AS total_records
FROM staging.stg_keystrokes;

SELECT *
FROM analytics.user_typing_metrics;