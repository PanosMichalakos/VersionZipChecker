import ntpath
import zipfile


def comparezipfiles(file1, file2):
    filename1 = ntpath.basename(file1.replace('.zip', ''))
    filename2 = ntpath.basename(file2.replace('.zip', ''))

    with zipfile.ZipFile(file1, mode='r') as zipfile1, zipfile.ZipFile(file2, mode='r') as zipfile2:
        filelist1 = [i for i in zipfile1.infolist() if not i.filename.endswith('/')]
        namelist1 = [i for i in zipfile1.namelist() if not i.endswith('/')]
        filelist2 = [i for i in zipfile2.infolist() if not i.filename.endswith('/')]
        namelist2 = [i for i in zipfile2.namelist() if not i.endswith('/')]

        dltdfileslist = [i for i in namelist1 if i not in namelist2]
        newfileslist = [i for i in namelist2 if i not in namelist1]
        diffileslist = [n for i in filelist2 for n in filelist1 if i.filename == n.filename and i.CRC != n.CRC]

        print('* Checking number of files between versions {} and {}'.format(filename1, filename2))
        print('* {} has {} files and {} has {} files'.format(filename1, len(filelist1), filename2, len(filelist2)))
        print('* {} files are new for version {}'.format(len(newfileslist), filename2))
        print('* {} have been deleted since {}'.format(len(dltdfileslist), filename1))
        print('* {} files have been updated/changed between versions {} and {}'.format(len(diffileslist), filename1,
                                                                                       filename2))
    while True:
        command = input(
            '* Choose an option below'
            '\nA: Print list of files added'
            '\nB: Print list of files removed'
            '\nC: Print list of files updated'
            '\nQ: Quit or Continue to next step'
            '\n>')
        if command.lower() == 'a':
            for i in newfileslist:
                print('-', i)
        elif command.lower() == 'b':
            for i in dltdfileslist:
                print('-', i)
        elif command.lower() == 'c':
            for i in diffileslist:
                print('-', i.filename)
        elif command.lower() == 'q':
            break
        else:
            print('Command is not valid')
            continue


def checkxmlforversion(xmlfile, version, versionsql):
    if '<item key="' + version + '" value="' + versionsql + '" />' in xmlfile:
        print('SUCCESS: XML has version {}'.format(version))
    else:
        print('FAIL: Check XML')


def checksqlxmlfilesforlatest(i, version, versionsql):
    with zipfile.ZipFile(i, mode='r') as z:
        # print(z.namelist())
        sqllist = [ntpath.basename(i) for i in z.namelist() if i.startswith('sql/')]
        if versionsql in sqllist:
            print('SUCCESS: Update script found in SQL folder')
            sqlread = z.read('sql/' + versionsql).decode('utf-8')
            version2 = '.'.join(a + b for a, b in zip(version[::2], version[1::2]))
            if version2 in sqlread:
                print('SUCCESS: Version ' + version2 + ' found in ' + versionsql)
            else:
                print('FAIL: Check Update script')
        else:
            print('FAIL: Update script not found in SQL folder')

        versionXML = z.read('sql/versions.xml').decode('utf-8')
        checkxmlforversion(versionXML, version, versionsql)
