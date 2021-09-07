# ds-mod-tools

[![Docker Pulls](https://img.shields.io/docker/pulls/viktorpopkov/ds-mod-tools)](https://hub.docker.com/r/viktorpopkov/ds-mod-tools)
[![CI](https://img.shields.io/github/workflow/status/victorpopkov/ds-mod-tools/CI?label=CI)](https://github.com/victorpopkov/ds-mod-tools/actions/workflows/ci.yml)
[![Linux](https://img.shields.io/github/workflow/status/victorpopkov/ds-mod-tools/Linux?label=Linux)](https://github.com/victorpopkov/ds-mod-tools/actions/workflows/linux.yml)

> As I do sometimes develop mods for this game, I'm still dependent on this
> project. However, the development speed is kinda slow, so I've decided to make
> a proper fork and introduce some changes to speed things up.

This is a fork from the source code for the "Don't Starve Mod Tools" which is
available through Steam.

It is a port of the original mod tools to Linux and macOS. In addition, it also
improves the original animation compiler (i.e., SCML):

- Properly calculating the bounding boxes of animation frames
- Determining the correct frame to use in a timeline with variable images (i.e.,
  proper correlation of animation frame elements to build symbol frames)

The Linux and macOS porting, as well as the improvements mentioned above, were
done by [@nsimplex][]. @DeathDisciple was responsible for getting the tools
compiling once again under Windows, after the Unix port.

## Compilation-time dependencies

This project uses [Premake][] to generate the build files, so it must be
installed.

Additionally, a C++ compiler is required. For Windows, either Visual Studio or
MinGW may be used. For macOS, it is necessary to download and install XCode from
Apple. For Linux, `gcc` and `make` (GNU `make`, also known as `gmake`) are
required (you probably already have them).

## Runtime dependencies

Under Windows, the tools have no runtime dependencies other than those bundled
within the tools.

For macOS and Linux, a system-wide installation of Python 2.7 is assumed, as well
as the Python Imaging Library (PIL) or its backwards-compatible fork
([Pillow][]). A system wide installation of the TEX converter `ktech` in
[ktools][] is also assumed.

## Compilation instructions

To customize the build files placed in `build/proj/`, instead of running
`src/premake.bat` or `src/premake.sh`, the `premake4` program may be run
directly from a terminal (`cmd.exe`, under Windows). For the full list of
options, run `premake4 --help`, but the most significant scenario is generating
GNU make files for compilation using MinGW, under Windows. This can be done via:

```shell
$ premake4 gmake
```

### Windows

1. Run `src/premake4.bat` to generate a Visual Studio 2010 project in
   `build/proj/`.
2. Open the generated project in Visual Studio and build it.

The output is built to `build/win32`. For MinGW, see the note below.

### Linux & macOS

1. Run `src/premake.sh` to generate `Makefiles` in `build/proj/`.
2. Run `make` within the `build/proj/` directory.

The output is built to `build/osx` or `build/linux` respectively.

## Usage

The tools were designed for being run by the `autocompiler`, which in turn was
designed under the assumption the mod tools would be placed in a directory
alongside Don't Starve's installation directory with the same structure as when
installing them via Steam. In order to use the `autocompiler`, a directory
structure such as this must be replicated (for example, under Windows, the
folder placed at `build/win32/mod_tools` after compilation must be relocated in
such a way that `mod_tools/../../dont_starve` is Don't Starve's installation
directory).

Alternatively, the `scml` compiler may be used directly. I takes two arguments:
the first one is the path to SCML file to build, and the second one is the
path to the directory of the mod in which to place the final product (an `anim/`
directory is created within the mod's if it doesn't exist).

[@nsimplex]: https://github.com/nsimplex/
[ktools]: https://github.com/nsimplex/ktools#installation-from-source
[pillow]: https://pillow.readthedocs.io/en/stable/
[premake]: https://premake.github.io/
