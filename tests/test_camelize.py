"""
Test camelization.
"""

import pytest

import humps


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("fallback_url", "fallbackUrl"),
        ("scrubber_media_url", "scrubberMediaUrl"),
        ("dash_url", "dashUrl"),
        ("_fallback_url", "_fallbackUrl"),
        ("__scrubber_media___url_", "__scrubberMediaUrl_"),
        ("_url__", "_url__"),
        ("API", "API"),
        ("_API_", "_API_"),
        ("__API__", "__API__"),
        ("APIResponse", "APIResponse"),
        ("_APIResponse_", "_APIResponse_"),
        ("__APIResponse__", "__APIResponse__"),
        # Fixed issue #128
        ("whatever_10", "whatever10"),
        # Fixed issue # 18
        ("test-1-2-3-4-5-6", "test123456"),
        # Fixed issue # 61
        ("test_n_test", "testNTest"),
        # Fixed issue # 148
        ("field_value_2_type", "fieldValue2Type"),
        # Fixed issue # 256
        ("", ""),
        (None, ""),
        # Strings with spaces
        ("test string", "testString"),
        ("test   string", "testString"),
        ("  test string  ", "testString"),
        # strings with underscores and spaces
        ("test_string with spaces", "testStringWithSpaces"),
        ("test__string with   spaces", "testStringWithSpaces"),
        ("  test_string with spaces  ", "testStringWithSpaces"),
        # strings with mixed cases
        ("TestString", "testString"),
    ],
)
def test_camelize(input_str, expected_output):
    """
    :param input_str: String that will be transformed.
    :param expected_output: The expected transformation.
    """
    output = humps.camelize(input_str)
    assert output == expected_output, "{} != {}".format(
        output, expected_output
    )


def test_camelize_dict_list():
    actual = humps.camelize(
        {
            "videos": [
                {
                    "fallback_url": "https://media.io/video",
                    "scrubber_media_url": "https://media.io/video",
                    "dash_url": "https://media.io/video",
                }
            ],
            "images": [
                {
                    "fallback_url": "https://media.io/image",
                    "scrubber_media_url": "https://media.io/image",
                    "url": "https://media.io/image",
                }
            ],
            "other": [
                {
                    "_fallback_url": "https://media.io/image",
                    "__scrubber_media___url_": "https://media.io/image",
                    "_url__": "https://media.io/image",
                },
                {
                    "API": "test_upper",
                    "_API_": "test_upper",
                    "__API__": "test_upper",
                    "APIResponse": "test_acronym",
                    "_APIResponse_": "test_acronym",
                    "__APIResponse__": "test_acronym",
                },
            ],
        }
    )
    expected = {
        "videos": [
            {
                "fallbackUrl": "https://media.io/video",
                "scrubberMediaUrl": "https://media.io/video",
                "dashUrl": "https://media.io/video",
            }
        ],
        "images": [
            {
                "fallbackUrl": "https://media.io/image",
                "scrubberMediaUrl": "https://media.io/image",
                "url": "https://media.io/image",
            }
        ],
        "other": [
            {
                "_fallbackUrl": "https://media.io/image",
                "__scrubberMediaUrl_": "https://media.io/image",
                "_url__": "https://media.io/image",
            },
            {
                "API": "test_upper",
                "_API_": "test_upper",
                "__API__": "test_upper",
                "APIResponse": "test_acronym",
                "_APIResponse_": "test_acronym",
                "__APIResponse__": "test_acronym",
            },
        ],
    }
    assert actual == expected
