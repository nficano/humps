"""
Test kebabization.
"""

import pytest

import humps


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("fallback_url", "fallback-url"),
        ("scrubber_media_url", "scrubber-media-url"),
        ("dash_url", "dash-url"),
        ("_fallback_url", "_fallback-url"),
        ("__scrubber_media___url_", "__scrubber-media-url_"),
        ("_url__", "_url__"),
        ("API", "API"),
        ("_API_", "_API_"),
        ("__API__", "__API__"),
        ("API_Response", "API-Response"),
        ("_API_Response_", "_API-Response_"),
        ("__API_Response__", "__API-Response__"),
        # Strings with spaces
        ("test string", "test-string"),
        ("test   string", "test-string"),
        ("  test string  ", "test-string"),
        # strings with underscores and spaces
        ("test_string with spaces", "test-string-with-spaces"),
        ("test__string with   spaces", "test-string-with-spaces"),
        ("  test_string with spaces  ", "test-string-with-spaces"),
        # strings with mixed cases
        ("TestString", "test-string"),
    ],
)
def test_kebabize(input_str, expected_output):
    """
    :param input_str: String that will be transformed.
    :param expected_output: The expected transformation.
    """
    output = humps.kebabize(input_str)
    assert output == expected_output, "{} != {}".format(
        output, expected_output
    )


def test_kebabize_dict_list():
    actual = humps.kebabize(
        {
            "videos": [
                {
                    "fallback_url": "https://media.io/video",
                    "scrubber_Media_Url": "https://media.io/video",
                    "dash_Url": "https://media.io/video",
                }
            ],
            "images": [
                {
                    "fallback_url": "https://media.io/image",
                    "scrubber_Media_Url": "https://media.io/image",
                    "url": "https://media.io/image",
                }
            ],
            "other": [
                {
                    "_fallback_url": "https://media.io/image",
                    "__scrubber_Media___Url_": "https://media.io/image",
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
                "fallback-url": "https://media.io/video",
                "scrubber-Media-Url": "https://media.io/video",
                "dash-Url": "https://media.io/video",
            }
        ],
        "images": [
            {
                "fallback-url": "https://media.io/image",
                "scrubber-Media-Url": "https://media.io/image",
                "url": "https://media.io/image",
            }
        ],
        "other": [
            {
                "_fallback-url": "https://media.io/image",
                "__scrubber-Media-Url_": "https://media.io/image",
                "_url__": "https://media.io/image",
            },
            {
                "API": "test_upper",
                "_API_": "test_upper",
                "__API__": "test_upper",
                "api-response": "test_acronym",
                "_api-response_": "test_acronym",
                "__api-response__": "test_acronym",
            },
        ],
    }
    assert actual == expected
