"""
Test pascalizing.
"""
import pytest

import humps


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("fallback_url", "FallbackUrl"),
        ("scrubber_media_url", "ScrubberMediaUrl"),
        ("dash_url", "DashUrl"),
        ("_fallback_url", "_FallbackUrl"),
        ("__scrubber_media___url_", "__ScrubberMediaUrl_"),
        ("_url__", "_Url__"),
        ("API", "API"),
        ("_API_", "_API_"),
        ("__API__", "__API__"),
        ("APIResponse", "APIResponse"),
        ("_APIResponse_", "_APIResponse_"),
        ("__APIResponse__", "__APIResponse__"),
    ],
)
def test_pascalize(input_str, expected_output):
    """
    :param input_str: String that will be transformed.
    :param expected_output: The expected transformation.
    """
    output = humps.pascalize(input_str)
    assert output == expected_output, "{} != {}".format(
        output, expected_output
    )


def test_pascalize_dict_list():
    actual = humps.pascalize(
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
        "Videos": [
            {
                "FallbackUrl": "https://media.io/video",
                "ScrubberMediaUrl": "https://media.io/video",
                "DashUrl": "https://media.io/video",
            }
        ],
        "Images": [
            {
                "FallbackUrl": "https://media.io/image",
                "ScrubberMediaUrl": "https://media.io/image",
                "Url": "https://media.io/image",
            }
        ],
        "Other": [
            {
                "_FallbackUrl": "https://media.io/image",
                "__ScrubberMediaUrl_": "https://media.io/image",
                "_Url__": "https://media.io/image",
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
    assert actual == expected, "{} != {}".format(actual, expected)
