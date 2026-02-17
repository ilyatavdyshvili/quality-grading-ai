import pytest
from unittest.mock import Mock
from src.application.services import QualityControlService
from src.domain.entities import ProductSample, QualityGrade

@pytest.mark.parametrize(
    "sample, expected_label",
    [
        # Standard
        (ProductSample(acidity=5.0, density=0.95, alcohol_content=10.0), "Standard"),
        (ProductSample(acidity=4.5, density=0.9, alcohol_content=10.5), "Standard"),
        (ProductSample(acidity=6.0, density=0.92, alcohol_content=10.5), "Standard"),
        # Premium
        (ProductSample(acidity=8.0, density=1.05, alcohol_content=15.0), "Premium"),
        (ProductSample(acidity=7.5, density=1.02, alcohol_content=14.0), "Premium"),
        (ProductSample(acidity=9.0, density=1.08, alcohol_content=16.0), "Premium"),
    ]
)
def test_quality_control_service(sample, expected_label):
    mock_classifier = Mock()
    # Mock возвращает категорию в зависимости от input
    mock_classifier.evaluate.return_value = QualityGrade(score=0.85, label=expected_label)

    service = QualityControlService(mock_classifier)
    result = service.evaluate_sample(sample)

    assert result.label == expected_label
    mock_classifier.evaluate.assert_called_once()

