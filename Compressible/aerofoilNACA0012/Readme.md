Supersonic flow over an airfoil:

The idea was to look for high speed flow over a symmetric airfoil (NACA 0012), checking for the shock wave formation. This study is at its inception and I want to apply it towards flow stabilization for combustors with non-axial flows, namely the continuous detonation engine. Although a nozzle is preferred due to high temperatures at the exit, implementing active methods for stabilization could prove beneficial.

The study uses a transient solver for turbulent flow of compressible fluids. It employs the PIMPLE algorithm, a combination of PISO and SIMPLE algorithms. An external loop is added to the PISO algorithm, making the method iterative and allowing for counting with Courant number > 1.

Flow parameters:

Fluid: Air

Velocity: 300 m/s

Domain: 5.7 x 4 (m)

Solver: rhoPimpleFoam

Turbulence model: k-omega SST
