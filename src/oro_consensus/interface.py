"""Public interface for oro-consensus.

Re-exports the primary public API for the consensus brick.
All concrete implementations live in their own modules.

Usage:
    from oro_consensus.interface import VRF, ValidatorSelector, AntiGamingEngine
"""

from .anti_gaming import AntiGamingEngine, compute_diversity_score, compute_tenure_penalty, detect_collusion_patterns
from .models import (
    AttestationType,
    DiversityConstraints,
    ElevationProposal,
    ElevationVote,
    EpochTransition,
    IdentityAttestation,
    SlashingEvent,
    SlashingOffense,
    SlashingStatus,
    StakeRegistration,
    StakeStatus,
    Validator,
    ValidatorSet,
    ValidatorStatus,
    ValidatorTier,
)
from .selection import ValidatorSelector, compute_selection_weight, derive_epoch_seed, select_validators
from .vrf import VRF, VRFOutput, VRFProof

__all__ = [
    # VRF
    "VRF",
    "VRFProof",
    "VRFOutput",
    # Models
    "Validator",
    "ValidatorSet",
    "ValidatorTier",
    "ValidatorStatus",
    "StakeRegistration",
    "StakeStatus",
    "IdentityAttestation",
    "AttestationType",
    "SlashingEvent",
    "SlashingOffense",
    "SlashingStatus",
    "EpochTransition",
    "DiversityConstraints",
    "ElevationProposal",
    "ElevationVote",
    # Selection
    "ValidatorSelector",
    "compute_selection_weight",
    "derive_epoch_seed",
    "select_validators",
    # Anti-Gaming
    "AntiGamingEngine",
    "compute_tenure_penalty",
    "compute_diversity_score",
    "detect_collusion_patterns",
]
