# Rubrik-modify_share

Purpose: Provide a cli method of modifying a Rubrik NAS Share if the path needs to change

Steps Before Use:
1. Create an credentials file, containing 'username|pw'. Method: echo -n 'admin:abcd1234' > ~/special_cdm_auth

2. Update auth.cfg within search_and_restore package with credential file location. Method echo -n '~/special_cdm_auth' > auth.cfg

Usage: 

    python modify_share.py <cdm_ip> <host_share_uuid> <path>

    
Example: 

 Using: HostShare:::318fd70b-85d3-4116-a575-22743b2709ec

    python modify_share.py 10.35.36.165 318fd70b-85d3-4116-a575-22743b2709ec /new_share_path