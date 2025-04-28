<p align="center">
  <a href="https://pieetie.github.io/colorally/">
    <img src="docs/assets/logo/logo_colorally_w.png" alt="Logo" width="200" />
  </a>
</p>

<p align="center">
  <a href="https://pieetie.github.io/colorally/"><img src="https://img.shields.io/badge/Try%20Colorally-Live%20Demo-brightgreen" alt="Live Demo"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-blue" alt="License"></a>
  <a href="https://github.com/pieetie/colorally"><img src="https://img.shields.io/badge/GitHub-Repository-lightgrey" alt="GitHub"></a>
</p>

## Abstract
Colorally is a tool that generates accessible color palettes distinguishable across normal vision, various types of color blindness (protanopia, deuteranopia, tritanopia) and grey scale applications such as printing.  
Based on reviews by [Nicolas Burrus](https://github.com/nburrus) and the work of Gustavo M. Machado, Manuel M. Oliveira and Leandro A. F. Fernandes, Colorally uses vision simulation matrices to convert colors and assess their perceptual differences.  
The core algorithm employs the CIEDE2000 color difference formula to ensure minimum perceptual distance between colors.  
The main purpose is to provide color palettes that remain distinguishable across all vision types and maintain their distinctiveness when printed.
The tool generates palettes containing 2 to 5 colors through a structured pipeline.
Colorally uses specific Delta E thresholds (ΔE ≥ 10 for normal vision, ΔE ≥ 15 for color blindness and grey scale) that ensure good distinguishability. The default values provide optimal results for scientific visualization but it is also possible to generate custom palettes with customized parameters. 
An additional greedy algorithm exploration found a maximum of 5 colors under these constraints.
A different algorithmic approach would be needed to determine the theoretical maximum palette size with these settings.

## Documentation

- [Try Colorally](https://pieetie.github.io/colorally/)
- [How it works](docs/guides/METHODOLOGY.md)
- [Usage Guide](docs/guides/USAGE.md)
- [Contributing](CONTRIBUTING.md)

## References
- [Review of Open Source Color Blindness Simulations (Nicolas Burrus)](https://daltonlens.org/opensource-cvd-simulation/)
- [Understanding LMS-based Color Blindness Simulations (Nicolas Burrus)](https://daltonlens.org/understanding-cvd-simulation/)
- [A Physiologically-based Model for Simulation of Color Vision Deficiency (Machado et al.)](https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html#Results)
- [Delta E (CIE 2000) formula (Bruce Lindbloom)](http://www.brucelindbloom.com/index.html?Eqn_DeltaE_CIE2000.html)

## Credits
- Logo and favicons were created by [Elisa PERRIN](https://www.linkedin.com/in/elisa-perrin-092082226/)
