import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm  # Colormaps used for mapping values to colors
import matplotlib as mpl  # General matplotlib functions

import enum
from urllib.parse import quote_from_bytes
import numpy as np
import os, sys


# Insert the custom module's path into system path
sys.path.insert(0, f"{os.path.expanduser('~')}/Dropbox/my_py_modules/graphs_and_animations")
from add_latex import *  # Custom LaTeX module for rendering LaTeX equations in plots


from qutip import *  # Import QuTiP for working with quantum objects and simulations

# Function to generate time-dependent Hamiltonian term Delta(t)
def Delta_t(t, args):
    Delta_0 = args['Delta_0']  # Initial value of Delta
    Delta_tau = args['Delta_tau']  # Final value of Delta at time tau
    tau = args['tau']  # Total evolution time
    
    # Linear interpolation of Delta between Delta_0 and Delta_tau
    return (Delta_tau - Delta_0) * t / tau + Delta_0

# Function to compute the Bloch vector components (rx, ry, rz) from a density matrix
def qubit_Bloch_vector_from_density_matrix(rho):
    rx = 2*rho[0,1].real  # x-component of the Bloch vector (real part of off-diagonal)
    ry = -2*rho[0,1].imag  # y-component of the Bloch vector (imaginary part of off-diagonal)
    rz = 2*rho[0,0].real-1  # z-component of the Bloch vector (diagonal elements)
    return rx, ry, rz



# Parameters for the system evolution
J = 0.5  # Coupling constant for sigma_x term in the Hamiltonian
hz = -1.0  # Z-direction field strength
tau = 10  # Total evolution time
p = 0.1  # Amplitude damping parameter
nts = 101  # Number of time steps for the evolution
tlist = np.linspace(0, tau, nts)  # List of times for the evolution

# Arguments for the time-dependent Hamiltonian
H_args = {'Delta_0': -0.5*hz, 'Delta_tau': hz, 'tau': tau}

# Define the time-independent and time-dependent parts of the Hamiltonian
H_0 = J * sigmax()  # Time-independent sigma_x term
H_1 = sigmaz()  # Time-dependent sigma_z term

# Combine the Hamiltonian terms into a time-dependent Hamiltonian
H_td = [H_0, [H_1, Delta_t]]

# Define amplitude damping (Kraus) operators
K_0 = np.array([[1, 0], [0, np.sqrt(1-p)]])  # Operator for no excitation loss
K_1 = np.array([[0, np.sqrt(p)], [0, 0]])  # Operator for amplitude damping
K_ops = [Qobj(K_0), Qobj(K_1)]  # Convert to QuTiP quantum objects

# Initial state of the system (a mixed state with probability p_0 in |0⟩)
p_0 = 0.9
rho_0 = Qobj(np.array([[p_0, 0], [0, 1-p_0]]))  # Initial density matrix


# Evolve the system using the Lindblad master equation
rho_ts = mesolve(H_td, rho_0, tlist=tlist, args=H_args, c_ops=K_ops, e_ops=[]).states


# Prepare to store results for Bloch vector evolution
P_ts = np.zeros(nts)  # Purity of the state at each time step
pts = []  # List of Bloch vector components at each time step

# Loop over all time steps to compute the Bloch vectors and purities
for it, t in enumerate(tlist):
    rho_t = rho_ts[it]  # Get density matrix at time t
    rx, ry, rz = qubit_Bloch_vector_from_density_matrix(rho_t)  # Compute Bloch vector
    P = rho_t.purity()  # Compute the purity of the state at time t
    P_ts[it] = P  # Store purity value
    pts.append([rx, ry, rz])  # Store Bloch vector components


# Normalize purity values and create a colormap based on purity
norm = mpl.colors.Normalize(vmin=P_ts.min(), vmax=P_ts.max())  # Normalize purity values
cmap = cm.rainbow  # Use rainbow colormap
m = cm.ScalarMappable(norm=norm, cmap=cmap)  # Create a scalar mappable to convert purities to colors

# Map purity values to colors for the points on the Bloch sphere
cores = [m.to_rgba(P) for P in P_ts]


# Initialize Bloch sphere visualization
b = Bloch()

# Add basis vectors to the Bloch sphere (x, y, z axes)
b.vector_color = ['k']  # Black color for basis vectors
b.add_vectors([1,0,0])  # x-axis vector
b.add_vectors([0,1,0])  # y-axis vector
b.add_vectors([0,0,1])  # z-axis vector

b.point_color = cores  # Set point colors based on purity
b.point_marker = ['o']  # Use circular markers for points

# Add points to the Bloch sphere, representing the state evolution
for pt in pts:
    b.add_points(pt)

# Add annotation for the initial state
b.add_annotation([pts[0][0], pts[0][1]+0.05, pts[0][2]], r'$\quad \quad \quad \quad  \hat{\rho}_0$', ha='left')

# Add annotation for the final state
b.add_annotation([pts[-1][0], pts[-1][1]-0.075, pts[-1][2]], r'$\hat{\rho}_\tau \quad \quad \quad \quad \quad  $', ha='right')

# Render the Bloch sphere with the points and vectors
b.render()
b.make_sphere()
# Save the Bloch sphere image to a file
plt.savefig('qubit_amplitude_damping.png', transparent=True)

# Show the plot
plt.show()