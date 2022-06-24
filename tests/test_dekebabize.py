"""
Test dekabization.
"""
import pytest

import humps


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("symbol", "symbol"),
        ("last-price", "last_price"),
        ("Change-Pct", "Change_Pct"),
        ("implied-Volatility", "implied_Volatility"),
        ("_symbol", "_symbol"),
        ("change-pct_", "change_pct_"),
        ("_last-price__", "_last_price__"),
        ("__implied-volatility_", "__implied_volatility_"),
        ("API", "API"),
        ("_API_", "_API_"),
        ("__API__", "__API__"),
        ("API-Response", "API_Response"),
        ("_API-Response_", "_API_Response_"),
        ("__API-Response__", "__API_Response__"),
        ("12345", "12345"),
    ],
)
def test_dekebabize(input_str, expected_output):
    """
    :param input_str: String that will be transformed.
    :param expected_output: The expected transformation.
    """
    output = humps.dekebabize(input_str)
    assert output == expected_output, "{} != {}".format(
        output, expected_output
    )


def test_dekebabize_dict_list():
    actual = humps.dekebabize(
        [
            {
                "symbol": "AAL",
                "last-price": 31.78,
                "Change-Pct": 2.8146,
                "implied-Volatility": 0.482,
            },
            {
                "symbol": "LBTYA",
                "last-price": 25.95,
                "Change-Pct": 2.6503,
                "implied-Volatility": 0.7287,
            },
            {
                "_symbol": "LBTYK",
                "Change-Pct_": 2.5827,
                "_last-price__": 25.42,
                "__implied-Volatility_": 0.4454,
            },
            {
                "API": "test_upper",
                "_API_": "test_upper",
                "__API__": "test_upper",
                "API-Response": "test_acronym",
                "_API-Response_": "test_acronym",
                "__API-Response__": "test_acronym",
                "ruby_tuesdays": "ruby_tuesdays",
                "_item-ID": "_item_id",
            },
        ]
    )
    expected = [
        {
            "symbol": "AAL",
            "last_price": 31.78,
            "Change_Pct": 2.8146,
            "implied_Volatility": 0.482,
        },
        {
            "symbol": "LBTYA",
            "last_price": 25.95,
            "Change_Pct": 2.6503,
            "implied_Volatility": 0.7287,
        },
        {
            "_symbol": "LBTYK",
            "Change_Pct_": 2.5827,
            "_last_price__": 25.42,
            "__implied_Volatility_": 0.4454,
        },
        {
            "API": "test_upper",
            "_API_": "test_upper",
            "__API__": "test_upper",
            "API_Response": "test_acronym",
            "_API_Response_": "test_acronym",
            "__API_Response__": "test_acronym",
            "ruby_tuesdays": "ruby_tuesdays",
            "_item_ID": "_item_id",
        },
    ]

    assert actual == expected, "{} != {}".format(actual, expected)
