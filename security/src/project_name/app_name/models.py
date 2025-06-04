from django.db import models


class PrintClass(models.Model):
    user_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'app_name_printfun'
        verbose_name = 'printfun'
        verbose_name_plural = 'printfuns'

    def __str__(self):
        return self.user_name


class PingLog(models.Model):
    ping_host = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_name_ping_view'
        verbose_name = 'ping_view'
        verbose_name_plural = 'ping_view'

    def __str__(self):
        return self.ping_host


class DomainLog(models.Model):
    ssl_domain = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_name_ssl_view'
        verbose_name = 'ssl_view'
        verbose_name_plural = 'ssl_views'

    def __str__(self):
        return self.ssl_domain


class HttpLog(models.Model):
    securityheaders_domain = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_name_check_http_view'
        verbose_name = 'check_http_view'
        verbose_name_plural = 'check_http_views'

    def __str__(self):
        return self.securityheaders_domain


class ChecksslClass(models.Model):
    ssllabs_domain = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_name_check_ssl_view'
        verbose_name = 'check_ssl_view'
        verbose_name_plural = 'check_ssl_views'

    def __str__(self):
        return self.ssllabs_domain


class CheckcmtechClass(models.Model):
    domain = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_name_check_cmtech_view'
        verbose_name = 'check_cmtech_view'
        verbose_name_plural = 'check_cmtech_view'

    def __str__(self):
        return self.domain


class CheckcveClass(models.Model):
    tech_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_name_check_cve_view'
        verbose_name = 'check_cve_view'
        verbose_name_plural = 'check_cve_view'

    def __str__(self):
        return self.tech_name


class CloudClass(models.Model):
    cloudflare_domain = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_name_check_cloudfare_view'
        verbose_name = 'check_cloudfare_view'
        verbose_name_plural = 'check_cloudfare_view'

    def __str__(self):
        return self.cloudflare_domain


class NsClass(models.Model):
    ns_lookup_domain = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_name_check_ns_view_view'
        verbose_name = 'check_check_ns_view'
        verbose_name_plural = 'check_ns_views'

    def __str__(self):
        return self.ns_lookup_domain