# -*- coding: utf-8 -*-
from imio.gdpr.interfaces import IImioGdprLayer
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.interface import directlyProvides

import imio.gdpr


class ImioGdprLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=imio.gdpr)

    def setUpPloneSite(self, portal):
        directlyProvides(portal.REQUEST, IImioGdprLayer)  # noqa
        applyProfile(portal, 'imio.gdpr:default')


IMIO_GDPR_FIXTURE = ImioGdprLayer()


IMIO_GDPR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IMIO_GDPR_FIXTURE,),
    name='ImioGdprLayer:IntegrationTesting',
)


IMIO_GDPR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IMIO_GDPR_FIXTURE,),
    name='ImioGdprLayer:FunctionalTesting',
)


IMIO_GDPR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        IMIO_GDPR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ImioGdprLayer:AcceptanceTesting',
)
