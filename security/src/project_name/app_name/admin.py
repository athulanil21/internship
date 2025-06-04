from django.contrib import admin

from app_name.models import PrintClass, PingLog, DomainLog, HttpLog, ChecksslClass, CheckcmtechClass, CheckcveClass, \
    CloudClass, NsClass


class PrintAdmin(admin.ModelAdmin):
    list_display = ['user_name']


admin.site.register(PrintClass, PrintAdmin)


class PingLogAdmin(admin.ModelAdmin):
    list_display = ['ping_host']


admin.site.register(PingLog, PingLogAdmin)


class DomainLogAdmin(admin.ModelAdmin):
    list_display = ['ssl_domain']


admin.site.register(DomainLog, DomainLogAdmin)


class HttpLogAdmin(admin.ModelAdmin):
    list_display = ['securityheaders_domain']


admin.site.register(HttpLog, HttpLogAdmin)


class ChecksslClassAdmin(admin.ModelAdmin):
    list_display = ['ssllabs_domain']


admin.site.register(ChecksslClass, ChecksslClassAdmin)


class CheckcmtechClassAdmin(admin.ModelAdmin):
    list_display = ['domain']


admin.site.register(CheckcmtechClass, CheckcmtechClassAdmin)


class CloudClassAdmin(admin.ModelAdmin):
    list_display = ['cloudflare_domain']


admin.site.register(CloudClass, CloudClassAdmin)


class NsClassAdmin(admin.ModelAdmin):
    list_display = ['ns_lookup_domain']


admin.site.register(NsClass, NsClassAdmin)
