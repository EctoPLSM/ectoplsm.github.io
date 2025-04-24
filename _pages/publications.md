---
title: "Publications"
layout: single
permalink: /publications/
lang: en
---
An auto-update list of my publications can also be found at [Google Scholar](https://scholar.google.co.jp/citations?user=lb2prtEAAAAJ) or [ORCID](https://orcid.org/0009-0003-4594-3715).

## Upcoming papers

<ul>
{% for pub in site.data.publications.upcoming %}
  <li>
  {{ pub.title }} <br>
  {{ pub.authors }} <br>
  {{ pub.year }}, submitted to {{ pub.journal }}, 
    <a href="https://arxiv.org/abs/{{ pub.arxiv }}">arXiv: {{ pub.arxiv }}</a>
  </li>
{% endfor %}
</ul>

## Published papers
### First author publications

<ul>
{% for pub in site.data.publications.published.lead_author %}
  <li>
  {{ pub.title }} <br>
  {{ pub.authors }} <br>
  {{ pub.year }}, {{ pub.journal }} {{ pub.volume }}, {{ pub.number }}, 
    <a href="https://ui.adsabs.harvard.edu/abs/{{ pub.doi }}/abstract">ADS</a>, 
    <a href="http://dx.doi.org/{{ pub.doi }}">doi: {{ pub.doi }}</a>, 
    <a href="https://arxiv.org/abs/{{ pub.arxiv }}">arXiv: {{ pub.arxiv }}</a>.
  </li>
{% endfor %}
</ul>
