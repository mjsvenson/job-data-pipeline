import psycopg2

conn = psycopg2.connect(
    dbname="job_pipeline",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT job_json FROM raw_jobs")
rows = cur.fetchall()

for row in rows:
    job = row[0]

    title = job.get("title")
    
    company_field = job.get("company")
    if isinstance(company_field, dict):
        company = company_field.get("display_name")
    else:
        company = company_field
    
    location_field = job.get("location")
    if isinstance(location_field, dict):
        location = location_field.get("display_name")
    else:
        location = location_field
    
    salary_min = job.get("salary_min")
    salary_max = job.get("salary_max")    
    created = job.get("created")

    cur.execute("""
        INSERT INTO jobs_clean (title, company, location, salary_min, salary_max, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, company, location, salary_min, salary_max, created))

conn.commit()
cur.close()
conn.close()


