defaults = {}

if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            'unifi': {
                'installed': True,
                'needs': [
                    'action:apt_update_unifi',
                ],
                'triggers': [
                    'svc_systemd:unifi:restart',
                ]
            },
            'gnupg': {
                'installed': True,
            }
        }
    }
