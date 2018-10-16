## Humps

Convert strings (and dictionary keys) between snake case, camel case and pascal case in Python. Inspired by [Humps](https://github.com/domchristie/humps) for Node.

### Why

When creating an API, the author will often use the character casing that is idiomatic to the backend language, thus forcing the consumer to either live with an inconsistent casing style, write hardcoded mappings between them, or lug around some case conversion utility functions from one project to the next.

While none of these are inherently wrong, it would still be nice to have a dependable solution just a few keystrokes away.

### Installation

To install humps, simply use pipenv (or pip, of course):

```bash
$ pipenv install pyhumps
```

### Usage

#### Converting strings

```python
import humps

humps.camelize('jack_in_the_box')  # jackInTheBox
humps.decamelize('rubyTuesdays')  # ruby_tuesdays
humps.pascalize('red_robin')  # RedRobin
```

#### Converting dictionary keys

```python
import humps

humps.decamelize_keys([
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

# [{'symbol': 'AAL',
#   'last_price': 31.78,
#   'change_pct': 2.8146,
#   'implied_volatality': 0.482},
#  {'symbol': 'LBTYA',
#   'last_price': 25.95,
#   'change_pct': 2.6503,
#   'implied_volatality': 0.7287},
#  {'symbol': 'LBTYK',
#   'change_pct': 2.5827,
#   'last_price': 25.42,
#   'implied_volatality': 0.4454}]
```

#### API Methods
```python
import humps
humps.camelize(string)
humps.decamelize(string)
humps.depascalize(string)
humps.pascalize(string)

humps.camelize_keys(obj_or_list)
humps.decamelize_keys(obj_or_list)
humps.depascalize_keys(obj_or_list)
humps.pascalize_keys(obj_or_list)

humps.is_camelcase(string)
humps.is_pascalcase(string)
humps.is_snakecase(string)
```
