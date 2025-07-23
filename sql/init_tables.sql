CREATE TABLE IF NOT EXISTS ad_sales (
    date TEXT,
    item_id INTEGER,
    ad_sales FLOAT,
    impressions INTEGER,
    ad_spend FLOAT,
    clicks INTEGER,
    units_sold INTEGER
);

CREATE TABLE IF NOT EXISTS eligibility (
    eligibility_datetime_utc TEXT,
    item_id INTEGER,
    eligibility TEXT,
    message TEXT
);

CREATE TABLE IF NOT EXISTS total_sales (
    date TEXT,
    item_id INTEGER,
    total_sales FLOAT,
    total_units_ordered INTEGER
);
