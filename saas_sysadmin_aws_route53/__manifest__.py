{
    "name": """Saas Sysadmin AWS Route53""",
    "summary": """This module can be used by other SaaS modules when DNS needed""",
    "category": "SaaS",
    "images": [],
    "version": "12.0.1.0.0",

    "author": "IT-Projects LLC, Ildar Nasyrov, Nicolas JEUDY",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info",
    "license": "LGPL-3",
    # "price": 9.00,
    # "currency": "EUR",

    "depends": [
        "saas_sysadmin",
        "saas_sysadmin_aws",
    ],
    "external_dependencies": {"python": ['boto'], "bin": []},
    "data": [
        "views/saas_sysadmin_aws_route53.xml",
    ],
    "demo": [
    ],
    "installable": False,
    "auto_install": False,
}
