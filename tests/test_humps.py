import humps


def test_converting_strings():
    assert humps.camelize('jack_in_the_box') == 'jackInTheBox'
    assert humps.decamelize('rubyTuesdays') == 'ruby_tuesdays'
    assert humps.pascalize('red_robin') == 'RedRobin'


def test_decamelize_keys():
    camelcase_keys = [
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
    ]
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

    assert humps.decamelize(camelcase_keys) == expected
