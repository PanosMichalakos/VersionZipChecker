import ntpath
import zipfile
from modules import comparezipfiles, checksqlxmlfilesforlatest
from paths import *

rczip = rcpath + 'rc.zip'

while True:
    print('Choose 1 to check RC.zip, 2 to check version.zip, Q to exit program')
    mode = input('> ')

    if mode == '1':
        print('*** STEP1: CHECKING RC FILES ***')
        print('* Creating RC.zip copies for checking')
        rcversionzip = rcpath + 'rcversion.zip'
        rcupdzip = rcpath + 'rcversion_upd.zip'
        with zipfile.ZipFile(rczip, 'r') as zrc, zipfile.ZipFile(rcversionzip, 'w') as z1, zipfile.ZipFile(rcupdzip,

                                                                                                           'w') as z2:
            excludeversionfolders = ['ess/Node cli/', 'ess/csproj-includes/']
            excludeupdatefolders = excludeversionfolders + ['ess/Docs/', 'ess/ErrorsHistory/', 'ess/Reports/',
                                                            'ess/service/config',
                                                            'ess/Temp/']
            versionfolders = [i for i in zrc.namelist() if i not in excludeversionfolders]
            updatefolders = [i for i in zrc.namelist() if i not in excludeupdatefolders]

            # IMPROVE LOOP
            for item in versionfolders:
                buffer = zrc.read(item)
                if not item.startswith('sql/') and not item.startswith('ess/Node cli/') \
                        and not item.startswith('ess/csproj-includes/'):
                    z1.writestr(item, buffer)
            for item in updatefolders:
                buffer = zrc.read(item)
                if not item.startswith('db/') and not item.startswith('ess/Node cli/') \
                        and not item.startswith('ess/csproj-includes/') and not item.startswith('ess/Docs/') \
                        and not item.startswith('ess/ErrorsHistory/') and not item.startswith('ess/Reports/') \
                        and not item.startswith('ess/service/config') and not item.startswith('ess/Temp/'):
                    z2.writestr(item, buffer)

        while True:

            # Compare RC with previous version zips
            print('What is the RC version? (2xxxxxxxx) Type Q to quit')
            versiontocheck = input('> ')
            if versiontocheck.lower() == 'q':
                break
            elif not versiontocheck.isnumeric():
                print('This is not a valid version. Version has to be in numeric form (2xxxxxxx)')
                continue
            elif len(versiontocheck) != 8:
                print('This is not a valid version. Version has to be in numeric form (2xxxxxxx)')
                continue
            else:
                for o in latestversionfiles:
                    if ntpath.basename(o.replace('.zip', '')).isnumeric():
                        zip1 = rcversionzip
                        print('* Now Checking ' + zip1)
                    else:
                        zip1 = rcupdzip
                        print('* Now Checking ' + zip1)
                    comparezipfiles(o, zip1)

            # Check Version Script and XML
            version = versiontocheck
            versionsql = versiontocheck + '.sql'
            checksqlxmlfilesforlatest(rcupdzip, version, versionsql)
            break
        continue
    elif mode == '2':

        # Compare version zips with previous zips
        print('*** STEP1: CHECKING ZIP FILES ***')
        for o in latestversionfiles:
            if ntpath.basename(o.replace('.zip', '')).isnumeric():
                zip1 = max(archiveversionfiles, key=os.path.getctime)
            else:
                zip1 = max(archiveupdatefiles, key=os.path.getctime)
            print('* Now Checking ' + o)
            comparezipfiles(zip1, o)

        # Check Version Script and XML
        print('*** STEP2: CHECKING VERSION SCRIPT AND XML ***')
        for i in latestupdatefiles:
            version = ntpath.basename(i.replace('_upd.zip', ''))
            versionsql = ntpath.basename(i.replace('_upd.zip', '.sql'))
            checksqlxmlfilesforlatest(i, version, versionsql)
        continue
    elif mode.lower() == 'q':
        break
    else:
        print('Command is not valid')
        continue
