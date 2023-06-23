#' @importFrom htmltools tag htmlDependency tagList
#' @export
example_number_input <- function(id, ...) {
  contents <- list(id = id, ...)
  tagList(
    component_dep(),
    tag("example-number-input", contents)
  )
}


component_dep <- function() {
  tagList(
    open_props_dep(),
    htmlDependency(
      name = "componenttemplate",
      version = as.character(packageVersion("componenttemplate")),
      src = system.file(package = "componenttemplate", "www"),
      script = list(src = "example-number-input.js", type = "module")
    )
  )
}


open_props_dep <- function() {
  htmlDependency(
    name = "open-props",
    version = as.character(packageVersion("componenttemplate")),
    src = system.file(package = "componenttemplate", "www"),
    stylesheet = "open-props.min.css"
  )
}
