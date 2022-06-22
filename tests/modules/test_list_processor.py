import pytest

from src.modules.list_processor import ListProcessor


class TestListProcessor:
    @pytest.mark.parametrize(
        "test_data, expected_results",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([[1, 2, 3], [4, 5, 6], []], [1, 2, 3, 4, 5, 6]),
        ]
    )
    def test__flatten__returns_list(self, test_data, expected_results):
        assert expected_results == ListProcessor.flatten(test_data)
    
    @pytest.mark.parametrize(
        "test_data, expected_error_msg",
        [
            ("not a list", "Input is not an instance of a list: not a list"),
            ([[1, 2, 3], [4, 5, 6], "not a list"], "An item is not an instance of a list: not a list"),
        ]
    )
    def test__flatten__raises_value_error(self, test_data, expected_error_msg):
        with pytest.raises(ValueError) as excinfo:
            ListProcessor.flatten(test_data)
        assert expected_error_msg == str(excinfo.value)
