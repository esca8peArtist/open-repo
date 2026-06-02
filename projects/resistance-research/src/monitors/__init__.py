"""
Phase 2 Automation Monitors

Domain-specific monitoring modules for rapid-response distribution triggering:
- scotus_opinion_monitor: Trump v. Barbara ruling tracking
- hhs_guidance_monitor: Healthcare disenrollment tracking
- election_events_monitor: Voting suppression/election integrity tracking
- coalition_email_router: Auto-tag responses by domain expertise

All monitors integrate with phase-1-adoption-tracking-script.py for unified
orchestration and CHECKIN.md synthesis.
"""

from .scotus_opinion_monitor import SCOTUSOpinionMonitor
from .hhs_guidance_monitor import HHSGuidanceMonitor
from .election_events_monitor import ElectionEventsMonitor
from .coalition_email_router import CoalitionEmailRouter

__all__ = [
    "SCOTUSOpinionMonitor",
    "HHSGuidanceMonitor",
    "ElectionEventsMonitor",
    "CoalitionEmailRouter",
]
