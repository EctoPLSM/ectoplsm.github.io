---
title: "Presentations"
layout: single
permalink: /presentations/
lang: en
---
## International Conferences
### Talks
<ul>
{% for pres in site.data.presentations.international.talks %}
  <li>
    {{ pres.title }}<br>
    {{ pres.authors }}<br>
    {% if pres.link %} <a href="{{ pres.link }}">{{ pres.event }}</a>{% else %}{{ pres.event}}{% endif %}, {{ pres.location }}, {{ pres.year }}
  </li>
{% endfor %}
</ul>

### Posters
<ul>
{% for pres in site.data.presentations.international.posters %}
  <li>
    {{ pres.title }}<br>
    {{ pres.authors }}<br>
    {% if pres.link %} <a href="{{ pres.link }}">{{ pres.event }}</a>{% else %}{{ pres.event}}{% endif %}, {{ pres.location }}, {{ pres.year }}
  </li>
{% endfor %}
</ul>

## Domestic Conferences
### Talks
<ul>
{% for pres in site.data.presentations.domestic.talks %}
  <li>
    {{ pres.title }}<br>
    {{ pres.authors }}<br>
    {% if pres.link %} <a href="{{ pres.link }}">{{ pres.event }}</a>{% else %}{{ pres.event}}{% endif %}, {{ pres.location }}, {{ pres.year }}
  </li>
{% endfor %}
</ul>

### Posters
<ul>
{% for pres in site.data.presentations.domestic.posters %}
  <li>
    {{ pres.title }}<br>
    {{ pres.authors }}<br>
    {% if pres.link %} <a href="{{ pres.link }}">{{ pres.event }}</a>{% else %}{{ pres.event}}{% endif %}, {{ pres.location }}, {{ pres.year }}
  </li>
{% endfor %}
</ul>
