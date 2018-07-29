pkg_apt = {
    'unifi': {
        'needs': [
            'action:apt_update_unifi',
        ],
        'triggers': [
            'svc_systemd:unifi:restart',
        ],
    }
}

svc_systemd = {
    'unifi': {
        'needs': [
            'pkg_apt:unifi',
        ],
        'enabled': True,
    }
}

files = {
    '/etc/apt/sources.list.d/100-ubnt-unifi.list': {
        'content': 'deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti',
    },
}

actions = {
    'download_unifi_gpg': {
        'command': 'sudo wget -O /etc/apt/trusted.gpg.d/unifi-repo.gpg https://dl.ubnt.com/unifi/unifi-repo.gpg',
        'triggers': [
            'action:apt_update_unifi',
        ],
    },
    'apt_update_unifi': {
        'command': 'apt-get update',
        'triggered': True,
        'needs': [
            'file:/etc/apt/sources.list.d/100-ubnt-unifi.list',
        ],
    },
}