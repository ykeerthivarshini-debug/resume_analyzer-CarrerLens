import pandas as pd
import os

def check_my_csv():
    csv_path = 'live_jobs.csv'
    
    if not os.path.exists(csv_path):
        print(f"❌ Error: {csv_path} not found in this folder.")
        return

    try:
        # Read only the first few rows to check format
        df = pd.read_csv(csv_path)
        print("✅ CSV Found!")
        print("\n--- Your Current Headers ---")
        print(df.columns.tolist())
        
        # Check for required columns
        required = ['title', 'company', 'location', 'required_skills', 'link']
        missing = [col for col in required if col not in df.columns]
        
        if not missing:
            print("\n✅ All required headers are present!")
        else:
            print(f"\n❌ Missing headers: {missing}")
            print(f"Please rename your Excel columns to: {required}")

        print("\n--- First 2 Rows of Data ---")
        print(df.head(2))

    except Exception as e:
        print(f"❌ Error reading CSV: {e}")

if __name__ == "__main__":
    check_my_csv()