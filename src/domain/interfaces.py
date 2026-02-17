from abc import ABC, abstractmethod
from .entities import ProductSample, QualityGrade

class IQualityClassifier(ABC):
    @abstractmethod
    def evaluate(self, sample: ProductSample) -> QualityGrade:
        pass
