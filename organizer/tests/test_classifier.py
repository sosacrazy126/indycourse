"""
Basic tests for organizer.classifier
"""

from organizer.classifier import classify_file

def test_transcript():
    result = classify_file("090oR--s__8.md")
    assert result is not None, "Should classify"
    assert result["category"] == "transcript", f"Expected transcript, got {result['category']}"
    assert isinstance(result["title"], str) and result["title"], "Should extract title"

def test_lesson():
    result = classify_file("principledaicodingv4.txt")
    assert result is not None, "Should classify"
    assert result["category"] == "lesson", f"Expected lesson, got {result['category']}"
    assert isinstance(result["title"], str) and result["title"], "Should extract title"

if __name__ == "__main__":
    test_transcript()
    test_lesson()
    print("All tests passed.")