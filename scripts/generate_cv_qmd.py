"""
generate_cv_qmd.py

1. Reads _config.yml for author info
2. Converts each _data/*.yml into section YAML suitable for
   the quarto-awesomecv-typst template's #resume-entry
3. Writes them to generated/<section>.yml
4. Builds CV.qmd with a proper header and include shortcodes
"""

import yaml
from pathlib import Path

# --- CONFIG PATHS ---
CONFIG_YML = "_config.yml"
DATA_DIR   = Path("_data")
OUT_DIR    = Path("temp")
QMD_OUT    = Path("CV.qmd")

# ensure output dir exists
OUT_DIR.mkdir(exist_ok=True)

# --- 1) LOAD _config.yml FOR AUTHOR METADATA ---
with open(CONFIG_YML, encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

name = cfg.get("author", {}).get("name", "")
firstname, lastname = name.split(" ", 1)

position = cfg.get("author", {}).get("bio", "")
address  = cfg.get("author", {}).get("location", "")
# assemble contacts
contacts = []

# home page
home_url = name = cfg.get("url", {})
contacts.append({
    "icon": "fa house",
    "text": home_url,
    "url":  home_url
})

# email, github, orcid
for link in cfg.get("author", {}).get("links", []):
    icon = link.get("icon","")
    if icon.startswith("fas"):
        icon = icon.replace("fas fa-fw fa-", "fa ")
    elif icon.startswith("fab"):
        icon = icon.replace("fab fa-fw fa-", "fa brands ")

    link_type = link.get("label","")
    url = link.get("url","")

    if link_type == "Email":
        text = url.replace("mailto:","")
    elif link_type == "GitHub":
        text = url.replace("https://github.com/","")
    elif link_type == "ORCID":
        text = url.replace("https://orcid.org/","")
    else:
        continue
        
    contacts.append({
        "icon": icon,
        "text": text,
        "url":  url
    })

header = {
    "author": {
        "firstname": firstname,
        "lastname":  lastname,
        "address":   address,
        "position":  position,
        "contacts":  contacts
    }
}


# --- 2) HELPER TO WRITE A LIST OF DICTS TO YAML FILE ---
def write_section(section_name, entries):
    out = OUT_DIR / f"{section_name}.yml"
    with open(out, "w", encoding="utf-8") as f:
        yaml.safe_dump(entries, f, sort_keys=False)

# --- 3) CONVERT YOUR CV SECTIONS ---
cv = yaml.safe_load(open(DATA_DIR / "cv.yml", encoding="utf-8"))

# EDUCATION
edu_entries = []
for item in cv.get("education", []):
    date = f"{item.get('start','')} – {item.get('end','')}"
    ent = {
        "title":       item.get("degree",""),
        "location":    item.get("location",""),
        "date":        date,
        "description":     item.get("department",{}).get("name","") + ", " + item.get("institution","")
    }
    details = []
    if topic := item.get("topic"):
        details.append(f"Topic: {topic}")
    if advisors := item.get("advisors", []):
        advisor_names = ", ".join([a.get("name", "") for a in advisors])
        details.append(f"Advisors: {advisor_names}")
    if advisor := item.get("advisor", []):
        for adv in advisor:
            details.append(f"Advisor: {adv.get('name', '')}")
    if details:
        ent["details"] = details
    edu_entries.append(ent)
write_section("education", edu_entries)

# GRANTS & FELLOWSHIPS
gf_entries = []
for item in cv.get("grants_fellowships", []):
    date = f"{item.get('start','')} – {item.get('end','')}"
    title = item.get("title",{}).get("text","")
    ent = {
        "title":       title,
        "location":    "",
        "date":        date,
        "description": item.get("amount","")
    }
    gf_entries.append(ent)
write_section("grants_fellowships", gf_entries)

# HONOURS & AWARDS
ha_entries = []
for item in cv.get("honours_awards", []):
    ent = {
        "title":       item.get("title",{}).get("text",""),
        "location":    item.get("location",""),
        "date":        item.get("date",""),
        "description": item.get("issuer",""),
        "details":     [item.get("note","")]
    }
    ha_entries.append(ent)
write_section("honours_awards", ha_entries)

# RESEARCH EXPERIENCE
re_entries = []
for item in cv.get("research_experience", []):
    ent = {
        "title":       item.get("title",{}).get("text",""),
        "location":    item.get("location",""),
        "date":        item.get("date",""),
        "description": item.get("title",{}).get("institution","")
    }
    details = []
    if note := item.get("note",""):
        details.append(note)
    if name := item.get("host",{}).get("name",""):
        details.append(f"Host: {name}")
    if details:
        ent["details"] = details
    re_entries.append(ent)
write_section("research_experience", re_entries)

# OUTREACH
or_entries = []
for item in cv.get("outreach", []):
    date = f"{item.get('start','')} – {item.get('end','')}"
    t = item.get("title",{})
    ent = {
        "title":    t.get("text",""),
        "location": "",
        "date":     date,
        "description": t.get("organisation","")
    }
    or_entries.append(ent)
write_section("outreach", or_entries)

# --- 4) CONVERT PRESENTATIONS ---
pres = yaml.safe_load(open(DATA_DIR / "presentations.yml", encoding="utf-8"))
for scope in ['international']:
    for kind in ['talks', 'posters']:
        entries = []
        for item in pres.get(scope, {}).get(kind, []):
            location = item.get('location', '')
            if location: # Leave only "city, country"
                parts = location.rsplit(',', 2)
                location = ', '.join(parts[-2:])

            ent = {
                'title':       item.get('event', ''),
                'location':    location,
                'date':        str(item.get('year', '')),
                'description': item.get('title', '')
            }
            entries.append(ent)
        write_section(f"{scope}_{kind}", entries)

# --- 5) CONVERT PUBLICATIONS ---
pub = yaml.safe_load(open(DATA_DIR / "publications.yml", encoding="utf-8"))
# upcoming
up_entries = []
for item in pub.get('upcoming', []):
    ent = {
        'title':       item.get('title', ''),
        'location':    "",
        'date':        str(item.get('year', '')),
        'description': item.get('authors', '')
    }
    details = []
    details.append("Submitted to " + item.get('journal', ''))
    if arxiv := item.get('arxiv'):
        details.append(f"https://arxiv.org/abs/{arxiv}")
    if details:
        ent['details'] = details
    up_entries.append(ent)
write_section('publications_upcoming', up_entries)

# published.lead_author
lead_author = []
for item in pub.get('published', {}).get('lead_author', []):
    ent = {
        'title':       item.get('title', ''),
        'location':    "",
        'date':        str(item.get('year', '')),
        'description': item.get('authors', '')
    }
    details = []
    details.append(f"{item.get('journal', '')}, {item.get('volume', '')}, {item.get('number', '')}")
    if arxiv := item.get('arxiv'):
        details.append(f"https://arxiv.org/abs/{arxiv}")
    if details:
        ent['details'] = details
    lead_author.append(ent)
write_section('publications_lead_author', lead_author)

# --- 6) EMIT CV.qmd WITH FRONTMATTER + YAML SHORTCODES ---
with open(QMD_OUT, "w", encoding="utf-8") as f:
    # -- header block --
    f.write("---\n")
    yaml.safe_dump(header, f, sort_keys=False)
    f.write("format: awesomecv-typst\n")
    f.write("---\n\n")

    # Interest section
    f.write("## Research Interests\n\n")
    f.write("Supernovae, circumstellar material, evolution of massive stars\n\n")

    # -- body include for each section --
    sections = [
        ("Education",          "education"),
        ("Grants and Fellowships","grants_fellowships"),
        ("Honours and Awards",   "honours_awards"),
        ("Research Experience","research_experience"),
    ]
    for title, key in sections:
        f.write(f"## {title}\n\n")
        f.write(f"{{{{< yaml {OUT_DIR}/{key}.yml >}}}}\n\n")

    # Publications
    f.write("## Publications\n\n")
    f.write("### Upcoming\n\n")
    f.write(f"{{{{< yaml {OUT_DIR}/publications_upcoming.yml >}}}}\n\n")
    f.write("### Published — Lead Author\n\n")
    f.write(f"{{{{< yaml {OUT_DIR}/publications_lead_author.yml >}}}}\n\n")

    f.write("## Selected Conference Presentations\n\n")
    f.write("### Contributed Talks\n\n")
    f.write(f"{{{{< yaml {OUT_DIR}/international_talks.yml >}}}}\n\n")
    f.write("### Posters\n\n")
    f.write(f"{{{{< yaml {OUT_DIR}/international_posters.yml >}}}}\n\n")

    f.write("## Outreach \n\n")
    f.write(f"{{{{< yaml {OUT_DIR}/outreach.yml >}}}}\n\n")

    # Skills
    f.write("## Skills\n\n")
    f.write("Languages: Japanese (Native), English (proficient), German (Intermediate), Chinese (Intermediate), Spanish (Beginner), French (Beginner), Russian (Beginner), Korean (Beginner)\n\n")
    f.write("Programming Languages: Python, C++, Fortran\n\n")
