# -*- coding: UTF-8 -*-

import subprocess
import numpy as np
import matplotlib.pyplot as plt
from helixmc.pose import HelixPose

# Quick prerun to get the avg. link at relaxed state #
cmdline  = 'helixmc-run '
cmdline += '-params_file DNA_default.npz '
cmdline += '-n_bp 500 '
cmdline += '-n_step 20 '
cmdline += '-force 5 '
cmdline += '-compute_fuller_link True '
cmdline += '-out prerun'

print 'Prerun command line:', cmdline
subprocess.check_call( cmdline.split() )

data = np.load('prerun.npz') # Load the prerun output
avg_link =  np.average(data['twist'] + data['writhe']) #avg. link in radian
print 'Avg. Z relaxed:', np.average(data['coord_terminal'][:,2]) #avg. z-extension in Å
print 'Avg. link relaxed:', avg_link

# Link constrained run #
target_link = avg_link + 8 * ( 2 * np.pi ) #set the center of link contraint at +8 turns
print 'Target link:', target_link

cmdline  = 'helixmc-run '
cmdline += '-params_file DNA_default.npz '
cmdline += '-n_bp 500 '
cmdline += '-n_step 20 '
cmdline += '-force 5 '
cmdline += '-compute_fuller_link True '
cmdline += '-target_link %f ' % target_link
cmdline += '-trap_stiffness 2000 '
cmdline += '-out link_cst'

print 'Link contrained command line:', cmdline
subprocess.check_call( cmdline.split() )

# Data Analysis #
data = np.load('link_cst.npz')
print 'Avg. Z (8 turns):', np.average(data['coord_terminal'][:,2]) #avg. z-extension in Å
print 'Avg. Link (8 turns):', np.average(data['twist'] + data['writhe']) #avg. link in radian

