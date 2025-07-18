---
title: "Curriculum Vitae"
layout: single
permalink: /cv/
lang: en
---

## PDF version
<iframe src="https://docs.google.com/viewer?url={{ site.url }}/assets/cv.pdf&embedded=true" style="width:100%; height:450px;" frameborder="0"></iframe>

[Download CV (PDF)]({{ site.url }}/assets/cv.pdf)

PDF built using [quarto-awesomecv-typst](https://github.com/kazuyanagimoto/quarto-awesomecv-typst) template!

## Education

{% for edu in site.data.cv.education %}
-  **{{ edu.start }} – {{ edu.end }}** <br>
  **{{ edu.degree }}**, {% if edu.department.url %}[{{ edu.department.name }}]({{ edu.department.url }}), {% else %}{{ edu.department.name }}, {% endif %}{{ edu.institution }}{% if edu.topic %}  
  Topic: {{ edu.topic }}{% endif %} <br>
  {% if edu.advisors %}Advisors: {% for adv in edu.advisors %}{% if adv.url %}[{{ adv.name }}]({{ adv.url }}){% else %}{{ adv.name }}{% endif %}{% if forloop.last %}{% else %}, {% endif %}{% endfor %}{% elsif edu.advisor %}Advisor: {% for adv in edu.advisor %}{% if adv.url %}[{{ adv.name }}]({{ adv.url }}){% else %}{{ adv.name }}{% endif %}{% if forloop.last %}{% else %}, {% endif %}{% endfor %}{% endif %}
{% endfor %}

## Grants & Fellowships

{% for gf in site.data.cv.grants_fellowships %}
- {% if gf.end %}**{{ gf.start }} – {{ gf.end }}** {% else %}**{{ gf.start }}** {% endif %}  <br>
  {% if gf.title.url %}[**{{ gf.title.text }}**]({{ gf.title.url }}){% else %}{{ gf.title.text }}{% endif %} ({{ gf.amount }})

{% endfor %}

## Honours & Awards

{% for ha in site.data.cv.honours_awards %}
- **{{ ha.date }}**  <br>
  {% if ha.title.url %}[**{{ ha.title.text }}**]({{ ha.title.url }}){% else %}**{{ ha.title.text }}**{% endif %}{% if ha.issuer %}, {{ ha.issuer }}{% endif %}<br>
  {% if ha.note %}{{ ha.note }}{% endif %}

{% endfor %}

## Research Experience

{% for rexp in site.data.cv.research_experience %}
- **{{ rexp.date }}**<br>
  {% if rexp.title.url %}[**{{ rexp.title.text }}**]({{ rexp.title.url }})<br>{% else %}**{{ rexp.title.text }}**<br>{% endif %}
  {% if rexp.note %}{{ rexp.note }}<br>{% else %}{% endif %}
  {% if rexp.host %}Host: {% if rexp.host.url %}[{{ rexp.host.name }}]({{ rexp.host.url }}){% else %}{{ rexp.host.name }}{% endif %}{% endif %}
{% endfor %}

## Outreach

{% for out in site.data.cv.outreach %}
- **{{ out.start }} – {{ out.end }}**<br>
  {{ out.title.text }}, {% if out.title.url %}[{{ out.title.organisation }}]({{ out.title.url }}){% else %}{{ out.title.text }}{% endif %}

{% endfor %}