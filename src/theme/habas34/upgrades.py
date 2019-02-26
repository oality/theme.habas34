# -*- coding: utf-8 -*-
from plone import api
from plone.app.upgrade.utils import loadMigrationProfile


def reload_gs_profile(context):
    loadMigrationProfile(
        context,
        'profile-theme.habas34:default',
    )


def uninstall_banner(context):
    portal_setup = api.portal.get_tool('portal_setup')
    portal_setup.runAllImportStepsFromProfile(
        'profile-collective.behavior.banner:uninstall'
    )
