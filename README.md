# A color palette generator for normal, color-blind, and grey scale vision
## Abstract
Colorally is a tool that generates accessible color palettes distinguishable across normal vision, various types of color blindness (protanopia, deuteranopia, tritanopia) and grey scale applications such as printing.
Based on the articles and reviews by Nicolas Burrus and the work of Gustavo M. Machado, Manuel M. Oliveira and Leandro A. F. Fernandes, Colorally uses vision simulation matrices to convert colors and assess their perceptual differences. 
The core algorithm employs the CIEDE2000 color difference formula to ensure minimum perceptual distance between colors with a threshold set at delta E ≥ 10 for reliable distinguishability.
The tool generates palettes containing 2 to 7 colors through a structured pipeline. 
An additional greedy algorithm exploration found a maximum of 8 colors under these constraints, with computational time scaling significantly for larger palettes. 
A different algorithmic approach would be needed to determine the theoretical maximum palette size with these settings.