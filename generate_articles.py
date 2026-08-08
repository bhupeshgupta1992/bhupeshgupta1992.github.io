import json
from pathlib import Path
from html import escape


# ---------------------------------------
# Load article data
# ---------------------------------------

with open("data/articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)


# ---------------------------------------
# Load article template
# ---------------------------------------

template = Path(
    "article-template.html"
).read_text(encoding="utf-8")


# ---------------------------------------
# Generate each article
# ---------------------------------------

for article in articles:

    article_id = article["id"]

    title = escape(
        article.get("title", "")
    )

    article_type = escape(
        article.get("type", "ORIGINAL ARTICLE")
    )

    authors = article.get("authors", [])


    # -----------------------------------
    # Authors HTML
    # -----------------------------------

    authors_html = ""

    for author in authors:

        name = escape(
            author.get("name", "")
        )

        affiliation = escape(
            author.get("affiliation", "")
        )

        authors_html += f"""
<div class="author-box">

<h3>{name}</h3>

<p>
{affiliation}
</p>

</div>
"""


    # -----------------------------------
    # Google Scholar author metadata
    # -----------------------------------

    authors_meta = ""

    for author in authors:

        name = escape(
            author.get("name", "")
        )

        authors_meta += (
            f'<meta name="citation_author" '
            f'content="{name}">\n'
        )


    # -----------------------------------
    # Schema.org authors
    # -----------------------------------

    schema_authors = []

    for author in authors:

        name = escape(
            author.get("name", "")
        )

        schema_authors.append(
            '{'
            '"@type":"Person",'
            f'"name":"{name}"'
            '}'
        )


    authors_schema = ",\n".join(
        schema_authors
    )


    # -----------------------------------
    # Abstract
    # -----------------------------------

    abstract_html = ""

    abstract = article.get(
        "abstract", {}
    )

    for heading, text in abstract.items():

        abstract_html += f"""
<h3>{escape(heading)}</h3>

<p>
{escape(text)}
</p>
"""


    # -----------------------------------
    # Keywords
    # -----------------------------------

    keywords_html = ""

    for keyword in article.get(
        "keywords", []
    ):

        keywords_html += f"""
<div class="keyword">
{escape(keyword)}
</div>
"""


    # -----------------------------------
    # DOI button
    # -----------------------------------

    doi = article.get(
        "doi", ""
    ).strip()


    if doi:

        doi_button = f"""
<a href="https://doi.org/{escape(doi)}"
   target="_blank"
   rel="noopener">
View DOI
</a>
"""

    else:

        doi_button = ""


    # -----------------------------------
    # Replace template variables
    # -----------------------------------

    replacements = {

        "{{ID}}":
            article_id,

        "{{TITLE}}":
            title,

        "{{TYPE}}":
            article_type,

        "{{AUTHORS_HTML}}":
            authors_html,

        "{{AUTHORS_META}}":
            authors_meta,

        "{{AUTHORS_SCHEMA}}":
            authors_schema,

        "{{CORRESPONDING_EMAIL}}":
            escape(
                article.get(
                    "corresponding_email",
                    ""
                )
            ),

        "{{RECEIVED}}":
            escape(
                article.get(
                    "received",
                    ""
                )
            ),

        "{{ACCEPTED}}":
            escape(
                article.get(
                    "accepted",
                    ""
                )
            ),

        "{{PUBLISHED}}":
            escape(
                article.get(
                    "published",
                    ""
                )
            ),

        "{{DATE}}":
            escape(
                article.get(
                    "publication_date",
                    ""
                )
            ),

        "{{PDF}}":
            escape(
                article.get(
                    "pdf",
                    ""
                )
            ),

        "{{ABSTRACT_HTML}}":
            abstract_html,

        "{{KEYWORDS_HTML}}":
            keywords_html,

        "{{DOI_BUTTON}}":
            doi_button
    }


    # -----------------------------------
    # Apply replacements
    # -----------------------------------

    html = template

    for key, value in replacements.items():

        html = html.replace(
            key,
            value
        )


    # -----------------------------------
    # Save article page
    # -----------------------------------

    output_file = Path(
        f"{article_id}.html"
    )

    output_file.write_text(
        html,
        encoding="utf-8"
    )


    print(
        f"Generated: {output_file}"
    )


print(
    f"\nSuccessfully generated "
    f"{len(articles)} article page(s)."
)
