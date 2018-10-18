# -*- coding: utf-8 -*-
import humps


def test_converting_strings():
    assert humps.camelize('jack_in_the_box') == 'jackInTheBox'
    assert humps.decamelize('rubyTuesdays') == 'ruby_tuesdays'
    assert humps.depascalize('UnosPizza') == 'unos_pizza'
    assert humps.pascalize('red_robin') == 'RedRobin'


def test_conditionals():
    assert humps.is_camelcase('jackInTheBox')
    assert humps.is_pascalcase('RedRobin')
    assert humps.is_snakecase('ruby_tuesdays')
    assert humps.is_camelcase('ruby_tuesdays') is False
    assert humps.is_snakecase('jackInTheBox') is False


def test_numeric():
    assert humps.camelize(1234) == 1234
    assert humps.decamelize(123) == 123
    assert humps.pascalize(123) == 123


def test_camelize():
    actual = humps.camelize({
        'videos': [
            {
                'fallback_url': 'https://media.io/video',
                'scrubber_media_url': 'https://media.io/video',
                'dash_url': 'https://media.io/video',
            },
        ],
        'images': [
            {
                'fallback_url': 'https://media.io/image',
                'scrubber_media_url': 'https://media.io/image',
                'url': 'https://media.io/image',
            },
        ],
    })
    expected = {
        'videos': [
            {
                'fallbackUrl': 'https://media.io/video',
                'scrubberMediaUrl': 'https://media.io/video',
                'dashUrl': 'https://media.io/video',
            },
        ],
        'images': [
            {
                'fallbackUrl': 'https://media.io/image',
                'scrubberMediaUrl': 'https://media.io/image',
                'url': 'https://media.io/image',
            },
        ],
    }
    assert actual == expected


def test_pascalize():
    actual = humps.pascalize({
        'videos': [
            {
                'fallback_url': 'https://media.io/video',
                'scrubber_media_url': 'https://media.io/video',
                'dash_url': 'https://media.io/video',
            },
        ],
        'images': [
            {
                'fallback_url': 'https://media.io/image',
                'scrubber_media_url': 'https://media.io/image',
                'url': 'https://media.io/image',
            },
        ],
    })
    expected = {
        'Videos': [
            {
                'FallbackUrl': 'https://media.io/video',
                'ScrubberMediaUrl': 'https://media.io/video',
                'DashUrl': 'https://media.io/video',
            },
        ],
        'Images': [
            {
                'FallbackUrl': 'https://media.io/image',
                'ScrubberMediaUrl': 'https://media.io/image',
                'Url': 'https://media.io/image',
            },
        ],
    }
    assert actual == expected


def test_decamelize():
    actual = humps.decamelize([
        {
            'symbol': 'AAL',
            'lastPrice': 31.78,
            'changePct': 2.8146,
            'impliedVolatality': 0.482,
        },
        {
            'symbol': 'LBTYA',
            'lastPrice': 25.95,
            'changePct': 2.6503,
            'impliedVolatality': 0.7287,
        },
        {
            'symbol': 'LBTYK',
            'changePct': 2.5827,
            'lastPrice': 25.42,
            'impliedVolatality': 0.4454,
        },
    ])
    expected = [
        {
            'symbol': 'AAL',
            'last_price': 31.78,
            'change_pct': 2.8146,
            'implied_volatality': 0.482,
        },
        {
            'symbol': 'LBTYA',
            'last_price': 25.95,
            'change_pct': 2.6503,
            'implied_volatality': 0.7287,
        },
        {
            'symbol': 'LBTYK',
            'change_pct': 2.5827,
            'last_price': 25.42,
            'implied_volatality': 0.4454,
        },
    ]

    assert actual == expected
