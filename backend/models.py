from pydantic import BaseModel
from typing import List, Optional

class SparkJobLog(BaseModel):
    job_id: str
    run_length: int  
    executor_count: int  
    operators: List[str]  
    errors: Optional[List[str]] = []  
    operator_lengths: List[int]  