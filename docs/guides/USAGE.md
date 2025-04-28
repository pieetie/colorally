# Usage Guide

This document explains how to use Colorally.

There are two ways to use this project: either access pre-generated palettes or generate more palettes with your own custom settings.

## Using Pre-generated Palettes

If you simply want to use the tool, you can visit https://pieetie.github.io/colorally/.

All pre-generated palettes are available in the `palettes/` folder.

## Generating Custom Palettes

If you want to generate more palettes, you can:

1. Change the number of palettes and generate more using the `main.py` file
2. Customize the Delta E values for each vision type in the `verify_colors.py` file located in the `scripts/` folder

Currently, there is no simplified tool for palette generation. You need to edit the code and pipeline files directly. In the future, I plan to implement a script to easily generate palettes by modifying all parameters in one place.