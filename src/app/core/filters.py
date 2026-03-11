import markdown2


def add_markdown_filter(templates):
    def markdown_filter(text):
        return markdown2.markdown(text, extras=["fenced-code-blocks"])
    templates.env.filters["markdown"] = markdown_filter
    return templates
