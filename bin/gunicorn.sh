#!/bin/bash
#
# This Runs gunicorn from within the VirtualEnv
# This is triggered by Upstart in /etc/init/gunicorn_apps.conf
# ----------------
# Creates log file in /var/log/gunicorn-apps.log

# Dynamically calculate the suggested worker count.
# The formula: 2n+1, eg: 2 cores=5, 3 cores=7, 4 cores=9
worker_total=$(( 2 * `cat /proc/cpuinfo | grep 'core id' | wc -l` + 1 ))

# Launch Gunicorn
# Ensure its loaded from our virtualenvironment to use all the correct files,
# hence the long path name.
exec /home/user/deploy/.virtualenvs/codezeus.com/bin/gunicorn wsgi:application \
  --name codezeus_com \
  --workers $worker_total \
  --log-level info \
  --bind unix:codezeus.sock -m 007 \
  --log-syslog \
  --capture-output


# To test the above command manually, remove "exec" from the line and copy/paste

