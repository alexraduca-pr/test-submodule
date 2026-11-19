import re

from odoo import api, models


class SlideSlide(models.Model):
    _inherit = "slide.slide"

    @api.model
    def _resolve_placeholder_links(self):
        pattern = re.compile(r"@@([a-z0-9_]+)@@")
        slides = self.search([("html_content", "like", "@@")])
        for slide in slides:

            def repl(match):
                rec = self.env.ref(
                    f"functional_training_data.{match.group(1)}",
                    raise_if_not_found=False,
                )
                return str(rec.id) if rec else match.group(0)

            slide.html_content = pattern.sub(repl, slide.html_content)
