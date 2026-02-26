import psycopg2
import sys

print("Connecting to PostgreSQL...")
try:
    conn = psycopg2.connect(
        user='postgres',
        password='maina',
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    print("Connected successfully.")
    
    cur = conn.cursor()
    
    print("Creating sample_user...")
    try:
        cur.execute("CREATE USER sample_user WITH PASSWORD 'password' CREATEDB")
        print("sample_user created.")
    except Exception as e:
        print(f"User creation info: {e}")
        
    print("Checking if database exists...")
    cur.execute("SELECT 1 FROM pg_database WHERE datname='login_task'")
    exists = cur.fetchone()
    
    if not exists:
        print("Creating database login_task...")
        cur.execute('CREATE DATABASE login_task')
        print("Database login_task created successfully.")
    else:
        print("Database login_task already exists.")
    
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
