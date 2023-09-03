# How to contribute


## Plan

The idea of this package is to create a cli tool to archive notes and urls

```sh
> cd somerepo/
somerepo> discard init
somerepo> discard add https://github.com/saxakile/discard
```

Other examples that come to mind are importers

```sh
discard import --google-keep file.json
```

```sh
discard import --google-takeout takeoutDir/
```

## How to do it

As an exercise it needs to be done only with python standard library.
We can use `argparse` module to create the cli and this RealPython [post](https://realpython.com/command-line-interfaces-python-argparse/#adding-subcommands-to-your-clis) is a good guide on how to use it. 