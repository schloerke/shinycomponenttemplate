from __future__ import annotations

__version__ = "0.0.1"

__all__ = ("example_number_input",)


from pathlib import PurePath

from htmltools import HTMLDependency, Tag, TagAttrs, TagAttrValue, TagChild, TagList


def example_number_input(
    id: str, *args: TagChild | TagAttrs, _add_ws: bool = True, **kwargs: TagAttrValue
) -> TagList:
    """
    Create a <example-number-input> tag.

    A WebComponent for creating number inputs.

    Parameters
    ----------
    *args
        Child elements to this tag.
    _add_ws
        Whether whitespace should be added around this tag.
    **kwargs
        Attributes to this tag.

    Returns
    -------
    :
        Tag

    See Also
    --------
    ~htmltools.Tag
    """

    return TagList(
        component_dep(),
        Tag("example-number-input", *args, id=id, _add_ws=_add_ws, **kwargs),
    )


www_path = str(PurePath(__file__).parent / "www")


def component_dep() -> list[HTMLDependency]:
    return [
        open_props_dep(),
        HTMLDependency(
            name="componenttemplate",
            version=__version__,
            source={
                "package": "componenttemplate",
                "subdir": www_path,
            },
            script={"src": "example-number-input.js", "type": "module"},
        ),
    ]


def open_props_dep() -> HTMLDependency:
    return HTMLDependency(
        name="open-props",
        version=__version__,
        source={
            "package": "componenttemplate",
            "subdir": www_path,
        },
        stylesheet={"href": "open-props.min.css"},
    )
