from charms.reactive import set_flag, when, when_not
from charmhelpers.fetch import get_upstream_version
from charmhelpers.core.hookenv import status_set
from charmhelpers.core.hookenv import application_version_set


@when('apt.installed.openfoam5')
@when_not('openfoam.version.set')
def set_version_status():
    """Set version and status
    """
    application_version_set(get_upstream_version('openfoam5'))
    status_set('active', 'openFOAM available')
    set_flag('openfoam.version.set')
