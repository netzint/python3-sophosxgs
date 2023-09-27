# Sophos Python API Module

## Basic usage

    from SophosAPI import SophosAPI
    api = SophosAPI("10.0.1.1", 4444, "admin", "123456789")

## Examples

### Get IPHosts
    from SophosAPI import SophosAPI, SophosAPIType
    api = SophosAPI("10.0.1.1", 4444, "admin", "123456789")
    api.get(SophosAPIType.IPHOST)

### Add IPHost
    from SophosAPI import SophosAPI, SophosAPIType, SophosAPIType_IPHost
    api = SophosAPI("10.0.1.1", 4444, "admin", "123456789")
    newhost = SophosAPIType_IPHost("test1", SophosAPIType_IPHost.IPFAMILY_IPV4, SophosAPIType_IPHost.HOSTTYPE_IP, ip="1.1.1.1")
    api.add(SophosAPIType.IPHOST, newhost)