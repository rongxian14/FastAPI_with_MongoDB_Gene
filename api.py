from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pymongo import MongoClient
from typing import List, Dict

app = FastAPI()
class ExpressionItem(BaseModel):
    Sample_ID: str = Field(..., alias='Sample ID')
    Expression_Level: float = Field(..., alias='Expression Level')
    Condition: str

class SampleItem(BaseModel):
    Sample_ID: str = Field(..., alias='Sample ID')
    Patient_ID: str = Field(..., alias='Patient ID')
    Collection_Date: str = Field(..., alias='Collection Date')
    Condition: str
    Tissue_Type: str = Field(..., alias='Tissue Type')

class Gene(BaseModel):
    Gene_ID: str = Field(..., alias='Gene ID')
    Gene_Name: str = Field(..., alias='Gene Name')
    Chromosome: str
    Start_Position: int = Field(..., alias='Start Position')
    End_Position: int = Field(..., alias='End Position')
    expression: List[ExpressionItem]
    sample: List[SampleItem]
    
class ExpressionDataResponse(BaseModel):
    expression: List[ExpressionItem]

class SampleDataResponse(BaseModel):
    sample: List[SampleItem]

@app.get("/")
async def home():
    return {
        "message":"Welcome to the Gene Expression API",
   
        "done": "by Lee Rong Xian A21EC0043"""
    }

@app.get("/gene/", response_model=List[str])
async def get_gene():
    """Retrieve all information about a specific gene by Gene ID"""
    with MongoClient(host='localhost', port=27017) as client:
        col = client['sample']['expression_data']
        gene_list = col.distinct("Gene ID")
        return gene_list
    
@app.get("/gene/{gene_id}", response_model=Gene)
async def get_gene_info(gene_id: str):
    """Retrieve all information about a specific gene by Gene ID"""
    with MongoClient(host='localhost', port=27017) as client:
        col = client['sample']['expression_data']
        gene_info = col.find_one({"Gene ID": gene_id})
        if gene_info is None:
            raise HTTPException(status_code=404, detail="Gene not found")
        return Gene(**gene_info)
    
@app.get("/gene/{gene_id}/expression", response_model=ExpressionDataResponse)
async def get_expression_data(gene_id: str):
    """Retrieve expression data for a specific gene across all samples"""
    try:
        with MongoClient(host='localhost', port=27017) as client:
            col = client['sample']['expression_data']
            gene_info = col.find_one({"Gene ID": gene_id}, {"_id": 0, "expression": 1})
            if gene_info is None:
                raise HTTPException(status_code=404, detail="Gene not found")
            return ExpressionDataResponse(expression=gene_info['expression'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/patient/{patient_id}/samples", response_model=SampleDataResponse)
async def get_patient_samples(patient_id: str):
    """Retrieve all sample information for a specific patient"""
    try:
        with MongoClient(host='localhost', port=27017) as client:
            col = client['sample']['expression_data']
            samples = col.find({"sample.Patient ID": patient_id}, {"_id": 0, "sample.$": 1})
            if not samples:
                raise HTTPException(status_code=404, detail="Patient not found")
            sample_list = [sample['sample'][0] for sample in samples]
            return SampleDataResponse(sample=sample_list)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))