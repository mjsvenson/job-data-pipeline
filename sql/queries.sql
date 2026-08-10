-- Top hiring companies
SELECT company, COUNT(*) as job_count
FROM jobs_clean
GROUP BY company
ORDER BY job_count DESC
LIMIT 10;

-- Average salary range
SELECT 
    AVG(salary_min) as avg_min,
    AVG(salary_max) as avg_max
FROM jobs_clean;

-- Jobs by location
SELECT location, COUNT(*)
FROM jobs_clean
GROUP BY location
ORDER BY COUNT(*) DESC;