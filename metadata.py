@metadata_processor
def add_apt_packages(metadata):
    if node.has_bundle("apt"):
        metadata.setdefault('apt', {})
        metadata['apt'].setdefault('packages', {})

        metadata['apt']['packages']['unifi'] = {'installed': True, 'needs': ['action:apt_update_unifi'],
                                                'triggers': ['svc_systemd:unifi:restart']}

    return metadata, DONE
