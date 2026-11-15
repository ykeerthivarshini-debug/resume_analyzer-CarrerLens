import sqlite3
import pandas as pd
import os

def initialize_database():
    # 1. Setup paths
    db_folder = 'dataset'
    db_path = os.path.join(db_folder, 'jobs.db')
    csv_path = 'live_jobs.csv' # Ensure your Excel is saved as this CSV name

    # Create folder if it doesn't exist
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    # 2. Connect to SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 3. Create the table structure
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            required_skills TEXT,
            link TEXT
        )
    ''')

    # 4. Sample 2026 Data (In case your CSV is empty)
    sample_data = [
        ("Software Engineer III (Gen AI)", "JPMorganChase", "Hyderabad", "python, sql, nlp", "https://jpmc.com/careers"),
        ("AI Python Intern", "Techolution", "Hyderabad", "python, pytorch, machine learning", "https://techolution.com"),
        ("Python Developer (Fresher)", "Virtue Software", "Hyderabad", "python, flask, sql", "#"),
        ("Junior AI Engineer", "Exelo Technologies", "Hyderabad", "python, deep learning, qiskit", "#"),
        ("ML Data Operations", "Amazon", "Hyderabad", "python, pandas, sql", "https://amazon.jobs")
    ]

    # 5. Load from CSV if it exists, otherwise use sample data
    try:
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            # Ensure CSV columns match: title, company, location, required_skills, link
            df.to_sql('jobs', conn, if_exists='replace', index=False)
            print(f"✅ Success: Imported data from {csv_path}")
        else:
            cursor.executemany('INSERT INTO jobs (title, company, location, required_skills, link) VALUES (?,?,?,?,?)', sample_data)
            print("💡 Note: No CSV found. Inserted sample March 2026 vacancies instead.")
    
    except Exception as e:
        print(f"❌ Error: {e}")

    conn.commit()
    conn.close()
    print(f"🚀 Database ready at {db_path}")

if __name__ == "__main__":
    initialize_database()