from allauth.socialaccount import providers


def socialaccount_providers(request):
    from allauth.socialaccount import providers
    return {'socialaccount_providers': list(providers.registry.provider_map.values())}
