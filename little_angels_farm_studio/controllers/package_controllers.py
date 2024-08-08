# -*- coding: utf-8 -*-

import requests
from odoo import http
from odoo.http import request, Controller, route


class PackageTypes(http.Controller):
    @http.route(
        ["/one-plan", "/second-plan", "/third-plan"], auth="public", website=True
    )
    def show_plan(self, **kw):
        plan_map = {
            "/one-plan": "1-plan",
            "/second-plan": "2-plan",
            "/third-plan": "3-plan",
        }
        plan_name = plan_map.get(request.httprequest.path)
        return request.render(
            "little_angels_farm_studio.website_package_type_plans", {"plan_name": plan_name}
        )


class SubmitPackageType(http.Controller):
    ADMIN_EMAIL = "dheerajsaini814@gmail.com"

    WHATSAPP_URL = "https://graph.facebook.com/v20.0/{phone_number_id}/messages"
    WHATSAPP_PHONE_NUMBER_ID = "370377679495772"
    WHATSAPP_AUTH_TOKEN = "EAASIr0x0Ko8BOZBAtdumnNpUWDtfJt3KW4p0LANRaz85jppinK6iUOOc5eYdpR8svEsTwycHK3w8KmaWwjqz1B70G9yXDc4ZC1Sm6EOdkb7MUosBJrgpoN8GiDDlOJqxYt6ogeZCIzcA025NGGfrdZCtjqVV1Ox3Pguj3NUCegkVvtVZA6sClXDZABt68yY33S9vayznHMKgpqEYITVsYZD"
    WHATSAPP_TO_PHONE_NUMBER = "919509925997"

    @http.route("/submit_package", type="http", auth="public")
    def submit_package(self, **post):
        try:
            self.send_email_to_admin(post)
            # self.send_custom_contact_message()
        except Exception as e:
            # Log the exception and show a friendly error message
            request.env["ir.logging"].sudo().create(
                {
                    "name": "SubmitPackageType",
                    "type": "server",
                    "level": "error",
                    "message": str(e),
                }
            )
            return request.redirect("/contactus-error")

        return request.redirect("/contactus-thank-you")

    def send_email_to_admin(self, post):
        admin_user = (
            request.env["res.users"].sudo().search([("id", "=", 2)], limit=1)
        )  # Assuming the admin user has ID 1
        admin_email = admin_user.email or self.ADMIN_EMAIL

        email_template = """
            <p>Hello Admin,</p>
            <p>A new package submission has been received with the following details:</p>
            <ul>
                <li>Name: {name}</li>
                <li>Mobile No.: {phone}</li>
                <li>Email: {email}</li>
                <li>Package Type: {plan_type}</li>
                <!-- Add more fields as necessary -->
            </ul>
            <p>Regards,<br/>Your Company</p>
        """
        email_body = email_template.format(
            name=post.get("name"),
            phone=post.get("phone"),
            email=post.get("email"),
            plan_type=post.get("plan_type"),
        )

        email_values = {
            "subject": "New Package Submission",
            "email_from": post.get("email"),
            "email_to": admin_email,
            "body_html": email_body,
        }

        mail = request.env["mail.mail"].sudo().create(email_values)
        mail.send()

    def send_custom_contact_message(self):
        url = self.WHATSAPP_URL.format(phone_number_id=self.WHATSAPP_PHONE_NUMBER_ID)
        headers = {
            "Authorization": f"Bearer {self.WHATSAPP_AUTH_TOKEN}",
            "Content-Type": "application/json",
        }
        data = {
            "messaging_product": "whatsapp",
            "to": self.WHATSAPP_TO_PHONE_NUMBER,
            "type": "template",
            "template": {"name": "hello_world", "language": {"code": "en_US"}},
        }

        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            raise Exception(f"Failed to send WhatsApp message: {response.json()}")
