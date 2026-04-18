import markdown2


def add_markdown_filter(templates):
    def markdown_filter(text):
        return markdown2.markdown(text, extras=["fenced-code-blocks"])
    templates.env.filters["markdown"] = markdown_filter
    return templates


def datetime_filter(value, format="%Y-%m-%d %H:%M"):
    if value is None:
        return ""
    if hasattr(value, "strftime"):
        return value.strftime(format)
    return str(value)