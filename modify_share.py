#!/usr/bin/python


import sys

try:
    with open('auth.cfg', 'r') as auth:
        auth_path = auth.readline().rstrip()
except:
    auth_path = None
    pass
auth = '-H "Authorization: Basic $(cat %s | base64)"'%(auth_path) if auth_path is not None else None

def modify_share_path(cdm, share_id, path):
    request = 'PATCH'
    modifySharePathHeader = "--header 'Content-Type: application/json' --header 'Accept: text/plain'"
    path = '-d '+ "'" + '{"exportPoint": "%s"}'%(path) + "' " + 'https://%s/api/internal/host/share/HostShare:::%s'%(cdm, share_id)
    curl = 'curl -X {request} {auth} {modifySharePathHeader} {path} --insecure'.format(
        request = request,
        modifySharePathHeader = modifySharePathHeader.rstrip(),
        auth = auth.rstrip(),
        path = path
    )
    print(curl)
    if '\n' in curl:
        for i,v in enumerate(curl):
            if v == '\n':
                print(i)
    import os
    os.system(curl)
def usage():
    print("Usage: \n    python modify_share.py <cdm_ip> <host_share_uuid> <path>")
    print("Example: \n Using: HostShare:::318fd70b-85d3-4116-a575-22743b2709ec\n    python modify_share.py 10.35.36.165 318fd70b-85d3-4116-a575-22743b2709ec /new_share_path")

if __name__ == "__main__":
    cdm = sys.argv[1] if len(sys.argv) > 1 else None
    share_id = sys.argv[2] if len(sys.argv) > 2 else None
    path = sys.argv[3] if len(sys.argv) > 3 else None
    if auth_path == None or auth_path == '':
        print("Missing auth path to credentials file, please add to auth.cfg. See https://github.com/codemation/Rubrik-modify_share")
    else:
        if cdm is not None:
            if share_id is not None:
                if path is not None:
                    modify_share_path(cdm, share_id, path)
                else:
                    usage()
            else:
                usage()
        else:
            usage()
        