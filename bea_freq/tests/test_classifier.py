"""
Tests — DotSignalClassifier
"""
import pytest

from bea_freq import DotSignalClassifier, NodeDesignation, SIGNAL_VOCAB

clf = DotSignalClassifier()


# ── Basic detection ───────────────────────────────────────────────────────────

def test_y_signal_detected():
    signals = clf.classify("let's play")
    words = [s.word for s in signals]
    assert "play" in words


def test_x_signal_detected():
    signals = clf.classify("system in flux")
    words = [s.word for s in signals]
    assert "flux" in words


def test_z_signal_detected():
    signals = clf.classify("there's a buzz in here")
    words = [s.word for s in signals]
    assert "buzz" in words


def test_i_signal_vision():
    signals = clf.classify("I need vision")
    words = [s.word.lower() for s in signals]
    assert "vision" in words


def test_cross_node_unity():
    signals = clf.classify("unity is the goal")
    words = [s.word for s in signals]
    assert "unity" in words


def test_emergency_signal():
    signals = clf.classify("this is an emergency")
    assert any(s.e_score == 31 for s in signals)
    assert any(s.word == "emergency" for s in signals)


# ── Node assignment ───────────────────────────────────────────────────────────

def test_play_is_y_node():
    signals = clf.classify("play")
    assert signals[0].node == NodeDesignation.Y


def test_flux_is_x_node():
    signals = clf.classify("flux")
    assert signals[0].node == NodeDesignation.X


def test_buzz_is_z_node():
    signals = clf.classify("buzz")
    assert signals[0].node == NodeDesignation.Z


def test_vision_is_i_node():
    signals = clf.classify("vision")
    assert signals[0].node == NodeDesignation.I


def test_emergency_is_cross_node():
    signals = clf.classify("emergency")
    assert signals[0].node == NodeDesignation.CROSS


# ── E-score ───────────────────────────────────────────────────────────────────

def test_away_is_silence():
    signals = clf.classify("away")
    assert signals[0].e_score == 0
    assert signals[0].is_silence()


def test_play_is_active():
    signals = clf.classify("play")
    assert signals[0].is_active()


def test_betray_is_warning():
    signals = clf.classify("betray")
    assert signals[0].is_warning()


def test_pray_is_heritage():
    signals = clf.classify("pray")
    assert signals[0].is_heritage()


# ── highest_e_score ───────────────────────────────────────────────────────────

def test_highest_e_score_picks_emergency():
    signal = clf.highest_e_score("betray the emergency system")
    assert signal is not None
    assert signal.e_score == 31


def test_highest_e_score_none_on_no_match():
    assert clf.highest_e_score("hello world") is None


# ── Case insensitivity ────────────────────────────────────────────────────────

def test_uppercase_word_detected():
    signals = clf.classify("PLAY")
    assert len(signals) >= 1
    assert signals[0].word == "play"


def test_mixed_case_detected():
    signals = clf.classify("Play the Relay")
    words = [s.word for s in signals]
    assert "play" in words
    assert "relay" in words


# ── No false positives ────────────────────────────────────────────────────────

def test_no_match_returns_empty():
    assert clf.classify("hello world") == []


def test_partial_word_not_matched():
    # "played" should not match "play" (word boundary)
    signals = clf.classify("played")
    words = [s.word for s in signals]
    assert "play" not in words


# ── Multiple signals in one text ──────────────────────────────────────────────

def test_multiple_signals():
    signals = clf.classify("play and relay the mission")
    words = {s.word for s in signals}
    assert "play" in words
    assert "relay" in words
    assert "mission" in words


def test_repeated_word_returns_multiple():
    signals = clf.classify("play play")
    assert len(signals) == 2


# ── filter_by_node ────────────────────────────────────────────────────────────

def test_filter_by_node_y():
    signals = clf.filter_by_node("play and buzz", ".y")
    assert all(s.node == NodeDesignation.Y for s in signals)
    words = [s.word for s in signals]
    assert "play" in words
    assert "buzz" not in words


# ── summary ───────────────────────────────────────────────────────────────────

def test_summary_emergency():
    s = clf.summary("emergency")
    assert s["has_emergency"] is True
    assert s["max_e_score"] == 31


def test_summary_empty():
    s = clf.summary("hello world")
    assert s["count"] == 0
    assert s["max_e_score"] is None
    assert s["has_emergency"] is False


# ── Full vocabulary coverage ──────────────────────────────────────────────────

def test_all_vocab_words_detectable():
    """Every word in the vocabulary must be detectable when surrounded by spaces.
    The .i node ('I') is always uppercase in English — tested with capital I.
    """
    failures = []
    for word in SIGNAL_VOCAB:
        # "I" (.i node declaration) is only detected as standalone capital I
        probe = "I" if word == "i" else word
        results = clf.classify(f"test {probe} end")
        found = any(s.word.lower() == word.lower() for s in results)
        if not found:
            failures.append(word)
    assert failures == [], f"Vocab words not detected: {failures}"
