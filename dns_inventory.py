import dns.resolver

def get_dns_records(domain):
    records = {}
    record_types = ['A', 'AAAA', 'TXT', 'CNAME', 'MX', 'SOA', 'NS', 'SRV']
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [str(rdata) for rdata in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            records[record_type] = []
    return records
