#!/usr/bin/env python

import urllib2
import urllib
import subprocess
import argparse


def get_instance_metadata(path):
    base = 'http://169.254.169.254/latest/'
    p = subprocess.Popen('curl {0}{1}'.format(base, path),
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.communicate()[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bootstrap_url')
    args = parser.parse_args()

    params = urllib.urlencode({
        'host': get_instance_metadata('meta-data/public-hostname'),
        'private_ip': get_instance_metadata('meta-data/local-ipv4'),
        'instance_id': get_instance_metadata('meta-data/instance-id'),
        'user_data': get_instance_metadata('user-data')
    })
    res = urllib2.urlopen(args.bootstrap_url, params)

    print res.read()
    res.close()


if __name__ == "__main__":
    main()
