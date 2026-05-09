"""
Tests — AgeGate
"""
import pytest

from bea_freq import AgeGate, ContentRating, ProfileType, SIGNAL_VOCAB


def get(word: str):
    sig = SIGNAL_VOCAB.get(word.lower())
    assert sig is not None, f"'{word}' not in SIGNAL_VOCAB"
    return sig


# ── G-rated signals ───────────────────────────────────────────────────────────

def test_g_passes_owner():
    assert AgeGate(ProfileType.OWNER).filter(get("play")) is not None

def test_g_passes_user():
    assert AgeGate(ProfileType.USER).filter(get("play")) is not None

def test_g_passes_child():
    assert AgeGate(ProfileType.CHILD).filter(get("play")) is not None

def test_g_passes_guest():
    assert AgeGate(ProfileType.GUEST).filter(get("play")) is not None

def test_g_word_unchanged_for_all_profiles():
    signal = get("play")
    for p in ProfileType:
        result = AgeGate(p).filter(signal)
        assert result is not None
        assert result.word == "play"


# ── M-rated signals ───────────────────────────────────────────────────────────

def test_m_passes_owner():
    result = AgeGate(ProfileType.OWNER).filter(get("gay"))
    assert result is not None
    assert result.word == "gay"

def test_m_passes_user():
    result = AgeGate(ProfileType.USER).filter(get("gay"))
    assert result is not None
    assert result.word == "gay"

def test_m_gay_substituted_for_child():
    result = AgeGate(ProfileType.CHILD).filter(get("gay"))
    assert result is not None
    assert result.word == "okay"
    assert result.rating == ContentRating.G

def test_m_hex_substituted_for_child():
    result = AgeGate(ProfileType.CHILD).filter(get("hex"))
    assert result is not None
    assert result.word == "reflex"
    assert result.rating == ContentRating.G

def test_m_stripped_for_guest():
    assert AgeGate(ProfileType.GUEST).filter(get("gay")) is None

def test_m_stripped_for_guest_hex():
    assert AgeGate(ProfileType.GUEST).filter(get("hex")) is None


# ── R-rated signals ───────────────────────────────────────────────────────────
# No R signals exist in v0.1 vocabulary, but the gate logic should be exercised.
# We mock by patching a G signal's rating for the test.

def test_r_passes_owner_with_unlock():
    # Simulate an R-rated signal using a mock FreqSignal
    from bea_freq.schema import FreqSignal, NodeDesignation
    r_signal = FreqSignal(
        signal_key="test.r",
        word="testword",
        node=NodeDesignation.Z,
        e_score=20,
        rating=ContentRating.R,
        protocol_meaning="test R signal",
    )
    gate = AgeGate(ProfileType.OWNER, r_unlocked=True)
    assert gate.filter(r_signal) is r_signal

def test_r_stripped_for_owner_without_unlock():
    from bea_freq.schema import FreqSignal, NodeDesignation
    r_signal = FreqSignal(
        signal_key="test.r",
        word="testword",
        node=NodeDesignation.Z,
        e_score=20,
        rating=ContentRating.R,
        protocol_meaning="test R signal",
    )
    assert AgeGate(ProfileType.OWNER, r_unlocked=False).filter(r_signal) is None

def test_r_routed_to_silence_for_child():
    from bea_freq.schema import FreqSignal, NodeDesignation
    r_signal = FreqSignal(
        signal_key="test.r",
        word="testword",
        node=NodeDesignation.Z,
        e_score=20,
        rating=ContentRating.R,
        protocol_meaning="test R signal",
    )
    result = AgeGate(ProfileType.CHILD).filter(r_signal)
    assert result is not None
    assert result.word == "silence"

def test_r_stripped_for_user():
    from bea_freq.schema import FreqSignal, NodeDesignation
    r_signal = FreqSignal(
        signal_key="test.r",
        word="testword",
        node=NodeDesignation.Z,
        e_score=20,
        rating=ContentRating.R,
        protocol_meaning="test R signal",
    )
    assert AgeGate(ProfileType.USER).filter(r_signal) is None


# ── filter_all ────────────────────────────────────────────────────────────────

def test_filter_all_child_substitutes_m():
    signals = [get("play"), get("gay"), get("flux")]
    gate = AgeGate(ProfileType.CHILD)
    result = gate.filter_all(signals)
    words = [s.word for s in result]
    assert "play" in words
    assert "okay" in words       # gay → okay
    assert "flux" in words
    assert "gay" not in words

def test_filter_all_guest_strips_m():
    signals = [get("play"), get("gay"), get("hex")]
    gate = AgeGate(ProfileType.GUEST)
    result = gate.filter_all(signals)
    words = [s.word for s in result]
    assert "play" in words
    assert "gay" not in words
    assert "hex" not in words

def test_filter_all_owner_passes_m():
    signals = [get("play"), get("gay"), get("hex")]
    gate = AgeGate(ProfileType.OWNER)
    result = gate.filter_all(signals)
    assert len(result) == 3


# ── Never-block guarantee ─────────────────────────────────────────────────────

def test_child_m_never_returns_none():
    """CHILD profile must never strip M signals — it must reroute them."""
    m_signals = [s for s in SIGNAL_VOCAB.values() if s.rating == ContentRating.M]
    gate = AgeGate(ProfileType.CHILD)
    for sig in m_signals:
        result = gate.filter(sig)
        assert result is not None, f"M signal '{sig.word}' was stripped for CHILD (should be rerouted)"
        assert result.rating == ContentRating.G, f"CHILD substitute for '{sig.word}' is not G-rated"
