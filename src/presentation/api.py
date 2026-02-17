from fastapi import FastAPI
from src.domain.models import ProductSample
from src.infrastructure.mock_classifier import FormulaClassifier
from src.application.services import QualityControlService

app = FastAPI()
classifier = FormulaClassifier()
service = QualityControlService(classifier)

@app.post("/evaluate")
def evaluate(sample: ProductSample):
    result = service.evaluate_sample(sample)
    return result.dict()
