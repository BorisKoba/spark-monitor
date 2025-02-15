from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.models import SparkJobLog
import pyiceberg
import os
import json

app = FastAPI()

iceberg_file_path = "./iceberg_logs"
os.makedirs(iceberg_file_path, exist_ok=True)
@app.get("/logs/")
async def get_logs():
    logs = []
    try:
        for filename in os.listdir(iceberg_file_path):
            if filename.endswith(".json"):
                with open(os.path.join(iceberg_file_path, filename), "r") as f:
                    logs.append(json.load(f)) 
        return logs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading logs: {str(e)}")
@app.post("/submit_log/")
async def submit_log(log: SparkJobLog):
    log_data = log.dict()   
    log_file = os.path.join(iceberg_file_path, f"{log.job_id}.json")
    try:
        with open(log_file, "w") as f:
            json.dump(log_data, f)
        return {"status": "success", "message": "Log saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))