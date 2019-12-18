{{ imagewizard }}
{{ imagewizard|count * "=" }}

{% if imagewizard.readme_pypi_badge -%}
.. image:: https://img.shields.io/pypi/v/{{ imagewizard }}.svg
    :target: https://pypi.python.org/pypi/{{ imagewizard }}
    :alt: Latest PyPI version
{%- endif %}

{% if imagewizard.readme_travis_badge -%}
.. image:: {{ imagewizard.readme_travis_url }}.png
   :target: {{ imagewizard.readme_travis_url }}
   :alt: Latest Travis CI build status
{%- endif %}

{{ imagewizard.package_description }}

Usage
-----

Installation
------------

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`imagewizard` was written by `Swaroop Padala <soupspring47@gmail.com>`_.
