import glob
import os

archive_path = r''
latestversion_path = r''
rcpath = r''
archivefiles = set(sorted(glob.glob(archive_path + '*[0-9]*.zip'), key=os.path.getctime, reverse=True))
archiveupdatefiles = set(sorted(glob.glob(archive_path + '*upd.zip'), key=os.path.getctime, reverse=True))
archiveversionfiles = archivefiles - archiveupdatefiles
latestversionfiles = sorted(glob.glob(latestversion_path + '*[0-9]*.zip'), key=os.path.getctime, reverse=True)
latestupdatefiles = sorted(glob.glob(latestversion_path + '*upd.zip'), key=os.path.getctime, reverse=True)
