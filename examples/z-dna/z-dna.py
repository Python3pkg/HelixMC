# -*- coding: UTF-8 -*-

import subprocess
import numpy as np
import matplotlib.pyplot as plt
from helixmc.pose import HelixPose

# Run HelixMC #
cmdline = 'helixmc-run '
cmdline += '-params Z-DNA.npz '
cmdline += '-n_bp 100 '
cmdline += '-n_step 10 '
cmdline += '-seq GC '
cmdline += '-force 5 '
cmdline += '-compute_fuller_link '
cmdline += '-out_frame test_run'

print('Z-DNA command line:', cmdline)
subprocess.check_call(cmdline.split())

# Data Analysis #
data = np.load('MC_data.npz')
# avg. z-extension in Å
print('Avg. Z:', np.average(data['coord_terminal'][:, 2]))
# avg. link in radian
print('Avg. Link:', np.average(data['twist'] + data['writhe']))

# Helix Plotting #
pose = HelixPose.from_file('test_run.npz')
pose.plot_centerline(show=False)  # plot the centerline
plt.title('Center line')


pose.plot_helix(show=False, rb_width=15)  # plot the entire helix
plt.title('Helix Plot')
plt.show()
