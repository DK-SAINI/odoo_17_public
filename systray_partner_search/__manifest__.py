# -*- coding: utf-8 -*-
{
    "name": "Systray Partner Search",
    "summary": "Quick Partner Search From Systray.",
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "17.0.0.1",
    "depends": ["base", "contacts"],
    "data":[
        "security/user_group.xml",
    ],
    "assets": {
        "web.assets_backend": {
            "/systray_partner_search/static/src/component/*/*.js",
            "/systray_partner_search/static/src/component/*/*.xml",
        },
    },
}
