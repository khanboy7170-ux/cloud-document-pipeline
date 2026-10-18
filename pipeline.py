import os
import json
from supabase import create_client, Client

# Supabase Credentials
SUPABASE_URL = "https://mmxetrkmzttpzhukpkzc.supabase.co"
SUPABASE_KEY = "YOUR_SUPABASE_SERVICE_ROLE_KEY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

INPUT_BUCKET = "khan.boy"
OUTPUT_BUCKET = "processed-results"

def process_documents():
    print(f"[1] Checking input bucket '{INPUT_BUCKET}' for new files...")
    files = supabase.storage.from_(INPUT_BUCKET).list()
    
    if not files:
        print("Koi file nahi mili! Pehle Supabase par file upload karo.")
        return

    for file in files:
        file_name = file['name']
        if file_name.startswith('.'):
            continue
        
        print(f"\n[2] Processing file: {file_name}")
        data = supabase.storage.from_(INPUT_BUCKET).download(file_name)
        content = data.decode('utf-8')
        
        lines = len(content.splitlines())
        words = len(content.split())
        chars = len(content)
        
        print(f"    Lines: {lines} | Words: {words} | Characters: {chars}")
        
        # 1. JSON report create karke output bucket me save karo
        report = {
            "file_name": file_name,
            "status": "COMPLETED",
            "lines": lines,
            "words": words,
            "characters": chars
        }
        report_name = f"result_{file_name}.json"
        supabase.storage.from_(OUTPUT_BUCKET).upload(
            path=report_name,
            file=json.dumps(report, indent=4).encode('utf-8'),
            file_options={"upsert": "true"}
        )
        print(f"[3] Report saved to '{OUTPUT_BUCKET}/{report_name}'")
        
        # 2. Database table 'document_logs' me status entry / update karo
        supabase.table("document_logs").upsert({
            "file_name": file_name,
            "status": "PROCESSED",
            "word_count": words
        }).execute()
        print(f"[4] Status logged to 'document_logs' database table!")

if __name__ == "__main__":
    process_documents()
