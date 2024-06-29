from fastapi import FastAPI
from pydantic import BaseModel
import math
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with the specific origin of your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class InputData(BaseModel):
  E: float
  I: float
  L: float


@app.post("/calculate/")
async def calculate(data: InputData):
  P_cr = (math.pi**2 * data.E * data.I) / (data.L**2)
  return {"Resultado": P_cr}
