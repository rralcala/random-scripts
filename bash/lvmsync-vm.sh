#!/bin/bash
# The idea about this script is to incrementally keep a remote volume of a KVM guest in sync
# You can add this to cron to have a evey n hour sync for fault tolerance
# In some cases I've found this aproach simpler compared to having a shared fs to allow live
# migrations.
#
# Before using:
# You'll need ruby 1.8+
# (both hosts) git clone git@github.com:rralcala/lvmsync.git (Acutal credits to: mpalmer/lvmsync)
# (both hosts) add lvmsync to your path
# lvcreate --snapshot -L5G -n origin_snap origin_vg/origin_lv
# dd if=/dev/origin_vg/origin_snap bs=1M | ssh dest_host dd of=/dev/dest_vg/dest_lv bs=1M

origin_vg=vg_orion
origin_lv=lv_amnesia_root
origin_snap=lv_amnesia_root-snap
dest_vg=VolGroup
dest_lv=lv_amnesia_root
dest_host=shogun
vm_name=amnesia

if [ ! -e /dev/$origin_vg/$origin_snap ]; then
        echo "Snapshot must exist"
        exit 1
fi

virsh shutdown $vm_name

while [ $(virsh list | grep $vm_name | wc -l) -eq 1 ]; do
        sleep 1;
done

lvmsync /dev/$origin_vg/$origin_snap $dest_host:/dev/$dest_vg/$dest_lv

if [ $? -eq 0 ]; then
        lvremove -f $origin_vg/$origin_snap
        lvcreate --snapshot -L5G -n $origin_snap $origin_vg/$origin_lv
fi

virsh start $vm_name

