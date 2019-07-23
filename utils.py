import markdown2


def convert_markdown_to_html(markdown_str):
    """Converts a markdown string to an html string"""
    return markdown2.markdown(markdown_str)
