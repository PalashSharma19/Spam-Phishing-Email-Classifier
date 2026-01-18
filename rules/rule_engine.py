import re

def rule_score(text):
    score = 0
    triggered_rules = []

    original_text = text
    text_lower = text.lower()
    words = original_text.split()

    # -----------------------------
    # 1. URL-RELATED RULES
    # -----------------------------

    has_url = ("http://" in text_lower) or ("https://" in text_lower) or ("www." in text_lower)
    if has_url:
        score += 1
        triggered_rules.append("contains_url")

    url_shorteners = ["bit.ly", "goo.gl", "tinyurl", "ow.ly", "t.co"]
    if any(shortener in text_lower for shortener in url_shorteners):
        score += 2
        triggered_rules.append("url_shortener")

    url_count = len(re.findall(r"http[s]?://", text_lower))
    if url_count >= 2:
        score += 2
        triggered_rules.append("multiple_urls")

    # -----------------------------
    # 2. URGENCY & ACTION LANGUAGE
    # -----------------------------

    urgent_words = [
        "urgent", "immediately", "asap", "act now", "limited time",
        "verify now", "important", "attention", "warning",
        "final notice", "last chance"
    ]

    if any(word in text_lower for word in urgent_words):
        score += 1
        triggered_rules.append("urgency_language")

    action_words = [
        "click", "verify", "confirm", "update", "reset",
        "download", "visit", "claim", "contact"
    ]

    if any(word in text_lower for word in action_words):
        score += 1
        triggered_rules.append("action_language")

    # -----------------------------
    # 3. SENSITIVE CONTEXT (WEAK ALONE, STRONG IN COMBO)
    # -----------------------------

    sensitive_terms = [
        "password", "otp", "bank", "credit card",
        "login", "account suspended", "security alert",
        "unauthorized access"
    ]

    has_sensitive = any(term in text_lower for term in sensitive_terms)

    # Action + sensitive = strong phishing signal
    if has_sensitive and any(word in text_lower for word in action_words):
        score += 2
        triggered_rules.append("action_and_sensitive")

    # URL + urgency = very strong phishing signal
    if has_url and any(word in text_lower for word in urgent_words):
        score += 3
        triggered_rules.append("url_and_urgency")

    # -----------------------------
    # 4. STRUCTURAL / FORMAT RULES
    # -----------------------------

    # ALL CAPS word
    if any(len(word) > 4 and word.isupper() for word in words):
        score += 1
        triggered_rules.append("all_caps_word")

    # Short message + URL (low context phishing)
    if has_url and len(text_lower.split()) < 8:
        score += 2
        triggered_rules.append("short_text_with_url")

    # Excessive punctuation
    if re.search(r"[!?]{3,}", original_text):
        score += 1
        triggered_rules.append("excessive_punctuation")

    # Repeated characters (e.g., winnnn, loooose)
    if re.search(r"(.)\1{3,}", text_lower):
        score += 1
        triggered_rules.append("repeated_characters")

    # -----------------------------
    # 5. NUMERIC / CURRENCY SIGNALS
    # -----------------------------

    # Long numbers (phone numbers, IDs)
    if re.search(r"\d{10,}", text_lower):
        score += 1
        triggered_rules.append("long_number_present")

    # Currency symbols
    if "$" in text_lower or "₹" in text_lower:
        score += 1
        triggered_rules.append("currency_symbol")

    # -----------------------------
    return score, triggered_rules
