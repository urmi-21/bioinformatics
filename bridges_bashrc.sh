# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=


# User specific aliases and functions
function mkdcd () {
     mkdir "$1" && cd "$1"
}




#ALIASES
alias interactive='srun --pty -p RM -N 1 -C EGRESS -t 6:00:00 /bin/bash -l'
alias interactive_lm='srun --pty -p LM -N 1 -C EGRESS --mem=1000G -t 6:00:00 /bin/bash -l'
alias work='cd /pylon5/bi5611p/usingh'
alias js='squeue -u usingh'
export PATH=/pylon5/bi5611p/usingh/rnafold/ViennaRNA-2.4.2/src/bin:$PATH
export PATH=/pylon5/bi5611p/usingh/salmon/Salmon-0.8.2_linux_x86_64/bin:$PATH
export PATH=/pylon5/bi5611p/usingh/softwares/sratoolkit.2.8.2-1-centos_linux64/bin:$PATH
#export PATH=/pylon2/bi5611p/usingh/softwares/ascp_connect/bin:$PATH
export PATH=/home/usingh/.local/lib/python2.7/site-packages/busco:$PATH
export PATH=/pylon5/bi5611p/usingh/softwares/augustus.2.5.5/bin:$PATH
export PATH=/pylon5/bi5611p/usingh/softwares/ncbi-blast-2.7.1+/bin:$PATH
export AUGUSTUS_CONFIG_PATH=/pylon5/bi5611p/usingh/softwares/augustus.2.5.5/config
alias dtn='ssh usingh@br030.dmz.bridges.psc.edu'
