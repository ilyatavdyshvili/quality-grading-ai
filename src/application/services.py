from src.domain.entities import ProductSample, QualityGrade
from src.domain.interfaces import IQualityClassifier

class QualityControlService:
    def __init__(self, classifier: IQualityClassifier):
        self.classifier = classifier

    def evaluate_sample(self, sample: ProductSample) -> QualityGrade:
        # Масштабирование признаков (Min-Max 0..1)
        scaled_sample = ProductSample(
            acidity=sample.acidity / 10,
            density=sample.density / 1.1,
            alcohol_content=sample.alcohol_content / 16
        )
        return self.classifier.evaluate(scaled_sample)
