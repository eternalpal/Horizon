"""Feishu Webhook service for sending notifications."""

import os
import logging
import time
import hmac
import hashlib
import requests

from ..models import FeishuWebhookConfig

logger = logging.getLogger(__name__)


class FeishuWebhookManager:
    """Manages Feishu Webhook notifications."""

    def __init__(self, config: FeishuWebhookConfig, console=None):
        self.config = config
        self.webhook_url = config.webhook_url or os.getenv(config.webhook_url_env)
        self.secret = config.secret or os.getenv(config.secret_env)
        if console is None:
            try:
                from rich.console import Console
                self.console = Console()
            except ImportError:
                class DummyConsole:
                    def print(self, *args, **kwargs):
                        print(*args, **kwargs)
                self.console = DummyConsole()
        else:
            self.console = console

        if not self.webhook_url and self.config.enabled:
            logger.warning(
                f"Feishu Webhook URL not set. Please set {config.webhook_url_env} environment variable."
            )
            self.console.print(f"[yellow]Warning: Feishu Webhook URL not set. Please set {config.webhook_url_env} environment variable.[/yellow]")

    def send_notification(self, summary_md: str, subject: str):
        """Sends the summary via Feishu Webhook."""
        if not self.config.enabled or not self.webhook_url:
            return

        try:
            # Prepare the payload
            payload = {
                "msg_type": "interactive",
                "card": {
                    "config": {
                        "wide_screen_mode": True
                    },
                    "header": {
                        "title": {
                            "tag": "plain_text",
                            "content": subject
                        }
                    },
                    "elements": [
                        {
                            "tag": "markdown",
                            "content": summary_md
                        }
                    ]
                }
            }

            # Calculate signature if secret is provided
            headers = {"Content-Type": "application/json"}
            if self.secret:
                timestamp = str(int(time.time()))
                secret = self.secret
                string_to_sign = f"{timestamp}\n{secret}"
                hmac_code = hmac.new(
                    string_to_sign.encode("utf-8"),
                    digestmod=hashlib.sha256
                ).digest()
                import base64
                sign = base64.b64encode(hmac_code).decode("utf-8")
                headers["X-Timestamp"] = timestamp
                headers["X-Signature"] = f"v1={sign}"

            # Send the request
            response = requests.post(
                self.webhook_url,
                headers=headers,
                json=payload,
                timeout=10
            )

            response.raise_for_status()
            logger.info("Successfully sent Feishu Webhook notification")
            self.console.print("[green]Successfully sent Feishu Webhook notification[/green]")

        except Exception as e:
            logger.error(f"Failed to send Feishu Webhook notification: {e}")
            self.console.print(f"[red]Failed to send Feishu Webhook notification: {e}[/red]")
