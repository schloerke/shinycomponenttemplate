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
  htmlDependency(
    name = "componenttemplate",
    version = as.character(packageVersion("componenttemplate")),
    src = system.file(package = "componenttemplate", "www"),
    stylesheet = "open-props.min.css",
    script = list(src = "example-number-input.js", type = "module")
  )
}
