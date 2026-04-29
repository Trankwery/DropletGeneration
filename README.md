# DOD-Droplet-Gen: Parameter Tuning & Visualization
This repository provides a suite of tools for optimizing the operation of Drop-on-Demand (DOD) droplet generators.
It allows users to map the stable operating regime of their generator by visualizing the dimensionless parameter space and calculating 
critical physical constants required for uniform droplet production. 
## Features 
### Parameter Space Visualization:
Generates $We$ vs. $Re$ plots to identify the "stable drop formation" region (e.g., based on the Ohnesorge number $Oh$ or the $Z$ parameter).
### Capillary Time Calculation:
Determines the characteristic time scale $\tau_c$ for droplet oscillations and pinch-off. 
### Minimal Velocity Estimation: 
Calculates the theoretical $v_{min}$ required to overcome surface tension and eject a droplet. 
## Physical Background: 
The code utilizes fluid dynamics principles to predict droplet behavior. The primary dimensionless numbers used are the Reynolds number ($Re$) and the Weber number ($We$):

$$Re = \frac{\rho v d}{\mu}$$

$$We = \frac{\rho v^2 d}{\sigma}$$

Where: 
+ $\rho$: Density
+ $v$: Velocity 
+ $d$: Orifice diameter
+ $\mu$: Dynamic viscosity
+ $\sigma$: Surface tension
## Critical Calculations
1. Characteristic Capillary Time ($\tau_c$): 
The time scale at which surface tension drives the contraction or oscillation of the droplet:
$$\tau_c = \sqrt{\frac{\rho r^3}{\sigma}}$$
2. Minimal Velocity ($v_{min}$):
To successfully eject a droplet from a nozzle, the kinetic energy must overcome the surface energy. The theoretical minimum velocity is calculated as:
$$v_{min} = \sqrt{\frac{4 \sigma}{\rho d}}$$
## Getting Started
### Prerequisites
+ Python 3.x
+ Dependencies: numpy, matplotlib, scipy
+ MATLAB
Usage Input your liquid properties (density, viscosity, surface tension) in config.py.Run visualize_params.py to see your current operating point relative to the stable regime ($2 < Z < 14$).Use calc_kinetics.py to output the required voltage-to-pressure estimations.
## License:
This project is licensed under the CC License—see the LICENSE file for details.
## Citation
If you use this code in your research, please cite it as: 
Your Name/Lab Name (2026). DOD-Droplet-Gen: Tools for Parameter Space Optimization.
