"""
Test decamelization.
"""
import pytest

import humps


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("symbol", "symbol"),
        ("lastPrice", "last_price"),
        ("changePct", "change_pct"),
        ("impliedVolatility", "implied_volatility"),
        ("_symbol", "_symbol"),
        ("changePct_", "change_pct_"),
        ("_lastPrice__", "_last_price__"),
        ("__impliedVolatility_", "__implied_volatility_"),
        ("API", "API"),
        ("_API_", "_API_"),
        ("__API__", "__API__"),
        ("APIResponse", "api_response"),
        ("_APIResponse_", "_api_response_"),
        ("__APIResponse__", "__api_response__"),
        # Fixed issue #2. 2021-05-01
        ("_itemID", "_item_id"),
        # Fixed issue #4. 2021-05-01
        ("memMB", "mem_mb"),
        # Fixed issue #127. 2021-09-13
        ("sizeX", "size_x"),
        # Fixed issue #168. 2021-09-13
        ("aB", "a_b"),
        # Fixed issue #201. 2021-10-12
        ("testNTest", "test_n_test"),
    ],
)
def test_decamelize(input_str, expected_output):
    """
    :param input_str: String that will be transformed.
    :param expected_output: The expected transformation.
    """
    output = humps.decamelize(input_str)
    assert output == expected_output, "{} != {}".format(
        output, expected_output
    )


def test_decamelize_dict_list():
    actual = humps.decamelize(
        [
            {
                "symbol": "AAL",
                "lastPrice": 31.78,
                "changePct": 2.8146,
                "impliedVolatility": 0.482,
            },
            {
                "symbol": "LBTYA",
                "lastPrice": 25.95,
                "changePct": 2.6503,
                "impliedVolatility": 0.7287,
            },
            {
                "_symbol": "LBTYK",
                "changePct_": 2.5827,
                "_lastPrice__": 25.42,
                "__impliedVolatility_": 0.4454,
            },
            {
                "API": "test_upper",
                "_API_": "test_upper",
                "__API__": "test_upper",
                "APIResponse": "test_acronym",
                "_APIResponse_": "test_acronym",
                "__APIResponse__": "test_acronym",
                "ruby_tuesdays": "ruby_tuesdays",
                "_itemID": "_item_id",
            },
        ]
    )
    expected = [
        {
            "symbol": "AAL",
            "last_price": 31.78,
            "change_pct": 2.8146,
            "implied_volatility": 0.482,
        },
        {
            "symbol": "LBTYA",
            "last_price": 25.95,
            "change_pct": 2.6503,
            "implied_volatility": 0.7287,
        },
        {
            "_symbol": "LBTYK",
            "change_pct_": 2.5827,
            "_last_price__": 25.42,
            "__implied_volatility_": 0.4454,
        },
        {
            "API": "test_upper",
            "_API_": "test_upper",
            "__API__": "test_upper",
            "api_response": "test_acronym",
            "_api_response_": "test_acronym",
            "__api_response__": "test_acronym",
            "ruby_tuesdays": "ruby_tuesdays",
            "_item_id": "_item_id",
        },
    ]

    assert actual == expected, "{} != {}".format(actual, expected)


@pytest.mark.parametrize(
    "punctuation", list(".,<>/?;:'\"[]{}\\|`~!@#$%^&*()=+")
)
def test_punctuation_is_already_a_word_boundary(punctuation):
    """Treat punctuation as an existing boundary."""
    assert (
        humps.decamelize("foo" + punctuation + "Bar")
        == "foo" + punctuation + "bar"
    )


def test_existing_separators_are_not_duplicated():
    """Keep existing separators single during case conversion."""
    assert humps.decamelize("foo_Bar") == "foo_bar"
    assert humps.decamelize("foo-Bar") == "foo-bar"


@pytest.mark.parametrize(
    "text, expected",
    [("fooBar", "foo_bar"), ("åBar", "å_bar"), ("foo1Bar", "foo1bar")],
)
def test_adjacent_letter_and_digit_boundaries(text, expected):
    """Preserve established letter and ASCII-digit splits."""
    assert humps.decamelize(text) == expected


@pytest.mark.parametrize("digit", ["\u0662", "\u09e8", "\u0968"])
def test_non_ascii_digit_boundaries_are_preserved(digit):
    """Preserve existing uppercase boundaries after non-ASCII digits."""
    assert humps.decamelize("foo{}Bar".format(digit)) == "foo{}_bar".format(
        digit
    )
