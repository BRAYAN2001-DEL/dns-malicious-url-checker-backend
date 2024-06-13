CREATE DATABASE dns;

CREATE TABLE url_analysis_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url_id VARCHAR(255) NOT NULL,
    url_name VARCHAR(255) NOT NULL,
    first_submission_date VARCHAR(255) NOT NULL
);
