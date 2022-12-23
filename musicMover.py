import os
import shutil
import time


def musicCopy(musicLoc, musicMoveLoc):
    if not os.path.exists(musicLoc):
        os.system("sudo mount.cifs //ryan_urq_laptop/c/ /mnt/windows-share/ -o user=ryan_urq,"
                  "pass=44Glenavna,ip=192.168.50.78")
    print("In background:\nChecking for laptop, then transferring music files")
    musicRAIDLoc = "/export/RAID/PlexMedia/Music/"
    if os.path.exists(musicLoc):
        print("Found laptop, checking for files to move now")
        os.system("rsync -rpEogvht --delete --update /mnt/windows-share/Users/ryan1/Music/Soggfy/ /export/NAS/Music/")
    if os.path.exists(musicRAIDLoc):
        print("\n\nFound RAID")
        os.system("rsync -rpEogvht --delete --update /mnt/windows-share/Users/ryan1/Music/Soggfy/ "
                  "/export/RAID/PlexMedia/Music/")
    if not os.path.exists(musicRAIDLoc):
        print("No RAID")
    print("Music dir up-to-date")
