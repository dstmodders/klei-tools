std = {
  max_code_line_length = 80,
  max_comment_line_length = 80,
  max_line_length = 80,
  max_string_line_length = 80,

  read_globals = {
    "assert",
    "error",
    "io",
    "ipairs",
    "os",
    "package",
    "pairs",
    "select",
    "table",
    "tostring",
    "type",
  },
}

files["src/premake4.lua"] = {
  globals = {
    "_OPTIONS",
    "apps",
    "libs",
    "os_properties",
    "pkg_map",
    "props",
  },
  read_globals = {
    "_ACTION",
    "configuration",
    "configurations",
    "defines",
    "files",
    "flags",
    "includedirs",
    "kind",
    "language",
    "links",
    "location",
    "project",
    "solution",
    "targetdir",
  },
}
