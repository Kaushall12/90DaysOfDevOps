#### Linux Volume Management (LVM)



##### 

##### 1\. Environment Preparation



Switched to root:



sudo -i



Created virtual disk (since no spare disk available):



dd if=/dev/zero of=/tmp/disk1.img bs=1M count=1024



Attached loop device:



losetup -fP /tmp/disk1.img



Checked device:



losetup -a



Example device:

/dev/loop0



##### 2\. Current Storage Check



Commands:



lsblk

pvs

vgs

lvs

df -h



Observation:

No existing physical volumes or volume groups before setup.



##### 3\. Create Physical Volume (PV)



pvcreate /dev/loop0



Verify:



pvs



Observation:

Physical volume successfully created.



##### 4\. Create Volume Group (VG)



vgcreate devops-vg /dev/loop0



Verify:



vgs



Observation:

Volume group devops-vg created with available space.



##### 5\. Create Logical Volume (LV)



lvcreate -L 500M -n app-data devops-vg



Verify:



lvs



Observation:

Logical volume app-data created inside devops-vg.



##### 6\. Format and Mount



Format filesystem:



mkfs.ext4 /dev/devops-vg/app-data



Create mount point:



mkdir -p /mnt/app-data



Mount:



mount /dev/devops-vg/app-data /mnt/app-data



Verify:



df -h /mnt/app-data



Observation:

Mounted successfully with 500MB available.



##### 7\. Extend Logical Volume



Extend volume:



lvextend -L +200M /dev/devops-vg/app-data



Resize filesystem:



resize2fs /dev/devops-vg/app-data



Verify:



df -h /mnt/app-data



Observation:

Volume successfully expanded to ~700MB without data loss.



##### Commands Used



dd

losetup

lsblk

pvcreate

vgcreate

lvcreate

mkfs.ext4

mount

lvextend

resize2fs



##### What I Learned



LVM provides flexible storage management.



Logical volumes can be extended without reformatting.



Resize requires two steps: extend LV + resize filesystem.



Physical → Volume Group → Logical Volume hierarchy.

