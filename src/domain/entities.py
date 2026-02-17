from pydantic import BaseModel

class ProductSample(BaseModel):
    acidity: float
    density: float
    alcohol_content: float

class QualityGrade(BaseModel):
    score: float
    label: str
