import json
from pathlib import Path
from html import escape


# ---------------------------------------
# Load article data
# ---------------------------------------

with open("data/articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)


# ---------------------------------------
# Load template
# ---------------------------------------

template = Path(
    "article-template.html"
).read_text(encoding="utf-8")


# ---------------------------------------
# Generate articles
# ---------------------------------------

for article in articles:

    article_id = article["id"]

    title = escape(
        article.get("title", "")
    )

    article_type = escape(
        article.get(
            "type",
            "ORIGINAL ARTICLE"
        )
    )


    # -----------------------------------
    # Authors
    # -----------------------------------

    authors = article.get(
        "authors",
        []
    )

    authors_html = ""

    for author in authors:

        name = escape(
            author.get("name", "")
        )

        affiliation = escape(
            author.get(
                "affiliation",
                ""
            )
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
    # Google Scholar authors
    # -----------------------------------

    authors_meta = ""

    for author in authors:

        name = escape(
            author.get("name", "")
        )

        authors_meta += (
            '<meta name="citation_author" '
            f'content="{name}">\n'
        )


    # -----------------------------------
    # Schema authors
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
        "abstract",
        {}
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
        "keywords",
        []
    ):

        keywords_html += f"""
<div class="keyword">
{escape(keyword)}
</div>
"""


    # -----------------------------------
    # DOI
    # -----------------------------------

    doi = article.get(
        "doi",
        ""
    ).strip()


    if doi:

        # If DOI is entered as a complete
        # https://doi.org/... URL, use it.
        if doi.startswith(
            "https://doi.org/"
        ):

            doi_url = doi

        else:

            doi_url = (
                "https://doi.org/"
                + doi
            )


        doi_button = f"""
<a href="{escape(doi_url)}"
   target="_blank"
   rel="noopener">
View DOI
</a>
"""

    else:

        doi_button = ""


    # -----------------------------------
    # Pages
    # -----------------------------------

    pages = article.get(
        "pages",
        ""
    ).strip()


    first_page = ""
    last_page = ""


    if pages:

        if "-" in pages:

            parts = pages.split(
                "-",
                1
            )

            first_page = parts[0].strip()
            last_page = parts[1].strip()

        else:

            first_page = pages
            last_page = pages


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

        "{{VOLUME}}":
            escape(
                article.get(
                    "volume",
                    ""
                )
            ),

        "{{ISSUE}}":
            escape(
                article.get(
                    "issue",
                    ""
                )
            ),

        "{{PAGES}}":
            escape(
                pages
            ),

        "{{FIRSTPAGE}}":
            escape(
                first_page
            ),

        "{{LASTPAGE}}":
            escape(
                last_page
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
    # Save generated article
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
