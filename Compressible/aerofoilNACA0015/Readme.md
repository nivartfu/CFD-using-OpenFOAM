Supersonic flow over a symmetric airfoil: NACA0015


The idea was to look for high speed flows over a symmetric airfoil, namely the NACA0015, checking for the shock wave formation. The study uses a transient solver for turbulent flow of compressible fluids.
It employs the PIMPLE algorithm, a combination of PISO and SIMPLE algorithms. 


Generated a C-type mesh with freestream conditions given to the inlet, upper and lower boundaries for providing flow conditions.


Flow conditions:
U_inlet = 300 m/s
T_inlet = 300K
p_inlet = 1e-5 


Turbulence model: k-Omega SST
Solver          : rhoPimpleFoam
