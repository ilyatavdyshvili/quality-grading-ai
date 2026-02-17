from src.domain.interfaces import IQualityClassifier
from src.domain.models import ProductSample, QualityGrade

class FormulaClassifier(IQualityClassifier):
    def evaluate(self, sample: ProductSample) -> QualityGrade:
        # Взвешенная формула оценки качества
        score = (sample.acidity * 0.3 + sample.density * 0.3 + sample.alcohol_content * 0.4) / 10
        label = "Premium" if score > 0.7 else "Standard"
        return QualityGrade(score=score, label=label)
