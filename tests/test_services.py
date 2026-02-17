from src.domain.entities import ProductSample, QualityGrade
from src.application.services import QualityControlService
from unittest.mock import Mock

def test_quality_control_service():
    mock_classifier = Mock()
    mock_classifier.evaluate.return_value = QualityGrade(score=0.85, label="Premium")

    service = QualityControlService(mock_classifier)
    sample = ProductSample(acidity=8, density=1.0, alcohol_content=14)

    result = service.evaluate_sample(sample)

    assert result.score == 0.85
    assert result.label == "Premium"
    mock_classifier.evaluate.assert_called_once()
