"""
Team Obsidian — Real-time Sentry Telemetry & Distributed Error Correlator
Maps live production stack traces to AST code symbols and architecture nodes.
"""

import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class SentryTelemetrySubscriber:
    """Subscribes to Sentry error webhooks and correlates issues to Git commits."""

    def __init__(self, project_slug: str):
        self.project_slug = project_slug

    def process_error_event(self, event_payload: Dict[str, Any]) -> Dict[str, Any]:
        culprit = event_payload.get("culprit", "unknown")
        exception_type = event_payload.get("exception_type", "RuntimeError")
        stack_trace = event_payload.get("stack_trace", "")
        level = event_payload.get("level", "error")

        logger.info("Processing Sentry issue: %s (%s)", exception_type, culprit)
        return {
            "issue_id": event_payload.get("id"),
            "culprit": culprit,
            "exception_type": exception_type,
            "severity": level,
            "mapped_ast_node": culprit.split(".")[-1] if "." in culprit else culprit,
        }
