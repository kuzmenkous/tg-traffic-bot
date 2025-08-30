def escape_markdown(text: str) -> str:
    return text.replace("_", "\\_").replace("-", "\\-")
