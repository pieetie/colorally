# Colorally

![colorally-preview](https://github.com/user-attachments/assets/4d50f778-93c0-4e10-ab66-36fe3f57c5b1)

## Abstract
Colorally is a tool that generates accessible color palettes distinguishable across normal vision, various types of color blindness (protanopia, deuteranopia, tritanopia) and grey scale applications such as printing.  
Based on a review by [Nicolas Burrus](https://github.com/nburrus) and the work of Gustavo M. Machado, Manuel M. Oliveira and Leandro A. F. Fernandes, Colorally uses vision simulation matrices to convert colors and assess their perceptual differences.  
The core algorithm employs the CIEDE2000 color difference formula to ensure minimum perceptual distance between colors with a threshold set at delta E ≥ 10 for reliable distinguishability.  
The tool generates palettes containing 2 to 7 colors through a structured pipeline.  
An additional greedy algorithm exploration found a maximum of 8 colors under these constraints, with computational time scaling significantly for larger palettes.
A different algorithmic approach would be needed to determine the theoretical maximum palette size with these settings.

## Documentation

- [Try Colorally](https://pieetie.github.io/colorally/)
- [How it works](docs/guides/METHODOLOGY.md)
- [Usage Guide](docs/guides/USAGE.md)
- [Contributing](CONTRIBUTING.md)

## References
- [Review of Open Source Color Blindness Simulations (Nicolas Burrus)](https://daltonlens.org/opensource-cvd-simulation/)
- [A Physiologically-based Model for Simulation of Color Vision Deficiency (Machado et al.)](https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html#Results)
- [Delta E (CIE 2000) formula (Bruce Lindbloom)](http://www.brucelindbloom.com/index.html?Eqn_DeltaE_CIE2000.html)
