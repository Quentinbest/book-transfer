from chapter_utils import sanitize_title_for_filename, unique_sorted_ranges


def test_sanitize_title_for_filename():
    assert sanitize_title_for_filename("A/B:C") == "A_B_C"
    assert sanitize_title_for_filename("***") == "Chapter"


def test_unique_sorted_ranges():
    assert unique_sorted_ranges([5, 1, 5, -1, 10], total_pages=10) == [1, 5, 10]
    assert unique_sorted_ranges([], total_pages=10) == [1]
    assert unique_sorted_ranges([3, 4], total_pages=10) == [1, 3, 4]
