import subprocess

# get this user
user = subprocess.check_output('whoami', shell=True).decode('utf-8').strip()

tmpfs_lines = [
    'tmpfs       /home/' + user + '/ram tmpfs   nodev,nosuid,noexec,size=64M   0 0'
]

for tmpfs_line in tmpfs_lines:

    # find out if the line is in the file
    line_in_file = False
    with open('/etc/fstab', 'r') as f:
        if tmpfs_line in f.read():
            line_in_file = True

    if not line_in_file:
        print('ramdisk not found, modifying fstab')
        with open('/etc/fstab', 'a') as f:
            f.write(tmpfs_line + '\n')
    else:
        print('ramdisk found')