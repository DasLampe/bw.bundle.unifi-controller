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
    'import_unifi_gpg': {
        'command': 'curl -L https://dl.ubnt.com/unifi/unifi-repo.gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/ubnt.gpg',
        'unless': 'test -f /etc/apt/trusted.gpg.d/ubnt.gpg',
        'triggers': [
            'action:apt_update_unifi',
        ],
        'needs': [
            'pkg_apt:gnupg',
        ]
    },
    'apt_update_unifi': {
        'command': 'apt-get update',
        'triggered': True,
        'needs': [
            'file:/etc/apt/sources.list.d/100-ubnt-unifi.list',
        ],
    },
}
