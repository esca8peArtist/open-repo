"""
Wizard step routers — one module per step.
"""
from wizard.steps import (
    step1_welcome,
    step2_profile,
    step3_multiagent,
    step4_channels,
    step5_knowledge,
    step6_integrations,
    step7_model_pull,
    step8_voice,
    step9_hardware,
    step10_license,
    step11_healthcheck,
    step12_golive,
)

ALL_ROUTERS = [
    step1_welcome.router,
    step2_profile.router,
    step3_multiagent.router,
    step4_channels.router,
    step5_knowledge.router,
    step6_integrations.router,
    step7_model_pull.router,
    step8_voice.router,
    step9_hardware.router,
    step10_license.router,
    step11_healthcheck.router,
    step12_golive.router,
]

__all__ = ["ALL_ROUTERS"]
