from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()


class InputData(BaseModel):
  E: float
  I: float
  L: float


@app.post("/calculate/")
async def calculate(data: InputData):
  P_cr = (math.pi**2 * data.E * data.I) / (data.L**2)
  return {"Resultado": P_cr}
